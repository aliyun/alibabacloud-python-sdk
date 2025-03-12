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

    def batch_kill_process_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.BatchKillProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.BatchKillProcessListResponse:
        """
        @summary You can call this operation to close sessions in batches. Please note that this operation is executed asynchronously. After calling this operation, you need to verify it by calling DescribeProcessStatsComposition.
        
        @param request: BatchKillProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchKillProcessListResponse
        """
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
            action='BatchKillProcessList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.BatchKillProcessListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.BatchKillProcessListResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_kill_process_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.BatchKillProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.BatchKillProcessListResponse:
        """
        @summary You can call this operation to close sessions in batches. Please note that this operation is executed asynchronously. After calling this operation, you need to verify it by calling DescribeProcessStatsComposition.
        
        @param request: BatchKillProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchKillProcessListResponse
        """
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
            action='BatchKillProcessList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.BatchKillProcessListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.BatchKillProcessListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_kill_process_list(
        self,
        request: ocean_base_pro_20190901_models.BatchKillProcessListRequest,
    ) -> ocean_base_pro_20190901_models.BatchKillProcessListResponse:
        """
        @summary You can call this operation to close sessions in batches. Please note that this operation is executed asynchronously. After calling this operation, you need to verify it by calling DescribeProcessStatsComposition.
        
        @param request: BatchKillProcessListRequest
        @return: BatchKillProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_kill_process_list_with_options(request, runtime)

    async def batch_kill_process_list_async(
        self,
        request: ocean_base_pro_20190901_models.BatchKillProcessListRequest,
    ) -> ocean_base_pro_20190901_models.BatchKillProcessListResponse:
        """
        @summary You can call this operation to close sessions in batches. Please note that this operation is executed asynchronously. After calling this operation, you need to verify it by calling DescribeProcessStatsComposition.
        
        @param request: BatchKillProcessListRequest
        @return: BatchKillProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_kill_process_list_with_options_async(request, runtime)

    def batch_kill_session_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.BatchKillSessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.BatchKillSessionListResponse:
        """
        @summary You can call this operation to close sessions between the ApsaraDB for OceanBase and the application in batches. Please note that this operation is executed asynchronously. After calling this operation, you need to verify it by calling DescribeSessionList.
        
        @param request: BatchKillSessionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchKillSessionListResponse
        """
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
            action='BatchKillSessionList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.BatchKillSessionListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.BatchKillSessionListResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_kill_session_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.BatchKillSessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.BatchKillSessionListResponse:
        """
        @summary You can call this operation to close sessions between the ApsaraDB for OceanBase and the application in batches. Please note that this operation is executed asynchronously. After calling this operation, you need to verify it by calling DescribeSessionList.
        
        @param request: BatchKillSessionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchKillSessionListResponse
        """
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
            action='BatchKillSessionList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.BatchKillSessionListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.BatchKillSessionListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_kill_session_list(
        self,
        request: ocean_base_pro_20190901_models.BatchKillSessionListRequest,
    ) -> ocean_base_pro_20190901_models.BatchKillSessionListResponse:
        """
        @summary You can call this operation to close sessions between the ApsaraDB for OceanBase and the application in batches. Please note that this operation is executed asynchronously. After calling this operation, you need to verify it by calling DescribeSessionList.
        
        @param request: BatchKillSessionListRequest
        @return: BatchKillSessionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_kill_session_list_with_options(request, runtime)

    async def batch_kill_session_list_async(
        self,
        request: ocean_base_pro_20190901_models.BatchKillSessionListRequest,
    ) -> ocean_base_pro_20190901_models.BatchKillSessionListResponse:
        """
        @summary You can call this operation to close sessions between the ApsaraDB for OceanBase and the application in batches. Please note that this operation is executed asynchronously. After calling this operation, you need to verify it by calling DescribeSessionList.
        
        @param request: BatchKillSessionListRequest
        @return: BatchKillSessionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_kill_session_list_with_options_async(request, runtime)

    def cancel_project_modify_record_with_options(
        self,
        request: ocean_base_pro_20190901_models.CancelProjectModifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse:
        """
        @summary 根据记录id取消修改操作 （仅支持处于 PENDING 状态的修改记录）
        
        @param request: CancelProjectModifyRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelProjectModifyRecordResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_project_modify_record_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CancelProjectModifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse:
        """
        @summary 根据记录id取消修改操作 （仅支持处于 PENDING 状态的修改记录）
        
        @param request: CancelProjectModifyRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelProjectModifyRecordResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_project_modify_record(
        self,
        request: ocean_base_pro_20190901_models.CancelProjectModifyRecordRequest,
    ) -> ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse:
        """
        @summary 根据记录id取消修改操作 （仅支持处于 PENDING 状态的修改记录）
        
        @param request: CancelProjectModifyRecordRequest
        @return: CancelProjectModifyRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_project_modify_record_with_options(request, runtime)

    async def cancel_project_modify_record_async(
        self,
        request: ocean_base_pro_20190901_models.CancelProjectModifyRecordRequest,
    ) -> ocean_base_pro_20190901_models.CancelProjectModifyRecordResponse:
        """
        @summary 根据记录id取消修改操作 （仅支持处于 PENDING 状态的修改记录）
        
        @param request: CancelProjectModifyRecordRequest
        @return: CancelProjectModifyRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_project_modify_record_with_options_async(request, runtime)

    def create_backup_set_download_link_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse:
        """
        @summary 创建备份任务下载链接
        
        @param request: CreateBackupSetDownloadLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupSetDownloadLinkResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse(),
                self.execute(params, req, runtime)
            )

    async def create_backup_set_download_link_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse:
        """
        @summary 创建备份任务下载链接
        
        @param request: CreateBackupSetDownloadLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupSetDownloadLinkResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_backup_set_download_link(
        self,
        request: ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkRequest,
    ) -> ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse:
        """
        @summary 创建备份任务下载链接
        
        @param request: CreateBackupSetDownloadLinkRequest
        @return: CreateBackupSetDownloadLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_set_download_link_with_options(request, runtime)

    async def create_backup_set_download_link_async(
        self,
        request: ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkRequest,
    ) -> ocean_base_pro_20190901_models.CreateBackupSetDownloadLinkResponse:
        """
        @summary 创建备份任务下载链接
        
        @param request: CreateBackupSetDownloadLinkRequest
        @return: CreateBackupSetDownloadLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_set_download_link_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateDatabaseResponse:
        """
        @summary The request ID.
        
        @param request: CreateDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatabaseResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateDatabaseResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateDatabaseResponse(),
                self.execute(params, req, runtime)
            )

    async def create_database_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateDatabaseResponse:
        """
        @summary The request ID.
        
        @param request: CreateDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatabaseResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateDatabaseResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateDatabaseResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_database(
        self,
        request: ocean_base_pro_20190901_models.CreateDatabaseRequest,
    ) -> ocean_base_pro_20190901_models.CreateDatabaseResponse:
        """
        @summary The request ID.
        
        @param request: CreateDatabaseRequest
        @return: CreateDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: ocean_base_pro_20190901_models.CreateDatabaseRequest,
    ) -> ocean_base_pro_20190901_models.CreateDatabaseResponse:
        """
        @summary The request ID.
        
        @param request: CreateDatabaseRequest
        @return: CreateDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateInstanceResponse:
        """
        @summary You can call this operation to create an OceanBase cluster.
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cpu_arch):
            body['CpuArch'] = request.cpu_arch
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_instance_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateInstanceResponse:
        """
        @summary You can call this operation to create an OceanBase cluster.
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cpu_arch):
            body['CpuArch'] = request.cpu_arch
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_instance(
        self,
        request: ocean_base_pro_20190901_models.CreateInstanceRequest,
    ) -> ocean_base_pro_20190901_models.CreateInstanceResponse:
        """
        @summary You can call this operation to create an OceanBase cluster.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: ocean_base_pro_20190901_models.CreateInstanceRequest,
    ) -> ocean_base_pro_20190901_models.CreateInstanceResponse:
        """
        @summary You can call this operation to create an OceanBase cluster.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_label_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateLabelResponse:
        """
        @summary 创建标签
        
        @param request: CreateLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateLabelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateLabelResponse(),
                self.execute(params, req, runtime)
            )

    async def create_label_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateLabelResponse:
        """
        @summary 创建标签
        
        @param request: CreateLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateLabelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateLabelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_label(
        self,
        request: ocean_base_pro_20190901_models.CreateLabelRequest,
    ) -> ocean_base_pro_20190901_models.CreateLabelResponse:
        """
        @summary 创建标签
        
        @param request: CreateLabelRequest
        @return: CreateLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_label_with_options(request, runtime)

    async def create_label_async(
        self,
        request: ocean_base_pro_20190901_models.CreateLabelRequest,
    ) -> ocean_base_pro_20190901_models.CreateLabelResponse:
        """
        @summary 创建标签
        
        @param request: CreateLabelRequest
        @return: CreateLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_label_with_options_async(request, runtime)

    def create_my_sql_data_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateMySqlDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse:
        """
        @summary 创建 MySQL 数据源
        
        @param request: CreateMySqlDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMySqlDataSourceResponse
        """
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
        if not UtilClient.is_unset(request.use_ssl):
            body['UseSsl'] = request.use_ssl
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_my_sql_data_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateMySqlDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse:
        """
        @summary 创建 MySQL 数据源
        
        @param request: CreateMySqlDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMySqlDataSourceResponse
        """
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
        if not UtilClient.is_unset(request.use_ssl):
            body['UseSsl'] = request.use_ssl
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_my_sql_data_source(
        self,
        request: ocean_base_pro_20190901_models.CreateMySqlDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse:
        """
        @summary 创建 MySQL 数据源
        
        @param request: CreateMySqlDataSourceRequest
        @return: CreateMySqlDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_my_sql_data_source_with_options(request, runtime)

    async def create_my_sql_data_source_async(
        self,
        request: ocean_base_pro_20190901_models.CreateMySqlDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateMySqlDataSourceResponse:
        """
        @summary 创建 MySQL 数据源
        
        @param request: CreateMySqlDataSourceRequest
        @return: CreateMySqlDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_my_sql_data_source_with_options_async(request, runtime)

    def create_ocean_base_data_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateOceanBaseDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse:
        """
        @summary 创建 OceanBase 数据源
        
        @param request: CreateOceanBaseDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOceanBaseDataSourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_ocean_base_data_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateOceanBaseDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse:
        """
        @summary 创建 OceanBase 数据源
        
        @param request: CreateOceanBaseDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOceanBaseDataSourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_ocean_base_data_source(
        self,
        request: ocean_base_pro_20190901_models.CreateOceanBaseDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse:
        """
        @summary 创建 OceanBase 数据源
        
        @param request: CreateOceanBaseDataSourceRequest
        @return: CreateOceanBaseDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ocean_base_data_source_with_options(request, runtime)

    async def create_ocean_base_data_source_async(
        self,
        request: ocean_base_pro_20190901_models.CreateOceanBaseDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateOceanBaseDataSourceResponse:
        """
        @summary 创建 OceanBase 数据源
        
        @param request: CreateOceanBaseDataSourceRequest
        @return: CreateOceanBaseDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ocean_base_data_source_with_options_async(request, runtime)

    def create_oms_mysql_data_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse:
        """
        @summary You can call this operation to create a MySQL data source.
        
        @description To call this operation, you must add the IP address of the OceanBase Migration Service (OMS) server to the whitelist of the Alibaba Cloud database instance, the security rules of the ECS instance, or the security settings of your self-managed database (usually the firewall of your self-managed database) to ensure that OMS can successfully access your database instance. To obtain the IP address of the OMS server, go to the OMS data source management page in the OMS console.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_oms_mysql_data_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse:
        """
        @summary You can call this operation to create a MySQL data source.
        
        @description To call this operation, you must add the IP address of the OceanBase Migration Service (OMS) server to the whitelist of the Alibaba Cloud database instance, the security rules of the ECS instance, or the security settings of your self-managed database (usually the firewall of your self-managed database) to ensure that OMS can successfully access your database instance. To obtain the IP address of the OMS server, go to the OMS data source management page in the OMS console.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_oms_mysql_data_source(
        self,
        request: ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse:
        """
        @summary You can call this operation to create a MySQL data source.
        
        @description To call this operation, you must add the IP address of the OceanBase Migration Service (OMS) server to the whitelist of the Alibaba Cloud database instance, the security rules of the ECS instance, or the security settings of your self-managed database (usually the firewall of your self-managed database) to ensure that OMS can successfully access your database instance. To obtain the IP address of the OMS server, go to the OMS data source management page in the OMS console.
        
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
        @summary You can call this operation to create a MySQL data source.
        
        @description To call this operation, you must add the IP address of the OceanBase Migration Service (OMS) server to the whitelist of the Alibaba Cloud database instance, the security rules of the ECS instance, or the security settings of your self-managed database (usually the firewall of your self-managed database) to ensure that OMS can successfully access your database instance. To obtain the IP address of the OMS server, go to the OMS data source management page in the OMS console.
        
        @param request: CreateOmsMysqlDataSourceRequest
        @return: CreateOmsMysqlDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_oms_mysql_data_source_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param tmp_req: CreateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
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
        if not UtilClient.is_unset(tmp_req.reverse_incr_transfer_config):
            request.reverse_incr_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reverse_incr_transfer_config, 'ReverseIncrTransferConfig', 'json')
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
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.incr_transfer_config_shrink):
            body['IncrTransferConfig'] = request.incr_transfer_config_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_key):
            body['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.reverse_incr_transfer_config_shrink):
            body['ReverseIncrTransferConfig'] = request.reverse_incr_transfer_config_shrink
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateProjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateProjectResponse(),
                self.execute(params, req, runtime)
            )

    async def create_project_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param tmp_req: CreateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
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
        if not UtilClient.is_unset(tmp_req.reverse_incr_transfer_config):
            request.reverse_incr_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reverse_incr_transfer_config, 'ReverseIncrTransferConfig', 'json')
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
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.incr_transfer_config_shrink):
            body['IncrTransferConfig'] = request.incr_transfer_config_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_key):
            body['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.reverse_incr_transfer_config_shrink):
            body['ReverseIncrTransferConfig'] = request.reverse_incr_transfer_config_shrink
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateProjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateProjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_project(
        self,
        request: ocean_base_pro_20190901_models.CreateProjectRequest,
    ) -> ocean_base_pro_20190901_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: ocean_base_pro_20190901_models.CreateProjectRequest,
    ) -> ocean_base_pro_20190901_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_project_modify_records_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse:
        """
        @summary 修改传输对象（加减表）(仅支持处于 RUNNING/FAILED/SUSPEND 状态的项目)
        
        @param tmp_req: CreateProjectModifyRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectModifyRecordsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse(),
                self.execute(params, req, runtime)
            )

    async def create_project_modify_records_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse:
        """
        @summary 修改传输对象（加减表）(仅支持处于 RUNNING/FAILED/SUSPEND 状态的项目)
        
        @param tmp_req: CreateProjectModifyRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectModifyRecordsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_project_modify_records(
        self,
        request: ocean_base_pro_20190901_models.CreateProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse:
        """
        @summary 修改传输对象（加减表）(仅支持处于 RUNNING/FAILED/SUSPEND 状态的项目)
        
        @param request: CreateProjectModifyRecordsRequest
        @return: CreateProjectModifyRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_project_modify_records_with_options(request, runtime)

    async def create_project_modify_records_async(
        self,
        request: ocean_base_pro_20190901_models.CreateProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.CreateProjectModifyRecordsResponse:
        """
        @summary 修改传输对象（加减表）(仅支持处于 RUNNING/FAILED/SUSPEND 状态的项目)
        
        @param request: CreateProjectModifyRecordsRequest
        @return: CreateProjectModifyRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_project_modify_records_with_options_async(request, runtime)

    def create_rds_postgre_sqldata_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse:
        """
        @summary 创建RDS PG 数据源
        
        @param request: CreateRdsPostgreSQLDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRdsPostgreSQLDataSourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_rds_postgre_sqldata_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse:
        """
        @summary 创建RDS PG 数据源
        
        @param request: CreateRdsPostgreSQLDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRdsPostgreSQLDataSourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_rds_postgre_sqldata_source(
        self,
        request: ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse:
        """
        @summary 创建RDS PG 数据源
        
        @param request: CreateRdsPostgreSQLDataSourceRequest
        @return: CreateRdsPostgreSQLDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rds_postgre_sqldata_source_with_options(request, runtime)

    async def create_rds_postgre_sqldata_source_async(
        self,
        request: ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.CreateRdsPostgreSQLDataSourceResponse:
        """
        @summary 创建RDS PG 数据源
        
        @param request: CreateRdsPostgreSQLDataSourceRequest
        @return: CreateRdsPostgreSQLDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rds_postgre_sqldata_source_with_options_async(request, runtime)

    def create_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse:
        """
        @summary The name of the whitelist group.
        
        @param request: CreateSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def create_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse:
        """
        @summary The name of the whitelist group.
        
        @param request: CreateSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.CreateSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse:
        """
        @summary The name of the whitelist group.
        
        @param request: CreateSecurityIpGroupRequest
        @return: CreateSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_security_ip_group_with_options(request, runtime)

    async def create_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.CreateSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse:
        """
        @summary The name of the whitelist group.
        
        @param request: CreateSecurityIpGroupRequest
        @return: CreateSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_security_ip_group_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTagResponse:
        """
        @summary You can call this operation to create a tag group.
        
        @param request: CreateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTagResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTagResponse(),
                self.execute(params, req, runtime)
            )

    async def create_tag_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTagResponse:
        """
        @summary You can call this operation to create a tag group.
        
        @param request: CreateTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTagResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTagResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_tag(
        self,
        request: ocean_base_pro_20190901_models.CreateTagRequest,
    ) -> ocean_base_pro_20190901_models.CreateTagResponse:
        """
        @summary You can call this operation to create a tag group.
        
        @param request: CreateTagRequest
        @return: CreateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTagRequest,
    ) -> ocean_base_pro_20190901_models.CreateTagResponse:
        """
        @summary You can call this operation to create a tag group.
        
        @param request: CreateTagRequest
        @return: CreateTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def create_tag_value_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateTagValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTagValueResponse:
        """
        @summary You can call this operation to create a tag.
        
        @param request: CreateTagValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTagValue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTagValueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTagValueResponse(),
                self.execute(params, req, runtime)
            )

    async def create_tag_value_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTagValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTagValueResponse:
        """
        @summary You can call this operation to create a tag.
        
        @param request: CreateTagValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTagValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTagValue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTagValueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTagValueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_tag_value(
        self,
        request: ocean_base_pro_20190901_models.CreateTagValueRequest,
    ) -> ocean_base_pro_20190901_models.CreateTagValueResponse:
        """
        @summary You can call this operation to create a tag.
        
        @param request: CreateTagValueRequest
        @return: CreateTagValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tag_value_with_options(request, runtime)

    async def create_tag_value_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTagValueRequest,
    ) -> ocean_base_pro_20190901_models.CreateTagValueResponse:
        """
        @summary You can call this operation to create a tag.
        
        @param request: CreateTagValueRequest
        @return: CreateTagValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_value_with_options_async(request, runtime)

    def create_tenant_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantResponse:
        """
        @summary You can call this operation to create a tenant.
        
        @param tmp_req: CreateTenantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTenantResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.CreateTenantShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_params):
            request.create_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_params, 'CreateParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.charset):
            body['Charset'] = request.charset
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.create_params_shrink):
            body['CreateParams'] = request.create_params_shrink
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
        if not UtilClient.is_unset(request.user_vpc_owner_id):
            body['UserVpcOwnerId'] = request.user_vpc_owner_id
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantResponse(),
                self.execute(params, req, runtime)
            )

    async def create_tenant_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.CreateTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantResponse:
        """
        @summary You can call this operation to create a tenant.
        
        @param tmp_req: CreateTenantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTenantResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.CreateTenantShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_params):
            request.create_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_params, 'CreateParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.charset):
            body['Charset'] = request.charset
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.create_params_shrink):
            body['CreateParams'] = request.create_params_shrink
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
        if not UtilClient.is_unset(request.user_vpc_owner_id):
            body['UserVpcOwnerId'] = request.user_vpc_owner_id
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_tenant(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantResponse:
        """
        @summary You can call this operation to create a tenant.
        
        @param request: CreateTenantRequest
        @return: CreateTenantResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_with_options(request, runtime)

    async def create_tenant_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantResponse:
        """
        @summary You can call this operation to create a tenant.
        
        @param request: CreateTenantRequest
        @return: CreateTenantResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tenant_with_options_async(request, runtime)

    def create_tenant_read_only_connection_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse:
        """
        @summary The request ID.
        
        @param request: CreateTenantReadOnlyConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTenantReadOnlyConnectionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse(),
                self.execute(params, req, runtime)
            )

    async def create_tenant_read_only_connection_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse:
        """
        @summary The request ID.
        
        @param request: CreateTenantReadOnlyConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTenantReadOnlyConnectionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_tenant_read_only_connection(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse:
        """
        @summary The request ID.
        
        @param request: CreateTenantReadOnlyConnectionRequest
        @return: CreateTenantReadOnlyConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_read_only_connection_with_options(request, runtime)

    async def create_tenant_read_only_connection_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse:
        """
        @summary The request ID.
        
        @param request: CreateTenantReadOnlyConnectionRequest
        @return: CreateTenantReadOnlyConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tenant_read_only_connection_with_options_async(request, runtime)

    def create_tenant_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to create the security whitelist for the tenant.
        
        @param request: CreateTenantSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTenantSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def create_tenant_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to create the security whitelist for the tenant.
        
        @param request: CreateTenantSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTenantSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_tenant_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to create the security whitelist for the tenant.
        
        @param request: CreateTenantSecurityIpGroupRequest
        @return: CreateTenantSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_security_ip_group_with_options(request, runtime)

    async def create_tenant_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to create the security whitelist for the tenant.
        
        @param request: CreateTenantSecurityIpGroupRequest
        @return: CreateTenantSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tenant_security_ip_group_with_options_async(request, runtime)

    def create_tenant_user_with_options(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantUserResponse:
        """
        @summary CreateTenantUser
        
        @param request: CreateTenantUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTenantUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.global_permissions):
            body['GlobalPermissions'] = request.global_permissions
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantUserResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantUserResponse(),
                self.execute(params, req, runtime)
            )

    async def create_tenant_user_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.CreateTenantUserResponse:
        """
        @summary CreateTenantUser
        
        @param request: CreateTenantUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTenantUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.global_permissions):
            body['GlobalPermissions'] = request.global_permissions
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantUserResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.CreateTenantUserResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_tenant_user(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantUserRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantUserResponse:
        """
        @summary CreateTenantUser
        
        @param request: CreateTenantUserRequest
        @return: CreateTenantUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_user_with_options(request, runtime)

    async def create_tenant_user_async(
        self,
        request: ocean_base_pro_20190901_models.CreateTenantUserRequest,
    ) -> ocean_base_pro_20190901_models.CreateTenantUserResponse:
        """
        @summary CreateTenantUser
        
        @param request: CreateTenantUserRequest
        @return: CreateTenantUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tenant_user_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteDataSourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteDataSourceResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_data_source_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteDataSourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteDataSourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_data_source(
        self,
        request: ocean_base_pro_20190901_models.DeleteDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_databases_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteDatabasesResponse:
        """
        @summary The request ID.
        
        @param request: DeleteDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabasesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteDatabasesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteDatabasesResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_databases_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteDatabasesResponse:
        """
        @summary The request ID.
        
        @param request: DeleteDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabasesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteDatabasesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteDatabasesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_databases(
        self,
        request: ocean_base_pro_20190901_models.DeleteDatabasesRequest,
    ) -> ocean_base_pro_20190901_models.DeleteDatabasesResponse:
        """
        @summary The request ID.
        
        @param request: DeleteDatabasesRequest
        @return: DeleteDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_databases_with_options(request, runtime)

    async def delete_databases_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteDatabasesRequest,
    ) -> ocean_base_pro_20190901_models.DeleteDatabasesResponse:
        """
        @summary The request ID.
        
        @param request: DeleteDatabasesRequest
        @return: DeleteDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_databases_with_options_async(request, runtime)

    def delete_instances_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteInstancesResponse:
        """
        @summary You can call this operation to release an OceanBase cluster.
        
        @description Before you call this operation, ensure that the following requirements are met:
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_instances_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteInstancesResponse:
        """
        @summary You can call this operation to release an OceanBase cluster.
        
        @description Before you call this operation, ensure that the following requirements are met:
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_instances(
        self,
        request: ocean_base_pro_20190901_models.DeleteInstancesRequest,
    ) -> ocean_base_pro_20190901_models.DeleteInstancesResponse:
        """
        @summary You can call this operation to release an OceanBase cluster.
        
        @description Before you call this operation, ensure that the following requirements are met:
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
        @summary You can call this operation to release an OceanBase cluster.
        
        @description Before you call this operation, ensure that the following requirements are met:
        - The cluster is in the Running state.
        - The cluster is a primary cluster and the billing method is pay-as-you-go.
        
        @param request: DeleteInstancesRequest
        @return: DeleteInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instances_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteProjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteProjectResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteProjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteProjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_project(
        self,
        request: ocean_base_pro_20190901_models.DeleteProjectRequest,
    ) -> ocean_base_pro_20190901_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteProjectRequest,
    ) -> ocean_base_pro_20190901_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse:
        """
        @summary The name of the deleted IP address whitelist group.
        
        @param request: DeleteSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse:
        """
        @summary The name of the deleted IP address whitelist group.
        
        @param request: DeleteSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.DeleteSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse:
        """
        @summary The name of the deleted IP address whitelist group.
        
        @param request: DeleteSecurityIpGroupRequest
        @return: DeleteSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_security_ip_group_with_options(request, runtime)

    async def delete_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse:
        """
        @summary The name of the deleted IP address whitelist group.
        
        @param request: DeleteSecurityIpGroupRequest
        @return: DeleteSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_ip_group_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTagResponse:
        """
        @summary You can call this operation to delete a tag group.
        
        @param request: DeleteTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTagResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTagResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_tag_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTagResponse:
        """
        @summary You can call this operation to delete a tag group.
        
        @param request: DeleteTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTagResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTagResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_tag(
        self,
        request: ocean_base_pro_20190901_models.DeleteTagRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTagResponse:
        """
        @summary You can call this operation to delete a tag group.
        
        @param request: DeleteTagRequest
        @return: DeleteTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTagRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTagResponse:
        """
        @summary You can call this operation to delete a tag group.
        
        @param request: DeleteTagRequest
        @return: DeleteTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def delete_tag_value_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteTagValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTagValueResponse:
        """
        @summary You can call this operation to delete a tag from a tag group.
        
        @param request: DeleteTagValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTagValue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTagValueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTagValueResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_tag_value_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTagValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTagValueResponse:
        """
        @summary You can call this operation to delete a tag from a tag group.
        
        @param request: DeleteTagValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTagValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTagValue',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTagValueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTagValueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_tag_value(
        self,
        request: ocean_base_pro_20190901_models.DeleteTagValueRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTagValueResponse:
        """
        @summary You can call this operation to delete a tag from a tag group.
        
        @param request: DeleteTagValueRequest
        @return: DeleteTagValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_value_with_options(request, runtime)

    async def delete_tag_value_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTagValueRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTagValueResponse:
        """
        @summary You can call this operation to delete a tag from a tag group.
        
        @param request: DeleteTagValueRequest
        @return: DeleteTagValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_value_with_options_async(request, runtime)

    def delete_tenant_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to delete the information on the whitelist group of the tenant.
        
        @param request: DeleteTenantSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTenantSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_tenant_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to delete the information on the whitelist group of the tenant.
        
        @param request: DeleteTenantSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTenantSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_tenant_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to delete the information on the whitelist group of the tenant.
        
        @param request: DeleteTenantSecurityIpGroupRequest
        @return: DeleteTenantSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tenant_security_ip_group_with_options(request, runtime)

    async def delete_tenant_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to delete the information on the whitelist group of the tenant.
        
        @param request: DeleteTenantSecurityIpGroupRequest
        @return: DeleteTenantSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tenant_security_ip_group_with_options_async(request, runtime)

    def delete_tenant_users_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantUsersResponse:
        """
        @summary You can call this operation to delete one or more database accounts.
        
        @param request: DeleteTenantUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTenantUsersResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantUsersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantUsersResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_tenant_users_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantUsersResponse:
        """
        @summary You can call this operation to delete one or more database accounts.
        
        @param request: DeleteTenantUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTenantUsersResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantUsersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantUsersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_tenant_users(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantUsersRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantUsersResponse:
        """
        @summary You can call this operation to delete one or more database accounts.
        
        @param request: DeleteTenantUsersRequest
        @return: DeleteTenantUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tenant_users_with_options(request, runtime)

    async def delete_tenant_users_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantUsersRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantUsersResponse:
        """
        @summary You can call this operation to delete one or more database accounts.
        
        @param request: DeleteTenantUsersRequest
        @return: DeleteTenantUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tenant_users_with_options_async(request, runtime)

    def delete_tenants_with_options(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantsResponse:
        """
        @summary The return result of the request.
        
        @param request: DeleteTenantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTenantsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantsResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_tenants_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DeleteTenantsResponse:
        """
        @summary The return result of the request.
        
        @param request: DeleteTenantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTenantsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DeleteTenantsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_tenants(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantsResponse:
        """
        @summary The return result of the request.
        
        @param request: DeleteTenantsRequest
        @return: DeleteTenantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tenants_with_options(request, runtime)

    async def delete_tenants_async(
        self,
        request: ocean_base_pro_20190901_models.DeleteTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DeleteTenantsResponse:
        """
        @summary The return result of the request.
        
        @param request: DeleteTenantsRequest
        @return: DeleteTenantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tenants_with_options_async(request, runtime)

    def describe_anomaly_sqllist_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeAnomalySQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse:
        """
        @summary You can call this operation to obtain the list of SQL statements that may have performance problems according to the diagnostic system.
        
        @param tmp_req: DescribeAnomalySQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAnomalySQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_anomaly_sqllist_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeAnomalySQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse:
        """
        @summary You can call this operation to obtain the list of SQL statements that may have performance problems according to the diagnostic system.
        
        @param tmp_req: DescribeAnomalySQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAnomalySQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_anomaly_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeAnomalySQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse:
        """
        @summary You can call this operation to obtain the list of SQL statements that may have performance problems according to the diagnostic system.
        
        @param request: DescribeAnomalySQLListRequest
        @return: DescribeAnomalySQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_anomaly_sqllist_with_options(request, runtime)

    async def describe_anomaly_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAnomalySQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse:
        """
        @summary You can call this operation to obtain the list of SQL statements that may have performance problems according to the diagnostic system.
        
        @param request: DescribeAnomalySQLListRequest
        @return: DescribeAnomalySQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_anomaly_sqllist_with_options_async(request, runtime)

    def describe_available_cpu_resource_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableCpuResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse:
        """
        @summary The maximum number of CPU cores per resource unit.
        
        @param request: DescribeAvailableCpuResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableCpuResourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_available_cpu_resource_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableCpuResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse:
        """
        @summary The maximum number of CPU cores per resource unit.
        
        @param request: DescribeAvailableCpuResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableCpuResourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_available_cpu_resource(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableCpuResourceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse:
        """
        @summary The maximum number of CPU cores per resource unit.
        
        @param request: DescribeAvailableCpuResourceRequest
        @return: DescribeAvailableCpuResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cpu_resource_with_options(request, runtime)

    async def describe_available_cpu_resource_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableCpuResourceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse:
        """
        @summary The maximum number of CPU cores per resource unit.
        
        @param request: DescribeAvailableCpuResourceRequest
        @return: DescribeAvailableCpuResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_cpu_resource_with_options_async(request, runtime)

    def describe_available_mem_resource_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableMemResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse:
        """
        @summary You can call this operation to query the available memory resource of an OceanBase Database tenant.
        
        @param request: DescribeAvailableMemResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableMemResourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_available_mem_resource_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableMemResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse:
        """
        @summary You can call this operation to query the available memory resource of an OceanBase Database tenant.
        
        @param request: DescribeAvailableMemResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableMemResourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_available_mem_resource(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableMemResourceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse:
        """
        @summary You can call this operation to query the available memory resource of an OceanBase Database tenant.
        
        @param request: DescribeAvailableMemResourceRequest
        @return: DescribeAvailableMemResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_mem_resource_with_options(request, runtime)

    async def describe_available_mem_resource_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableMemResourceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse:
        """
        @summary You can call this operation to query the available memory resource of an OceanBase Database tenant.
        
        @param request: DescribeAvailableMemResourceRequest
        @return: DescribeAvailableMemResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_mem_resource_with_options_async(request, runtime)

    def describe_available_spec_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableSpecResponse:
        """
        @summary 获取集群变配页可选配置
        
        @param request: DescribeAvailableSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableSpecResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableSpecResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableSpecResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_available_spec_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableSpecResponse:
        """
        @summary 获取集群变配页可选配置
        
        @param request: DescribeAvailableSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableSpecResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableSpecResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableSpecResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_available_spec(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableSpecRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableSpecResponse:
        """
        @summary 获取集群变配页可选配置
        
        @param request: DescribeAvailableSpecRequest
        @return: DescribeAvailableSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_spec_with_options(request, runtime)

    async def describe_available_spec_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableSpecRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableSpecResponse:
        """
        @summary 获取集群变配页可选配置
        
        @param request: DescribeAvailableSpecRequest
        @return: DescribeAvailableSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_spec_with_options_async(request, runtime)

    def describe_available_zone_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableZoneResponse:
        """
        @summary 获取集群售卖页可选配置
        
        @param request: DescribeAvailableZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableZoneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_arch):
            body['CpuArch'] = request.cpu_arch
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableZoneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableZoneResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_available_zone_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableZoneResponse:
        """
        @summary 获取集群售卖页可选配置
        
        @param request: DescribeAvailableZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableZoneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_arch):
            body['CpuArch'] = request.cpu_arch
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableZoneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeAvailableZoneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_available_zone(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableZoneRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableZoneResponse:
        """
        @summary 获取集群售卖页可选配置
        
        @param request: DescribeAvailableZoneRequest
        @return: DescribeAvailableZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_zone_with_options(request, runtime)

    async def describe_available_zone_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeAvailableZoneRequest,
    ) -> ocean_base_pro_20190901_models.DescribeAvailableZoneResponse:
        """
        @summary 获取集群售卖页可选配置
        
        @param request: DescribeAvailableZoneRequest
        @return: DescribeAvailableZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_zone_with_options_async(request, runtime)

    def describe_backup_encrypted_string_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupEncryptedStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeBackupEncryptedStringResponse:
        """
        @summary DescribeBackupEncryptedString
        
        @param request: DescribeBackupEncryptedStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupEncryptedStringResponse
        """
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
            action='DescribeBackupEncryptedString',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeBackupEncryptedStringResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeBackupEncryptedStringResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_backup_encrypted_string_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupEncryptedStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeBackupEncryptedStringResponse:
        """
        @summary DescribeBackupEncryptedString
        
        @param request: DescribeBackupEncryptedStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupEncryptedStringResponse
        """
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
            action='DescribeBackupEncryptedString',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeBackupEncryptedStringResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeBackupEncryptedStringResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_backup_encrypted_string(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupEncryptedStringRequest,
    ) -> ocean_base_pro_20190901_models.DescribeBackupEncryptedStringResponse:
        """
        @summary DescribeBackupEncryptedString
        
        @param request: DescribeBackupEncryptedStringRequest
        @return: DescribeBackupEncryptedStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_encrypted_string_with_options(request, runtime)

    async def describe_backup_encrypted_string_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupEncryptedStringRequest,
    ) -> ocean_base_pro_20190901_models.DescribeBackupEncryptedStringResponse:
        """
        @summary DescribeBackupEncryptedString
        
        @param request: DescribeBackupEncryptedStringRequest
        @return: DescribeBackupEncryptedStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_encrypted_string_with_options_async(request, runtime)

    def describe_backup_set_download_link_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse:
        """
        @summary You can call this operation to query the link for downloading a backup set of OceanBase Database.
        
        @param request: DescribeBackupSetDownloadLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupSetDownloadLinkResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_backup_set_download_link_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse:
        """
        @summary You can call this operation to query the link for downloading a backup set of OceanBase Database.
        
        @param request: DescribeBackupSetDownloadLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupSetDownloadLinkResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_backup_set_download_link(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkRequest,
    ) -> ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse:
        """
        @summary You can call this operation to query the link for downloading a backup set of OceanBase Database.
        
        @param request: DescribeBackupSetDownloadLinkRequest
        @return: DescribeBackupSetDownloadLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_set_download_link_with_options(request, runtime)

    async def describe_backup_set_download_link_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkRequest,
    ) -> ocean_base_pro_20190901_models.DescribeBackupSetDownloadLinkResponse:
        """
        @summary You can call this operation to query the link for downloading a backup set of OceanBase Database.
        
        @param request: DescribeBackupSetDownloadLinkRequest
        @return: DescribeBackupSetDownloadLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_set_download_link_with_options_async(request, runtime)

    def describe_charset_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeCharsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeCharsetResponse:
        """
        @summary You can call this operation to query the character sets of an OceanBase Database tenant.
        
        @param request: DescribeCharsetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCharsetResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeCharsetResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeCharsetResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_charset_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeCharsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeCharsetResponse:
        """
        @summary You can call this operation to query the character sets of an OceanBase Database tenant.
        
        @param request: DescribeCharsetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCharsetResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeCharsetResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeCharsetResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_charset(
        self,
        request: ocean_base_pro_20190901_models.DescribeCharsetRequest,
    ) -> ocean_base_pro_20190901_models.DescribeCharsetResponse:
        """
        @summary You can call this operation to query the character sets of an OceanBase Database tenant.
        
        @param request: DescribeCharsetRequest
        @return: DescribeCharsetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_charset_with_options(request, runtime)

    async def describe_charset_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeCharsetRequest,
    ) -> ocean_base_pro_20190901_models.DescribeCharsetResponse:
        """
        @summary You can call this operation to query the character sets of an OceanBase Database tenant.
        
        @param request: DescribeCharsetRequest
        @return: DescribeCharsetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_charset_with_options_async(request, runtime)

    def describe_data_backup_set_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeDataBackupSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeDataBackupSetResponse:
        """
        @summary 查询备份集信息
        
        @param request: DescribeDataBackupSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataBackupSetResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeDataBackupSetResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeDataBackupSetResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_data_backup_set_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeDataBackupSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeDataBackupSetResponse:
        """
        @summary 查询备份集信息
        
        @param request: DescribeDataBackupSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataBackupSetResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeDataBackupSetResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeDataBackupSetResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_data_backup_set(
        self,
        request: ocean_base_pro_20190901_models.DescribeDataBackupSetRequest,
    ) -> ocean_base_pro_20190901_models.DescribeDataBackupSetResponse:
        """
        @summary 查询备份集信息
        
        @param request: DescribeDataBackupSetRequest
        @return: DescribeDataBackupSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_backup_set_with_options(request, runtime)

    async def describe_data_backup_set_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeDataBackupSetRequest,
    ) -> ocean_base_pro_20190901_models.DescribeDataBackupSetResponse:
        """
        @summary 查询备份集信息
        
        @param request: DescribeDataBackupSetRequest
        @return: DescribeDataBackupSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_backup_set_with_options_async(request, runtime)

    def describe_databases_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeDatabasesResponse:
        """
        @summary You can call this operation to query databases in a tenant.
        
        @param request: DescribeDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabasesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeDatabasesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeDatabasesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_databases_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeDatabasesResponse:
        """
        @summary You can call this operation to query databases in a tenant.
        
        @param request: DescribeDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabasesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeDatabasesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeDatabasesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_databases(
        self,
        request: ocean_base_pro_20190901_models.DescribeDatabasesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeDatabasesResponse:
        """
        @summary You can call this operation to query databases in a tenant.
        
        @param request: DescribeDatabasesRequest
        @return: DescribeDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    async def describe_databases_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeDatabasesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeDatabasesResponse:
        """
        @summary You can call this operation to query databases in a tenant.
        
        @param request: DescribeDatabasesRequest
        @return: DescribeDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_databases_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceResponse:
        """
        @summary You can call this operation to query the detailed information of an OceanBase cluster.
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceResponse:
        """
        @summary You can call this operation to query the detailed information of an OceanBase cluster.
        
        @param request: DescribeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceResponse:
        """
        @summary You can call this operation to query the detailed information of an OceanBase cluster.
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceResponse:
        """
        @summary You can call this operation to query the detailed information of an OceanBase cluster.
        
        @param request: DescribeInstanceRequest
        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_instance_creatable_zone_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse:
        """
        @summary The ID of the zone.
        
        @param request: DescribeInstanceCreatableZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceCreatableZoneResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_creatable_zone_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse:
        """
        @summary The ID of the zone.
        
        @param request: DescribeInstanceCreatableZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceCreatableZoneResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_creatable_zone(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse:
        """
        @summary The ID of the zone.
        
        @param request: DescribeInstanceCreatableZoneRequest
        @return: DescribeInstanceCreatableZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_creatable_zone_with_options(request, runtime)

    async def describe_instance_creatable_zone_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse:
        """
        @summary The ID of the zone.
        
        @param request: DescribeInstanceCreatableZoneRequest
        @return: DescribeInstanceCreatableZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_creatable_zone_with_options_async(request, runtime)

    def describe_instance_sslwith_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSSLResponse:
        """
        @summary 查询集群SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSSLResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSSLResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSSLResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_sslwith_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSSLResponse:
        """
        @summary 查询集群SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSSLResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSSLResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSSLResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_ssl(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSSLRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSSLResponse:
        """
        @summary 查询集群SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @return: DescribeInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sslwith_options(request, runtime)

    async def describe_instance_ssl_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSSLRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSSLResponse:
        """
        @summary 查询集群SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @return: DescribeInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_sslwith_options_async(request, runtime)

    def describe_instance_security_configs_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse:
        """
        @summary You can call this operation to query security check items of an OceanBase cluster.
        
        @param request: DescribeInstanceSecurityConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSecurityConfigsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_security_configs_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse:
        """
        @summary You can call this operation to query security check items of an OceanBase cluster.
        
        @param request: DescribeInstanceSecurityConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSecurityConfigsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_security_configs(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse:
        """
        @summary You can call this operation to query security check items of an OceanBase cluster.
        
        @param request: DescribeInstanceSecurityConfigsRequest
        @return: DescribeInstanceSecurityConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_security_configs_with_options(request, runtime)

    async def describe_instance_security_configs_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse:
        """
        @summary You can call this operation to query security check items of an OceanBase cluster.
        
        @param request: DescribeInstanceSecurityConfigsRequest
        @return: DescribeInstanceSecurityConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_security_configs_with_options_async(request, runtime)

    def describe_instance_summary_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSummaryResponse:
        """
        @summary Obtains the overview information about OceanBase instances.
        
        @param request: DescribeInstanceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSummary',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSummaryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSummaryResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_summary_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSummaryResponse:
        """
        @summary Obtains the overview information about OceanBase instances.
        
        @param request: DescribeInstanceSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSummary',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSummaryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceSummaryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_summary(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSummaryRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSummaryResponse:
        """
        @summary Obtains the overview information about OceanBase instances.
        
        @param request: DescribeInstanceSummaryRequest
        @return: DescribeInstanceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_summary_with_options(request, runtime)

    async def describe_instance_summary_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceSummaryRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceSummaryResponse:
        """
        @summary Obtains the overview information about OceanBase instances.
        
        @param request: DescribeInstanceSummaryRequest
        @return: DescribeInstanceSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_summary_with_options_async(request, runtime)

    def describe_instance_tags_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTagsResponse:
        """
        @summary You can call this operation to query the tags of clusters.
        
        @param request: DescribeInstanceTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTagsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTagsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_tags_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTagsResponse:
        """
        @summary You can call this operation to query the tags of clusters.
        
        @param request: DescribeInstanceTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTagsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTagsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_tags(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTagsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTagsResponse:
        """
        @summary You can call this operation to query the tags of clusters.
        
        @param request: DescribeInstanceTagsRequest
        @return: DescribeInstanceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_tags_with_options(request, runtime)

    async def describe_instance_tags_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTagsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTagsResponse:
        """
        @summary You can call this operation to query the tags of clusters.
        
        @param request: DescribeInstanceTagsRequest
        @return: DescribeInstanceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_tags_with_options_async(request, runtime)

    def describe_instance_tenant_modes_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTenantModesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse:
        """
        @summary The return result of the request.
        
        @param request: DescribeInstanceTenantModesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceTenantModesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_tenant_modes_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTenantModesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse:
        """
        @summary The return result of the request.
        
        @param request: DescribeInstanceTenantModesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceTenantModesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_tenant_modes(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTenantModesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse:
        """
        @summary The return result of the request.
        
        @param request: DescribeInstanceTenantModesRequest
        @return: DescribeInstanceTenantModesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_tenant_modes_with_options(request, runtime)

    async def describe_instance_tenant_modes_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTenantModesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse:
        """
        @summary The return result of the request.
        
        @param request: DescribeInstanceTenantModesRequest
        @return: DescribeInstanceTenantModesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_tenant_modes_with_options_async(request, runtime)

    def describe_instance_topology_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse:
        """
        @summary You can call this operation to query the topology of an OceanBase cluster.
        
        @param request: DescribeInstanceTopologyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceTopologyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instance_topology_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse:
        """
        @summary You can call this operation to query the topology of an OceanBase cluster.
        
        @param request: DescribeInstanceTopologyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceTopologyResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instance_topology(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTopologyRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse:
        """
        @summary You can call this operation to query the topology of an OceanBase cluster.
        
        @param request: DescribeInstanceTopologyRequest
        @return: DescribeInstanceTopologyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_topology_with_options(request, runtime)

    async def describe_instance_topology_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstanceTopologyRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse:
        """
        @summary You can call this operation to query the topology of an OceanBase cluster.
        
        @param request: DescribeInstanceTopologyRequest
        @return: DescribeInstanceTopologyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_topology_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstancesResponse:
        """
        @summary You can call this operation to obtain the list of OceanBase clusters.
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instances_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeInstancesResponse:
        """
        @summary You can call this operation to obtain the list of OceanBase clusters.
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instances(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstancesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstancesResponse:
        """
        @summary You can call this operation to obtain the list of OceanBase clusters.
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeInstancesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeInstancesResponse:
        """
        @summary You can call this operation to obtain the list of OceanBase clusters.
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_metrics_data_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeMetricsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeMetricsDataResponse:
        """
        @summary 查询监控指标数据
        
        @param request: DescribeMetricsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricsDataResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeMetricsDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeMetricsDataResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_metrics_data_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeMetricsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeMetricsDataResponse:
        """
        @summary 查询监控指标数据
        
        @param request: DescribeMetricsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetricsDataResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeMetricsDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeMetricsDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_metrics_data(
        self,
        request: ocean_base_pro_20190901_models.DescribeMetricsDataRequest,
    ) -> ocean_base_pro_20190901_models.DescribeMetricsDataResponse:
        """
        @summary 查询监控指标数据
        
        @param request: DescribeMetricsDataRequest
        @return: DescribeMetricsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metrics_data_with_options(request, runtime)

    async def describe_metrics_data_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeMetricsDataRequest,
    ) -> ocean_base_pro_20190901_models.DescribeMetricsDataResponse:
        """
        @summary 查询监控指标数据
        
        @param request: DescribeMetricsDataRequest
        @return: DescribeMetricsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metrics_data_with_options_async(request, runtime)

    def describe_node_metrics_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeNodeMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeNodeMetricsResponse:
        """
        @summary The list of nodes.
        
        @param request: DescribeNodeMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeMetricsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeNodeMetricsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeNodeMetricsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_node_metrics_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeNodeMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeNodeMetricsResponse:
        """
        @summary The list of nodes.
        
        @param request: DescribeNodeMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeMetricsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeNodeMetricsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeNodeMetricsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_node_metrics(
        self,
        request: ocean_base_pro_20190901_models.DescribeNodeMetricsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeNodeMetricsResponse:
        """
        @summary The list of nodes.
        
        @param request: DescribeNodeMetricsRequest
        @return: DescribeNodeMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_node_metrics_with_options(request, runtime)

    async def describe_node_metrics_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeNodeMetricsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeNodeMetricsResponse:
        """
        @summary The list of nodes.
        
        @param request: DescribeNodeMetricsRequest
        @return: DescribeNodeMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_metrics_with_options_async(request, runtime)

    def describe_oas_anomaly_sqllist_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasAnomalySQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse:
        """
        @summary You can call this API to view the list of SQL statements that are identified as having performance issues by the diagnostic system.
        
        @param request: DescribeOasAnomalySQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasAnomalySQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_oas_anomaly_sqllist_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasAnomalySQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse:
        """
        @summary You can call this API to view the list of SQL statements that are identified as having performance issues by the diagnostic system.
        
        @param request: DescribeOasAnomalySQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasAnomalySQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oas_anomaly_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasAnomalySQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse:
        """
        @summary You can call this API to view the list of SQL statements that are identified as having performance issues by the diagnostic system.
        
        @param request: DescribeOasAnomalySQLListRequest
        @return: DescribeOasAnomalySQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_anomaly_sqllist_with_options(request, runtime)

    async def describe_oas_anomaly_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasAnomalySQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasAnomalySQLListResponse:
        """
        @summary You can call this API to view the list of SQL statements that are identified as having performance issues by the diagnostic system.
        
        @param request: DescribeOasAnomalySQLListRequest
        @return: DescribeOasAnomalySQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_anomaly_sqllist_with_options_async(request, runtime)

    def describe_oas_sqldetails_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse:
        """
        @summary You can call this API to query detailed information about the SQL, including the SQL text, related table names, and so on.
        
        @param request: DescribeOasSQLDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasSQLDetailsResponse
        """
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
        if not UtilClient.is_unset(request.parse_table):
            body['ParseTable'] = request.parse_table
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_oas_sqldetails_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse:
        """
        @summary You can call this API to query detailed information about the SQL, including the SQL text, related table names, and so on.
        
        @param request: DescribeOasSQLDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasSQLDetailsResponse
        """
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
        if not UtilClient.is_unset(request.parse_table):
            body['ParseTable'] = request.parse_table
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oas_sqldetails(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLDetailsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse:
        """
        @summary You can call this API to query detailed information about the SQL, including the SQL text, related table names, and so on.
        
        @param request: DescribeOasSQLDetailsRequest
        @return: DescribeOasSQLDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_sqldetails_with_options(request, runtime)

    async def describe_oas_sqldetails_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLDetailsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLDetailsResponse:
        """
        @summary You can call this API to query detailed information about the SQL, including the SQL text, related table names, and so on.
        
        @param request: DescribeOasSQLDetailsRequest
        @return: DescribeOasSQLDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_sqldetails_with_options_async(request, runtime)

    def describe_oas_sqlhistory_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse:
        """
        @summary You can call this API to view the SQL execution history.
        
        @param request: DescribeOasSQLHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasSQLHistoryListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_oas_sqlhistory_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse:
        """
        @summary You can call this API to view the SQL execution history.
        
        @param request: DescribeOasSQLHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasSQLHistoryListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oas_sqlhistory_list(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse:
        """
        @summary You can call this API to view the SQL execution history.
        
        @param request: DescribeOasSQLHistoryListRequest
        @return: DescribeOasSQLHistoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_sqlhistory_list_with_options(request, runtime)

    async def describe_oas_sqlhistory_list_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLHistoryListResponse:
        """
        @summary You can call this API to view the SQL execution history.
        
        @param request: DescribeOasSQLHistoryListRequest
        @return: DescribeOasSQLHistoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_sqlhistory_list_with_options_async(request, runtime)

    def describe_oas_sqlplans_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse:
        """
        @summary You can call this API to retrieve information about the SQL execution plan stored in the diagnostic system based on the SQL ID.
        
        @param request: DescribeOasSQLPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasSQLPlansResponse
        """
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
        if not UtilClient.is_unset(request.plan_union_hash):
            body['PlanUnionHash'] = request.plan_union_hash
        if not UtilClient.is_unset(request.return_brief_info):
            body['ReturnBriefInfo'] = request.return_brief_info
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_oas_sqlplans_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse:
        """
        @summary You can call this API to retrieve information about the SQL execution plan stored in the diagnostic system based on the SQL ID.
        
        @param request: DescribeOasSQLPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasSQLPlansResponse
        """
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
        if not UtilClient.is_unset(request.plan_union_hash):
            body['PlanUnionHash'] = request.plan_union_hash
        if not UtilClient.is_unset(request.return_brief_info):
            body['ReturnBriefInfo'] = request.return_brief_info
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oas_sqlplans(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLPlansRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse:
        """
        @summary You can call this API to retrieve information about the SQL execution plan stored in the diagnostic system based on the SQL ID.
        
        @param request: DescribeOasSQLPlansRequest
        @return: DescribeOasSQLPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_sqlplans_with_options(request, runtime)

    async def describe_oas_sqlplans_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSQLPlansRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSQLPlansResponse:
        """
        @summary You can call this API to retrieve information about the SQL execution plan stored in the diagnostic system based on the SQL ID.
        
        @param request: DescribeOasSQLPlansRequest
        @return: DescribeOasSQLPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_sqlplans_with_options_async(request, runtime)

    def describe_oas_slow_sqllist_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSlowSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse:
        """
        @summary You can call this API to view a list of slow queries.
        
        @param request: DescribeOasSlowSQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasSlowSQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_oas_slow_sqllist_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSlowSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse:
        """
        @summary You can call this API to view a list of slow queries.
        
        @param request: DescribeOasSlowSQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasSlowSQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oas_slow_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSlowSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse:
        """
        @summary You can call this API to view a list of slow queries.
        
        @param request: DescribeOasSlowSQLListRequest
        @return: DescribeOasSlowSQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_slow_sqllist_with_options(request, runtime)

    async def describe_oas_slow_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasSlowSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasSlowSQLListResponse:
        """
        @summary You can call this API to view a list of slow queries.
        
        @param request: DescribeOasSlowSQLListRequest
        @return: DescribeOasSlowSQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_slow_sqllist_with_options_async(request, runtime)

    def describe_oas_top_sqllist_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasTopSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse:
        """
        @summary You can call this API to retrieve the list of data on the SQL execution performance collected by the diagnostic system.
        
        @param request: DescribeOasTopSQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasTopSQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_oas_top_sqllist_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasTopSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse:
        """
        @summary You can call this API to retrieve the list of data on the SQL execution performance collected by the diagnostic system.
        
        @param request: DescribeOasTopSQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOasTopSQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_oas_top_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasTopSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse:
        """
        @summary You can call this API to retrieve the list of data on the SQL execution performance collected by the diagnostic system.
        
        @param request: DescribeOasTopSQLListRequest
        @return: DescribeOasTopSQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oas_top_sqllist_with_options(request, runtime)

    async def describe_oas_top_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOasTopSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOasTopSQLListResponse:
        """
        @summary You can call this API to retrieve the list of data on the SQL execution performance collected by the diagnostic system.
        
        @param request: DescribeOasTopSQLListRequest
        @return: DescribeOasTopSQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oas_top_sqllist_with_options_async(request, runtime)

    def describe_outline_binding_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeOutlineBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOutlineBindingResponse:
        """
        @summary You can call this operation to query the outline binding information or throttling information of an SQL statement in the database based on an SQLID.
        
        @param request: DescribeOutlineBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOutlineBindingResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOutlineBindingResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOutlineBindingResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_outline_binding_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOutlineBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeOutlineBindingResponse:
        """
        @summary You can call this operation to query the outline binding information or throttling information of an SQL statement in the database based on an SQLID.
        
        @param request: DescribeOutlineBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOutlineBindingResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOutlineBindingResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeOutlineBindingResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_outline_binding(
        self,
        request: ocean_base_pro_20190901_models.DescribeOutlineBindingRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOutlineBindingResponse:
        """
        @summary You can call this operation to query the outline binding information or throttling information of an SQL statement in the database based on an SQLID.
        
        @param request: DescribeOutlineBindingRequest
        @return: DescribeOutlineBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_outline_binding_with_options(request, runtime)

    async def describe_outline_binding_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeOutlineBindingRequest,
    ) -> ocean_base_pro_20190901_models.DescribeOutlineBindingResponse:
        """
        @summary You can call this operation to query the outline binding information or throttling information of an SQL statement in the database based on an SQLID.
        
        @param request: DescribeOutlineBindingRequest
        @return: DescribeOutlineBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_outline_binding_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeParametersResponse:
        """
        @summary Indicates whether a restart is required for changes to the parameter to take effect. Valid values: - true: A restart is required. - false: A restart is not required.
        
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeParametersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeParametersResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_parameters_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeParametersResponse:
        """
        @summary Indicates whether a restart is required for changes to the parameter to take effect. Valid values: - true: A restart is required. - false: A restart is not required.
        
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeParametersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeParametersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_parameters(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersRequest,
    ) -> ocean_base_pro_20190901_models.DescribeParametersResponse:
        """
        @summary Indicates whether a restart is required for changes to the parameter to take effect. Valid values: - true: A restart is required. - false: A restart is not required.
        
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersRequest,
    ) -> ocean_base_pro_20190901_models.DescribeParametersResponse:
        """
        @summary Indicates whether a restart is required for changes to the parameter to take effect. Valid values: - true: A restart is required. - false: A restart is not required.
        
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_parameters_history_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeParametersHistoryResponse:
        """
        @summary You can call this operation to query the modification history of cluster or tenant parameters.
        
        @param request: DescribeParametersHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersHistoryResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeParametersHistoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeParametersHistoryResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_parameters_history_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeParametersHistoryResponse:
        """
        @summary You can call this operation to query the modification history of cluster or tenant parameters.
        
        @param request: DescribeParametersHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersHistoryResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeParametersHistoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeParametersHistoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_parameters_history(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersHistoryRequest,
    ) -> ocean_base_pro_20190901_models.DescribeParametersHistoryResponse:
        """
        @summary You can call this operation to query the modification history of cluster or tenant parameters.
        
        @param request: DescribeParametersHistoryRequest
        @return: DescribeParametersHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_history_with_options(request, runtime)

    async def describe_parameters_history_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeParametersHistoryRequest,
    ) -> ocean_base_pro_20190901_models.DescribeParametersHistoryResponse:
        """
        @summary You can call this operation to query the modification history of cluster or tenant parameters.
        
        @param request: DescribeParametersHistoryRequest
        @return: DescribeParametersHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_history_with_options_async(request, runtime)

    def describe_process_stats_composition_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProcessStatsCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProcessStatsCompositionResponse:
        """
        @summary You can call this operation to query session information.
        
        @param request: DescribeProcessStatsCompositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessStatsCompositionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.server_ip):
            body['ServerIp'] = request.server_ip
        if not UtilClient.is_unset(request.sql_text):
            body['SqlText'] = request.sql_text
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.uid):
            body['UId'] = request.uid
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProcessStatsComposition',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProcessStatsCompositionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProcessStatsCompositionResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_process_stats_composition_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProcessStatsCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProcessStatsCompositionResponse:
        """
        @summary You can call this operation to query session information.
        
        @param request: DescribeProcessStatsCompositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessStatsCompositionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.server_ip):
            body['ServerIp'] = request.server_ip
        if not UtilClient.is_unset(request.sql_text):
            body['SqlText'] = request.sql_text
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.uid):
            body['UId'] = request.uid
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProcessStatsComposition',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProcessStatsCompositionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProcessStatsCompositionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_process_stats_composition(
        self,
        request: ocean_base_pro_20190901_models.DescribeProcessStatsCompositionRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProcessStatsCompositionResponse:
        """
        @summary You can call this operation to query session information.
        
        @param request: DescribeProcessStatsCompositionRequest
        @return: DescribeProcessStatsCompositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_process_stats_composition_with_options(request, runtime)

    async def describe_process_stats_composition_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProcessStatsCompositionRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProcessStatsCompositionResponse:
        """
        @summary You can call this operation to query session information.
        
        @param request: DescribeProcessStatsCompositionRequest
        @return: DescribeProcessStatsCompositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_stats_composition_with_options_async(request, runtime)

    def describe_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectResponse:
        """
        @summary 查询项目详情
        
        @param request: DescribeProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectResponse:
        """
        @summary 查询项目详情
        
        @param request: DescribeProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_project(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectResponse:
        """
        @summary 查询项目详情
        
        @param request: DescribeProjectRequest
        @return: DescribeProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_with_options(request, runtime)

    async def describe_project_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectResponse:
        """
        @summary 查询项目详情
        
        @param request: DescribeProjectRequest
        @return: DescribeProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_with_options_async(request, runtime)

    def describe_project_components_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectComponentsResponse:
        """
        @summary 获取项目的组件信息
        
        @param request: DescribeProjectComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectComponentsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectComponentsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectComponentsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_project_components_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectComponentsResponse:
        """
        @summary 获取项目的组件信息
        
        @param request: DescribeProjectComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectComponentsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectComponentsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectComponentsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_project_components(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectComponentsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectComponentsResponse:
        """
        @summary 获取项目的组件信息
        
        @param request: DescribeProjectComponentsRequest
        @return: DescribeProjectComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_components_with_options(request, runtime)

    async def describe_project_components_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectComponentsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectComponentsResponse:
        """
        @summary 获取项目的组件信息
        
        @param request: DescribeProjectComponentsRequest
        @return: DescribeProjectComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_components_with_options_async(request, runtime)

    def describe_project_progress_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectProgressResponse:
        """
        @summary 获取迁移/同步项目 Progress 信息
        
        @param request: DescribeProjectProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectProgressResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectProgressResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectProgressResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_project_progress_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectProgressResponse:
        """
        @summary 获取迁移/同步项目 Progress 信息
        
        @param request: DescribeProjectProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectProgressResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectProgressResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectProgressResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_project_progress(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectProgressRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectProgressResponse:
        """
        @summary 获取迁移/同步项目 Progress 信息
        
        @param request: DescribeProjectProgressRequest
        @return: DescribeProjectProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_progress_with_options(request, runtime)

    async def describe_project_progress_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectProgressRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectProgressResponse:
        """
        @summary 获取迁移/同步项目 Progress 信息
        
        @param request: DescribeProjectProgressRequest
        @return: DescribeProjectProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_progress_with_options_async(request, runtime)

    def describe_project_step_metric_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse:
        """
        @summary 查询项目步骤指标
        
        @param request: DescribeProjectStepMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectStepMetricResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_project_step_metric_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse:
        """
        @summary 查询项目步骤指标
        
        @param request: DescribeProjectStepMetricRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectStepMetricResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_project_step_metric(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepMetricRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse:
        """
        @summary 查询项目步骤指标
        
        @param request: DescribeProjectStepMetricRequest
        @return: DescribeProjectStepMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_step_metric_with_options(request, runtime)

    async def describe_project_step_metric_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepMetricRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepMetricResponse:
        """
        @summary 查询项目步骤指标
        
        @param request: DescribeProjectStepMetricRequest
        @return: DescribeProjectStepMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_step_metric_with_options_async(request, runtime)

    def describe_project_steps_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepsResponse:
        """
        @summary 查询项目步骤
        
        @param request: DescribeProjectStepsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectStepsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectStepsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectStepsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_project_steps_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepsResponse:
        """
        @summary 查询项目步骤
        
        @param request: DescribeProjectStepsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectStepsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectStepsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProjectStepsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_project_steps(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepsResponse:
        """
        @summary 查询项目步骤
        
        @param request: DescribeProjectStepsRequest
        @return: DescribeProjectStepsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_project_steps_with_options(request, runtime)

    async def describe_project_steps_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProjectStepsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProjectStepsResponse:
        """
        @summary 查询项目步骤
        
        @param request: DescribeProjectStepsRequest
        @return: DescribeProjectStepsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_steps_with_options_async(request, runtime)

    def describe_proxy_service_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProxyServiceResponse:
        """
        @summary 查询代理服务信息
        
        @param request: DescribeProxyServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProxyServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProxyService',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProxyServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProxyServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_proxy_service_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProxyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeProxyServiceResponse:
        """
        @summary 查询代理服务信息
        
        @param request: DescribeProxyServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProxyServiceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProxyService',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProxyServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeProxyServiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_proxy_service(
        self,
        request: ocean_base_pro_20190901_models.DescribeProxyServiceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProxyServiceResponse:
        """
        @summary 查询代理服务信息
        
        @param request: DescribeProxyServiceRequest
        @return: DescribeProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_proxy_service_with_options(request, runtime)

    async def describe_proxy_service_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeProxyServiceRequest,
    ) -> ocean_base_pro_20190901_models.DescribeProxyServiceResponse:
        """
        @summary 查询代理服务信息
        
        @param request: DescribeProxyServiceRequest
        @return: DescribeProxyServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_proxy_service_with_options_async(request, runtime)

    def describe_recommend_index_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeRecommendIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeRecommendIndexResponse:
        """
        @summary The tenant mode.   Valid values:
        Oracle
        MySQL
        
        @param request: DescribeRecommendIndexRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecommendIndexResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeRecommendIndexResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeRecommendIndexResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_recommend_index_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeRecommendIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeRecommendIndexResponse:
        """
        @summary The tenant mode.   Valid values:
        Oracle
        MySQL
        
        @param request: DescribeRecommendIndexRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecommendIndexResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeRecommendIndexResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeRecommendIndexResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_recommend_index(
        self,
        request: ocean_base_pro_20190901_models.DescribeRecommendIndexRequest,
    ) -> ocean_base_pro_20190901_models.DescribeRecommendIndexResponse:
        """
        @summary The tenant mode.   Valid values:
        Oracle
        MySQL
        
        @param request: DescribeRecommendIndexRequest
        @return: DescribeRecommendIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_index_with_options(request, runtime)

    async def describe_recommend_index_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeRecommendIndexRequest,
    ) -> ocean_base_pro_20190901_models.DescribeRecommendIndexResponse:
        """
        @summary The tenant mode.   Valid values:
        Oracle
        MySQL
        
        @param request: DescribeRecommendIndexRequest
        @return: DescribeRecommendIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_recommend_index_with_options_async(request, runtime)

    def describe_restorable_tenants_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeRestorableTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeRestorableTenantsResponse:
        """
        @summary Queries information about restorable OceanBase Database tenants.
        
        @param request: DescribeRestorableTenantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestorableTenantsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_online):
            body['IsOnline'] = request.is_online
        if not UtilClient.is_unset(request.is_remote):
            body['IsRemote'] = request.is_remote
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.restore_mode):
            body['RestoreMode'] = request.restore_mode
        if not UtilClient.is_unset(request.restore_object_type):
            body['RestoreObjectType'] = request.restore_object_type
        if not UtilClient.is_unset(request.set_id):
            body['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRestorableTenants',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeRestorableTenantsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeRestorableTenantsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_restorable_tenants_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeRestorableTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeRestorableTenantsResponse:
        """
        @summary Queries information about restorable OceanBase Database tenants.
        
        @param request: DescribeRestorableTenantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestorableTenantsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_online):
            body['IsOnline'] = request.is_online
        if not UtilClient.is_unset(request.is_remote):
            body['IsRemote'] = request.is_remote
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.restore_mode):
            body['RestoreMode'] = request.restore_mode
        if not UtilClient.is_unset(request.restore_object_type):
            body['RestoreObjectType'] = request.restore_object_type
        if not UtilClient.is_unset(request.set_id):
            body['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRestorableTenants',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeRestorableTenantsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeRestorableTenantsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_restorable_tenants(
        self,
        request: ocean_base_pro_20190901_models.DescribeRestorableTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeRestorableTenantsResponse:
        """
        @summary Queries information about restorable OceanBase Database tenants.
        
        @param request: DescribeRestorableTenantsRequest
        @return: DescribeRestorableTenantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_restorable_tenants_with_options(request, runtime)

    async def describe_restorable_tenants_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeRestorableTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeRestorableTenantsResponse:
        """
        @summary Queries information about restorable OceanBase Database tenants.
        
        @param request: DescribeRestorableTenantsRequest
        @return: DescribeRestorableTenantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_restorable_tenants_with_options_async(request, runtime)

    def describe_sqldetails_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLDetailsResponse:
        """
        @summary The username.
        
        @param request: DescribeSQLDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLDetailsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLDetailsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLDetailsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sqldetails_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLDetailsResponse:
        """
        @summary The username.
        
        @param request: DescribeSQLDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLDetailsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLDetailsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLDetailsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sqldetails(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLDetailsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLDetailsResponse:
        """
        @summary The username.
        
        @param request: DescribeSQLDetailsRequest
        @return: DescribeSQLDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqldetails_with_options(request, runtime)

    async def describe_sqldetails_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLDetailsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLDetailsResponse:
        """
        @summary The username.
        
        @param request: DescribeSQLDetailsRequest
        @return: DescribeSQLDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqldetails_with_options_async(request, runtime)

    def describe_sqlhistory_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse:
        """
        @summary You can call this operation to query the execution history of an SQL statement in a specified period based on an SQL ID.
        
        @param request: DescribeSQLHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLHistoryListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sqlhistory_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse:
        """
        @summary You can call this operation to query the execution history of an SQL statement in a specified period based on an SQL ID.
        
        @param request: DescribeSQLHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLHistoryListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sqlhistory_list(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse:
        """
        @summary You can call this operation to query the execution history of an SQL statement in a specified period based on an SQL ID.
        
        @param request: DescribeSQLHistoryListRequest
        @return: DescribeSQLHistoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlhistory_list_with_options(request, runtime)

    async def describe_sqlhistory_list_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse:
        """
        @summary You can call this operation to query the execution history of an SQL statement in a specified period based on an SQL ID.
        
        @param request: DescribeSQLHistoryListRequest
        @return: DescribeSQLHistoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlhistory_list_with_options_async(request, runtime)

    def describe_sqlplans_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLPlansResponse:
        """
        @summary You can call this operation to query the information about the SQL execution plans stored in the diagnostic system based on an SQL ID.
        
        @param request: DescribeSQLPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLPlansResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLPlansResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLPlansResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sqlplans_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLPlansResponse:
        """
        @summary You can call this operation to query the information about the SQL execution plans stored in the diagnostic system based on an SQL ID.
        
        @param request: DescribeSQLPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLPlansResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLPlansResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLPlansResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sqlplans(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLPlansRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLPlansResponse:
        """
        @summary You can call this operation to query the information about the SQL execution plans stored in the diagnostic system based on an SQL ID.
        
        @param request: DescribeSQLPlansRequest
        @return: DescribeSQLPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlplans_with_options(request, runtime)

    async def describe_sqlplans_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLPlansRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLPlansResponse:
        """
        @summary You can call this operation to query the information about the SQL execution plans stored in the diagnostic system based on an SQL ID.
        
        @param request: DescribeSQLPlansRequest
        @return: DescribeSQLPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlplans_with_options_async(request, runtime)

    def describe_sqlsamples_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLSamplesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLSamplesResponse:
        """
        @summary You can call this API to view the sample data of the execution details of the slow queries.
        
        @param request: DescribeSQLSamplesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLSamplesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.return_sql_text):
            body['ReturnSqlText'] = request.return_sql_text
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLSamplesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLSamplesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sqlsamples_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLSamplesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLSamplesResponse:
        """
        @summary You can call this API to view the sample data of the execution details of the slow queries.
        
        @param request: DescribeSQLSamplesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLSamplesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.return_sql_text):
            body['ReturnSqlText'] = request.return_sql_text
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLSamplesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLSamplesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sqlsamples(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLSamplesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLSamplesResponse:
        """
        @summary You can call this API to view the sample data of the execution details of the slow queries.
        
        @param request: DescribeSQLSamplesRequest
        @return: DescribeSQLSamplesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlsamples_with_options(request, runtime)

    async def describe_sqlsamples_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLSamplesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLSamplesResponse:
        """
        @summary You can call this API to view the sample data of the execution details of the slow queries.
        
        @param request: DescribeSQLSamplesRequest
        @return: DescribeSQLSamplesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlsamples_with_options_async(request, runtime)

    def describe_sqltuning_advices_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesResponse:
        """
        @summary 获取单个 SQL 的调优建议，包括计划推荐和索引推荐
        
        @param request: DescribeSQLTuningAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLTuningAdvicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
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
            action='DescribeSQLTuningAdvices',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sqltuning_advices_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesResponse:
        """
        @summary 获取单个 SQL 的调优建议，包括计划推荐和索引推荐
        
        @param request: DescribeSQLTuningAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLTuningAdvicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
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
            action='DescribeSQLTuningAdvices',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sqltuning_advices(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesResponse:
        """
        @summary 获取单个 SQL 的调优建议，包括计划推荐和索引推荐
        
        @param request: DescribeSQLTuningAdvicesRequest
        @return: DescribeSQLTuningAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqltuning_advices_with_options(request, runtime)

    async def describe_sqltuning_advices_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSQLTuningAdvicesResponse:
        """
        @summary 获取单个 SQL 的调优建议，包括计划推荐和索引推荐
        
        @param request: DescribeSQLTuningAdvicesRequest
        @return: DescribeSQLTuningAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqltuning_advices_with_options_async(request, runtime)

    def describe_sample_sql_raw_texts_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse:
        """
        @summary 查询采样SQL的原始文本
        
        @param request: DescribeSampleSqlRawTextsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSampleSqlRawTextsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sample_sql_raw_texts_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse:
        """
        @summary 查询采样SQL的原始文本
        
        @param request: DescribeSampleSqlRawTextsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSampleSqlRawTextsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sample_sql_raw_texts(
        self,
        request: ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse:
        """
        @summary 查询采样SQL的原始文本
        
        @param request: DescribeSampleSqlRawTextsRequest
        @return: DescribeSampleSqlRawTextsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_sql_raw_texts_with_options(request, runtime)

    async def describe_sample_sql_raw_texts_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSampleSqlRawTextsResponse:
        """
        @summary 查询采样SQL的原始文本
        
        @param request: DescribeSampleSqlRawTextsRequest
        @return: DescribeSampleSqlRawTextsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sample_sql_raw_texts_with_options_async(request, runtime)

    def describe_security_ip_groups_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSecurityIpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse:
        """
        @summary The name of the security group.
        
        @param request: DescribeSecurityIpGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIpGroupsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_security_ip_groups_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSecurityIpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse:
        """
        @summary The name of the security group.
        
        @param request: DescribeSecurityIpGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIpGroupsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_security_ip_groups(
        self,
        request: ocean_base_pro_20190901_models.DescribeSecurityIpGroupsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse:
        """
        @summary The name of the security group.
        
        @param request: DescribeSecurityIpGroupsRequest
        @return: DescribeSecurityIpGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ip_groups_with_options(request, runtime)

    async def describe_security_ip_groups_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSecurityIpGroupsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse:
        """
        @summary The name of the security group.
        
        @param request: DescribeSecurityIpGroupsRequest
        @return: DescribeSecurityIpGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_ip_groups_with_options_async(request, runtime)

    def describe_session_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSessionListResponse:
        """
        @summary You can call this operation to query sessions between the ApsaraDB for OceanBase and the application.
        
        @param request: DescribeSessionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSessionListResponse
        """
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
            action='DescribeSessionList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSessionListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSessionListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_session_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSessionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSessionListResponse:
        """
        @summary You can call this operation to query sessions between the ApsaraDB for OceanBase and the application.
        
        @param request: DescribeSessionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSessionListResponse
        """
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
            action='DescribeSessionList',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSessionListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSessionListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_session_list(
        self,
        request: ocean_base_pro_20190901_models.DescribeSessionListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSessionListResponse:
        """
        @summary You can call this operation to query sessions between the ApsaraDB for OceanBase and the application.
        
        @param request: DescribeSessionListRequest
        @return: DescribeSessionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_session_list_with_options(request, runtime)

    async def describe_session_list_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSessionListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSessionListResponse:
        """
        @summary You can call this operation to query sessions between the ApsaraDB for OceanBase and the application.
        
        @param request: DescribeSessionListRequest
        @return: DescribeSessionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_session_list_with_options_async(request, runtime)

    def describe_slow_sqlhistory_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse:
        """
        @summary You can call this operation to query the execution history of an SQL statement by SQL ID that is determined as a slow SQL statement during a specified period of time.
        
        @param request: DescribeSlowSQLHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowSQLHistoryListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_slow_sqlhistory_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse:
        """
        @summary You can call this operation to query the execution history of an SQL statement by SQL ID that is determined as a slow SQL statement during a specified period of time.
        
        @param request: DescribeSlowSQLHistoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowSQLHistoryListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_slow_sqlhistory_list(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse:
        """
        @summary You can call this operation to query the execution history of an SQL statement by SQL ID that is determined as a slow SQL statement during a specified period of time.
        
        @param request: DescribeSlowSQLHistoryListRequest
        @return: DescribeSlowSQLHistoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_sqlhistory_list_with_options(request, runtime)

    async def describe_slow_sqlhistory_list_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse:
        """
        @summary You can call this operation to query the execution history of an SQL statement by SQL ID that is determined as a slow SQL statement during a specified period of time.
        
        @param request: DescribeSlowSQLHistoryListRequest
        @return: DescribeSlowSQLHistoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_sqlhistory_list_with_options_async(request, runtime)

    def describe_slow_sqllist_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeSlowSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLListResponse:
        """
        @summary You can call this operation to query the list of slow SQL statements
        
        @param tmp_req: DescribeSlowSQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowSQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSlowSQLListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSlowSQLListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_slow_sqllist_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeSlowSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLListResponse:
        """
        @summary You can call this operation to query the list of slow SQL statements
        
        @param tmp_req: DescribeSlowSQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowSQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSlowSQLListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeSlowSQLListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_slow_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLListResponse:
        """
        @summary You can call this operation to query the list of slow SQL statements
        
        @param request: DescribeSlowSQLListRequest
        @return: DescribeSlowSQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_sqllist_with_options(request, runtime)

    async def describe_slow_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeSlowSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeSlowSQLListResponse:
        """
        @summary You can call this operation to query the list of slow SQL statements
        
        @param request: DescribeSlowSQLListRequest
        @return: DescribeSlowSQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_sqllist_with_options_async(request, runtime)

    def describe_standby_create_mode_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeStandbyCreateModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeStandbyCreateModeResponse:
        """
        @summary DescribeStandbyCreateMode
        
        @param request: DescribeStandbyCreateModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStandbyCreateModeResponse
        """
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
            action='DescribeStandbyCreateMode',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeStandbyCreateModeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeStandbyCreateModeResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_standby_create_mode_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeStandbyCreateModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeStandbyCreateModeResponse:
        """
        @summary DescribeStandbyCreateMode
        
        @param request: DescribeStandbyCreateModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStandbyCreateModeResponse
        """
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
            action='DescribeStandbyCreateMode',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeStandbyCreateModeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeStandbyCreateModeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_standby_create_mode(
        self,
        request: ocean_base_pro_20190901_models.DescribeStandbyCreateModeRequest,
    ) -> ocean_base_pro_20190901_models.DescribeStandbyCreateModeResponse:
        """
        @summary DescribeStandbyCreateMode
        
        @param request: DescribeStandbyCreateModeRequest
        @return: DescribeStandbyCreateModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_standby_create_mode_with_options(request, runtime)

    async def describe_standby_create_mode_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeStandbyCreateModeRequest,
    ) -> ocean_base_pro_20190901_models.DescribeStandbyCreateModeResponse:
        """
        @summary DescribeStandbyCreateMode
        
        @param request: DescribeStandbyCreateModeRequest
        @return: DescribeStandbyCreateModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_standby_create_mode_with_options_async(request, runtime)

    def describe_tag_values_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTagValuesResponse:
        """
        @summary You can call this operation to query tags.
        
        @param request: DescribeTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagValuesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTagValues',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTagValuesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTagValuesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tag_values_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTagValuesResponse:
        """
        @summary You can call this operation to query tags.
        
        @param request: DescribeTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTagValuesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTagValues',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTagValuesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTagValuesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tag_values(
        self,
        request: ocean_base_pro_20190901_models.DescribeTagValuesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTagValuesResponse:
        """
        @summary You can call this operation to query tags.
        
        @param request: DescribeTagValuesRequest
        @return: DescribeTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_values_with_options(request, runtime)

    async def describe_tag_values_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTagValuesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTagValuesResponse:
        """
        @summary You can call this operation to query tags.
        
        @param request: DescribeTagValuesRequest
        @return: DescribeTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_values_with_options_async(request, runtime)

    def describe_tenant_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantResponse:
        """
        @summary You can call this operation to query the information of a specific tenant in a specific cluster.
        
        @param request: DescribeTenantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantResponse:
        """
        @summary You can call this operation to query the information of a specific tenant in a specific cluster.
        
        @param request: DescribeTenantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantResponse:
        """
        @summary You can call this operation to query the information of a specific tenant in a specific cluster.
        
        @param request: DescribeTenantRequest
        @return: DescribeTenantResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_with_options(request, runtime)

    async def describe_tenant_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantResponse:
        """
        @summary You can call this operation to query the information of a specific tenant in a specific cluster.
        
        @param request: DescribeTenantRequest
        @return: DescribeTenantResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_with_options_async(request, runtime)

    def describe_tenant_encryption_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantEncryptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse:
        """
        @summary 查询租户加密信息
        
        @param request: DescribeTenantEncryptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantEncryptionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_encryption_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantEncryptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse:
        """
        @summary 查询租户加密信息
        
        @param request: DescribeTenantEncryptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantEncryptionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant_encryption(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantEncryptionRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse:
        """
        @summary 查询租户加密信息
        
        @param request: DescribeTenantEncryptionRequest
        @return: DescribeTenantEncryptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_encryption_with_options(request, runtime)

    async def describe_tenant_encryption_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantEncryptionRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantEncryptionResponse:
        """
        @summary 查询租户加密信息
        
        @param request: DescribeTenantEncryptionRequest
        @return: DescribeTenantEncryptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_encryption_with_options_async(request, runtime)

    def describe_tenant_metrics_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantMetricsResponse:
        """
        @summary The list of tenant IDs.
        
        @param request: DescribeTenantMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantMetricsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantMetricsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantMetricsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_metrics_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantMetricsResponse:
        """
        @summary The list of tenant IDs.
        
        @param request: DescribeTenantMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantMetricsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantMetricsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantMetricsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant_metrics(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantMetricsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantMetricsResponse:
        """
        @summary The list of tenant IDs.
        
        @param request: DescribeTenantMetricsRequest
        @return: DescribeTenantMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_metrics_with_options(request, runtime)

    async def describe_tenant_metrics_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantMetricsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantMetricsResponse:
        """
        @summary The list of tenant IDs.
        
        @param request: DescribeTenantMetricsRequest
        @return: DescribeTenantMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_metrics_with_options_async(request, runtime)

    def describe_tenant_readable_scn_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantReadableScnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantReadableScnResponse:
        """
        @summary You can call this operation to query the maximum readable timestamp of a tenant.
        
        @param request: DescribeTenantReadableScnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantReadableScnResponse
        """
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
            action='DescribeTenantReadableScn',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantReadableScnResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantReadableScnResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_readable_scn_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantReadableScnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantReadableScnResponse:
        """
        @summary You can call this operation to query the maximum readable timestamp of a tenant.
        
        @param request: DescribeTenantReadableScnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantReadableScnResponse
        """
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
            action='DescribeTenantReadableScn',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantReadableScnResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantReadableScnResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant_readable_scn(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantReadableScnRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantReadableScnResponse:
        """
        @summary You can call this operation to query the maximum readable timestamp of a tenant.
        
        @param request: DescribeTenantReadableScnRequest
        @return: DescribeTenantReadableScnResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_readable_scn_with_options(request, runtime)

    async def describe_tenant_readable_scn_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantReadableScnRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantReadableScnResponse:
        """
        @summary You can call this operation to query the maximum readable timestamp of a tenant.
        
        @param request: DescribeTenantReadableScnRequest
        @return: DescribeTenantReadableScnResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_readable_scn_with_options_async(request, runtime)

    def describe_tenant_security_configs_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse:
        """
        @summary You can call this operation to query security check items of an OceanBase Database tenant.
        
        @param request: DescribeTenantSecurityConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantSecurityConfigsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_security_configs_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse:
        """
        @summary You can call this operation to query security check items of an OceanBase Database tenant.
        
        @param request: DescribeTenantSecurityConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantSecurityConfigsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant_security_configs(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse:
        """
        @summary You can call this operation to query security check items of an OceanBase Database tenant.
        
        @param request: DescribeTenantSecurityConfigsRequest
        @return: DescribeTenantSecurityConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_security_configs_with_options(request, runtime)

    async def describe_tenant_security_configs_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse:
        """
        @summary You can call this operation to query security check items of an OceanBase Database tenant.
        
        @param request: DescribeTenantSecurityConfigsRequest
        @return: DescribeTenantSecurityConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_security_configs_with_options_async(request, runtime)

    def describe_tenant_security_ip_groups_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse:
        """
        @summary You can call this operation to view the list of whitelist groups of the tenant.
        
        @param request: DescribeTenantSecurityIpGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantSecurityIpGroupsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_security_ip_groups_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse:
        """
        @summary You can call this operation to view the list of whitelist groups of the tenant.
        
        @param request: DescribeTenantSecurityIpGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantSecurityIpGroupsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant_security_ip_groups(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse:
        """
        @summary You can call this operation to view the list of whitelist groups of the tenant.
        
        @param request: DescribeTenantSecurityIpGroupsRequest
        @return: DescribeTenantSecurityIpGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_security_ip_groups_with_options(request, runtime)

    async def describe_tenant_security_ip_groups_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantSecurityIpGroupsResponse:
        """
        @summary You can call this operation to view the list of whitelist groups of the tenant.
        
        @param request: DescribeTenantSecurityIpGroupsRequest
        @return: DescribeTenantSecurityIpGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_security_ip_groups_with_options_async(request, runtime)

    def describe_tenant_tags_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantTagsResponse:
        """
        @summary You can call this operation to query the tags of tenants in a cluster.
        
        @param request: DescribeTenantTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantTagsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantTagsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_tags_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantTagsResponse:
        """
        @summary You can call this operation to query the tags of tenants in a cluster.
        
        @param request: DescribeTenantTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantTagsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantTagsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant_tags(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantTagsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantTagsResponse:
        """
        @summary You can call this operation to query the tags of tenants in a cluster.
        
        @param request: DescribeTenantTagsRequest
        @return: DescribeTenantTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_tags_with_options(request, runtime)

    async def describe_tenant_tags_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantTagsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantTagsResponse:
        """
        @summary You can call this operation to query the tags of tenants in a cluster.
        
        @param request: DescribeTenantTagsRequest
        @return: DescribeTenantTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_tags_with_options_async(request, runtime)

    def describe_tenant_user_roles_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse:
        """
        @summary You can call this operation to obtain the account authorization information of the tenant.
        
        @param request: DescribeTenantUserRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantUserRolesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_user_roles_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse:
        """
        @summary You can call this operation to obtain the account authorization information of the tenant.
        
        @param request: DescribeTenantUserRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantUserRolesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant_user_roles(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse:
        """
        @summary You can call this operation to obtain the account authorization information of the tenant.
        
        @param request: DescribeTenantUserRolesRequest
        @return: DescribeTenantUserRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_user_roles_with_options(request, runtime)

    async def describe_tenant_user_roles_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse:
        """
        @summary You can call this operation to obtain the account authorization information of the tenant.
        
        @param request: DescribeTenantUserRolesRequest
        @return: DescribeTenantUserRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_user_roles_with_options_async(request, runtime)

    def describe_tenant_users_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUsersResponse:
        """
        @summary The return result of the request.
        
        @param request: DescribeTenantUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantUsersResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantUsersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantUsersResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_users_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUsersResponse:
        """
        @summary The return result of the request.
        
        @param request: DescribeTenantUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantUsersResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantUsersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantUsersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant_users(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUsersRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUsersResponse:
        """
        @summary The return result of the request.
        
        @param request: DescribeTenantUsersRequest
        @return: DescribeTenantUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_users_with_options(request, runtime)

    async def describe_tenant_users_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantUsersRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantUsersResponse:
        """
        @summary The return result of the request.
        
        @param request: DescribeTenantUsersRequest
        @return: DescribeTenantUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_users_with_options_async(request, runtime)

    def describe_tenant_zones_read_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantZonesReadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse:
        """
        @summary Indicates whether a read-only connection has been created.
        
        @param request: DescribeTenantZonesReadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantZonesReadResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenant_zones_read_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantZonesReadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse:
        """
        @summary Indicates whether a read-only connection has been created.
        
        @param request: DescribeTenantZonesReadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantZonesReadResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenant_zones_read(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantZonesReadRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse:
        """
        @summary Indicates whether a read-only connection has been created.
        
        @param request: DescribeTenantZonesReadRequest
        @return: DescribeTenantZonesReadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_zones_read_with_options(request, runtime)

    async def describe_tenant_zones_read_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantZonesReadRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse:
        """
        @summary Indicates whether a read-only connection has been created.
        
        @param request: DescribeTenantZonesReadRequest
        @return: DescribeTenantZonesReadResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenant_zones_read_with_options_async(request, runtime)

    def describe_tenants_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantsResponse:
        """
        @summary You can call this operation to query the tenants in an OceanBase cluster.
        
        @param request: DescribeTenantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_tenants_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTenantsResponse:
        """
        @summary You can call this operation to query the tenants in an OceanBase cluster.
        
        @param request: DescribeTenantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTenantsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTenantsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_tenants(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantsResponse:
        """
        @summary You can call this operation to query the tenants in an OceanBase cluster.
        
        @param request: DescribeTenantsRequest
        @return: DescribeTenantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tenants_with_options(request, runtime)

    async def describe_tenants_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTenantsRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTenantsResponse:
        """
        @summary You can call this operation to query the tenants in an OceanBase cluster.
        
        @param request: DescribeTenantsRequest
        @return: DescribeTenantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tenants_with_options_async(request, runtime)

    def describe_time_zones_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTimeZonesResponse:
        """
        @summary The time zones supported by the tenant.
        
        @param request: DescribeTimeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTimeZonesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTimeZonesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTimeZonesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_time_zones_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTimeZonesResponse:
        """
        @summary The time zones supported by the tenant.
        
        @param request: DescribeTimeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTimeZonesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTimeZonesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTimeZonesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_time_zones(self) -> ocean_base_pro_20190901_models.DescribeTimeZonesResponse:
        """
        @summary The time zones supported by the tenant.
        
        @return: DescribeTimeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_time_zones_with_options(runtime)

    async def describe_time_zones_async(self) -> ocean_base_pro_20190901_models.DescribeTimeZonesResponse:
        """
        @summary The time zones supported by the tenant.
        
        @return: DescribeTimeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_time_zones_with_options_async(runtime)

    def describe_top_sqllist_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeTopSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTopSQLListResponse:
        """
        @summary The name of the database.
        
        @param tmp_req: DescribeTopSQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopSQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTopSQLListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTopSQLListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_top_sqllist_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.DescribeTopSQLListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeTopSQLListResponse:
        """
        @summary The name of the database.
        
        @param tmp_req: DescribeTopSQLListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopSQLListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTopSQLListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeTopSQLListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_top_sqllist(
        self,
        request: ocean_base_pro_20190901_models.DescribeTopSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTopSQLListResponse:
        """
        @summary The name of the database.
        
        @param request: DescribeTopSQLListRequest
        @return: DescribeTopSQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_top_sqllist_with_options(request, runtime)

    async def describe_top_sqllist_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeTopSQLListRequest,
    ) -> ocean_base_pro_20190901_models.DescribeTopSQLListResponse:
        """
        @summary The name of the database.
        
        @param request: DescribeTopSQLListRequest
        @return: DescribeTopSQLListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_sqllist_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: ocean_base_pro_20190901_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeZonesResponse:
        """
        @summary The deployment mode.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_arch):
            body['CpuArch'] = request.cpu_arch
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeZonesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeZonesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_zones_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.DescribeZonesResponse:
        """
        @summary The deployment mode.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_arch):
            body['CpuArch'] = request.cpu_arch
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeZonesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.DescribeZonesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_zones(
        self,
        request: ocean_base_pro_20190901_models.DescribeZonesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeZonesResponse:
        """
        @summary The deployment mode.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: ocean_base_pro_20190901_models.DescribeZonesRequest,
    ) -> ocean_base_pro_20190901_models.DescribeZonesResponse:
        """
        @summary The deployment mode.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def get_upload_oss_url_with_options(
        self,
        request: ocean_base_pro_20190901_models.GetUploadOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.GetUploadOssUrlResponse:
        """
        @summary 公有云上传OSS 获取一个临时上传url
        
        @param request: GetUploadOssUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadOssUrlResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.GetUploadOssUrlResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.GetUploadOssUrlResponse(),
                self.execute(params, req, runtime)
            )

    async def get_upload_oss_url_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.GetUploadOssUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.GetUploadOssUrlResponse:
        """
        @summary 公有云上传OSS 获取一个临时上传url
        
        @param request: GetUploadOssUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadOssUrlResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.GetUploadOssUrlResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.GetUploadOssUrlResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_upload_oss_url(
        self,
        request: ocean_base_pro_20190901_models.GetUploadOssUrlRequest,
    ) -> ocean_base_pro_20190901_models.GetUploadOssUrlResponse:
        """
        @summary 公有云上传OSS 获取一个临时上传url
        
        @param request: GetUploadOssUrlRequest
        @return: GetUploadOssUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_upload_oss_url_with_options(request, runtime)

    async def get_upload_oss_url_async(
        self,
        request: ocean_base_pro_20190901_models.GetUploadOssUrlRequest,
    ) -> ocean_base_pro_20190901_models.GetUploadOssUrlResponse:
        """
        @summary 公有云上传OSS 获取一个临时上传url
        
        @param request: GetUploadOssUrlRequest
        @return: GetUploadOssUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_oss_url_with_options_async(request, runtime)

    def kill_process_list_with_options(
        self,
        request: ocean_base_pro_20190901_models.KillProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.KillProcessListResponse:
        """
        @summary You can call this operation to close a session.
        
        @param request: KillProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.KillProcessListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.KillProcessListResponse(),
                self.execute(params, req, runtime)
            )

    async def kill_process_list_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.KillProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.KillProcessListResponse:
        """
        @summary You can call this operation to close a session.
        
        @param request: KillProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessListResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.KillProcessListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.KillProcessListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def kill_process_list(
        self,
        request: ocean_base_pro_20190901_models.KillProcessListRequest,
    ) -> ocean_base_pro_20190901_models.KillProcessListResponse:
        """
        @summary You can call this operation to close a session.
        
        @param request: KillProcessListRequest
        @return: KillProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_process_list_with_options(request, runtime)

    async def kill_process_list_async(
        self,
        request: ocean_base_pro_20190901_models.KillProcessListRequest,
    ) -> ocean_base_pro_20190901_models.KillProcessListResponse:
        """
        @summary You can call this operation to close a session.
        
        @param request: KillProcessListRequest
        @return: KillProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_process_list_with_options_async(request, runtime)

    def list_all_labels_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListAllLabelsResponse:
        """
        @summary 查询标签列表
        
        @param request: ListAllLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllLabelsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListAllLabelsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListAllLabelsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_all_labels_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListAllLabelsResponse:
        """
        @summary 查询标签列表
        
        @param request: ListAllLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllLabelsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListAllLabelsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListAllLabelsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_all_labels(self) -> ocean_base_pro_20190901_models.ListAllLabelsResponse:
        """
        @summary 查询标签列表
        
        @return: ListAllLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_labels_with_options(runtime)

    async def list_all_labels_async(self) -> ocean_base_pro_20190901_models.ListAllLabelsResponse:
        """
        @summary 查询标签列表
        
        @return: ListAllLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_labels_with_options_async(runtime)

    def list_data_source_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListDataSourceResponse:
        """
        @summary 查询数据源列表 (MySql、OB_MYSQL、OB_ORACLE)
        
        @param tmp_req: ListDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListDataSourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListDataSourceResponse(),
                self.execute(params, req, runtime)
            )

    async def list_data_source_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListDataSourceResponse:
        """
        @summary 查询数据源列表 (MySql、OB_MYSQL、OB_ORACLE)
        
        @param tmp_req: ListDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListDataSourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListDataSourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_data_source(
        self,
        request: ocean_base_pro_20190901_models.ListDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.ListDataSourceResponse:
        """
        @summary 查询数据源列表 (MySql、OB_MYSQL、OB_ORACLE)
        
        @param request: ListDataSourceRequest
        @return: ListDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_with_options(request, runtime)

    async def list_data_source_async(
        self,
        request: ocean_base_pro_20190901_models.ListDataSourceRequest,
    ) -> ocean_base_pro_20190901_models.ListDataSourceResponse:
        """
        @summary 查询数据源列表 (MySql、OB_MYSQL、OB_ORACLE)
        
        @param request: ListDataSourceRequest
        @return: ListDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_with_options_async(request, runtime)

    def list_project_full_verify_result_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListProjectFullVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse:
        """
        @summary 查询项目的全量校验结果
        
        @param tmp_req: ListProjectFullVerifyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectFullVerifyResultResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse(),
                self.execute(params, req, runtime)
            )

    async def list_project_full_verify_result_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListProjectFullVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse:
        """
        @summary 查询项目的全量校验结果
        
        @param tmp_req: ListProjectFullVerifyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectFullVerifyResultResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_project_full_verify_result(
        self,
        request: ocean_base_pro_20190901_models.ListProjectFullVerifyResultRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse:
        """
        @summary 查询项目的全量校验结果
        
        @param request: ListProjectFullVerifyResultRequest
        @return: ListProjectFullVerifyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_full_verify_result_with_options(request, runtime)

    async def list_project_full_verify_result_async(
        self,
        request: ocean_base_pro_20190901_models.ListProjectFullVerifyResultRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectFullVerifyResultResponse:
        """
        @summary 查询项目的全量校验结果
        
        @param request: ListProjectFullVerifyResultRequest
        @return: ListProjectFullVerifyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_project_full_verify_result_with_options_async(request, runtime)

    def list_project_modify_records_with_options(
        self,
        request: ocean_base_pro_20190901_models.ListProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse:
        """
        @summary 根据项目 ID 查询项目的修改记录
        
        @param request: ListProjectModifyRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectModifyRecordsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_project_modify_records_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ListProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse:
        """
        @summary 根据项目 ID 查询项目的修改记录
        
        @param request: ListProjectModifyRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectModifyRecordsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_project_modify_records(
        self,
        request: ocean_base_pro_20190901_models.ListProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse:
        """
        @summary 根据项目 ID 查询项目的修改记录
        
        @param request: ListProjectModifyRecordsRequest
        @return: ListProjectModifyRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_project_modify_records_with_options(request, runtime)

    async def list_project_modify_records_async(
        self,
        request: ocean_base_pro_20190901_models.ListProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectModifyRecordsResponse:
        """
        @summary 根据项目 ID 查询项目的修改记录
        
        @param request: ListProjectModifyRecordsRequest
        @return: ListProjectModifyRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_project_modify_records_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectsResponse:
        """
        @summary 查询项目列表
        
        @param tmp_req: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
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
        if not UtilClient.is_unset(request.need_related_info):
            body['NeedRelatedInfo'] = request.need_related_info
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_projects_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListProjectsResponse:
        """
        @summary 查询项目列表
        
        @param tmp_req: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
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
        if not UtilClient.is_unset(request.need_related_info):
            body['NeedRelatedInfo'] = request.need_related_info
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListProjectsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_projects(
        self,
        request: ocean_base_pro_20190901_models.ListProjectsRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectsResponse:
        """
        @summary 查询项目列表
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: ocean_base_pro_20190901_models.ListProjectsRequest,
    ) -> ocean_base_pro_20190901_models.ListProjectsResponse:
        """
        @summary 查询项目列表
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_worker_instances_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListWorkerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListWorkerInstancesResponse:
        """
        @summary 查询传输实例列表
        
        @param tmp_req: ListWorkerInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkerInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListWorkerInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListWorkerInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_worker_instances_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.ListWorkerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ListWorkerInstancesResponse:
        """
        @summary 查询传输实例列表
        
        @param tmp_req: ListWorkerInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkerInstancesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListWorkerInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ListWorkerInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_worker_instances(
        self,
        request: ocean_base_pro_20190901_models.ListWorkerInstancesRequest,
    ) -> ocean_base_pro_20190901_models.ListWorkerInstancesResponse:
        """
        @summary 查询传输实例列表
        
        @param request: ListWorkerInstancesRequest
        @return: ListWorkerInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_worker_instances_with_options(request, runtime)

    async def list_worker_instances_async(
        self,
        request: ocean_base_pro_20190901_models.ListWorkerInstancesRequest,
    ) -> ocean_base_pro_20190901_models.ListWorkerInstancesResponse:
        """
        @summary 查询传输实例列表
        
        @param request: ListWorkerInstancesRequest
        @return: ListWorkerInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_worker_instances_with_options_async(request, runtime)

    def modify_database_description_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse:
        """
        @summary The request ID.
        
        @param request: ModifyDatabaseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseDescriptionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_database_description_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse:
        """
        @summary The request ID.
        
        @param request: ModifyDatabaseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseDescriptionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_database_description(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseDescriptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse:
        """
        @summary The request ID.
        
        @param request: ModifyDatabaseDescriptionRequest
        @return: ModifyDatabaseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_database_description_with_options(request, runtime)

    async def modify_database_description_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseDescriptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse:
        """
        @summary The request ID.
        
        @param request: ModifyDatabaseDescriptionRequest
        @return: ModifyDatabaseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_description_with_options_async(request, runtime)

    def modify_database_user_roles_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse:
        """
        @summary The accounts that have privileges on the database.
        
        @param request: ModifyDatabaseUserRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseUserRolesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_database_user_roles_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse:
        """
        @summary The accounts that have privileges on the database.
        
        @param request: ModifyDatabaseUserRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseUserRolesResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_database_user_roles(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse:
        """
        @summary The accounts that have privileges on the database.
        
        @param request: ModifyDatabaseUserRolesRequest
        @return: ModifyDatabaseUserRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_database_user_roles_with_options(request, runtime)

    async def modify_database_user_roles_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyDatabaseUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse:
        """
        @summary The accounts that have privileges on the database.
        
        @param request: ModifyDatabaseUserRolesRequest
        @return: ModifyDatabaseUserRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_user_roles_with_options_async(request, runtime)

    def modify_instance_name_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNameResponse:
        """
        @summary The name of the OceanBase cluster.
        
        @param request: ModifyInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceNameResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceNameResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceNameResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_name_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNameResponse:
        """
        @summary The name of the OceanBase cluster.
        
        @param request: ModifyInstanceNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceNameResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceNameResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceNameResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance_name(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNameRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNameResponse:
        """
        @summary The name of the OceanBase cluster.
        
        @param request: ModifyInstanceNameRequest
        @return: ModifyInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    async def modify_instance_name_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNameRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNameResponse:
        """
        @summary The name of the OceanBase cluster.
        
        @param request: ModifyInstanceNameRequest
        @return: ModifyInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_name_with_options_async(request, runtime)

    def modify_instance_node_num_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNodeNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse:
        """
        @summary You can call this operation to modify the number of nodes in a cluster.
        
        @param request: ModifyInstanceNodeNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceNodeNumResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_node_num_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNodeNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse:
        """
        @summary You can call this operation to modify the number of nodes in a cluster.
        
        @param request: ModifyInstanceNodeNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceNodeNumResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance_node_num(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNodeNumRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse:
        """
        @summary You can call this operation to modify the number of nodes in a cluster.
        
        @param request: ModifyInstanceNodeNumRequest
        @return: ModifyInstanceNodeNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_node_num_with_options(request, runtime)

    async def modify_instance_node_num_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceNodeNumRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse:
        """
        @summary You can call this operation to modify the number of nodes in a cluster.
        
        @param request: ModifyInstanceNodeNumRequest
        @return: ModifyInstanceNodeNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_node_num_with_options_async(request, runtime)

    def modify_instance_sslwith_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSSLResponse:
        """
        @summary You can call this operation to modify the Secure Sockets Layer (SSL) setting for an OceanBase cluster instance.
        
        @description There is currently no authorization information disclosed in the API.
        
        @param request: ModifyInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_ssl):
            body['EnableSSL'] = request.enable_ssl
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceSSLResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceSSLResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_sslwith_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSSLResponse:
        """
        @summary You can call this operation to modify the Secure Sockets Layer (SSL) setting for an OceanBase cluster instance.
        
        @description There is currently no authorization information disclosed in the API.
        
        @param request: ModifyInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_ssl):
            body['EnableSSL'] = request.enable_ssl
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceSSLResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceSSLResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance_ssl(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSSLRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSSLResponse:
        """
        @summary You can call this operation to modify the Secure Sockets Layer (SSL) setting for an OceanBase cluster instance.
        
        @description There is currently no authorization information disclosed in the API.
        
        @param request: ModifyInstanceSSLRequest
        @return: ModifyInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_sslwith_options(request, runtime)

    async def modify_instance_ssl_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSSLRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSSLResponse:
        """
        @summary You can call this operation to modify the Secure Sockets Layer (SSL) setting for an OceanBase cluster instance.
        
        @description There is currently no authorization information disclosed in the API.
        
        @param request: ModifyInstanceSSLRequest
        @return: ModifyInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_sslwith_options_async(request, runtime)

    def modify_instance_spec_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSpecResponse:
        """
        @summary You can call this operation to modify the cluster specifications and storage space.
        
        @param request: ModifyInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSpecResponse
        """
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
        if not UtilClient.is_unset(request.upgrade_spec_native):
            body['UpgradeSpecNative'] = request.upgrade_spec_native
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceSpecResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceSpecResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_spec_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSpecResponse:
        """
        @summary You can call this operation to modify the cluster specifications and storage space.
        
        @param request: ModifyInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSpecResponse
        """
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
        if not UtilClient.is_unset(request.upgrade_spec_native):
            body['UpgradeSpecNative'] = request.upgrade_spec_native
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceSpecResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceSpecResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance_spec(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSpecRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSpecResponse:
        """
        @summary You can call this operation to modify the cluster specifications and storage space.
        
        @param request: ModifyInstanceSpecRequest
        @return: ModifyInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    async def modify_instance_spec_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceSpecRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceSpecResponse:
        """
        @summary You can call this operation to modify the cluster specifications and storage space.
        
        @param request: ModifyInstanceSpecRequest
        @return: ModifyInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_spec_with_options_async(request, runtime)

    def modify_instance_tags_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTagsResponse:
        """
        @summary You can call this operation to modify the tags of a cluster.
        
        @param request: ModifyInstanceTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceTagsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceTagsResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_tags_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTagsResponse:
        """
        @summary You can call this operation to modify the tags of a cluster.
        
        @param request: ModifyInstanceTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceTagsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceTagsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance_tags(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTagsRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTagsResponse:
        """
        @summary You can call this operation to modify the tags of a cluster.
        
        @param request: ModifyInstanceTagsRequest
        @return: ModifyInstanceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_tags_with_options(request, runtime)

    async def modify_instance_tags_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTagsRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTagsResponse:
        """
        @summary You can call this operation to modify the tags of a cluster.
        
        @param request: ModifyInstanceTagsRequest
        @return: ModifyInstanceTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_tags_with_options_async(request, runtime)

    def modify_instance_temporary_capacity_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse:
        """
        @summary You can call this operation to modify the temporary capacity of the OceanBase cluster.
        
        @param request: ModifyInstanceTemporaryCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceTemporaryCapacityResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_temporary_capacity_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse:
        """
        @summary You can call this operation to modify the temporary capacity of the OceanBase cluster.
        
        @param request: ModifyInstanceTemporaryCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceTemporaryCapacityResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance_temporary_capacity(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse:
        """
        @summary You can call this operation to modify the temporary capacity of the OceanBase cluster.
        
        @param request: ModifyInstanceTemporaryCapacityRequest
        @return: ModifyInstanceTemporaryCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_temporary_capacity_with_options(request, runtime)

    async def modify_instance_temporary_capacity_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityRequest,
    ) -> ocean_base_pro_20190901_models.ModifyInstanceTemporaryCapacityResponse:
        """
        @summary You can call this operation to modify the temporary capacity of the OceanBase cluster.
        
        @param request: ModifyInstanceTemporaryCapacityRequest
        @return: ModifyInstanceTemporaryCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_temporary_capacity_with_options_async(request, runtime)

    def modify_parameters_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyParametersResponse:
        """
        @summary The modification results.
        
        @param request: ModifyParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParametersResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyParametersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyParametersResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_parameters_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyParametersResponse:
        """
        @summary The modification results.
        
        @param request: ModifyParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParametersResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyParametersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyParametersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_parameters(
        self,
        request: ocean_base_pro_20190901_models.ModifyParametersRequest,
    ) -> ocean_base_pro_20190901_models.ModifyParametersResponse:
        """
        @summary The modification results.
        
        @param request: ModifyParametersRequest
        @return: ModifyParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    async def modify_parameters_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyParametersRequest,
    ) -> ocean_base_pro_20190901_models.ModifyParametersResponse:
        """
        @summary The modification results.
        
        @param request: ModifyParametersRequest
        @return: ModifyParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameters_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifySecurityIpsResponse:
        """
        @summary The name of the security group.
        
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifySecurityIpsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifySecurityIpsResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_security_ips_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifySecurityIpsResponse:
        """
        @summary The name of the security group.
        
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifySecurityIpsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifySecurityIpsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_security_ips(
        self,
        request: ocean_base_pro_20190901_models.ModifySecurityIpsRequest,
    ) -> ocean_base_pro_20190901_models.ModifySecurityIpsResponse:
        """
        @summary The name of the security group.
        
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: ocean_base_pro_20190901_models.ModifySecurityIpsRequest,
    ) -> ocean_base_pro_20190901_models.ModifySecurityIpsResponse:
        """
        @summary The name of the security group.
        
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_tag_name_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTagNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTagNameResponse:
        """
        @param request: ModifyTagNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTagNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.new_key):
            body['NewKey'] = request.new_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTagName',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTagNameResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTagNameResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tag_name_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTagNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTagNameResponse:
        """
        @param request: ModifyTagNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTagNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.new_key):
            body['NewKey'] = request.new_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTagName',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTagNameResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTagNameResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tag_name(
        self,
        request: ocean_base_pro_20190901_models.ModifyTagNameRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTagNameResponse:
        """
        @param request: ModifyTagNameRequest
        @return: ModifyTagNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_name_with_options(request, runtime)

    async def modify_tag_name_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTagNameRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTagNameResponse:
        """
        @param request: ModifyTagNameRequest
        @return: ModifyTagNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tag_name_with_options_async(request, runtime)

    def modify_tag_value_name_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTagValueNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTagValueNameResponse:
        """
        @summary You can call this operation to rename a tag.
        
        @param request: ModifyTagValueNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTagValueNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.new_value):
            body['NewValue'] = request.new_value
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTagValueName',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTagValueNameResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTagValueNameResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tag_value_name_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTagValueNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTagValueNameResponse:
        """
        @summary You can call this operation to rename a tag.
        
        @param request: ModifyTagValueNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTagValueNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.new_value):
            body['NewValue'] = request.new_value
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTagValueName',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTagValueNameResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTagValueNameResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tag_value_name(
        self,
        request: ocean_base_pro_20190901_models.ModifyTagValueNameRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTagValueNameResponse:
        """
        @summary You can call this operation to rename a tag.
        
        @param request: ModifyTagValueNameRequest
        @return: ModifyTagValueNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tag_value_name_with_options(request, runtime)

    async def modify_tag_value_name_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTagValueNameRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTagValueNameResponse:
        """
        @summary You can call this operation to rename a tag.
        
        @param request: ModifyTagValueNameRequest
        @return: ModifyTagValueNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tag_value_name_with_options_async(request, runtime)

    def modify_tenant_encryption_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantEncryptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse:
        """
        @summary 租户加密变更
        
        @param request: ModifyTenantEncryptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantEncryptionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tenant_encryption_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantEncryptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse:
        """
        @summary 租户加密变更
        
        @param request: ModifyTenantEncryptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantEncryptionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tenant_encryption(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantEncryptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse:
        """
        @summary 租户加密变更
        
        @param request: ModifyTenantEncryptionRequest
        @return: ModifyTenantEncryptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_encryption_with_options(request, runtime)

    async def modify_tenant_encryption_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantEncryptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantEncryptionResponse:
        """
        @summary 租户加密变更
        
        @param request: ModifyTenantEncryptionRequest
        @return: ModifyTenantEncryptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_encryption_with_options_async(request, runtime)

    def modify_tenant_primary_zone_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse:
        """
        @summary The return result of the request.
        
        @param request: ModifyTenantPrimaryZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantPrimaryZoneResponse
        """
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
        if not UtilClient.is_unset(request.user_vpc_owner_id):
            body['UserVpcOwnerId'] = request.user_vpc_owner_id
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tenant_primary_zone_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse:
        """
        @summary The return result of the request.
        
        @param request: ModifyTenantPrimaryZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantPrimaryZoneResponse
        """
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
        if not UtilClient.is_unset(request.user_vpc_owner_id):
            body['UserVpcOwnerId'] = request.user_vpc_owner_id
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tenant_primary_zone(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse:
        """
        @summary The return result of the request.
        
        @param request: ModifyTenantPrimaryZoneRequest
        @return: ModifyTenantPrimaryZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_primary_zone_with_options(request, runtime)

    async def modify_tenant_primary_zone_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse:
        """
        @summary The return result of the request.
        
        @param request: ModifyTenantPrimaryZoneRequest
        @return: ModifyTenantPrimaryZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_primary_zone_with_options_async(request, runtime)

    def modify_tenant_resource_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantResourceResponse:
        """
        @summary You can call this operation to modify the specifications of a tenant in an OceanBase cluster.
        
        @param request: ModifyTenantResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantResourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantResourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantResourceResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tenant_resource_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantResourceResponse:
        """
        @summary You can call this operation to modify the specifications of a tenant in an OceanBase cluster.
        
        @param request: ModifyTenantResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantResourceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantResourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantResourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tenant_resource(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantResourceRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantResourceResponse:
        """
        @summary You can call this operation to modify the specifications of a tenant in an OceanBase cluster.
        
        @param request: ModifyTenantResourceRequest
        @return: ModifyTenantResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_resource_with_options(request, runtime)

    async def modify_tenant_resource_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantResourceRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantResourceResponse:
        """
        @summary You can call this operation to modify the specifications of a tenant in an OceanBase cluster.
        
        @param request: ModifyTenantResourceRequest
        @return: ModifyTenantResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_resource_with_options_async(request, runtime)

    def modify_tenant_security_ip_group_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to modify the information on the whitelist group of the tenant.
        
        @param request: ModifyTenantSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tenant_security_ip_group_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to modify the information on the whitelist group of the tenant.
        
        @param request: ModifyTenantSecurityIpGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantSecurityIpGroupResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tenant_security_ip_group(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to modify the information on the whitelist group of the tenant.
        
        @param request: ModifyTenantSecurityIpGroupRequest
        @return: ModifyTenantSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_security_ip_group_with_options(request, runtime)

    async def modify_tenant_security_ip_group_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantSecurityIpGroupResponse:
        """
        @summary You can call this operation to modify the information on the whitelist group of the tenant.
        
        @param request: ModifyTenantSecurityIpGroupRequest
        @return: ModifyTenantSecurityIpGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_security_ip_group_with_options_async(request, runtime)

    def modify_tenant_tags_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantTagsResponse:
        """
        @summary You can call this operation to modify the tags of a tenant.
        
        @param request: ModifyTenantTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantTagsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantTagsResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tenant_tags_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantTagsResponse:
        """
        @summary You can call this operation to modify the tags of a tenant.
        
        @param request: ModifyTenantTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantTagsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantTagsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantTagsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tenant_tags(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantTagsRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantTagsResponse:
        """
        @summary You can call this operation to modify the tags of a tenant.
        
        @param request: ModifyTenantTagsRequest
        @return: ModifyTenantTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_tags_with_options(request, runtime)

    async def modify_tenant_tags_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantTagsRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantTagsResponse:
        """
        @summary You can call this operation to modify the tags of a tenant.
        
        @param request: ModifyTenantTagsRequest
        @return: ModifyTenantTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_tags_with_options_async(request, runtime)

    def modify_tenant_user_description_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse:
        """
        @summary The description of the database.
        
        @param request: ModifyTenantUserDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantUserDescriptionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tenant_user_description_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse:
        """
        @summary The description of the database.
        
        @param request: ModifyTenantUserDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantUserDescriptionResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tenant_user_description(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserDescriptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse:
        """
        @summary The description of the database.
        
        @param request: ModifyTenantUserDescriptionRequest
        @return: ModifyTenantUserDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_description_with_options(request, runtime)

    async def modify_tenant_user_description_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserDescriptionRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse:
        """
        @summary The description of the database.
        
        @param request: ModifyTenantUserDescriptionRequest
        @return: ModifyTenantUserDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_user_description_with_options_async(request, runtime)

    def modify_tenant_user_password_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse:
        """
        @summary The request ID.
        
        @param request: ModifyTenantUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantUserPasswordResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tenant_user_password_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse:
        """
        @summary The request ID.
        
        @param request: ModifyTenantUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantUserPasswordResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tenant_user_password(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserPasswordRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse:
        """
        @summary The request ID.
        
        @param request: ModifyTenantUserPasswordRequest
        @return: ModifyTenantUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_password_with_options(request, runtime)

    async def modify_tenant_user_password_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserPasswordRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse:
        """
        @summary The request ID.
        
        @param request: ModifyTenantUserPasswordRequest
        @return: ModifyTenantUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_user_password_with_options_async(request, runtime)

    def modify_tenant_user_roles_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse:
        """
        @summary Indicates whether the privilege was granted to the role.
        
        @param request: ModifyTenantUserRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantUserRolesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.global_permissions):
            body['GlobalPermissions'] = request.global_permissions
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
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tenant_user_roles_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse:
        """
        @summary Indicates whether the privilege was granted to the role.
        
        @param request: ModifyTenantUserRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantUserRolesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.global_permissions):
            body['GlobalPermissions'] = request.global_permissions
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
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tenant_user_roles(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse:
        """
        @summary Indicates whether the privilege was granted to the role.
        
        @param request: ModifyTenantUserRolesRequest
        @return: ModifyTenantUserRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_roles_with_options(request, runtime)

    async def modify_tenant_user_roles_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserRolesRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse:
        """
        @summary Indicates whether the privilege was granted to the role.
        
        @param request: ModifyTenantUserRolesRequest
        @return: ModifyTenantUserRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_user_roles_with_options_async(request, runtime)

    def modify_tenant_user_status_with_options(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse:
        """
        @summary The ID of the tenant.
        
        @param request: ModifyTenantUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantUserStatusResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_tenant_user_status_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse:
        """
        @summary The ID of the tenant.
        
        @param request: ModifyTenantUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTenantUserStatusResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_tenant_user_status(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserStatusRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse:
        """
        @summary The ID of the tenant.
        
        @param request: ModifyTenantUserStatusRequest
        @return: ModifyTenantUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_status_with_options(request, runtime)

    async def modify_tenant_user_status_async(
        self,
        request: ocean_base_pro_20190901_models.ModifyTenantUserStatusRequest,
    ) -> ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse:
        """
        @summary The ID of the tenant.
        
        @param request: ModifyTenantUserStatusRequest
        @return: ModifyTenantUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tenant_user_status_with_options_async(request, runtime)

    def release_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.ReleaseProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseProjectResponse:
        """
        @summary 释放项目
        
        @param request: ReleaseProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ReleaseProjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ReleaseProjectResponse(),
                self.execute(params, req, runtime)
            )

    async def release_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseProjectResponse:
        """
        @summary 释放项目
        
        @param request: ReleaseProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ReleaseProjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ReleaseProjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def release_project(
        self,
        request: ocean_base_pro_20190901_models.ReleaseProjectRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseProjectResponse:
        """
        @summary 释放项目
        
        @param request: ReleaseProjectRequest
        @return: ReleaseProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_project_with_options(request, runtime)

    async def release_project_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseProjectRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseProjectResponse:
        """
        @summary 释放项目
        
        @param request: ReleaseProjectRequest
        @return: ReleaseProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_project_with_options_async(request, runtime)

    def release_worker_instance_with_options(
        self,
        request: ocean_base_pro_20190901_models.ReleaseWorkerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse:
        """
        @summary 释放传输实例 （未绑定项目时才可以释放）
        
        @param request: ReleaseWorkerInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseWorkerInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def release_worker_instance_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseWorkerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse:
        """
        @summary 释放传输实例 （未绑定项目时才可以释放）
        
        @param request: ReleaseWorkerInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseWorkerInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def release_worker_instance(
        self,
        request: ocean_base_pro_20190901_models.ReleaseWorkerInstanceRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse:
        """
        @summary 释放传输实例 （未绑定项目时才可以释放）
        
        @param request: ReleaseWorkerInstanceRequest
        @return: ReleaseWorkerInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_worker_instance_with_options(request, runtime)

    async def release_worker_instance_async(
        self,
        request: ocean_base_pro_20190901_models.ReleaseWorkerInstanceRequest,
    ) -> ocean_base_pro_20190901_models.ReleaseWorkerInstanceResponse:
        """
        @summary 释放传输实例 （未绑定项目时才可以释放）
        
        @param request: ReleaseWorkerInstanceRequest
        @return: ReleaseWorkerInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_worker_instance_with_options_async(request, runtime)

    def remove_standby_instance_with_options(
        self,
        request: ocean_base_pro_20190901_models.RemoveStandbyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.RemoveStandbyInstanceResponse:
        """
        @summary 备实例解耦
        
        @param request: RemoveStandbyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveStandbyInstanceResponse
        """
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
            action='RemoveStandbyInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.RemoveStandbyInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.RemoveStandbyInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def remove_standby_instance_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.RemoveStandbyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.RemoveStandbyInstanceResponse:
        """
        @summary 备实例解耦
        
        @param request: RemoveStandbyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveStandbyInstanceResponse
        """
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
            action='RemoveStandbyInstance',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.RemoveStandbyInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.RemoveStandbyInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def remove_standby_instance(
        self,
        request: ocean_base_pro_20190901_models.RemoveStandbyInstanceRequest,
    ) -> ocean_base_pro_20190901_models.RemoveStandbyInstanceResponse:
        """
        @summary 备实例解耦
        
        @param request: RemoveStandbyInstanceRequest
        @return: RemoveStandbyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_standby_instance_with_options(request, runtime)

    async def remove_standby_instance_async(
        self,
        request: ocean_base_pro_20190901_models.RemoveStandbyInstanceRequest,
    ) -> ocean_base_pro_20190901_models.RemoveStandbyInstanceResponse:
        """
        @summary 备实例解耦
        
        @param request: RemoveStandbyInstanceRequest
        @return: RemoveStandbyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_standby_instance_with_options_async(request, runtime)

    def resume_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.ResumeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ResumeProjectResponse:
        """
        @summary 恢复项目
        
        @param request: ResumeProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ResumeProjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ResumeProjectResponse(),
                self.execute(params, req, runtime)
            )

    async def resume_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.ResumeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.ResumeProjectResponse:
        """
        @summary 恢复项目
        
        @param request: ResumeProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ResumeProjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.ResumeProjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def resume_project(
        self,
        request: ocean_base_pro_20190901_models.ResumeProjectRequest,
    ) -> ocean_base_pro_20190901_models.ResumeProjectResponse:
        """
        @summary 恢复项目
        
        @param request: ResumeProjectRequest
        @return: ResumeProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_project_with_options(request, runtime)

    async def resume_project_async(
        self,
        request: ocean_base_pro_20190901_models.ResumeProjectRequest,
    ) -> ocean_base_pro_20190901_models.ResumeProjectResponse:
        """
        @summary 恢复项目
        
        @param request: ResumeProjectRequest
        @return: ResumeProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_project_with_options_async(request, runtime)

    def retry_project_modify_records_with_options(
        self,
        request: ocean_base_pro_20190901_models.RetryProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse:
        """
        @summary 根据修改记录 ID 重试修改操作（仅支持处于 FAILED 状态的修改记录）
        
        @param request: RetryProjectModifyRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryProjectModifyRecordsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse(),
                self.execute(params, req, runtime)
            )

    async def retry_project_modify_records_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.RetryProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse:
        """
        @summary 根据修改记录 ID 重试修改操作（仅支持处于 FAILED 状态的修改记录）
        
        @param request: RetryProjectModifyRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryProjectModifyRecordsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def retry_project_modify_records(
        self,
        request: ocean_base_pro_20190901_models.RetryProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse:
        """
        @summary 根据修改记录 ID 重试修改操作（仅支持处于 FAILED 状态的修改记录）
        
        @param request: RetryProjectModifyRecordsRequest
        @return: RetryProjectModifyRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retry_project_modify_records_with_options(request, runtime)

    async def retry_project_modify_records_async(
        self,
        request: ocean_base_pro_20190901_models.RetryProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.RetryProjectModifyRecordsResponse:
        """
        @summary 根据修改记录 ID 重试修改操作（仅支持处于 FAILED 状态的修改记录）
        
        @param request: RetryProjectModifyRecordsRequest
        @return: RetryProjectModifyRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retry_project_modify_records_with_options_async(request, runtime)

    def start_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.StartProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartProjectResponse:
        """
        @summary 启动项目
        
        @param request: StartProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StartProjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StartProjectResponse(),
                self.execute(params, req, runtime)
            )

    async def start_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StartProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartProjectResponse:
        """
        @summary 启动项目
        
        @param request: StartProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StartProjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StartProjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_project(
        self,
        request: ocean_base_pro_20190901_models.StartProjectRequest,
    ) -> ocean_base_pro_20190901_models.StartProjectResponse:
        """
        @summary 启动项目
        
        @param request: StartProjectRequest
        @return: StartProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_project_with_options(request, runtime)

    async def start_project_async(
        self,
        request: ocean_base_pro_20190901_models.StartProjectRequest,
    ) -> ocean_base_pro_20190901_models.StartProjectResponse:
        """
        @summary 启动项目
        
        @param request: StartProjectRequest
        @return: StartProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_project_with_options_async(request, runtime)

    def start_projects_by_label_with_options(
        self,
        request: ocean_base_pro_20190901_models.StartProjectsByLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartProjectsByLabelResponse:
        """
        @summary 启动该label下的所有未启动项目
        
        @param request: StartProjectsByLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartProjectsByLabelResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StartProjectsByLabelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StartProjectsByLabelResponse(),
                self.execute(params, req, runtime)
            )

    async def start_projects_by_label_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StartProjectsByLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StartProjectsByLabelResponse:
        """
        @summary 启动该label下的所有未启动项目
        
        @param request: StartProjectsByLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartProjectsByLabelResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StartProjectsByLabelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StartProjectsByLabelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_projects_by_label(
        self,
        request: ocean_base_pro_20190901_models.StartProjectsByLabelRequest,
    ) -> ocean_base_pro_20190901_models.StartProjectsByLabelResponse:
        """
        @summary 启动该label下的所有未启动项目
        
        @param request: StartProjectsByLabelRequest
        @return: StartProjectsByLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_projects_by_label_with_options(request, runtime)

    async def start_projects_by_label_async(
        self,
        request: ocean_base_pro_20190901_models.StartProjectsByLabelRequest,
    ) -> ocean_base_pro_20190901_models.StartProjectsByLabelResponse:
        """
        @summary 启动该label下的所有未启动项目
        
        @param request: StartProjectsByLabelRequest
        @return: StartProjectsByLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_projects_by_label_with_options_async(request, runtime)

    def stop_project_with_options(
        self,
        request: ocean_base_pro_20190901_models.StopProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectResponse:
        """
        @summary 暂停项目
        
        @param request: StopProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_project_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectResponse:
        """
        @summary 暂停项目
        
        @param request: StopProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopProjectResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_project(
        self,
        request: ocean_base_pro_20190901_models.StopProjectRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectResponse:
        """
        @summary 暂停项目
        
        @param request: StopProjectRequest
        @return: StopProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_project_with_options(request, runtime)

    async def stop_project_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectResponse:
        """
        @summary 暂停项目
        
        @param request: StopProjectRequest
        @return: StopProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_project_with_options_async(request, runtime)

    def stop_project_modify_records_with_options(
        self,
        request: ocean_base_pro_20190901_models.StopProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse:
        """
        @summary 根据修改记录 ID 终止修改操作，不可恢复（仅支持处于 RUNNING / FAILED 状态的修改记录）
        
        @param request: StopProjectModifyRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopProjectModifyRecordsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_project_modify_records_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectModifyRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse:
        """
        @summary 根据修改记录 ID 终止修改操作，不可恢复（仅支持处于 RUNNING / FAILED 状态的修改记录）
        
        @param request: StopProjectModifyRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopProjectModifyRecordsResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_project_modify_records(
        self,
        request: ocean_base_pro_20190901_models.StopProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse:
        """
        @summary 根据修改记录 ID 终止修改操作，不可恢复（仅支持处于 RUNNING / FAILED 状态的修改记录）
        
        @param request: StopProjectModifyRecordsRequest
        @return: StopProjectModifyRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_project_modify_records_with_options(request, runtime)

    async def stop_project_modify_records_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectModifyRecordsRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectModifyRecordsResponse:
        """
        @summary 根据修改记录 ID 终止修改操作，不可恢复（仅支持处于 RUNNING / FAILED 状态的修改记录）
        
        @param request: StopProjectModifyRecordsRequest
        @return: StopProjectModifyRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_project_modify_records_with_options_async(request, runtime)

    def stop_projects_by_label_with_options(
        self,
        request: ocean_base_pro_20190901_models.StopProjectsByLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectsByLabelResponse:
        """
        @summary 暂停该label下的所有运行中项目
        
        @param request: StopProjectsByLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopProjectsByLabelResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectsByLabelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectsByLabelResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_projects_by_label_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectsByLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.StopProjectsByLabelResponse:
        """
        @summary 暂停该label下的所有运行中项目
        
        @param request: StopProjectsByLabelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopProjectsByLabelResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectsByLabelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.StopProjectsByLabelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_projects_by_label(
        self,
        request: ocean_base_pro_20190901_models.StopProjectsByLabelRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectsByLabelResponse:
        """
        @summary 暂停该label下的所有运行中项目
        
        @param request: StopProjectsByLabelRequest
        @return: StopProjectsByLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_projects_by_label_with_options(request, runtime)

    async def stop_projects_by_label_async(
        self,
        request: ocean_base_pro_20190901_models.StopProjectsByLabelRequest,
    ) -> ocean_base_pro_20190901_models.StopProjectsByLabelResponse:
        """
        @summary 暂停该label下的所有运行中项目
        
        @param request: StopProjectsByLabelRequest
        @return: StopProjectsByLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_projects_by_label_with_options_async(request, runtime)

    def switchover_instance_with_options(
        self,
        request: ocean_base_pro_20190901_models.SwitchoverInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.SwitchoverInstanceResponse:
        """
        @summary You can call this operation to switch between the primary and standby instances of OceanBase.
        
        @param request: SwitchoverInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchoverInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.SwitchoverInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.SwitchoverInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def switchover_instance_with_options_async(
        self,
        request: ocean_base_pro_20190901_models.SwitchoverInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.SwitchoverInstanceResponse:
        """
        @summary You can call this operation to switch between the primary and standby instances of OceanBase.
        
        @param request: SwitchoverInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchoverInstanceResponse
        """
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.SwitchoverInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.SwitchoverInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def switchover_instance(
        self,
        request: ocean_base_pro_20190901_models.SwitchoverInstanceRequest,
    ) -> ocean_base_pro_20190901_models.SwitchoverInstanceResponse:
        """
        @summary You can call this operation to switch between the primary and standby instances of OceanBase.
        
        @param request: SwitchoverInstanceRequest
        @return: SwitchoverInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switchover_instance_with_options(request, runtime)

    async def switchover_instance_async(
        self,
        request: ocean_base_pro_20190901_models.SwitchoverInstanceRequest,
    ) -> ocean_base_pro_20190901_models.SwitchoverInstanceResponse:
        """
        @summary You can call this operation to switch between the primary and standby instances of OceanBase.
        
        @param request: SwitchoverInstanceRequest
        @return: SwitchoverInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switchover_instance_with_options_async(request, runtime)

    def update_project_config_with_options(
        self,
        tmp_req: ocean_base_pro_20190901_models.UpdateProjectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.UpdateProjectConfigResponse:
        """
        @summary 更新项目配置 Action=UpdateProjectConfig
        
        @param tmp_req: UpdateProjectConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.UpdateProjectConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.common_transfer_config):
            request.common_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_transfer_config, 'CommonTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.full_transfer_config):
            request.full_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.full_transfer_config, 'FullTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.incr_transfer_config):
            request.incr_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.incr_transfer_config, 'IncrTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.reverse_incr_transfer_config):
            request.reverse_incr_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reverse_incr_transfer_config, 'ReverseIncrTransferConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.common_transfer_config_shrink):
            body['CommonTransferConfig'] = request.common_transfer_config_shrink
        if not UtilClient.is_unset(request.full_transfer_config_shrink):
            body['FullTransferConfig'] = request.full_transfer_config_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.incr_transfer_config_shrink):
            body['IncrTransferConfig'] = request.incr_transfer_config_shrink
        if not UtilClient.is_unset(request.reverse_incr_transfer_config_shrink):
            body['ReverseIncrTransferConfig'] = request.reverse_incr_transfer_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectConfig',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.UpdateProjectConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.UpdateProjectConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def update_project_config_with_options_async(
        self,
        tmp_req: ocean_base_pro_20190901_models.UpdateProjectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ocean_base_pro_20190901_models.UpdateProjectConfigResponse:
        """
        @summary 更新项目配置 Action=UpdateProjectConfig
        
        @param tmp_req: UpdateProjectConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.UpdateProjectConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.common_transfer_config):
            request.common_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_transfer_config, 'CommonTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.full_transfer_config):
            request.full_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.full_transfer_config, 'FullTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.incr_transfer_config):
            request.incr_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.incr_transfer_config, 'IncrTransferConfig', 'json')
        if not UtilClient.is_unset(tmp_req.reverse_incr_transfer_config):
            request.reverse_incr_transfer_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reverse_incr_transfer_config, 'ReverseIncrTransferConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.common_transfer_config_shrink):
            body['CommonTransferConfig'] = request.common_transfer_config_shrink
        if not UtilClient.is_unset(request.full_transfer_config_shrink):
            body['FullTransferConfig'] = request.full_transfer_config_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.incr_transfer_config_shrink):
            body['IncrTransferConfig'] = request.incr_transfer_config_shrink
        if not UtilClient.is_unset(request.reverse_incr_transfer_config_shrink):
            body['ReverseIncrTransferConfig'] = request.reverse_incr_transfer_config_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectConfig',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.UpdateProjectConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                ocean_base_pro_20190901_models.UpdateProjectConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_project_config(
        self,
        request: ocean_base_pro_20190901_models.UpdateProjectConfigRequest,
    ) -> ocean_base_pro_20190901_models.UpdateProjectConfigResponse:
        """
        @summary 更新项目配置 Action=UpdateProjectConfig
        
        @param request: UpdateProjectConfigRequest
        @return: UpdateProjectConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_project_config_with_options(request, runtime)

    async def update_project_config_async(
        self,
        request: ocean_base_pro_20190901_models.UpdateProjectConfigRequest,
    ) -> ocean_base_pro_20190901_models.UpdateProjectConfigResponse:
        """
        @summary 更新项目配置 Action=UpdateProjectConfig
        
        @param request: UpdateProjectConfigRequest
        @return: UpdateProjectConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_project_config_with_options_async(request, runtime)
