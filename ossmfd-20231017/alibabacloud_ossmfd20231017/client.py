# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_ossmfd20231017 import models as oss_mfd_20231017_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('ossmfd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_mfd_service_open_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.CheckMfdServiceOpenResponse:
        """
        @summary 检查服务是否开通
        
        @param request: CheckMfdServiceOpenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckMfdServiceOpenResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckMfdServiceOpen',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.CheckMfdServiceOpenResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_mfd_service_open_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.CheckMfdServiceOpenResponse:
        """
        @summary 检查服务是否开通
        
        @param request: CheckMfdServiceOpenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckMfdServiceOpenResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckMfdServiceOpen',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.CheckMfdServiceOpenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_mfd_service_open(self) -> oss_mfd_20231017_models.CheckMfdServiceOpenResponse:
        """
        @summary 检查服务是否开通
        
        @return: CheckMfdServiceOpenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_mfd_service_open_with_options(runtime)

    async def check_mfd_service_open_async(self) -> oss_mfd_20231017_models.CheckMfdServiceOpenResponse:
        """
        @summary 检查服务是否开通
        
        @return: CheckMfdServiceOpenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_mfd_service_open_with_options_async(runtime)

    def create_oss_bucket_scan_task_with_options(
        self,
        request: oss_mfd_20231017_models.CreateOssBucketScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.CreateOssBucketScanTaskResponse:
        """
        @summary 创建bucket扫描任务
        
        @param request: CreateOssBucketScanTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssBucketScanTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not UtilClient.is_unset(request.bucket_name_list):
            query['BucketNameList'] = request.bucket_name_list
        if not UtilClient.is_unset(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not UtilClient.is_unset(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not UtilClient.is_unset(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not UtilClient.is_unset(request.exclude_key_suffix_list):
            query['ExcludeKeySuffixList'] = request.exclude_key_suffix_list
        if not UtilClient.is_unset(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not UtilClient.is_unset(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not UtilClient.is_unset(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not UtilClient.is_unset(request.scan_mode):
            query['ScanMode'] = request.scan_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOssBucketScanTask',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.CreateOssBucketScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oss_bucket_scan_task_with_options_async(
        self,
        request: oss_mfd_20231017_models.CreateOssBucketScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.CreateOssBucketScanTaskResponse:
        """
        @summary 创建bucket扫描任务
        
        @param request: CreateOssBucketScanTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssBucketScanTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not UtilClient.is_unset(request.bucket_name_list):
            query['BucketNameList'] = request.bucket_name_list
        if not UtilClient.is_unset(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not UtilClient.is_unset(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not UtilClient.is_unset(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not UtilClient.is_unset(request.exclude_key_suffix_list):
            query['ExcludeKeySuffixList'] = request.exclude_key_suffix_list
        if not UtilClient.is_unset(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not UtilClient.is_unset(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not UtilClient.is_unset(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not UtilClient.is_unset(request.scan_mode):
            query['ScanMode'] = request.scan_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOssBucketScanTask',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.CreateOssBucketScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oss_bucket_scan_task(
        self,
        request: oss_mfd_20231017_models.CreateOssBucketScanTaskRequest,
    ) -> oss_mfd_20231017_models.CreateOssBucketScanTaskResponse:
        """
        @summary 创建bucket扫描任务
        
        @param request: CreateOssBucketScanTaskRequest
        @return: CreateOssBucketScanTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_oss_bucket_scan_task_with_options(request, runtime)

    async def create_oss_bucket_scan_task_async(
        self,
        request: oss_mfd_20231017_models.CreateOssBucketScanTaskRequest,
    ) -> oss_mfd_20231017_models.CreateOssBucketScanTaskResponse:
        """
        @summary 创建bucket扫描任务
        
        @param request: CreateOssBucketScanTaskRequest
        @return: CreateOssBucketScanTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_oss_bucket_scan_task_with_options_async(request, runtime)

    def create_oss_scan_config_with_options(
        self,
        request: oss_mfd_20231017_models.CreateOssScanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.CreateOssScanConfigResponse:
        """
        @summary 创建Bucket检测策略配置
        
        @param request: CreateOssScanConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssScanConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not UtilClient.is_unset(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not UtilClient.is_unset(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not UtilClient.is_unset(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not UtilClient.is_unset(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.real_time_incr):
            query['RealTimeIncr'] = request.real_time_incr
        if not UtilClient.is_unset(request.scan_day_list):
            query['ScanDayList'] = request.scan_day_list
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOssScanConfig',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.CreateOssScanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oss_scan_config_with_options_async(
        self,
        request: oss_mfd_20231017_models.CreateOssScanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.CreateOssScanConfigResponse:
        """
        @summary 创建Bucket检测策略配置
        
        @param request: CreateOssScanConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssScanConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not UtilClient.is_unset(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not UtilClient.is_unset(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not UtilClient.is_unset(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not UtilClient.is_unset(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.real_time_incr):
            query['RealTimeIncr'] = request.real_time_incr
        if not UtilClient.is_unset(request.scan_day_list):
            query['ScanDayList'] = request.scan_day_list
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOssScanConfig',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.CreateOssScanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oss_scan_config(
        self,
        request: oss_mfd_20231017_models.CreateOssScanConfigRequest,
    ) -> oss_mfd_20231017_models.CreateOssScanConfigResponse:
        """
        @summary 创建Bucket检测策略配置
        
        @param request: CreateOssScanConfigRequest
        @return: CreateOssScanConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_oss_scan_config_with_options(request, runtime)

    async def create_oss_scan_config_async(
        self,
        request: oss_mfd_20231017_models.CreateOssScanConfigRequest,
    ) -> oss_mfd_20231017_models.CreateOssScanConfigResponse:
        """
        @summary 创建Bucket检测策略配置
        
        @param request: CreateOssScanConfigRequest
        @return: CreateOssScanConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_oss_scan_config_with_options_async(request, runtime)

    def describe_export_info_with_options(
        self,
        request: oss_mfd_20231017_models.DescribeExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.DescribeExportInfoResponse:
        """
        @summary 查询导出信息
        
        @param request: DescribeExportInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExportInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportInfo',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.DescribeExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_export_info_with_options_async(
        self,
        request: oss_mfd_20231017_models.DescribeExportInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.DescribeExportInfoResponse:
        """
        @summary 查询导出信息
        
        @param request: DescribeExportInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExportInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportInfo',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.DescribeExportInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_export_info(
        self,
        request: oss_mfd_20231017_models.DescribeExportInfoRequest,
    ) -> oss_mfd_20231017_models.DescribeExportInfoResponse:
        """
        @summary 查询导出信息
        
        @param request: DescribeExportInfoRequest
        @return: DescribeExportInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_export_info_with_options(request, runtime)

    async def describe_export_info_async(
        self,
        request: oss_mfd_20231017_models.DescribeExportInfoRequest,
    ) -> oss_mfd_20231017_models.DescribeExportInfoResponse:
        """
        @summary 查询导出信息
        
        @param request: DescribeExportInfoRequest
        @return: DescribeExportInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_export_info_with_options_async(request, runtime)

    def describe_service_linked_role_status_with_options(
        self,
        request: oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusResponse:
        """
        @summary 查询您是否已创建云安全中心服务关联角色
        
        @param request: DescribeServiceLinkedRoleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceLinkedRoleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceLinkedRoleStatus',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_linked_role_status_with_options_async(
        self,
        request: oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusResponse:
        """
        @summary 查询您是否已创建云安全中心服务关联角色
        
        @param request: DescribeServiceLinkedRoleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceLinkedRoleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceLinkedRoleStatus',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_linked_role_status(
        self,
        request: oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusRequest,
    ) -> oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusResponse:
        """
        @summary 查询您是否已创建云安全中心服务关联角色
        
        @param request: DescribeServiceLinkedRoleStatusRequest
        @return: DescribeServiceLinkedRoleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_linked_role_status_with_options(request, runtime)

    async def describe_service_linked_role_status_async(
        self,
        request: oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusRequest,
    ) -> oss_mfd_20231017_models.DescribeServiceLinkedRoleStatusResponse:
        """
        @summary 查询您是否已创建云安全中心服务关联角色
        
        @param request: DescribeServiceLinkedRoleStatusRequest
        @return: DescribeServiceLinkedRoleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_linked_role_status_with_options_async(request, runtime)

    def export_record_with_options(
        self,
        request: oss_mfd_20231017_models.ExportRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ExportRecordResponse:
        """
        @summary 导出恶意文件列表
        
        @param request: ExportRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRecord',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ExportRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_record_with_options_async(
        self,
        request: oss_mfd_20231017_models.ExportRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ExportRecordResponse:
        """
        @summary 导出恶意文件列表
        
        @param request: ExportRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRecord',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ExportRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_record(
        self,
        request: oss_mfd_20231017_models.ExportRecordRequest,
    ) -> oss_mfd_20231017_models.ExportRecordResponse:
        """
        @summary 导出恶意文件列表
        
        @param request: ExportRecordRequest
        @return: ExportRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_record_with_options(request, runtime)

    async def export_record_async(
        self,
        request: oss_mfd_20231017_models.ExportRecordRequest,
    ) -> oss_mfd_20231017_models.ExportRecordResponse:
        """
        @summary 导出恶意文件列表
        
        @param request: ExportRecordRequest
        @return: ExportRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_record_with_options_async(request, runtime)

    def get_file_detect_report_with_options(
        self,
        request: oss_mfd_20231017_models.GetFileDetectReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.GetFileDetectReportResponse:
        """
        @summary 获取沙箱检测报告。
        
        @param request: GetFileDetectReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileDetectReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.file_hash):
            query['FileHash'] = request.file_hash
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileDetectReport',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.GetFileDetectReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_detect_report_with_options_async(
        self,
        request: oss_mfd_20231017_models.GetFileDetectReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.GetFileDetectReportResponse:
        """
        @summary 获取沙箱检测报告。
        
        @param request: GetFileDetectReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileDetectReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.file_hash):
            query['FileHash'] = request.file_hash
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileDetectReport',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.GetFileDetectReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_detect_report(
        self,
        request: oss_mfd_20231017_models.GetFileDetectReportRequest,
    ) -> oss_mfd_20231017_models.GetFileDetectReportResponse:
        """
        @summary 获取沙箱检测报告。
        
        @param request: GetFileDetectReportRequest
        @return: GetFileDetectReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_file_detect_report_with_options(request, runtime)

    async def get_file_detect_report_async(
        self,
        request: oss_mfd_20231017_models.GetFileDetectReportRequest,
    ) -> oss_mfd_20231017_models.GetFileDetectReportResponse:
        """
        @summary 获取沙箱检测报告。
        
        @param request: GetFileDetectReportRequest
        @return: GetFileDetectReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_file_detect_report_with_options_async(request, runtime)

    def get_oss_bucket_scan_statistic_with_options(
        self,
        request: oss_mfd_20231017_models.GetOssBucketScanStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.GetOssBucketScanStatisticResponse:
        """
        @summary 获取bucket检测统计信息
        
        @param request: GetOssBucketScanStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssBucketScanStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name_list):
            query['BucketNameList'] = request.bucket_name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssBucketScanStatistic',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.GetOssBucketScanStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_bucket_scan_statistic_with_options_async(
        self,
        request: oss_mfd_20231017_models.GetOssBucketScanStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.GetOssBucketScanStatisticResponse:
        """
        @summary 获取bucket检测统计信息
        
        @param request: GetOssBucketScanStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssBucketScanStatisticResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name_list):
            query['BucketNameList'] = request.bucket_name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssBucketScanStatistic',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.GetOssBucketScanStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_bucket_scan_statistic(
        self,
        request: oss_mfd_20231017_models.GetOssBucketScanStatisticRequest,
    ) -> oss_mfd_20231017_models.GetOssBucketScanStatisticResponse:
        """
        @summary 获取bucket检测统计信息
        
        @param request: GetOssBucketScanStatisticRequest
        @return: GetOssBucketScanStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_oss_bucket_scan_statistic_with_options(request, runtime)

    async def get_oss_bucket_scan_statistic_async(
        self,
        request: oss_mfd_20231017_models.GetOssBucketScanStatisticRequest,
    ) -> oss_mfd_20231017_models.GetOssBucketScanStatisticResponse:
        """
        @summary 获取bucket检测统计信息
        
        @param request: GetOssBucketScanStatisticRequest
        @return: GetOssBucketScanStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_bucket_scan_statistic_with_options_async(request, runtime)

    def get_oss_scan_config_with_options(
        self,
        request: oss_mfd_20231017_models.GetOssScanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.GetOssScanConfigResponse:
        """
        @summary 获取Bucket检测配置
        
        @param request: GetOssScanConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssScanConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssScanConfig',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.GetOssScanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_scan_config_with_options_async(
        self,
        request: oss_mfd_20231017_models.GetOssScanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.GetOssScanConfigResponse:
        """
        @summary 获取Bucket检测配置
        
        @param request: GetOssScanConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssScanConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssScanConfig',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.GetOssScanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_scan_config(
        self,
        request: oss_mfd_20231017_models.GetOssScanConfigRequest,
    ) -> oss_mfd_20231017_models.GetOssScanConfigResponse:
        """
        @summary 获取Bucket检测配置
        
        @param request: GetOssScanConfigRequest
        @return: GetOssScanConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_oss_scan_config_with_options(request, runtime)

    async def get_oss_scan_config_async(
        self,
        request: oss_mfd_20231017_models.GetOssScanConfigRequest,
    ) -> oss_mfd_20231017_models.GetOssScanConfigResponse:
        """
        @summary 获取Bucket检测配置
        
        @param request: GetOssScanConfigRequest
        @return: GetOssScanConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_scan_config_with_options_async(request, runtime)

    def list_object_scan_event_with_options(
        self,
        request: oss_mfd_20231017_models.ListObjectScanEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ListObjectScanEventResponse:
        """
        @summary 获取文件检测告警列表
        
        @param request: ListObjectScanEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListObjectScanEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_event_id):
            query['ParentEventId'] = request.parent_event_id
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.time_end):
            query['TimeEnd'] = request.time_end
        if not UtilClient.is_unset(request.time_start):
            query['TimeStart'] = request.time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjectScanEvent',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ListObjectScanEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_object_scan_event_with_options_async(
        self,
        request: oss_mfd_20231017_models.ListObjectScanEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ListObjectScanEventResponse:
        """
        @summary 获取文件检测告警列表
        
        @param request: ListObjectScanEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListObjectScanEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_event_id):
            query['ParentEventId'] = request.parent_event_id
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.time_end):
            query['TimeEnd'] = request.time_end
        if not UtilClient.is_unset(request.time_start):
            query['TimeStart'] = request.time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjectScanEvent',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ListObjectScanEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_object_scan_event(
        self,
        request: oss_mfd_20231017_models.ListObjectScanEventRequest,
    ) -> oss_mfd_20231017_models.ListObjectScanEventResponse:
        """
        @summary 获取文件检测告警列表
        
        @param request: ListObjectScanEventRequest
        @return: ListObjectScanEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_object_scan_event_with_options(request, runtime)

    async def list_object_scan_event_async(
        self,
        request: oss_mfd_20231017_models.ListObjectScanEventRequest,
    ) -> oss_mfd_20231017_models.ListObjectScanEventResponse:
        """
        @summary 获取文件检测告警列表
        
        @param request: ListObjectScanEventRequest
        @return: ListObjectScanEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_object_scan_event_with_options_async(request, runtime)

    def list_oss_bucket_with_options(
        self,
        request: oss_mfd_20231017_models.ListOssBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ListOssBucketResponse:
        """
        @summary 列举用户所有的bucket
        
        @param request: ListOssBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOssBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOssBucket',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ListOssBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oss_bucket_with_options_async(
        self,
        request: oss_mfd_20231017_models.ListOssBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ListOssBucketResponse:
        """
        @summary 列举用户所有的bucket
        
        @param request: ListOssBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOssBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOssBucket',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ListOssBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oss_bucket(
        self,
        request: oss_mfd_20231017_models.ListOssBucketRequest,
    ) -> oss_mfd_20231017_models.ListOssBucketResponse:
        """
        @summary 列举用户所有的bucket
        
        @param request: ListOssBucketRequest
        @return: ListOssBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_oss_bucket_with_options(request, runtime)

    async def list_oss_bucket_async(
        self,
        request: oss_mfd_20231017_models.ListOssBucketRequest,
    ) -> oss_mfd_20231017_models.ListOssBucketResponse:
        """
        @summary 列举用户所有的bucket
        
        @param request: ListOssBucketRequest
        @return: ListOssBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_oss_bucket_with_options_async(request, runtime)

    def list_oss_bucket_scan_info_with_options(
        self,
        request: oss_mfd_20231017_models.ListOssBucketScanInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ListOssBucketScanInfoResponse:
        """
        @summary 获取bucket详情
        
        @param request: ListOssBucketScanInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOssBucketScanInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.fuzz_bucket_name):
            query['FuzzBucketName'] = request.fuzz_bucket_name
        if not UtilClient.is_unset(request.has_risk):
            query['HasRisk'] = request.has_risk
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOssBucketScanInfo',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ListOssBucketScanInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oss_bucket_scan_info_with_options_async(
        self,
        request: oss_mfd_20231017_models.ListOssBucketScanInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ListOssBucketScanInfoResponse:
        """
        @summary 获取bucket详情
        
        @param request: ListOssBucketScanInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOssBucketScanInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.fuzz_bucket_name):
            query['FuzzBucketName'] = request.fuzz_bucket_name
        if not UtilClient.is_unset(request.has_risk):
            query['HasRisk'] = request.has_risk
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOssBucketScanInfo',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ListOssBucketScanInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oss_bucket_scan_info(
        self,
        request: oss_mfd_20231017_models.ListOssBucketScanInfoRequest,
    ) -> oss_mfd_20231017_models.ListOssBucketScanInfoResponse:
        """
        @summary 获取bucket详情
        
        @param request: ListOssBucketScanInfoRequest
        @return: ListOssBucketScanInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_oss_bucket_scan_info_with_options(request, runtime)

    async def list_oss_bucket_scan_info_async(
        self,
        request: oss_mfd_20231017_models.ListOssBucketScanInfoRequest,
    ) -> oss_mfd_20231017_models.ListOssBucketScanInfoResponse:
        """
        @summary 获取bucket详情
        
        @param request: ListOssBucketScanInfoRequest
        @return: ListOssBucketScanInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_oss_bucket_scan_info_with_options_async(request, runtime)

    def list_support_object_suffix_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ListSupportObjectSuffixResponse:
        """
        @summary 获取支持的文件后缀
        
        @param request: ListSupportObjectSuffixRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSupportObjectSuffixResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSupportObjectSuffix',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ListSupportObjectSuffixResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_support_object_suffix_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.ListSupportObjectSuffixResponse:
        """
        @summary 获取支持的文件后缀
        
        @param request: ListSupportObjectSuffixRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSupportObjectSuffixResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSupportObjectSuffix',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.ListSupportObjectSuffixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_support_object_suffix(self) -> oss_mfd_20231017_models.ListSupportObjectSuffixResponse:
        """
        @summary 获取支持的文件后缀
        
        @return: ListSupportObjectSuffixResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_support_object_suffix_with_options(runtime)

    async def list_support_object_suffix_async(self) -> oss_mfd_20231017_models.ListSupportObjectSuffixResponse:
        """
        @summary 获取支持的文件后缀
        
        @return: ListSupportObjectSuffixResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_support_object_suffix_with_options_async(runtime)

    def operate_bucket_scan_task_with_options(
        self,
        request: oss_mfd_20231017_models.OperateBucketScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.OperateBucketScanTaskResponse:
        """
        @summary 操作oss检测任务
        
        @param request: OperateBucketScanTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateBucketScanTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.operate_code):
            query['OperateCode'] = request.operate_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateBucketScanTask',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.OperateBucketScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_bucket_scan_task_with_options_async(
        self,
        request: oss_mfd_20231017_models.OperateBucketScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.OperateBucketScanTaskResponse:
        """
        @summary 操作oss检测任务
        
        @param request: OperateBucketScanTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateBucketScanTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.operate_code):
            query['OperateCode'] = request.operate_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateBucketScanTask',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.OperateBucketScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_bucket_scan_task(
        self,
        request: oss_mfd_20231017_models.OperateBucketScanTaskRequest,
    ) -> oss_mfd_20231017_models.OperateBucketScanTaskResponse:
        """
        @summary 操作oss检测任务
        
        @param request: OperateBucketScanTaskRequest
        @return: OperateBucketScanTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_bucket_scan_task_with_options(request, runtime)

    async def operate_bucket_scan_task_async(
        self,
        request: oss_mfd_20231017_models.OperateBucketScanTaskRequest,
    ) -> oss_mfd_20231017_models.OperateBucketScanTaskResponse:
        """
        @summary 操作oss检测任务
        
        @param request: OperateBucketScanTaskRequest
        @return: OperateBucketScanTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_bucket_scan_task_with_options_async(request, runtime)

    def update_oss_scan_config_with_options(
        self,
        request: oss_mfd_20231017_models.UpdateOssScanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.UpdateOssScanConfigResponse:
        """
        @summary 修改Bucket检测配置
        
        @param request: UpdateOssScanConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOssScanConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not UtilClient.is_unset(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not UtilClient.is_unset(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not UtilClient.is_unset(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not UtilClient.is_unset(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.real_time_incr):
            query['RealTimeIncr'] = request.real_time_incr
        if not UtilClient.is_unset(request.scan_day_list):
            query['ScanDayList'] = request.scan_day_list
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssScanConfig',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.UpdateOssScanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oss_scan_config_with_options_async(
        self,
        request: oss_mfd_20231017_models.UpdateOssScanConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oss_mfd_20231017_models.UpdateOssScanConfigResponse:
        """
        @summary 修改Bucket检测配置
        
        @param request: UpdateOssScanConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOssScanConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not UtilClient.is_unset(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not UtilClient.is_unset(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not UtilClient.is_unset(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not UtilClient.is_unset(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.real_time_incr):
            query['RealTimeIncr'] = request.real_time_incr
        if not UtilClient.is_unset(request.scan_day_list):
            query['ScanDayList'] = request.scan_day_list
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOssScanConfig',
            version='2023-10-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oss_mfd_20231017_models.UpdateOssScanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oss_scan_config(
        self,
        request: oss_mfd_20231017_models.UpdateOssScanConfigRequest,
    ) -> oss_mfd_20231017_models.UpdateOssScanConfigResponse:
        """
        @summary 修改Bucket检测配置
        
        @param request: UpdateOssScanConfigRequest
        @return: UpdateOssScanConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_oss_scan_config_with_options(request, runtime)

    async def update_oss_scan_config_async(
        self,
        request: oss_mfd_20231017_models.UpdateOssScanConfigRequest,
    ) -> oss_mfd_20231017_models.UpdateOssScanConfigResponse:
        """
        @summary 修改Bucket检测配置
        
        @param request: UpdateOssScanConfigRequest
        @return: UpdateOssScanConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_oss_scan_config_with_options_async(request, runtime)
