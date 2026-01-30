# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ossmfd20231017 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def check_mfd_service_open_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMfdServiceOpenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckMfdServiceOpen',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMfdServiceOpenResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_mfd_service_open_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMfdServiceOpenResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'CheckMfdServiceOpen',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMfdServiceOpenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_mfd_service_open(self) -> main_models.CheckMfdServiceOpenResponse:
        runtime = RuntimeOptions()
        return self.check_mfd_service_open_with_options(runtime)

    async def check_mfd_service_open_async(self) -> main_models.CheckMfdServiceOpenResponse:
        runtime = RuntimeOptions()
        return await self.check_mfd_service_open_with_options_async(runtime)

    def create_oss_bucket_scan_task_with_options(
        self,
        request: main_models.CreateOssBucketScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOssBucketScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not DaraCore.is_null(request.bucket_name_list):
            query['BucketNameList'] = request.bucket_name_list
        if not DaraCore.is_null(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not DaraCore.is_null(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not DaraCore.is_null(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not DaraCore.is_null(request.exclude_key_suffix_list):
            query['ExcludeKeySuffixList'] = request.exclude_key_suffix_list
        if not DaraCore.is_null(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not DaraCore.is_null(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not DaraCore.is_null(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not DaraCore.is_null(request.scan_mode):
            query['ScanMode'] = request.scan_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOssBucketScanTask',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOssBucketScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oss_bucket_scan_task_with_options_async(
        self,
        request: main_models.CreateOssBucketScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOssBucketScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not DaraCore.is_null(request.bucket_name_list):
            query['BucketNameList'] = request.bucket_name_list
        if not DaraCore.is_null(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not DaraCore.is_null(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not DaraCore.is_null(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not DaraCore.is_null(request.exclude_key_suffix_list):
            query['ExcludeKeySuffixList'] = request.exclude_key_suffix_list
        if not DaraCore.is_null(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not DaraCore.is_null(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not DaraCore.is_null(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not DaraCore.is_null(request.scan_mode):
            query['ScanMode'] = request.scan_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOssBucketScanTask',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOssBucketScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oss_bucket_scan_task(
        self,
        request: main_models.CreateOssBucketScanTaskRequest,
    ) -> main_models.CreateOssBucketScanTaskResponse:
        runtime = RuntimeOptions()
        return self.create_oss_bucket_scan_task_with_options(request, runtime)

    async def create_oss_bucket_scan_task_async(
        self,
        request: main_models.CreateOssBucketScanTaskRequest,
    ) -> main_models.CreateOssBucketScanTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_oss_bucket_scan_task_with_options_async(request, runtime)

    def create_oss_scan_config_with_options(
        self,
        request: main_models.CreateOssScanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOssScanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not DaraCore.is_null(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not DaraCore.is_null(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not DaraCore.is_null(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not DaraCore.is_null(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.real_time_incr):
            query['RealTimeIncr'] = request.real_time_incr
        if not DaraCore.is_null(request.scan_day_list):
            query['ScanDayList'] = request.scan_day_list
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOssScanConfig',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOssScanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oss_scan_config_with_options_async(
        self,
        request: main_models.CreateOssScanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOssScanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not DaraCore.is_null(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not DaraCore.is_null(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not DaraCore.is_null(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not DaraCore.is_null(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.real_time_incr):
            query['RealTimeIncr'] = request.real_time_incr
        if not DaraCore.is_null(request.scan_day_list):
            query['ScanDayList'] = request.scan_day_list
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOssScanConfig',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOssScanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oss_scan_config(
        self,
        request: main_models.CreateOssScanConfigRequest,
    ) -> main_models.CreateOssScanConfigResponse:
        runtime = RuntimeOptions()
        return self.create_oss_scan_config_with_options(request, runtime)

    async def create_oss_scan_config_async(
        self,
        request: main_models.CreateOssScanConfigRequest,
    ) -> main_models.CreateOssScanConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_oss_scan_config_with_options_async(request, runtime)

    def describe_export_info_with_options(
        self,
        request: main_models.DescribeExportInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExportInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExportInfo',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExportInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_export_info_with_options_async(
        self,
        request: main_models.DescribeExportInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExportInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_id):
            query['ExportId'] = request.export_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExportInfo',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExportInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_export_info(
        self,
        request: main_models.DescribeExportInfoRequest,
    ) -> main_models.DescribeExportInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_export_info_with_options(request, runtime)

    async def describe_export_info_async(
        self,
        request: main_models.DescribeExportInfoRequest,
    ) -> main_models.DescribeExportInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_export_info_with_options_async(request, runtime)

    def describe_service_linked_role_status_with_options(
        self,
        request: main_models.DescribeServiceLinkedRoleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceLinkedRoleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceLinkedRoleStatus',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceLinkedRoleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_linked_role_status_with_options_async(
        self,
        request: main_models.DescribeServiceLinkedRoleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServiceLinkedRoleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServiceLinkedRoleStatus',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServiceLinkedRoleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_linked_role_status(
        self,
        request: main_models.DescribeServiceLinkedRoleStatusRequest,
    ) -> main_models.DescribeServiceLinkedRoleStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_service_linked_role_status_with_options(request, runtime)

    async def describe_service_linked_role_status_async(
        self,
        request: main_models.DescribeServiceLinkedRoleStatusRequest,
    ) -> main_models.DescribeServiceLinkedRoleStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_service_linked_role_status_with_options_async(request, runtime)

    def export_record_with_options(
        self,
        request: main_models.ExportRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportRecord',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_record_with_options_async(
        self,
        request: main_models.ExportRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_type):
            query['ExportType'] = request.export_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportRecord',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_record(
        self,
        request: main_models.ExportRecordRequest,
    ) -> main_models.ExportRecordResponse:
        runtime = RuntimeOptions()
        return self.export_record_with_options(request, runtime)

    async def export_record_async(
        self,
        request: main_models.ExportRecordRequest,
    ) -> main_models.ExportRecordResponse:
        runtime = RuntimeOptions()
        return await self.export_record_with_options_async(request, runtime)

    def get_file_detect_report_with_options(
        self,
        request: main_models.GetFileDetectReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileDetectReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.field):
            query['Field'] = request.field
        if not DaraCore.is_null(request.file_hash):
            query['FileHash'] = request.file_hash
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileDetectReport',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileDetectReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_detect_report_with_options_async(
        self,
        request: main_models.GetFileDetectReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileDetectReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.field):
            query['Field'] = request.field
        if not DaraCore.is_null(request.file_hash):
            query['FileHash'] = request.file_hash
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileDetectReport',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileDetectReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_detect_report(
        self,
        request: main_models.GetFileDetectReportRequest,
    ) -> main_models.GetFileDetectReportResponse:
        runtime = RuntimeOptions()
        return self.get_file_detect_report_with_options(request, runtime)

    async def get_file_detect_report_async(
        self,
        request: main_models.GetFileDetectReportRequest,
    ) -> main_models.GetFileDetectReportResponse:
        runtime = RuntimeOptions()
        return await self.get_file_detect_report_with_options_async(request, runtime)

    def get_oss_bucket_scan_statistic_with_options(
        self,
        request: main_models.GetOssBucketScanStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssBucketScanStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name_list):
            query['BucketNameList'] = request.bucket_name_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssBucketScanStatistic',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssBucketScanStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_bucket_scan_statistic_with_options_async(
        self,
        request: main_models.GetOssBucketScanStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssBucketScanStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name_list):
            query['BucketNameList'] = request.bucket_name_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssBucketScanStatistic',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssBucketScanStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_bucket_scan_statistic(
        self,
        request: main_models.GetOssBucketScanStatisticRequest,
    ) -> main_models.GetOssBucketScanStatisticResponse:
        runtime = RuntimeOptions()
        return self.get_oss_bucket_scan_statistic_with_options(request, runtime)

    async def get_oss_bucket_scan_statistic_async(
        self,
        request: main_models.GetOssBucketScanStatisticRequest,
    ) -> main_models.GetOssBucketScanStatisticResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_bucket_scan_statistic_with_options_async(request, runtime)

    def get_oss_scan_config_with_options(
        self,
        request: main_models.GetOssScanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssScanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssScanConfig',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssScanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_scan_config_with_options_async(
        self,
        request: main_models.GetOssScanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssScanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssScanConfig',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssScanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_scan_config(
        self,
        request: main_models.GetOssScanConfigRequest,
    ) -> main_models.GetOssScanConfigResponse:
        runtime = RuntimeOptions()
        return self.get_oss_scan_config_with_options(request, runtime)

    async def get_oss_scan_config_async(
        self,
        request: main_models.GetOssScanConfigRequest,
    ) -> main_models.GetOssScanConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_scan_config_with_options_async(request, runtime)

    def list_object_scan_event_with_options(
        self,
        request: main_models.ListObjectScanEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListObjectScanEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_type):
            query['BatchType'] = request.batch_type
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.oss_key):
            query['OssKey'] = request.oss_key
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_event_id):
            query['ParentEventId'] = request.parent_event_id
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.time_end):
            query['TimeEnd'] = request.time_end
        if not DaraCore.is_null(request.time_start):
            query['TimeStart'] = request.time_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListObjectScanEvent',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListObjectScanEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_object_scan_event_with_options_async(
        self,
        request: main_models.ListObjectScanEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListObjectScanEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_type):
            query['BatchType'] = request.batch_type
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.oss_key):
            query['OssKey'] = request.oss_key
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_event_id):
            query['ParentEventId'] = request.parent_event_id
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.time_end):
            query['TimeEnd'] = request.time_end
        if not DaraCore.is_null(request.time_start):
            query['TimeStart'] = request.time_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListObjectScanEvent',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListObjectScanEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_object_scan_event(
        self,
        request: main_models.ListObjectScanEventRequest,
    ) -> main_models.ListObjectScanEventResponse:
        runtime = RuntimeOptions()
        return self.list_object_scan_event_with_options(request, runtime)

    async def list_object_scan_event_async(
        self,
        request: main_models.ListObjectScanEventRequest,
    ) -> main_models.ListObjectScanEventResponse:
        runtime = RuntimeOptions()
        return await self.list_object_scan_event_with_options_async(request, runtime)

    def list_oss_bucket_with_options(
        self,
        request: main_models.ListOssBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOssBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOssBucket',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOssBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oss_bucket_with_options_async(
        self,
        request: main_models.ListOssBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOssBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOssBucket',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOssBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oss_bucket(
        self,
        request: main_models.ListOssBucketRequest,
    ) -> main_models.ListOssBucketResponse:
        runtime = RuntimeOptions()
        return self.list_oss_bucket_with_options(request, runtime)

    async def list_oss_bucket_async(
        self,
        request: main_models.ListOssBucketRequest,
    ) -> main_models.ListOssBucketResponse:
        runtime = RuntimeOptions()
        return await self.list_oss_bucket_with_options_async(request, runtime)

    def list_oss_bucket_scan_info_with_options(
        self,
        request: main_models.ListOssBucketScanInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOssBucketScanInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.fuzz_bucket_name):
            query['FuzzBucketName'] = request.fuzz_bucket_name
        if not DaraCore.is_null(request.has_risk):
            query['HasRisk'] = request.has_risk
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOssBucketScanInfo',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOssBucketScanInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oss_bucket_scan_info_with_options_async(
        self,
        request: main_models.ListOssBucketScanInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOssBucketScanInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.fuzz_bucket_name):
            query['FuzzBucketName'] = request.fuzz_bucket_name
        if not DaraCore.is_null(request.has_risk):
            query['HasRisk'] = request.has_risk
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOssBucketScanInfo',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOssBucketScanInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oss_bucket_scan_info(
        self,
        request: main_models.ListOssBucketScanInfoRequest,
    ) -> main_models.ListOssBucketScanInfoResponse:
        runtime = RuntimeOptions()
        return self.list_oss_bucket_scan_info_with_options(request, runtime)

    async def list_oss_bucket_scan_info_async(
        self,
        request: main_models.ListOssBucketScanInfoRequest,
    ) -> main_models.ListOssBucketScanInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_oss_bucket_scan_info_with_options_async(request, runtime)

    def list_support_object_suffix_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportObjectSuffixResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListSupportObjectSuffix',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportObjectSuffixResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_support_object_suffix_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupportObjectSuffixResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListSupportObjectSuffix',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupportObjectSuffixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_support_object_suffix(self) -> main_models.ListSupportObjectSuffixResponse:
        runtime = RuntimeOptions()
        return self.list_support_object_suffix_with_options(runtime)

    async def list_support_object_suffix_async(self) -> main_models.ListSupportObjectSuffixResponse:
        runtime = RuntimeOptions()
        return await self.list_support_object_suffix_with_options_async(runtime)

    def operate_bucket_scan_task_with_options(
        self,
        request: main_models.OperateBucketScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateBucketScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.operate_code):
            query['OperateCode'] = request.operate_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateBucketScanTask',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateBucketScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_bucket_scan_task_with_options_async(
        self,
        request: main_models.OperateBucketScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateBucketScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.operate_code):
            query['OperateCode'] = request.operate_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateBucketScanTask',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateBucketScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_bucket_scan_task(
        self,
        request: main_models.OperateBucketScanTaskRequest,
    ) -> main_models.OperateBucketScanTaskResponse:
        runtime = RuntimeOptions()
        return self.operate_bucket_scan_task_with_options(request, runtime)

    async def operate_bucket_scan_task_async(
        self,
        request: main_models.OperateBucketScanTaskRequest,
    ) -> main_models.OperateBucketScanTaskResponse:
        runtime = RuntimeOptions()
        return await self.operate_bucket_scan_task_with_options_async(request, runtime)

    def update_oss_scan_config_with_options(
        self,
        request: main_models.UpdateOssScanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssScanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not DaraCore.is_null(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not DaraCore.is_null(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not DaraCore.is_null(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not DaraCore.is_null(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.real_time_incr):
            query['RealTimeIncr'] = request.real_time_incr
        if not DaraCore.is_null(request.scan_day_list):
            query['ScanDayList'] = request.scan_day_list
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssScanConfig',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssScanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oss_scan_config_with_options_async(
        self,
        request: main_models.UpdateOssScanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssScanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_key_prefix):
            query['AllKeyPrefix'] = request.all_key_prefix
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.decompress_max_file_count):
            query['DecompressMaxFileCount'] = request.decompress_max_file_count
        if not DaraCore.is_null(request.decompress_max_layer):
            query['DecompressMaxLayer'] = request.decompress_max_layer
        if not DaraCore.is_null(request.decryption_list):
            query['DecryptionList'] = request.decryption_list
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.key_prefix_list):
            query['KeyPrefixList'] = request.key_prefix_list
        if not DaraCore.is_null(request.key_suffix_list):
            query['KeySuffixList'] = request.key_suffix_list
        if not DaraCore.is_null(request.last_modified_start_time):
            query['LastModifiedStartTime'] = request.last_modified_start_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.real_time_incr):
            query['RealTimeIncr'] = request.real_time_incr
        if not DaraCore.is_null(request.scan_day_list):
            query['ScanDayList'] = request.scan_day_list
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssScanConfig',
            version = '2023-10-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssScanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oss_scan_config(
        self,
        request: main_models.UpdateOssScanConfigRequest,
    ) -> main_models.UpdateOssScanConfigResponse:
        runtime = RuntimeOptions()
        return self.update_oss_scan_config_with_options(request, runtime)

    async def update_oss_scan_config_async(
        self,
        request: main_models.UpdateOssScanConfigRequest,
    ) -> main_models.UpdateOssScanConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_oss_scan_config_with_options_async(request, runtime)
