# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_oceanbasepro20190901 import models as ocean_base_pro_20190901_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('oceanbasepro', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_project_modify_record_with_options(
        self,
        request: ocean_base_pro_20190901_models.CancelProjectModifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelProjectModifyRecord',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_project_modify_record_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CancelProjectModifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelProjectModifyRecord',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_project_modify_record(
        self,
        request: ocean_base_pro_20190901_models.CancelProjectModifyRecordRequest,
    ) -> ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_project_modify_record_with_options(request, runtime)

    async def cancel_project_modify_record_async(
        self,
        request: ocean_base_pro_20190901_models.CancelProjectModifyRecordRequest,
    ) -> ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_project_modify_record_with_options_async(request, runtime)

    def create_backup_set_download_link_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_set_id):
            body['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBackupSetDownloadLink',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_set_download_link_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_set_id):
            body['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBackupSetDownloadLink',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_set_download_link(
        self,
        request: ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkRequest,
    ) -> ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_set_download_link_with_options(request, runtime)

    async def create_backup_set_download_link_async(
        self,
        request: ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkRequest,
    ) -> ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_set_download_link_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.collation):
            body['Collation'] = request.collation
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.encoding):
            body['Encoding'] = request.encoding
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.collation):
            body['Collation'] = request.collation
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.encoding):
            body['Encoding'] = request.encoding
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database(
        self,
        request: ocean_base_pro_20190901_models.CreateDatabaseRequest,
    ) -> ocean_base_pro_20190901_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: ocean_base_pro_20190901_models.CreateDatabaseRequest,
    ) -> ocean_base_pro_20190901_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.disk_size):
            body['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            body['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_class):
            body['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.isolation_optimization):
            body['IsolationOptimization'] = request.isolation_optimization
        if not UtilClient.is_unset(request.ob_version):
            body['ObVersion'] = request.ob_version
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.primary_instance):
            body['PrimaryInstance'] = request.primary_instance
        if not UtilClient.is_unset(request.primary_region):
            body['PrimaryRegion'] = request.primary_region
        if not UtilClient.is_unset(request.replica_mode):
            body['ReplicaMode'] = request.replica_mode
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        if not UtilClient.is_unset(request.zones):
            body['Zones'] = request.zones
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.disk_size):
            body['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            body['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_class):
            body['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.isolation_optimization):
            body['IsolationOptimization'] = request.isolation_optimization
        if not UtilClient.is_unset(request.ob_version):
            body['ObVersion'] = request.ob_version
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.primary_instance):
            body['PrimaryInstance'] = request.primary_instance
        if not UtilClient.is_unset(request.primary_region):
            body['PrimaryRegion'] = request.primary_region
        if not UtilClient.is_unset(request.replica_mode):
            body['ReplicaMode'] = request.replica_mode
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        if not UtilClient.is_unset(request.zones):
            body['Zones'] = request.zones
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: ocean_base_pro_20190901_models.CreateInstanceRequest,
    ) -> ocean_base_pro_20190901_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: ocean_base_pro_20190901_models.CreateInstanceRequest,
    ) -> ocean_base_pro_20190901_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_label_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateLabelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabel',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_label_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateLabelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabel',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_label(
        self,
        request: ocean_base_pro_20190901_models.CreateLabelRequest,
    ) -> ocean_base_pro_20190901_models.CreateLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_label_with_options(request, runtime)

    async def create_label_async(
        self,
        request: ocean_base_pro_20190901_models.CreateLabelRequest,
    ) -> ocean_base_pro_20190901_models.CreateLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_label_with_options_async(request, runtime)

    def create_my_sql_data_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateMySqlDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dg_instance_id):
            body['DgInstanceId'] = request.dg_instance_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.schema):
            body['Schema'] = request.schema
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMySqlDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_my_sql_data_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateMySqlDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dg_instance_id):
            body['DgInstanceId'] = request.dg_instance_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.schema):
            body['Schema'] = request.schema
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMySqlDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_my_sql_data_source(
        self,
        request: ocean_base_pro_20190901_models.CreateMySqlDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_my_sql_data_source_with_options(request, runtime)

    async def create_my_sql_data_source_async(
        self,
        request: ocean_base_pro_20190901_models.CreateMySqlDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_my_sql_data_source_with_options_async(request, runtime)

    def create_ocean_base_data_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateOceanBaseDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster):
            body['Cluster'] = request.cluster
        if not UtilClient.is_unset(request.config_url):
            body['ConfigUrl'] = request.config_url
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.drc_password):
            body['DrcPassword'] = request.drc_password
        if not UtilClient.is_unset(request.drc_user_name):
            body['DrcUserName'] = request.drc_user_name
        if not UtilClient.is_unset(request.inner_drc_password):
            body['InnerDrcPassword'] = request.inner_drc_password
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.log_proxy_ip):
            body['LogProxyIp'] = request.log_proxy_ip
        if not UtilClient.is_unset(request.log_proxy_port):
            body['LogProxyPort'] = request.log_proxy_port
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.tenant):
            body['Tenant'] = request.tenant
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOceanBaseDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ocean_base_data_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateOceanBaseDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster):
            body['Cluster'] = request.cluster
        if not UtilClient.is_unset(request.config_url):
            body['ConfigUrl'] = request.config_url
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.drc_password):
            body['DrcPassword'] = request.drc_password
        if not UtilClient.is_unset(request.drc_user_name):
            body['DrcUserName'] = request.drc_user_name
        if not UtilClient.is_unset(request.inner_drc_password):
            body['InnerDrcPassword'] = request.inner_drc_password
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.log_proxy_ip):
            body['LogProxyIp'] = request.log_proxy_ip
        if not UtilClient.is_unset(request.log_proxy_port):
            body['LogProxyPort'] = request.log_proxy_port
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.tenant):
            body['Tenant'] = request.tenant
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOceanBaseDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ocean_base_data_source(
        self,
        request: ocean_base_pro_20190901_models.CreateOceanBaseDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ocean_base_data_source_with_options(request, runtime)

    async def create_ocean_base_data_source_async(
        self,
        request: ocean_base_pro_20190901_models.CreateOceanBaseDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ocean_base_data_source_with_options_async(request, runtime)

    def create_oms_mysql_data_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse:
        """
        To call this operation, you must add the IP address of the OceanBase Migration Service (OMS) server to the whitelist of the Alibaba Cloud database instance, the security rules of the ECS instance, or the security settings of your self-managed database (usually the firewall of your self-managed database) to ensure that OMS can successfully access your database instance. To obtain the IP address of the OMS server, go to the OMS data source management page in the OMS console.
        
        @param request: CreateOmsMysqlDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOmsMysqlDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dg_database_id):
            body['DgDatabaseId'] = request.dg_database_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.schema):
            body['Schema'] = request.schema
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOmsMysqlDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oms_mysql_data_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse:
        """
        To call this operation, you must add the IP address of the OceanBase Migration Service (OMS) server to the whitelist of the Alibaba Cloud database instance, the security rules of the ECS instance, or the security settings of your self-managed database (usually the firewall of your self-managed database) to ensure that OMS can successfully access your database instance. To obtain the IP address of the OMS server, go to the OMS data source management page in the OMS console.
        
        @param request: CreateOmsMysqlDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOmsMysqlDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dg_database_id):
            body['DgDatabaseId'] = request.dg_database_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.schema):
            body['Schema'] = request.schema
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOmsMysqlDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oms_mysql_data_source(
        self,
        request: ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse:
        """
        To call this operation, you must add the IP address of the OceanBase Migration Service (OMS) server to the whitelist of the Alibaba Cloud database instance, the security rules of the ECS instance, or the security settings of your self-managed database (usually the firewall of your self-managed database) to ensure that OMS can successfully access your database instance. To obtain the IP address of the OMS server, go to the OMS data source management page in the OMS console.
        
        @param request: CreateOmsMysqlDataSourceRequest
        @return: CreateOmsMysqlDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_oms_mysql_data_source_with_options(request, runtime)

    async def create_oms_mysql_data_source_async(
        self,
        request: ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse:
        """
        To call this operation, you must add the IP address of the OceanBase Migration Service (OMS) server to the whitelist of the Alibaba Cloud database instance, the security rules of the ECS instance, or the security settings of your self-managed database (usually the firewall of your self-managed database) to ensure that OMS can successfully access your database instance. To obtain the IP address of the OMS server, go to the OMS data source management page in the OMS console.
        
        @param request: CreateOmsMysqlDataSourceRequest
        @return: CreateOmsMysqlDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_oms_mysql_data_source_with_options_async(request, runtime)

    def create_oms_open_apiproject_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_config):
            request.dest_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_config, 'DestConfig', 'json')
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.source_config):
            request.source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_config, 'SourceConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transfer_mapping):
            request.transfer_mapping_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transfer_mapping, 'TransferMapping', 'json')
        if not UtilClient.is_unset(tmp_req.transfer_step_config):
            request.transfer_step_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transfer_step_config, 'TransferStepConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_name):
            body['BusinessName'] = request.business_name
        if not UtilClient.is_unset(request.dest_config_shrink):
            body['DestConfig'] = request.dest_config_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_config_shrink):
            body['SourceConfig'] = request.source_config_shrink
        if not UtilClient.is_unset(request.transfer_mapping_shrink):
            body['TransferMapping'] = request.transfer_mapping_shrink
        if not UtilClient.is_unset(request.transfer_step_config_shrink):
            body['TransferStepConfig'] = request.transfer_step_config_shrink
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oms_open_apiproject_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_config):
            request.dest_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_config, 'DestConfig', 'json')
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.source_config):
            request.source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_config, 'SourceConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transfer_mapping):
            request.transfer_mapping_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transfer_mapping, 'TransferMapping', 'json')
        if not UtilClient.is_unset(tmp_req.transfer_step_config):
            request.transfer_step_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transfer_step_config, 'TransferStepConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_name):
            body['BusinessName'] = request.business_name
        if not UtilClient.is_unset(request.dest_config_shrink):
            body['DestConfig'] = request.dest_config_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_config_shrink):
            body['SourceConfig'] = request.source_config_shrink
        if not UtilClient.is_unset(request.transfer_mapping_shrink):
            body['TransferMapping'] = request.transfer_mapping_shrink
        if not UtilClient.is_unset(request.transfer_step_config_shrink):
            body['TransferStepConfig'] = request.transfer_step_config_shrink
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oms_open_apiproject(
        self,
        request: ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_oms_open_apiproject_with_options(request, runtime)

    async def create_oms_open_apiproject_async(
        self,
        request: ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_oms_open_apiproject_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.common_transfer_config):
            request.common_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_transfer_config, 'CommonTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.full_transfer_config):
            request.full_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.full_transfer_config, 'FullTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.incr_transfer_config):
            request.incr_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.incr_transfer_config, 'IncrTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.struct_transfer_config):
            request.struct_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.struct_transfer_config, 'StructTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transfer_mapping):
            request.transfer_mapping_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transfer_mapping, 'TransferMapping', 'json')
        body = {}
        if not UtilClient.is_unset(request.common_transfer_config_shrink):
            body['CommonTransferConfig'] = request.common_transfer_config_shrink
        if not UtilClient.is_unset(request.enable_full_transfer):
            body['EnableFullTransfer'] = request.enable_full_transfer
        if not UtilClient.is_unset(request.enable_full_verify):
            body['EnableFullVerify'] = request.enable_full_verify
        if not UtilClient.is_unset(request.enable_incr_transfer):
            body['EnableIncrTransfer'] = request.enable_incr_transfer
        if not UtilClient.is_unset(request.enable_reverse_incr_transfer):
            body['EnableReverseIncrTransfer'] = request.enable_reverse_incr_transfer
        if not UtilClient.is_unset(request.enable_struct_transfer):
            body['EnableStructTransfer'] = request.enable_struct_transfer
        if not UtilClient.is_unset(request.full_transfer_config_shrink):
            body['FullTransferConfig'] = request.full_transfer_config_shrink
        if not UtilClient.is_unset(request.incr_transfer_config_shrink):
            body['IncrTransferConfig'] = request.incr_transfer_config_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_key):
            body['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.sink_endpoint_id):
            body['SinkEndpointId'] = request.sink_endpoint_id
        if not UtilClient.is_unset(request.source_endpoint_id):
            body['SourceEndpointId'] = request.source_endpoint_id
        if not UtilClient.is_unset(request.struct_transfer_config_shrink):
            body['StructTransferConfig'] = request.struct_transfer_config_shrink
        if not UtilClient.is_unset(request.transfer_mapping_shrink):
            body['TransferMapping'] = request.transfer_mapping_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.use_oss):
            body['UseOss'] = request.use_oss
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.common_transfer_config):
            request.common_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_transfer_config, 'CommonTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.full_transfer_config):
            request.full_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.full_transfer_config, 'FullTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.incr_transfer_config):
            request.incr_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.incr_transfer_config, 'IncrTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.struct_transfer_config):
            request.struct_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.struct_transfer_config, 'StructTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transfer_mapping):
            request.transfer_mapping_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transfer_mapping, 'TransferMapping', 'json')
        body = {}
        if not UtilClient.is_unset(request.common_transfer_config_shrink):
            body['CommonTransferConfig'] = request.common_transfer_config_shrink
        if not UtilClient.is_unset(request.enable_full_transfer):
            body['EnableFullTransfer'] = request.enable_full_transfer
        if not UtilClient.is_unset(request.enable_full_verify):
            body['EnableFullVerify'] = request.enable_full_verify
        if not UtilClient.is_unset(request.enable_incr_transfer):
            body['EnableIncrTransfer'] = request.enable_incr_transfer
        if not UtilClient.is_unset(request.enable_reverse_incr_transfer):
            body['EnableReverseIncrTransfer'] = request.enable_reverse_incr_transfer
        if not UtilClient.is_unset(request.enable_struct_transfer):
            body['EnableStructTransfer'] = request.enable_struct_transfer
        if not UtilClient.is_unset(request.full_transfer_config_shrink):
            body['FullTransferConfig'] = request.full_transfer_config_shrink
        if not UtilClient.is_unset(request.incr_transfer_config_shrink):
            body['IncrTransferConfig'] = request.incr_transfer_config_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_key):
            body['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.sink_endpoint_id):
            body['SinkEndpointId'] = request.sink_endpoint_id
        if not UtilClient.is_unset(request.source_endpoint_id):
            body['SourceEndpointId'] = request.source_endpoint_id
        if not UtilClient.is_unset(request.struct_transfer_config_shrink):
            body['StructTransferConfig'] = request.struct_transfer_config_shrink
        if not UtilClient.is_unset(request.transfer_mapping_shrink):
            body['TransferMapping'] = request.transfer_mapping_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.use_oss):
            body['UseOss'] = request.use_oss
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: ocean_base_pro_20190901_models.CreateProjectRequest,
    ) -> ocean_base_pro_20190901_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: ocean_base_pro_20190901_models.CreateProjectRequest,
    ) -> ocean_base_pro_20190901_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_project_modify_records_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.CreateProjectModifyRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.databases):
            request.databases_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.databases, 'Databases', 'json')
        body = {}
        if not UtilClient.is_unset(request.databases_shrink):
            body['Databases'] = request.databases_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProjectModifyRecords',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_modify_records_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.CreateProjectModifyRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.databases):
            request.databases_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.databases, 'Databases', 'json')
        body = {}
        if not UtilClient.is_unset(request.databases_shrink):
            body['Databases'] = request.databases_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProjectModifyRecords',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project_modify_records(
        self,
        request: ocean_base_pro_20190901_models.CreateProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_modify_records_with_options(request, runtime)

    async def create_project_modify_records_async(
        self,
        request: ocean_base_pro_20190901_models.CreateProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_modify_records_with_options_async(request, runtime)

    def create_rds_postgre_sqldata_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRdsPostgreSQLDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rds_postgre_sqldata_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRdsPostgreSQLDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rds_postgre_sqldata_source(
        self,
        request: ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rds_postgre_sqldata_source_with_options(request, runtime)

    async def create_rds_postgre_sqldata_source_async(
        self,
        request: ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rds_postgre_sqldata_source_with_options_async(request, runtime)

    def create_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.CreateSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_security_ip_group_with_options(request, runtime)

    async def create_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.CreateSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_security_ip_group_with_options_async(request, runtime)

    def create_tenant_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charset):
            body['Charset'] = request.charset
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_disk):
            body['LogDisk'] = request.log_disk
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.primary_zone):
            body['PrimaryZone'] = request.primary_zone
        if not UtilClient.is_unset(request.read_only_zone_list):
            body['ReadOnlyZoneList'] = request.read_only_zone_list
        if not UtilClient.is_unset(request.tenant_mode):
            body['TenantMode'] = request.tenant_mode
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.unit_num):
            body['UnitNum'] = request.unit_num
        if not UtilClient.is_unset(request.user_vswitch_id):
            body['UserVSwitchId'] = request.user_vswitch_id
        if not UtilClient.is_unset(request.user_vpc_id):
            body['UserVpcId'] = request.user_vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenant',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tenant_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charset):
            body['Charset'] = request.charset
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_disk):
            body['LogDisk'] = request.log_disk
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.primary_zone):
            body['PrimaryZone'] = request.primary_zone
        if not UtilClient.is_unset(request.read_only_zone_list):
            body['ReadOnlyZoneList'] = request.read_only_zone_list
        if not UtilClient.is_unset(request.tenant_mode):
            body['TenantMode'] = request.tenant_mode
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.unit_num):
            body['UnitNum'] = request.unit_num
        if not UtilClient.is_unset(request.user_vswitch_id):
            body['UserVSwitchId'] = request.user_vswitch_id
        if not UtilClient.is_unset(request.user_vpc_id):
            body['UserVpcId'] = request.user_vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenant',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tenant(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_with_options(request, runtime)

    async def create_tenant_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tenant_with_options_async(request, runtime)

    def create_tenant_read_only_connection_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantReadOnlyConnection',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tenant_read_only_connection_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantReadOnlyConnection',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tenant_read_only_connection(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_read_only_connection_with_options(request, runtime)

    async def create_tenant_read_only_connection_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tenant_read_only_connection_with_options_async(request, runtime)

    def create_tenant_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tenant_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tenant_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_security_ip_group_with_options(request, runtime)

    async def create_tenant_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tenant_security_ip_group_with_options_async(request, runtime)

    def create_tenant_user_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.roles):
            body['Roles'] = request.roles
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_password):
            body['UserPassword'] = request.user_password
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantUser',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateTenantUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tenant_user_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.roles):
            body['Roles'] = request.roles
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_password):
            body['UserPassword'] = request.user_password
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantUser',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.CreateTenantUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tenant_user(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantUserRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_user_with_options(request, runtime)

    async def create_tenant_user_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantUserRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tenant_user_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        request: ocean_base_pro_20190901_models.DeleteDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_databases_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteDatabasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_names):
            body['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabases',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_databases_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteDatabasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_names):
            body['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabases',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_databases(
        self,
        request: ocean_base_pro_20190901_models.DeleteDatabasesRequest,
    ) -> ocean_base_pro_20190901_models.DeleteDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_databases_with_options(request, runtime)

    async def delete_databases_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteDatabasesRequest,
    ) -> ocean_base_pro_20190901_models.DeleteDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_databases_with_options_async(request, runtime)

    def delete_instances_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteInstancesResponse:
        """
        Before you call this operation, ensure that the following requirements are met:
        - The cluster is in the Running state.
        - The cluster is a primary cluster and the billing method is pay-as-you-go.
        
        @param request: DeleteInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_retain_mode):
            body['BackupRetainMode'] = request.backup_retain_mode
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstances',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instances_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteInstancesResponse:
        """
        Before you call this operation, ensure that the following requirements are met:
        - The cluster is in the Running state.
        - The cluster is a primary cluster and the billing method is pay-as-you-go.
        
        @param request: DeleteInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_retain_mode):
            body['BackupRetainMode'] = request.backup_retain_mode
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstances',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instances(
        self,
        request: ocean_base_pro_20190901_models.DeleteInstancesRequest,
    ) -> ocean_base_pro_20190901_models.DeleteInstancesResponse:
        """
        Before you call this operation, ensure that the following requirements are met:
        - The cluster is in the Running state.
        - The cluster is a primary cluster and the billing method is pay-as-you-go.
        
        @param request: DeleteInstancesRequest
        @return: DeleteInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instances_with_options(request, runtime)

    async def delete_instances_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteInstancesRequest,
    ) -> ocean_base_pro_20190901_models.DeleteInstancesResponse:
        """
        Before you call this operation, ensure that the following requirements are met:
        - The cluster is in the Running state.
        - The cluster is a primary cluster and the billing method is pay-as-you-go.
        
        @param request: DeleteInstancesRequest
        @return: DeleteInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instances_with_options_async(request, runtime)

    def delete_oms_open_apiproject_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_oms_open_apiproject_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_oms_open_apiproject(
        self,
        request: ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_oms_open_apiproject_with_options(request, runtime)

    async def delete_oms_open_apiproject_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_oms_open_apiproject_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: ocean_base_pro_20190901_models.DeleteProjectRequest,
    ) -> ocean_base_pro_20190901_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteProjectRequest,
    ) -> ocean_base_pro_20190901_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.DeleteSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_security_ip_group_with_options(request, runtime)

    async def delete_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_ip_group_with_options_async(request, runtime)

    def delete_tenant_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTenantSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tenant_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTenantSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tenant_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tenant_security_ip_group_with_options(request, runtime)

    async def delete_tenant_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tenant_security_ip_group_with_options_async(request, runtime)

    def delete_tenant_users_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTenantUsers',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteTenantUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tenant_users_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTenantUsers',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteTenantUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tenant_users(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantUsersRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tenant_users_with_options(request, runtime)

    async def delete_tenant_users_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantUsersRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tenant_users_with_options_async(request, runtime)

    def delete_tenants_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_ids):
            body['TenantIds'] = request.tenant_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTenants',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tenants_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_ids):
            body['TenantIds'] = request.tenant_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTenants',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DeleteTenantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tenants(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tenants_with_options(request, runtime)

    async def delete_tenants_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tenants_with_options_async(request, runtime)

    def describe_anomaly_sqllist_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeAnomalySQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.DescribeAnomalySQLListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'FilterCondition', 'json')
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['FilterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_parameter):
            body['SearchParameter'] = request.search_parameter
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sort_column):
            body['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAnomalySQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_anomaly_sqllist_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeAnomalySQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.DescribeAnomalySQLListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'FilterCondition', 'json')
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['FilterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_parameter):
            body['SearchParameter'] = request.search_parameter
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sort_column):
            body['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAnomalySQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_anomaly_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeAnomalySQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_anomaly_sqllist_with_options(request, runtime)

    async def describe_anomaly_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAnomalySQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_anomaly_sqllist_with_options_async(request, runtime)

    def describe_available_cpu_resource_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableCpuResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableCpuResource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_cpu_resource_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableCpuResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableCpuResource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_cpu_resource(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableCpuResourceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cpu_resource_with_options(request, runtime)

    async def describe_available_cpu_resource_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableCpuResourceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_cpu_resource_with_options_async(request, runtime)

    def describe_available_mem_resource_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableMemResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_num):
            body['CpuNum'] = request.cpu_num
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.unit_num):
            body['UnitNum'] = request.unit_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableMemResource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_mem_resource_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableMemResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_num):
            body['CpuNum'] = request.cpu_num
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.unit_num):
            body['UnitNum'] = request.unit_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableMemResource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_mem_resource(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableMemResourceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_mem_resource_with_options(request, runtime)

    async def describe_available_mem_resource_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableMemResourceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_mem_resource_with_options_async(request, runtime)

    def describe_available_spec_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableSpecResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        if not UtilClient.is_unset(request.upgrade_type):
            body['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableSpec',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAvailableSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_spec_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableSpecResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        if not UtilClient.is_unset(request.upgrade_type):
            body['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableSpec',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAvailableSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_spec(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableSpecRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_spec_with_options(request, runtime)

    async def describe_available_spec_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableSpecRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_spec_with_options_async(request, runtime)

    def describe_available_zone_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableZoneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deploy_type):
            body['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.ob_version):
            body['ObVersion'] = request.ob_version
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableZone',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAvailableZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_zone_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableZoneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deploy_type):
            body['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.ob_version):
            body['ObVersion'] = request.ob_version
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableZone',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeAvailableZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_zone(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableZoneRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_zone_with_options(request, runtime)

    async def describe_available_zone_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableZoneRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_zone_with_options_async(request, runtime)

    def describe_backup_set_download_link_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.download_task_id):
            body['DownloadTaskId'] = request.download_task_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBackupSetDownloadLink',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_set_download_link_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.download_task_id):
            body['DownloadTaskId'] = request.download_task_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBackupSetDownloadLink',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_set_download_link(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkRequest,
    ) -> ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_set_download_link_with_options(request, runtime)

    async def describe_backup_set_download_link_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkRequest,
    ) -> ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_set_download_link_with_options_async(request, runtime)

    def describe_charset_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeCharsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeCharsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        if not UtilClient.is_unset(request.tenant_mode):
            body['TenantMode'] = request.tenant_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCharset',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeCharsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_charset_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeCharsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeCharsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        if not UtilClient.is_unset(request.tenant_mode):
            body['TenantMode'] = request.tenant_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCharset',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeCharsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_charset(
        self,
        request: ocean_base_pro_20190901_models.DescribeCharsetRequest,
    ) -> ocean_base_pro_20190901_models.DescribeCharsetResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_charset_with_options(request, runtime)

    async def describe_charset_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeCharsetRequest,
    ) -> ocean_base_pro_20190901_models.DescribeCharsetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_charset_with_options_async(request, runtime)

    def describe_data_backup_set_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeDataBackupSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeDataBackupSetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_object_type):
            body['BackupObjectType'] = request.backup_object_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDataBackupSet',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeDataBackupSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_backup_set_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeDataBackupSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeDataBackupSetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_object_type):
            body['BackupObjectType'] = request.backup_object_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDataBackupSet',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeDataBackupSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_backup_set(
        self,
        request: ocean_base_pro_20190901_models.DescribeDataBackupSetRequest,
    ) -> ocean_base_pro_20190901_models.DescribeDataBackupSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_backup_set_with_options(request, runtime)

    async def describe_data_backup_set_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeDataBackupSetRequest,
    ) -> ocean_base_pro_20190901_models.DescribeDataBackupSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_backup_set_with_options_async(request, runtime)

    def describe_databases_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.with_tables):
            body['WithTables'] = request.with_tables
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_databases_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.with_tables):
            body['WithTables'] = request.with_tables
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_databases(
        self,
        request: ocean_base_pro_20190901_models.DescribeDatabasesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    async def describe_databases_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeDatabasesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_databases_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_instance_creatable_zone_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceCreatableZone',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_creatable_zone_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceCreatableZone',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_creatable_zone(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_creatable_zone_with_options(request, runtime)

    async def describe_instance_creatable_zone_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_creatable_zone_with_options_async(request, runtime)

    def describe_instance_sslwith_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSSLResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSSL',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_sslwith_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSSLResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSSL',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ssl(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSSLRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sslwith_options(request, runtime)

    async def describe_instance_ssl_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSSLRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_sslwith_options_async(request, runtime)

    def describe_instance_security_configs_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_id):
            body['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSecurityConfigs',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_security_configs_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_id):
            body['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSecurityConfigs',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_security_configs(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_security_configs_with_options(request, runtime)

    async def describe_instance_security_configs_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_security_configs_with_options_async(request, runtime)

    def describe_instance_tags_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTags',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_tags_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTags',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_tags(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTagsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_tags_with_options(request, runtime)

    async def describe_instance_tags_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTagsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_tags_with_options_async(request, runtime)

    def describe_instance_tenant_modes_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTenantModesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTenantModes',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_tenant_modes_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTenantModesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTenantModes',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_tenant_modes(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTenantModesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_tenant_modes_with_options(request, runtime)

    async def describe_instance_tenant_modes_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTenantModesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_tenant_modes_with_options_async(request, runtime)

    def describe_instance_topology_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTopology',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_topology_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTopology',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_topology(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTopologyRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_topology_with_options(request, runtime)

    async def describe_instance_topology_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTopologyRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_topology_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstancesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstancesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_metrics_data_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeMetricsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeMetricsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by_labels):
            query['GroupByLabels'] = request.group_by_labels
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.sort_metric_key):
            query['SortMetricKey'] = request.sort_metric_key
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.replica_type):
            body['ReplicaType'] = request.replica_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMetricsData',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeMetricsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metrics_data_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeMetricsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeMetricsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by_labels):
            query['GroupByLabels'] = request.group_by_labels
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.sort_metric_key):
            query['SortMetricKey'] = request.sort_metric_key
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.replica_type):
            body['ReplicaType'] = request.replica_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMetricsData',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeMetricsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metrics_data(
        self,
        request: ocean_base_pro_20190901_models.DescribeMetricsDataRequest,
    ) -> ocean_base_pro_20190901_models.DescribeMetricsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metrics_data_with_options(request, runtime)

    async def describe_metrics_data_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeMetricsDataRequest,
    ) -> ocean_base_pro_20190901_models.DescribeMetricsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metrics_data_with_options_async(request, runtime)

    def describe_node_metrics_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeNodeMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeNodeMetricsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.node_id_list):
            body['NodeIdList'] = request.node_id_list
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodeMetrics',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeNodeMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_metrics_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeNodeMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeNodeMetricsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.node_id_list):
            body['NodeIdList'] = request.node_id_list
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodeMetrics',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeNodeMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_metrics(
        self,
        request: ocean_base_pro_20190901_models.DescribeNodeMetricsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeNodeMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_node_metrics_with_options(request, runtime)

    async def describe_node_metrics_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeNodeMetricsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeNodeMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_metrics_with_options_async(request, runtime)

    def describe_oas_anomaly_sqllist_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasAnomalySQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition):
            body['FilterCondition'] = request.filter_condition
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.merge_dynamic_sql):
            body['MergeDynamicSql'] = request.merge_dynamic_sql
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_param):
            body['SearchParam'] = request.search_param
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.sql_text_length):
            body['SqlTextLength'] = request.sql_text_length
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasAnomalySQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oas_anomaly_sqllist_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasAnomalySQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.current):
            body['Current'] = request.current
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition):
            body['FilterCondition'] = request.filter_condition
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.merge_dynamic_sql):
            body['MergeDynamicSql'] = request.merge_dynamic_sql
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_param):
            body['SearchParam'] = request.search_param
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.sql_text_length):
            body['SqlTextLength'] = request.sql_text_length
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasAnomalySQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oas_anomaly_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasAnomalySQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_anomaly_sqllist_with_options(request, runtime)

    async def describe_oas_anomaly_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasAnomalySQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_anomaly_sqllist_with_options_async(request, runtime)

    def describe_oas_sqldetails_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasSQLDetails',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oas_sqldetails_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasSQLDetails',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oas_sqldetails(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLDetailsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_sqldetails_with_options(request, runtime)

    async def describe_oas_sqldetails_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLDetailsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_sqldetails_with_options_async(request, runtime)

    def describe_oas_sqlhistory_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasSQLHistoryList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oas_sqlhistory_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasSQLHistoryList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oas_sqlhistory_list(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_sqlhistory_list_with_options(request, runtime)

    async def describe_oas_sqlhistory_list_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_sqlhistory_list_with_options_async(request, runtime)

    def describe_oas_sqlplans_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasSQLPlans',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oas_sqlplans_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasSQLPlans',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oas_sqlplans(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLPlansRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_sqlplans_with_options(request, runtime)

    async def describe_oas_sqlplans_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLPlansRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_sqlplans_with_options_async(request, runtime)

    def describe_oas_slow_sqllist_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSlowSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition):
            body['FilterCondition'] = request.filter_condition
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.merge_dynamic_sql):
            body['MergeDynamicSql'] = request.merge_dynamic_sql
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_param):
            body['SearchParam'] = request.search_param
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.sql_text_length):
            body['SqlTextLength'] = request.sql_text_length
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasSlowSQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oas_slow_sqllist_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSlowSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition):
            body['FilterCondition'] = request.filter_condition
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.merge_dynamic_sql):
            body['MergeDynamicSql'] = request.merge_dynamic_sql
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_param):
            body['SearchParam'] = request.search_param
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.sql_text_length):
            body['SqlTextLength'] = request.sql_text_length
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasSlowSQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oas_slow_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSlowSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_slow_sqllist_with_options(request, runtime)

    async def describe_oas_slow_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSlowSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_slow_sqllist_with_options_async(request, runtime)

    def describe_oas_top_sqllist_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasTopSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition):
            body['FilterCondition'] = request.filter_condition
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.merge_dynamic_sql):
            body['MergeDynamicSql'] = request.merge_dynamic_sql
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_param):
            body['SearchParam'] = request.search_param
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.sql_text_length):
            body['SqlTextLength'] = request.sql_text_length
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasTopSQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oas_top_sqllist_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasTopSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.dynamic_sql):
            body['DynamicSql'] = request.dynamic_sql
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition):
            body['FilterCondition'] = request.filter_condition
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.merge_dynamic_sql):
            body['MergeDynamicSql'] = request.merge_dynamic_sql
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_param):
            body['SearchParam'] = request.search_param
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.sql_text_length):
            body['SqlTextLength'] = request.sql_text_length
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOasTopSQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oas_top_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasTopSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_top_sqllist_with_options(request, runtime)

    async def describe_oas_top_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasTopSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_top_sqllist_with_options_async(request, runtime)

    def describe_oms_open_apiproject_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oms_open_apiproject_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oms_open_apiproject(
        self,
        request: ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oms_open_apiproject_with_options(request, runtime)

    async def describe_oms_open_apiproject_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oms_open_apiproject_with_options_async(request, runtime)

    def describe_oms_open_apiproject_steps_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOmsOpenAPIProjectSteps',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oms_open_apiproject_steps_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOmsOpenAPIProjectSteps',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oms_open_apiproject_steps(
        self,
        request: ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oms_open_apiproject_steps_with_options(request, runtime)

    async def describe_oms_open_apiproject_steps_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oms_open_apiproject_steps_with_options_async(request, runtime)

    def describe_outline_binding_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOutlineBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOutlineBindingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_concurrent_limit):
            body['IsConcurrentLimit'] = request.is_concurrent_limit
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOutlineBinding',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOutlineBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outline_binding_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOutlineBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOutlineBindingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_concurrent_limit):
            body['IsConcurrentLimit'] = request.is_concurrent_limit
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOutlineBinding',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeOutlineBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outline_binding(
        self,
        request: ocean_base_pro_20190901_models.DescribeOutlineBindingRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOutlineBindingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_outline_binding_with_options(request, runtime)

    async def describe_outline_binding_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOutlineBindingRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOutlineBindingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_outline_binding_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimension):
            body['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.dimension_value):
            body['DimensionValue'] = request.dimension_value
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimension):
            body['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.dimension_value):
            body['DimensionValue'] = request.dimension_value
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersRequest,
    ) -> ocean_base_pro_20190901_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersRequest,
    ) -> ocean_base_pro_20190901_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_parameters_history_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeParametersHistoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimension):
            body['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.dimension_value):
            body['DimensionValue'] = request.dimension_value
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeParametersHistory',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeParametersHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_history_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeParametersHistoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimension):
            body['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.dimension_value):
            body['DimensionValue'] = request.dimension_value
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeParametersHistory',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeParametersHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters_history(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersHistoryRequest,
    ) -> ocean_base_pro_20190901_models.DescribeParametersHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_history_with_options(request, runtime)

    async def describe_parameters_history_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersHistoryRequest,
    ) -> ocean_base_pro_20190901_models.DescribeParametersHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_history_with_options_async(request, runtime)

    def describe_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_project_with_options(request, runtime)

    async def describe_project_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_with_options_async(request, runtime)

    def describe_project_components_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectComponentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProjectComponents',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_components_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectComponentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProjectComponents',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_components(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectComponentsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_project_components_with_options(request, runtime)

    async def describe_project_components_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectComponentsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_components_with_options_async(request, runtime)

    def describe_project_progress_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectProgressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProjectProgress',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_progress_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectProgressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProjectProgress',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_progress(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectProgressRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_project_progress_with_options(request, runtime)

    async def describe_project_progress_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectProgressRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_progress_with_options_async(request, runtime)

    def describe_project_step_metric_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator):
            body['Aggregator'] = request.aggregator
        if not UtilClient.is_unset(request.begin_timestamp):
            body['BeginTimestamp'] = request.begin_timestamp
        if not UtilClient.is_unset(request.end_timestamp):
            body['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.max_point_num):
            body['MaxPointNum'] = request.max_point_num
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.step_name):
            body['StepName'] = request.step_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProjectStepMetric',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_step_metric_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregator):
            body['Aggregator'] = request.aggregator
        if not UtilClient.is_unset(request.begin_timestamp):
            body['BeginTimestamp'] = request.begin_timestamp
        if not UtilClient.is_unset(request.end_timestamp):
            body['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.max_point_num):
            body['MaxPointNum'] = request.max_point_num
        if not UtilClient.is_unset(request.metric_type):
            body['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.step_name):
            body['StepName'] = request.step_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProjectStepMetric',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_step_metric(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepMetricRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_project_step_metric_with_options(request, runtime)

    async def describe_project_step_metric_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepMetricRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_step_metric_with_options_async(request, runtime)

    def describe_project_steps_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProjectSteps',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectStepsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_steps_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProjectSteps',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeProjectStepsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_steps(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_project_steps_with_options(request, runtime)

    async def describe_project_steps_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_steps_with_options_async(request, runtime)

    def describe_recommend_index_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeRecommendIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeRecommendIndexResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRecommendIndex',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeRecommendIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recommend_index_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeRecommendIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeRecommendIndexResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRecommendIndex',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeRecommendIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recommend_index(
        self,
        request: ocean_base_pro_20190901_models.DescribeRecommendIndexRequest,
    ) -> ocean_base_pro_20190901_models.DescribeRecommendIndexResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_index_with_options(request, runtime)

    async def describe_recommend_index_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeRecommendIndexRequest,
    ) -> ocean_base_pro_20190901_models.DescribeRecommendIndexResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_recommend_index_with_options_async(request, runtime)

    def describe_sqldetails_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLDetailsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLDetails',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSQLDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqldetails_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLDetailsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLDetails',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSQLDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqldetails(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLDetailsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqldetails_with_options(request, runtime)

    async def describe_sqldetails_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLDetailsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqldetails_with_options_async(request, runtime)

    def describe_sqlhistory_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLHistoryList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlhistory_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLHistoryList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlhistory_list(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlhistory_list_with_options(request, runtime)

    async def describe_sqlhistory_list_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlhistory_list_with_options_async(request, runtime)

    def describe_sqlplans_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLPlansResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLPlans',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSQLPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlplans_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLPlansResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLPlans',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSQLPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlplans(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLPlansRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlplans_with_options(request, runtime)

    async def describe_sqlplans_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLPlansRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlplans_with_options_async(request, runtime)

    def describe_sqlsamples_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLSamplesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLSamplesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLSamples',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSQLSamplesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlsamples_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLSamplesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLSamplesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLSamples',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSQLSamplesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlsamples(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLSamplesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLSamplesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlsamples_with_options(request, runtime)

    async def describe_sqlsamples_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLSamplesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLSamplesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlsamples_with_options_async(request, runtime)

    def describe_sample_sql_raw_texts_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.trace_id):
            body['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSampleSqlRawTexts',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_sql_raw_texts_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.sql_id):
            body['SqlId'] = request.sql_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.trace_id):
            body['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSampleSqlRawTexts',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_sql_raw_texts(
        self,
        request: ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_sql_raw_texts_with_options(request, runtime)

    async def describe_sample_sql_raw_texts_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sample_sql_raw_texts_with_options_async(request, runtime)

    def describe_security_ip_groups_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSecurityIpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIpGroups',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_ip_groups_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSecurityIpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIpGroups',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_ip_groups(
        self,
        request: ocean_base_pro_20190901_models.DescribeSecurityIpGroupsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ip_groups_with_options(request, runtime)

    async def describe_security_ip_groups_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSecurityIpGroupsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_ip_groups_with_options_async(request, runtime)

    def describe_slow_sqlhistory_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowSQLHistoryList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_sqlhistory_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowSQLHistoryList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_sqlhistory_list(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_sqlhistory_list_with_options(request, runtime)

    async def describe_slow_sqlhistory_list_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_sqlhistory_list_with_options_async(request, runtime)

    def describe_slow_sqllist_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeSlowSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLListResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.DescribeSlowSQLListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'FilterCondition', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['FilterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_parameter):
            body['SearchParameter'] = request.search_parameter
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sort_column):
            body['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowSQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSlowSQLListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_sqllist_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeSlowSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLListResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.DescribeSlowSQLListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'FilterCondition', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['FilterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_parameter):
            body['SearchParameter'] = request.search_parameter
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sort_column):
            body['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowSQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeSlowSQLListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_sqllist_with_options(request, runtime)

    async def describe_slow_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_sqllist_with_options_async(request, runtime)

    def describe_tenant_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenant',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenant',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_with_options(request, runtime)

    async def describe_tenant_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_with_options_async(request, runtime)

    def describe_tenant_encryption_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantEncryptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantEncryption',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_encryption_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantEncryptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantEncryption',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_encryption(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantEncryptionRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_encryption_with_options(request, runtime)

    async def describe_tenant_encryption_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantEncryptionRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_encryption_with_options_async(request, runtime)

    def describe_tenant_metrics_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantMetricsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_id_list):
            body['TenantIdList'] = request.tenant_id_list
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantMetrics',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_metrics_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantMetricsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_id_list):
            body['TenantIdList'] = request.tenant_id_list
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantMetrics',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_metrics(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantMetricsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_metrics_with_options(request, runtime)

    async def describe_tenant_metrics_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantMetricsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_metrics_with_options_async(request, runtime)

    def describe_tenant_security_configs_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_id):
            body['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantSecurityConfigs',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_security_configs_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_id):
            body['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantSecurityConfigs',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_security_configs(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_security_configs_with_options(request, runtime)

    async def describe_tenant_security_configs_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_security_configs_with_options_async(request, runtime)

    def describe_tenant_security_ip_groups_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantSecurityIpGroups',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_security_ip_groups_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantSecurityIpGroups',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_security_ip_groups(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_security_ip_groups_with_options(request, runtime)

    async def describe_tenant_security_ip_groups_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_security_ip_groups_with_options_async(request, runtime)

    def describe_tenant_tags_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenant_ids):
            body['TenantIds'] = request.tenant_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantTags',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_tags_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenant_ids):
            body['TenantIds'] = request.tenant_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantTags',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_tags(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantTagsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_tags_with_options(request, runtime)

    async def describe_tenant_tags_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantTagsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_tags_with_options_async(request, runtime)

    def describe_tenant_user_roles_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantUserRoles',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_user_roles_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantUserRoles',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_user_roles(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_user_roles_with_options(request, runtime)

    async def describe_tenant_user_roles_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_user_roles_with_options_async(request, runtime)

    def describe_tenant_users_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantUsers',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_users_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantUsers',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_users(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUsersRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_users_with_options(request, runtime)

    async def describe_tenant_users_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUsersRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_users_with_options_async(request, runtime)

    def describe_tenant_zones_read_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantZonesReadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantZonesRead',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenant_zones_read_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantZonesReadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantZonesRead',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenant_zones_read(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantZonesReadRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_zones_read_with_options(request, runtime)

    async def describe_tenant_zones_read_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantZonesReadRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_zones_read_with_options_async(request, runtime)

    def describe_tenants_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenants',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tenants_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenants',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTenantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tenants(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tenants_with_options(request, runtime)

    async def describe_tenants_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenants_with_options_async(request, runtime)

    def describe_time_zones_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTimeZonesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTimeZones',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTimeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_time_zones_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTimeZonesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTimeZones',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTimeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_time_zones(self) -> ocean_base_pro_20190901_models.DescribeTimeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_time_zones_with_options(runtime)

    async def describe_time_zones_async(self) -> ocean_base_pro_20190901_models.DescribeTimeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_time_zones_with_options_async(runtime)

    def describe_top_sqllist_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeTopSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTopSQLListResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.DescribeTopSQLListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'FilterCondition', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['FilterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_parameter):
            body['SearchParameter'] = request.search_parameter
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sort_column):
            body['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTopSQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTopSQLListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_sqllist_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeTopSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTopSQLListResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.DescribeTopSQLListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'FilterCondition', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['FilterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_parameter):
            body['SearchParameter'] = request.search_parameter
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sort_column):
            body['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTopSQLList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeTopSQLListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_top_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeTopSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTopSQLListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_top_sqllist_with_options(request, runtime)

    async def describe_top_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTopSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTopSQLListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_sqllist_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deploy_type):
            body['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deploy_type):
            body['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: ocean_base_pro_20190901_models.DescribeZonesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeZonesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def get_upload_oss_url_with_options(
        self,
        request: ocean_base_pro_20190901_models.GetUploadOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.GetUploadOssUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.effective_time_minutes):
            body['EffectiveTimeMinutes'] = request.effective_time_minutes
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadOssUrl',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.GetUploadOssUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_oss_url_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.GetUploadOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.GetUploadOssUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.effective_time_minutes):
            body['EffectiveTimeMinutes'] = request.effective_time_minutes
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadOssUrl',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.GetUploadOssUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_oss_url(
        self,
        request: ocean_base_pro_20190901_models.GetUploadOssUrlRequest,
    ) -> ocean_base_pro_20190901_models.GetUploadOssUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_upload_oss_url_with_options(request, runtime)

    async def get_upload_oss_url_async(
        self,
        request: ocean_base_pro_20190901_models.GetUploadOssUrlRequest,
    ) -> ocean_base_pro_20190901_models.GetUploadOssUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_oss_url_with_options_async(request, runtime)

    def kill_process_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.KillProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.KillProcessListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.session_list):
            body['SessionList'] = request.session_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillProcessList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.KillProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_process_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.KillProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.KillProcessListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.session_list):
            body['SessionList'] = request.session_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillProcessList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.KillProcessListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_process_list(
        self,
        request: ocean_base_pro_20190901_models.KillProcessListRequest,
    ) -> ocean_base_pro_20190901_models.KillProcessListResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_process_list_with_options(request, runtime)

    async def kill_process_list_async(
        self,
        request: ocean_base_pro_20190901_models.KillProcessListRequest,
    ) -> ocean_base_pro_20190901_models.KillProcessListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_process_list_with_options_async(request, runtime)

    def list_all_labels_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListAllLabelsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAllLabels',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListAllLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_labels_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListAllLabelsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListAllLabels',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListAllLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_labels(self) -> ocean_base_pro_20190901_models.ListAllLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_all_labels_with_options(runtime)

    async def list_all_labels_async(self) -> ocean_base_pro_20190901_models.ListAllLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_all_labels_with_options_async(runtime)

    def list_data_source_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListDataSourceResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.ListDataSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        body = {}
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.types_shrink):
            body['Types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListDataSourceResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.ListDataSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        body = {}
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.types_shrink):
            body['Types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source(
        self,
        request: ocean_base_pro_20190901_models.ListDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.ListDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_with_options(request, runtime)

    async def list_data_source_async(
        self,
        request: ocean_base_pro_20190901_models.ListDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.ListDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_with_options_async(request, runtime)

    def list_project_full_verify_result_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListProjectFullVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.ListProjectFullVerifyResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_schemas):
            request.dest_schemas_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_schemas, 'DestSchemas', 'json')
        if not UtilClient.is_unset(tmp_req.source_schemas):
            request.source_schemas_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_schemas, 'SourceSchemas', 'json')
        body = {}
        if not UtilClient.is_unset(request.dest_schemas_shrink):
            body['DestSchemas'] = request.dest_schemas_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.source_schemas_shrink):
            body['SourceSchemas'] = request.source_schemas_shrink
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectFullVerifyResult',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_full_verify_result_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListProjectFullVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.ListProjectFullVerifyResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_schemas):
            request.dest_schemas_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_schemas, 'DestSchemas', 'json')
        if not UtilClient.is_unset(tmp_req.source_schemas):
            request.source_schemas_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_schemas, 'SourceSchemas', 'json')
        body = {}
        if not UtilClient.is_unset(request.dest_schemas_shrink):
            body['DestSchemas'] = request.dest_schemas_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.source_schemas_shrink):
            body['SourceSchemas'] = request.source_schemas_shrink
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectFullVerifyResult',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_full_verify_result(
        self,
        request: ocean_base_pro_20190901_models.ListProjectFullVerifyResultRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_full_verify_result_with_options(request, runtime)

    async def list_project_full_verify_result_async(
        self,
        request: ocean_base_pro_20190901_models.ListProjectFullVerifyResultRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_full_verify_result_with_options_async(request, runtime)

    def list_project_modify_records_with_options(
        self,
        request: ocean_base_pro_20190901_models.ListProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectModifyRecords',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_modify_records_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ListProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjectModifyRecords',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_modify_records(
        self,
        request: ocean_base_pro_20190901_models.ListProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_modify_records_with_options(request, runtime)

    async def list_project_modify_records_async(
        self,
        request: ocean_base_pro_20190901_models.ListProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_modify_records_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectsResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.sink_endpoint_types):
            request.sink_endpoint_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink_endpoint_types, 'SinkEndpointTypes', 'json')
        if not UtilClient.is_unset(tmp_req.source_endpoint_types):
            request.source_endpoint_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_endpoint_types, 'SourceEndpointTypes', 'json')
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        body = {}
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.sink_endpoint_types_shrink):
            body['SinkEndpointTypes'] = request.sink_endpoint_types_shrink
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.source_endpoint_types_shrink):
            body['SourceEndpointTypes'] = request.source_endpoint_types_shrink
        if not UtilClient.is_unset(request.status_shrink):
            body['Status'] = request.status_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.visible_sub_project):
            body['VisibleSubProject'] = request.visible_sub_project
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectsResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.sink_endpoint_types):
            request.sink_endpoint_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sink_endpoint_types, 'SinkEndpointTypes', 'json')
        if not UtilClient.is_unset(tmp_req.source_endpoint_types):
            request.source_endpoint_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_endpoint_types, 'SourceEndpointTypes', 'json')
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        body = {}
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.sink_endpoint_types_shrink):
            body['SinkEndpointTypes'] = request.sink_endpoint_types_shrink
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.source_endpoint_types_shrink):
            body['SourceEndpointTypes'] = request.source_endpoint_types_shrink
        if not UtilClient.is_unset(request.status_shrink):
            body['Status'] = request.status_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.visible_sub_project):
            body['VisibleSubProject'] = request.visible_sub_project
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: ocean_base_pro_20190901_models.ListProjectsRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: ocean_base_pro_20190901_models.ListProjectsRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_worker_instances_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListWorkerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListWorkerInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.ListWorkerInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.specs):
            request.specs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.specs, 'Specs', 'json')
        body = {}
        if not UtilClient.is_unset(request.dest_type):
            body['DestType'] = request.dest_type
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.only_bindable):
            body['OnlyBindable'] = request.only_bindable
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.specs_shrink):
            body['Specs'] = request.specs_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWorkerInstances',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListWorkerInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_worker_instances_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListWorkerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListWorkerInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.ListWorkerInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.specs):
            request.specs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.specs, 'Specs', 'json')
        body = {}
        if not UtilClient.is_unset(request.dest_type):
            body['DestType'] = request.dest_type
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.only_bindable):
            body['OnlyBindable'] = request.only_bindable
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.specs_shrink):
            body['Specs'] = request.specs_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWorkerInstances',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ListWorkerInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_worker_instances(
        self,
        request: ocean_base_pro_20190901_models.ListWorkerInstancesRequest,
    ) -> ocean_base_pro_20190901_models.ListWorkerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_worker_instances_with_options(request, runtime)

    async def list_worker_instances_async(
        self,
        request: ocean_base_pro_20190901_models.ListWorkerInstancesRequest,
    ) -> ocean_base_pro_20190901_models.ListWorkerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_worker_instances_with_options_async(request, runtime)

    def modify_database_description_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseDescription',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_description_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseDescription',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_description(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseDescriptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_description_with_options(request, runtime)

    async def modify_database_description_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseDescriptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_description_with_options_async(request, runtime)

    def modify_database_user_roles_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseUserRoles',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_user_roles_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseUserRoles',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_user_roles(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_user_roles_with_options(request, runtime)

    async def modify_database_user_roles_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_user_roles_with_options_async(request, runtime)

    def modify_instance_name_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceName',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_name_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNameResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceName',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_name(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNameRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    async def modify_instance_name_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNameRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_name_with_options_async(request, runtime)

    def modify_instance_node_num_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNodeNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_num):
            body['NodeNum'] = request.node_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceNodeNum',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_node_num_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNodeNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_num):
            body['NodeNum'] = request.node_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceNodeNum',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_node_num(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNodeNumRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_node_num_with_options(request, runtime)

    async def modify_instance_node_num_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNodeNumRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_node_num_with_options_async(request, runtime)

    def modify_instance_spec_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.disk_size):
            body['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            body['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_class):
            body['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_spec_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.disk_size):
            body['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            body['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.dry_run):
            body['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.instance_class):
            body['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_spec(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSpecRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    async def modify_instance_spec_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSpecRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_spec_with_options_async(request, runtime)

    def modify_instance_tags_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTags',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_tags_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTags',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_tags(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTagsRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_tags_with_options(request, runtime)

    async def modify_instance_tags_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTagsRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_tags_with_options_async(request, runtime)

    def modify_instance_temporary_capacity_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.disk_size):
            body['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTemporaryCapacity',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_temporary_capacity_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.disk_size):
            body['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.spec):
            body['Spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTemporaryCapacity',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_temporary_capacity(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_temporary_capacity_with_options(request, runtime)

    async def modify_instance_temporary_capacity_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_temporary_capacity_with_options_async(request, runtime)

    def modify_parameters_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyParametersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimension):
            body['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.dimension_value):
            body['DimensionValue'] = request.dimension_value
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyParameters',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameters_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyParametersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimension):
            body['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.dimension_value):
            body['DimensionValue'] = request.dimension_value
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyParameters',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameters(
        self,
        request: ocean_base_pro_20190901_models.ModifyParametersRequest,
    ) -> ocean_base_pro_20190901_models.ModifyParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    async def modify_parameters_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyParametersRequest,
    ) -> ocean_base_pro_20190901_models.ModifyParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameters_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifySecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ips(
        self,
        request: ocean_base_pro_20190901_models.ModifySecurityIpsRequest,
    ) -> ocean_base_pro_20190901_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: ocean_base_pro_20190901_models.ModifySecurityIpsRequest,
    ) -> ocean_base_pro_20190901_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_tenant_encryption_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantEncryptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encryption_key_id):
            body['EncryptionKeyId'] = request.encryption_key_id
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantEncryption',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_encryption_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantEncryptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encryption_key_id):
            body['EncryptionKeyId'] = request.encryption_key_id
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantEncryption',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_encryption(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantEncryptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_encryption_with_options(request, runtime)

    async def modify_tenant_encryption_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantEncryptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_encryption_with_options_async(request, runtime)

    def modify_tenant_primary_zone_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.master_intranet_address_zone):
            body['MasterIntranetAddressZone'] = request.master_intranet_address_zone
        if not UtilClient.is_unset(request.primary_zone):
            body['PrimaryZone'] = request.primary_zone
        if not UtilClient.is_unset(request.tenant_endpoint_direct_id):
            body['TenantEndpointDirectId'] = request.tenant_endpoint_direct_id
        if not UtilClient.is_unset(request.tenant_endpoint_id):
            body['TenantEndpointId'] = request.tenant_endpoint_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_direct_vswitch_id):
            body['UserDirectVSwitchId'] = request.user_direct_vswitch_id
        if not UtilClient.is_unset(request.user_vswitch_id):
            body['UserVSwitchId'] = request.user_vswitch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantPrimaryZone',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_primary_zone_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.master_intranet_address_zone):
            body['MasterIntranetAddressZone'] = request.master_intranet_address_zone
        if not UtilClient.is_unset(request.primary_zone):
            body['PrimaryZone'] = request.primary_zone
        if not UtilClient.is_unset(request.tenant_endpoint_direct_id):
            body['TenantEndpointDirectId'] = request.tenant_endpoint_direct_id
        if not UtilClient.is_unset(request.tenant_endpoint_id):
            body['TenantEndpointId'] = request.tenant_endpoint_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_direct_vswitch_id):
            body['UserDirectVSwitchId'] = request.user_direct_vswitch_id
        if not UtilClient.is_unset(request.user_vswitch_id):
            body['UserVSwitchId'] = request.user_vswitch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantPrimaryZone',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_primary_zone(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_primary_zone_with_options(request, runtime)

    async def modify_tenant_primary_zone_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_primary_zone_with_options_async(request, runtime)

    def modify_tenant_resource_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_disk):
            body['LogDisk'] = request.log_disk
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.read_only_zone_list):
            body['ReadOnlyZoneList'] = request.read_only_zone_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantResource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_resource_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.log_disk):
            body['LogDisk'] = request.log_disk
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.read_only_zone_list):
            body['ReadOnlyZoneList'] = request.read_only_zone_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantResource',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_resource(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantResourceRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_resource_with_options(request, runtime)

    async def modify_tenant_resource_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantResourceRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_resource_with_options_async(request, runtime)

    def modify_tenant_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantSecurityIpGroup',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_security_ip_group_with_options(request, runtime)

    async def modify_tenant_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_security_ip_group_with_options_async(request, runtime)

    def modify_tenant_tags_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantTags',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_tags_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantTagsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantTags',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_tags(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantTagsRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_tags_with_options(request, runtime)

    async def modify_tenant_tags_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantTagsRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_tags_with_options_async(request, runtime)

    def modify_tenant_user_description_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserDescription',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_user_description_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserDescription',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_user_description(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserDescriptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_description_with_options(request, runtime)

    async def modify_tenant_user_description_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserDescriptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_user_description_with_options_async(request, runtime)

    def modify_tenant_user_password_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_password):
            body['UserPassword'] = request.user_password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserPassword',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_user_password_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_password):
            body['UserPassword'] = request.user_password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserPassword',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_user_password(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserPasswordRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_password_with_options(request, runtime)

    async def modify_tenant_user_password_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserPasswordRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_user_password_with_options_async(request, runtime)

    def modify_tenant_user_roles_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_role):
            body['UserRole'] = request.user_role
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserRoles',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_user_roles_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_role):
            body['UserRole'] = request.user_role
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserRoles',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_user_roles(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_roles_with_options(request, runtime)

    async def modify_tenant_user_roles_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_user_roles_with_options_async(request, runtime)

    def modify_tenant_user_status_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_status):
            body['UserStatus'] = request.user_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tenant_user_status_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_status):
            body['UserStatus'] = request.user_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tenant_user_status(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserStatusRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_status_with_options(request, runtime)

    async def modify_tenant_user_status_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserStatusRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_user_status_with_options_async(request, runtime)

    def release_oms_open_apiproject_with_options(
        self,
        request: ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_oms_open_apiproject_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_oms_open_apiproject(
        self,
        request: ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_oms_open_apiproject_with_options(request, runtime)

    async def release_oms_open_apiproject_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_oms_open_apiproject_with_options_async(request, runtime)

    def release_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.ReleaseProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ReleaseProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ReleaseProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_project(
        self,
        request: ocean_base_pro_20190901_models.ReleaseProjectRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_project_with_options(request, runtime)

    async def release_project_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseProjectRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_project_with_options_async(request, runtime)

    def release_worker_instance_with_options(
        self,
        request: ocean_base_pro_20190901_models.ReleaseWorkerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseWorkerInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_worker_instance_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseWorkerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseWorkerInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_worker_instance(
        self,
        request: ocean_base_pro_20190901_models.ReleaseWorkerInstanceRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_worker_instance_with_options(request, runtime)

    async def release_worker_instance_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseWorkerInstanceRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_worker_instance_with_options_async(request, runtime)

    def reset_oms_open_apiproject_with_options(
        self,
        request: ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_oms_open_apiproject_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_oms_open_apiproject(
        self,
        request: ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_oms_open_apiproject_with_options(request, runtime)

    async def reset_oms_open_apiproject_async(
        self,
        request: ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_oms_open_apiproject_with_options_async(request, runtime)

    def resume_oms_open_apiproject_with_options(
        self,
        request: ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_oms_open_apiproject_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_oms_open_apiproject(
        self,
        request: ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_oms_open_apiproject_with_options(request, runtime)

    async def resume_oms_open_apiproject_async(
        self,
        request: ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_oms_open_apiproject_with_options_async(request, runtime)

    def resume_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.ResumeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ResumeProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ResumeProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ResumeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ResumeProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.ResumeProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_project(
        self,
        request: ocean_base_pro_20190901_models.ResumeProjectRequest,
    ) -> ocean_base_pro_20190901_models.ResumeProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_project_with_options(request, runtime)

    async def resume_project_async(
        self,
        request: ocean_base_pro_20190901_models.ResumeProjectRequest,
    ) -> ocean_base_pro_20190901_models.ResumeProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_project_with_options_async(request, runtime)

    def retry_project_modify_records_with_options(
        self,
        request: ocean_base_pro_20190901_models.RetryProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryProjectModifyRecords',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_project_modify_records_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.RetryProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryProjectModifyRecords',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_project_modify_records(
        self,
        request: ocean_base_pro_20190901_models.RetryProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_project_modify_records_with_options(request, runtime)

    async def retry_project_modify_records_async(
        self,
        request: ocean_base_pro_20190901_models.RetryProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_project_modify_records_with_options_async(request, runtime)

    def search_oms_open_apimonitor_metric_with_options(
        self,
        request: ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.begin_time):
            body['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_point_num):
            body['MaxPointNum'] = request.max_point_num
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchOmsOpenAPIMonitorMetric',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_oms_open_apimonitor_metric_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.begin_time):
            body['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_point_num):
            body['MaxPointNum'] = request.max_point_num
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchOmsOpenAPIMonitorMetric',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_oms_open_apimonitor_metric(
        self,
        request: ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricRequest,
    ) -> ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_oms_open_apimonitor_metric_with_options(request, runtime)

    async def search_oms_open_apimonitor_metric_async(
        self,
        request: ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricRequest,
    ) -> ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_oms_open_apimonitor_metric_with_options_async(request, runtime)

    def search_oms_open_apiprojects_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_db_types):
            request.dest_db_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_db_types, 'DestDbTypes', 'json')
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.source_db_types):
            request.source_db_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_db_types, 'SourceDbTypes', 'json')
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        body = {}
        if not UtilClient.is_unset(request.dest_db_types_shrink):
            body['DestDbTypes'] = request.dest_db_types_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.source_db_types_shrink):
            body['SourceDbTypes'] = request.source_db_types_shrink
        if not UtilClient.is_unset(request.status_list_shrink):
            body['StatusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchOmsOpenAPIProjects',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_oms_open_apiprojects_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsResponse:
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_db_types):
            request.dest_db_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_db_types, 'DestDbTypes', 'json')
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.source_db_types):
            request.source_db_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_db_types, 'SourceDbTypes', 'json')
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        body = {}
        if not UtilClient.is_unset(request.dest_db_types_shrink):
            body['DestDbTypes'] = request.dest_db_types_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.source_db_types_shrink):
            body['SourceDbTypes'] = request.source_db_types_shrink
        if not UtilClient.is_unset(request.status_list_shrink):
            body['StatusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchOmsOpenAPIProjects',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_oms_open_apiprojects(
        self,
        request: ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsRequest,
    ) -> ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_oms_open_apiprojects_with_options(request, runtime)

    async def search_oms_open_apiprojects_async(
        self,
        request: ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsRequest,
    ) -> ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_oms_open_apiprojects_with_options_async(request, runtime)

    def start_oms_open_apiproject_with_options(
        self,
        request: ocean_base_pro_20190901_models.StartOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StartOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_oms_open_apiproject_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StartOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StartOmsOpenAPIProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_oms_open_apiproject(
        self,
        request: ocean_base_pro_20190901_models.StartOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.StartOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_oms_open_apiproject_with_options(request, runtime)

    async def start_oms_open_apiproject_async(
        self,
        request: ocean_base_pro_20190901_models.StartOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.StartOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_oms_open_apiproject_with_options_async(request, runtime)

    def start_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.StartProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StartProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StartProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StartProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_project(
        self,
        request: ocean_base_pro_20190901_models.StartProjectRequest,
    ) -> ocean_base_pro_20190901_models.StartProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_project_with_options(request, runtime)

    async def start_project_async(
        self,
        request: ocean_base_pro_20190901_models.StartProjectRequest,
    ) -> ocean_base_pro_20190901_models.StartProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_project_with_options_async(request, runtime)

    def start_projects_by_label_with_options(
        self,
        request: ocean_base_pro_20190901_models.StartProjectsByLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartProjectsByLabelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartProjectsByLabel',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StartProjectsByLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_projects_by_label_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StartProjectsByLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartProjectsByLabelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartProjectsByLabel',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StartProjectsByLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_projects_by_label(
        self,
        request: ocean_base_pro_20190901_models.StartProjectsByLabelRequest,
    ) -> ocean_base_pro_20190901_models.StartProjectsByLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_projects_by_label_with_options(request, runtime)

    async def start_projects_by_label_async(
        self,
        request: ocean_base_pro_20190901_models.StartProjectsByLabelRequest,
    ) -> ocean_base_pro_20190901_models.StartProjectsByLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_projects_by_label_with_options_async(request, runtime)

    def stop_oms_open_apiproject_with_options(
        self,
        request: ocean_base_pro_20190901_models.StopOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StopOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_oms_open_apiproject_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StopOmsOpenAPIProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopOmsOpenAPIProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopOmsOpenAPIProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StopOmsOpenAPIProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_oms_open_apiproject(
        self,
        request: ocean_base_pro_20190901_models.StopOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.StopOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_oms_open_apiproject_with_options(request, runtime)

    async def stop_oms_open_apiproject_async(
        self,
        request: ocean_base_pro_20190901_models.StopOmsOpenAPIProjectRequest,
    ) -> ocean_base_pro_20190901_models.StopOmsOpenAPIProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_oms_open_apiproject_with_options_async(request, runtime)

    def stop_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.StopProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StopProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopProject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StopProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_project(
        self,
        request: ocean_base_pro_20190901_models.StopProjectRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_project_with_options(request, runtime)

    async def stop_project_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_project_with_options_async(request, runtime)

    def stop_project_modify_records_with_options(
        self,
        request: ocean_base_pro_20190901_models.StopProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopProjectModifyRecords',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_project_modify_records_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopProjectModifyRecords',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_project_modify_records(
        self,
        request: ocean_base_pro_20190901_models.StopProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_project_modify_records_with_options(request, runtime)

    async def stop_project_modify_records_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_project_modify_records_with_options_async(request, runtime)

    def stop_projects_by_label_with_options(
        self,
        request: ocean_base_pro_20190901_models.StopProjectsByLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectsByLabelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopProjectsByLabel',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StopProjectsByLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_projects_by_label_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectsByLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectsByLabelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopProjectsByLabel',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.StopProjectsByLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_projects_by_label(
        self,
        request: ocean_base_pro_20190901_models.StopProjectsByLabelRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectsByLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_projects_by_label_with_options(request, runtime)

    async def stop_projects_by_label_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectsByLabelRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectsByLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_projects_by_label_with_options_async(request, runtime)

    def switchover_instance_with_options(
        self,
        request: ocean_base_pro_20190901_models.SwitchoverInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.SwitchoverInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.forced):
            body['Forced'] = request.forced
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.target_instance_id):
            body['TargetInstanceId'] = request.target_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SwitchoverInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.SwitchoverInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def switchover_instance_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.SwitchoverInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.SwitchoverInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.forced):
            body['Forced'] = request.forced
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.target_instance_id):
            body['TargetInstanceId'] = request.target_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SwitchoverInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ocean_base_pro_20190901_models.SwitchoverInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switchover_instance(
        self,
        request: ocean_base_pro_20190901_models.SwitchoverInstanceRequest,
    ) -> ocean_base_pro_20190901_models.SwitchoverInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.switchover_instance_with_options(request, runtime)

    async def switchover_instance_async(
        self,
        request: ocean_base_pro_20190901_models.SwitchoverInstanceRequest,
    ) -> ocean_base_pro_20190901_models.SwitchoverInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switchover_instance_with_options_async(request, runtime)
