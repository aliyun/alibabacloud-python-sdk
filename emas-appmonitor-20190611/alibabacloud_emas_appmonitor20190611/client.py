# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_emas_appmonitor20190611 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('emas-appmonitor', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_tlog_task_with_options(
        self,
        request: main_models.CreateTlogTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTlogTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ali_yun_current_pk):
            body['AliYunCurrentPk'] = request.ali_yun_current_pk
        if not DaraCore.is_null(request.ali_yun_main_pk):
            body['AliYunMainPk'] = request.ali_yun_main_pk
        if not DaraCore.is_null(request.ali_yun_name):
            body['AliYunName'] = request.ali_yun_name
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.brand):
            body['Brand'] = request.brand
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.collection_nums):
            body['CollectionNums'] = request.collection_nums
        if not DaraCore.is_null(request.days):
            body['Days'] = request.days
        if not DaraCore.is_null(request.device_json):
            body['DeviceJson'] = request.device_json
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.error_type):
            body['ErrorType'] = request.error_type
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.notify_setting_json):
            body['NotifySettingJson'] = request.notify_setting_json
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.os_version):
            body['OsVersion'] = request.os_version
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTlogTask',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTlogTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tlog_task_with_options_async(
        self,
        request: main_models.CreateTlogTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTlogTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ali_yun_current_pk):
            body['AliYunCurrentPk'] = request.ali_yun_current_pk
        if not DaraCore.is_null(request.ali_yun_main_pk):
            body['AliYunMainPk'] = request.ali_yun_main_pk
        if not DaraCore.is_null(request.ali_yun_name):
            body['AliYunName'] = request.ali_yun_name
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.brand):
            body['Brand'] = request.brand
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.collection_nums):
            body['CollectionNums'] = request.collection_nums
        if not DaraCore.is_null(request.days):
            body['Days'] = request.days
        if not DaraCore.is_null(request.device_json):
            body['DeviceJson'] = request.device_json
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.error_type):
            body['ErrorType'] = request.error_type
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.notify_setting_json):
            body['NotifySettingJson'] = request.notify_setting_json
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.os_version):
            body['OsVersion'] = request.os_version
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTlogTask',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTlogTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tlog_task(
        self,
        request: main_models.CreateTlogTaskRequest,
    ) -> main_models.CreateTlogTaskResponse:
        runtime = RuntimeOptions()
        return self.create_tlog_task_with_options(request, runtime)

    async def create_tlog_task_async(
        self,
        request: main_models.CreateTlogTaskRequest,
    ) -> main_models.CreateTlogTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_tlog_task_with_options_async(request, runtime)

    def get_error_with_options(
        self,
        request: main_models.GetErrorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErrorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.biz_module):
            body['BizModule'] = request.biz_module
        if not DaraCore.is_null(request.client_time):
            body['ClientTime'] = request.client_time
        if not DaraCore.is_null(request.did):
            body['Did'] = request.did
        if not DaraCore.is_null(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetError',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_error_with_options_async(
        self,
        request: main_models.GetErrorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErrorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.biz_module):
            body['BizModule'] = request.biz_module
        if not DaraCore.is_null(request.client_time):
            body['ClientTime'] = request.client_time
        if not DaraCore.is_null(request.did):
            body['Did'] = request.did
        if not DaraCore.is_null(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetError',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_error(
        self,
        request: main_models.GetErrorRequest,
    ) -> main_models.GetErrorResponse:
        runtime = RuntimeOptions()
        return self.get_error_with_options(request, runtime)

    async def get_error_async(
        self,
        request: main_models.GetErrorRequest,
    ) -> main_models.GetErrorResponse:
        runtime = RuntimeOptions()
        return await self.get_error_with_options_async(request, runtime)

    def get_errors_with_options(
        self,
        tmp_req: main_models.GetErrorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErrorsResponse:
        tmp_req.validate()
        request = main_models.GetErrorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.biz_module):
            body['BizModule'] = request.biz_module
        if not DaraCore.is_null(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not DaraCore.is_null(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        body_flat = {}
        if not DaraCore.is_null(request.time_range):
            body_flat['TimeRange'] = request.time_range
        if not DaraCore.is_null(request.utdid):
            body['Utdid'] = request.utdid
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetErrors',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErrorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_errors_with_options_async(
        self,
        tmp_req: main_models.GetErrorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetErrorsResponse:
        tmp_req.validate()
        request = main_models.GetErrorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.biz_module):
            body['BizModule'] = request.biz_module
        if not DaraCore.is_null(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not DaraCore.is_null(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        body_flat = {}
        if not DaraCore.is_null(request.time_range):
            body_flat['TimeRange'] = request.time_range
        if not DaraCore.is_null(request.utdid):
            body['Utdid'] = request.utdid
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetErrors',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetErrorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_errors(
        self,
        request: main_models.GetErrorsRequest,
    ) -> main_models.GetErrorsResponse:
        runtime = RuntimeOptions()
        return self.get_errors_with_options(request, runtime)

    async def get_errors_async(
        self,
        request: main_models.GetErrorsRequest,
    ) -> main_models.GetErrorsResponse:
        runtime = RuntimeOptions()
        return await self.get_errors_with_options_async(request, runtime)

    def get_issue_with_options(
        self,
        tmp_req: main_models.GetIssueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIssueResponse:
        tmp_req.validate()
        request = main_models.GetIssueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.biz_module):
            body['BizModule'] = request.biz_module
        if not DaraCore.is_null(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not DaraCore.is_null(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        body_flat = {}
        if not DaraCore.is_null(request.time_range):
            body_flat['TimeRange'] = request.time_range
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIssue',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIssueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_issue_with_options_async(
        self,
        tmp_req: main_models.GetIssueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIssueResponse:
        tmp_req.validate()
        request = main_models.GetIssueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.biz_module):
            body['BizModule'] = request.biz_module
        if not DaraCore.is_null(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not DaraCore.is_null(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        body_flat = {}
        if not DaraCore.is_null(request.time_range):
            body_flat['TimeRange'] = request.time_range
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIssue',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIssueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_issue(
        self,
        request: main_models.GetIssueRequest,
    ) -> main_models.GetIssueResponse:
        runtime = RuntimeOptions()
        return self.get_issue_with_options(request, runtime)

    async def get_issue_async(
        self,
        request: main_models.GetIssueRequest,
    ) -> main_models.GetIssueResponse:
        runtime = RuntimeOptions()
        return await self.get_issue_with_options_async(request, runtime)

    def get_issues_with_options(
        self,
        tmp_req: main_models.GetIssuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIssuesResponse:
        tmp_req.validate()
        request = main_models.GetIssuesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.biz_module):
            body['BizModule'] = request.biz_module
        if not DaraCore.is_null(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.order_by):
            body['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            body['OrderType'] = request.order_type
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not DaraCore.is_null(request.time_range):
            body_flat['TimeRange'] = request.time_range
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIssues',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIssuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_issues_with_options_async(
        self,
        tmp_req: main_models.GetIssuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIssuesResponse:
        tmp_req.validate()
        request = main_models.GetIssuesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.biz_module):
            body['BizModule'] = request.biz_module
        if not DaraCore.is_null(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.order_by):
            body['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            body['OrderType'] = request.order_type
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not DaraCore.is_null(request.time_range):
            body_flat['TimeRange'] = request.time_range
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIssues',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIssuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_issues(
        self,
        request: main_models.GetIssuesRequest,
    ) -> main_models.GetIssuesResponse:
        runtime = RuntimeOptions()
        return self.get_issues_with_options(request, runtime)

    async def get_issues_async(
        self,
        request: main_models.GetIssuesRequest,
    ) -> main_models.GetIssuesResponse:
        runtime = RuntimeOptions()
        return await self.get_issues_with_options_async(request, runtime)

    def get_symbolic_files_with_options(
        self,
        request: main_models.GetSymbolicFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSymbolicFilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.build_id):
            body['BuildId'] = request.build_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.export_status):
            body['ExportStatus'] = request.export_status
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSymbolicFiles',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSymbolicFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_symbolic_files_with_options_async(
        self,
        request: main_models.GetSymbolicFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSymbolicFilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.build_id):
            body['BuildId'] = request.build_id
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.export_status):
            body['ExportStatus'] = request.export_status
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSymbolicFiles',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSymbolicFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_symbolic_files(
        self,
        request: main_models.GetSymbolicFilesRequest,
    ) -> main_models.GetSymbolicFilesResponse:
        runtime = RuntimeOptions()
        return self.get_symbolic_files_with_options(request, runtime)

    async def get_symbolic_files_async(
        self,
        request: main_models.GetSymbolicFilesRequest,
    ) -> main_models.GetSymbolicFilesResponse:
        runtime = RuntimeOptions()
        return await self.get_symbolic_files_with_options_async(request, runtime)

    def get_tlog_collect_list_with_options(
        self,
        request: main_models.GetTlogCollectListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogCollectListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.author):
            body['Author'] = request.author
        if not DaraCore.is_null(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.create_begin_date):
            body['CreateBeginDate'] = request.create_begin_date
        if not DaraCore.is_null(request.create_end_date):
            body['CreateEndDate'] = request.create_end_date
        if not DaraCore.is_null(request.device_id):
            body['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.os_version):
            body['OsVersion'] = request.os_version
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.positive_comment):
            body['PositiveComment'] = request.positive_comment
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.update_begin_date):
            body['UpdateBeginDate'] = request.update_begin_date
        if not DaraCore.is_null(request.update_end_date):
            body['UpdateEndDate'] = request.update_end_date
        if not DaraCore.is_null(request.user_nick):
            body['UserNick'] = request.user_nick
        if not DaraCore.is_null(request.utdid):
            body['Utdid'] = request.utdid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogCollectList',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogCollectListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tlog_collect_list_with_options_async(
        self,
        request: main_models.GetTlogCollectListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogCollectListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.author):
            body['Author'] = request.author
        if not DaraCore.is_null(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.create_begin_date):
            body['CreateBeginDate'] = request.create_begin_date
        if not DaraCore.is_null(request.create_end_date):
            body['CreateEndDate'] = request.create_end_date
        if not DaraCore.is_null(request.device_id):
            body['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.os_version):
            body['OsVersion'] = request.os_version
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.positive_comment):
            body['PositiveComment'] = request.positive_comment
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.update_begin_date):
            body['UpdateBeginDate'] = request.update_begin_date
        if not DaraCore.is_null(request.update_end_date):
            body['UpdateEndDate'] = request.update_end_date
        if not DaraCore.is_null(request.user_nick):
            body['UserNick'] = request.user_nick
        if not DaraCore.is_null(request.utdid):
            body['Utdid'] = request.utdid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogCollectList',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogCollectListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tlog_collect_list(
        self,
        request: main_models.GetTlogCollectListRequest,
    ) -> main_models.GetTlogCollectListResponse:
        runtime = RuntimeOptions()
        return self.get_tlog_collect_list_with_options(request, runtime)

    async def get_tlog_collect_list_async(
        self,
        request: main_models.GetTlogCollectListRequest,
    ) -> main_models.GetTlogCollectListResponse:
        runtime = RuntimeOptions()
        return await self.get_tlog_collect_list_with_options_async(request, runtime)

    def get_tlog_device_info_with_options(
        self,
        request: main_models.GetTlogDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogDeviceInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            body['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogDeviceInfo',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tlog_device_info_with_options_async(
        self,
        request: main_models.GetTlogDeviceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogDeviceInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.device_id):
            body['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogDeviceInfo',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tlog_device_info(
        self,
        request: main_models.GetTlogDeviceInfoRequest,
    ) -> main_models.GetTlogDeviceInfoResponse:
        runtime = RuntimeOptions()
        return self.get_tlog_device_info_with_options(request, runtime)

    async def get_tlog_device_info_async(
        self,
        request: main_models.GetTlogDeviceInfoRequest,
    ) -> main_models.GetTlogDeviceInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_tlog_device_info_with_options_async(request, runtime)

    def get_tlog_device_list_with_options(
        self,
        request: main_models.GetTlogDeviceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogDeviceListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.brand):
            body['Brand'] = request.brand
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.create_begin_date):
            body['CreateBeginDate'] = request.create_begin_date
        if not DaraCore.is_null(request.create_end_date):
            body['CreateEndDate'] = request.create_end_date
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.os_version):
            body['OsVersion'] = request.os_version
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.update_begin_date):
            body['UpdateBeginDate'] = request.update_begin_date
        if not DaraCore.is_null(request.update_end_date):
            body['UpdateEndDate'] = request.update_end_date
        if not DaraCore.is_null(request.user_nick):
            body['UserNick'] = request.user_nick
        if not DaraCore.is_null(request.utdid):
            body['Utdid'] = request.utdid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogDeviceList',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tlog_device_list_with_options_async(
        self,
        request: main_models.GetTlogDeviceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogDeviceListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.brand):
            body['Brand'] = request.brand
        if not DaraCore.is_null(request.city):
            body['City'] = request.city
        if not DaraCore.is_null(request.create_begin_date):
            body['CreateBeginDate'] = request.create_begin_date
        if not DaraCore.is_null(request.create_end_date):
            body['CreateEndDate'] = request.create_end_date
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.os_version):
            body['OsVersion'] = request.os_version
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.update_begin_date):
            body['UpdateBeginDate'] = request.update_begin_date
        if not DaraCore.is_null(request.update_end_date):
            body['UpdateEndDate'] = request.update_end_date
        if not DaraCore.is_null(request.user_nick):
            body['UserNick'] = request.user_nick
        if not DaraCore.is_null(request.utdid):
            body['Utdid'] = request.utdid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogDeviceList',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogDeviceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tlog_device_list(
        self,
        request: main_models.GetTlogDeviceListRequest,
    ) -> main_models.GetTlogDeviceListResponse:
        runtime = RuntimeOptions()
        return self.get_tlog_device_list_with_options(request, runtime)

    async def get_tlog_device_list_async(
        self,
        request: main_models.GetTlogDeviceListRequest,
    ) -> main_models.GetTlogDeviceListResponse:
        runtime = RuntimeOptions()
        return await self.get_tlog_device_list_with_options_async(request, runtime)

    def get_tlog_task_collections_with_options(
        self,
        request: main_models.GetTlogTaskCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogTaskCollectionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogTaskCollections',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogTaskCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tlog_task_collections_with_options_async(
        self,
        request: main_models.GetTlogTaskCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogTaskCollectionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogTaskCollections',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogTaskCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tlog_task_collections(
        self,
        request: main_models.GetTlogTaskCollectionsRequest,
    ) -> main_models.GetTlogTaskCollectionsResponse:
        runtime = RuntimeOptions()
        return self.get_tlog_task_collections_with_options(request, runtime)

    async def get_tlog_task_collections_async(
        self,
        request: main_models.GetTlogTaskCollectionsRequest,
    ) -> main_models.GetTlogTaskCollectionsResponse:
        runtime = RuntimeOptions()
        return await self.get_tlog_task_collections_with_options_async(request, runtime)

    def get_tlog_task_info_with_options(
        self,
        request: main_models.GetTlogTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogTaskInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogTaskInfo',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tlog_task_info_with_options_async(
        self,
        request: main_models.GetTlogTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlogTaskInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTlogTaskInfo',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlogTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tlog_task_info(
        self,
        request: main_models.GetTlogTaskInfoRequest,
    ) -> main_models.GetTlogTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.get_tlog_task_info_with_options(request, runtime)

    async def get_tlog_task_info_async(
        self,
        request: main_models.GetTlogTaskInfoRequest,
    ) -> main_models.GetTlogTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_tlog_task_info_with_options_async(request, runtime)

    def request_upload_token_with_options(
        self,
        request: main_models.RequestUploadTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequestUploadTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RequestUploadToken',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequestUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_upload_token_with_options_async(
        self,
        request: main_models.RequestUploadTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RequestUploadTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RequestUploadToken',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RequestUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_upload_token(
        self,
        request: main_models.RequestUploadTokenRequest,
    ) -> main_models.RequestUploadTokenResponse:
        runtime = RuntimeOptions()
        return self.request_upload_token_with_options(request, runtime)

    async def request_upload_token_async(
        self,
        request: main_models.RequestUploadTokenRequest,
    ) -> main_models.RequestUploadTokenResponse:
        runtime = RuntimeOptions()
        return await self.request_upload_token_with_options_async(request, runtime)

    def search_tlog_with_options(
        self,
        request: main_models.SearchTlogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTlogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.device_id):
            body['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.level_json):
            body['LevelJson'] = request.level_json
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchTlog',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTlogResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_tlog_with_options_async(
        self,
        request: main_models.SearchTlogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTlogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.begin_date):
            body['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.device_id):
            body['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.keyword):
            body['Keyword'] = request.keyword
        if not DaraCore.is_null(request.level_json):
            body['LevelJson'] = request.level_json
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.page_index):
            body['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchTlog',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTlogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_tlog(
        self,
        request: main_models.SearchTlogRequest,
    ) -> main_models.SearchTlogResponse:
        runtime = RuntimeOptions()
        return self.search_tlog_with_options(request, runtime)

    async def search_tlog_async(
        self,
        request: main_models.SearchTlogRequest,
    ) -> main_models.SearchTlogResponse:
        runtime = RuntimeOptions()
        return await self.search_tlog_with_options_async(request, runtime)

    def submit_symbolic_with_options(
        self,
        request: main_models.SubmitSymbolicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSymbolicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.build_id):
            body['BuildId'] = request.build_id
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['FilePath'] = request.file_path
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSymbolic',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSymbolicResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_symbolic_with_options_async(
        self,
        request: main_models.SubmitSymbolicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSymbolicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_key):
            body['AppKey'] = request.app_key
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.build_id):
            body['BuildId'] = request.build_id
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_path):
            body['FilePath'] = request.file_path
        if not DaraCore.is_null(request.file_type):
            body['FileType'] = request.file_type
        if not DaraCore.is_null(request.os):
            body['Os'] = request.os
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSymbolic',
            version = '2019-06-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSymbolicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_symbolic(
        self,
        request: main_models.SubmitSymbolicRequest,
    ) -> main_models.SubmitSymbolicResponse:
        runtime = RuntimeOptions()
        return self.submit_symbolic_with_options(request, runtime)

    async def submit_symbolic_async(
        self,
        request: main_models.SubmitSymbolicRequest,
    ) -> main_models.SubmitSymbolicResponse:
        runtime = RuntimeOptions()
        return await self.submit_symbolic_with_options_async(request, runtime)
