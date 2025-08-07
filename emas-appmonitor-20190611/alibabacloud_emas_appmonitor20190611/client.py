# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emas_appmonitor20190611 import models as emas_appmonitor_20190611_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_error_with_options(
        self,
        request: emas_appmonitor_20190611_models.GetErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetErrorResponse:
        """
        @summary 获取错误事件详情
        
        @param request: GetErrorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_module):
            body['BizModule'] = request.biz_module
        if not UtilClient.is_unset(request.client_time):
            body['ClientTime'] = request.client_time
        if not UtilClient.is_unset(request.did):
            body['Did'] = request.did
        if not UtilClient.is_unset(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetError',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetErrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_error_with_options_async(
        self,
        request: emas_appmonitor_20190611_models.GetErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetErrorResponse:
        """
        @summary 获取错误事件详情
        
        @param request: GetErrorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_module):
            body['BizModule'] = request.biz_module
        if not UtilClient.is_unset(request.client_time):
            body['ClientTime'] = request.client_time
        if not UtilClient.is_unset(request.did):
            body['Did'] = request.did
        if not UtilClient.is_unset(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetError',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetErrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_error(
        self,
        request: emas_appmonitor_20190611_models.GetErrorRequest,
    ) -> emas_appmonitor_20190611_models.GetErrorResponse:
        """
        @summary 获取错误事件详情
        
        @param request: GetErrorRequest
        @return: GetErrorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_error_with_options(request, runtime)

    async def get_error_async(
        self,
        request: emas_appmonitor_20190611_models.GetErrorRequest,
    ) -> emas_appmonitor_20190611_models.GetErrorResponse:
        """
        @summary 获取错误事件详情
        
        @param request: GetErrorRequest
        @return: GetErrorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_error_with_options_async(request, runtime)

    def get_errors_with_options(
        self,
        tmp_req: emas_appmonitor_20190611_models.GetErrorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetErrorsResponse:
        """
        @summary 获取某一聚合错误下所有的错误事件列表
        
        @param tmp_req: GetErrorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emas_appmonitor_20190611_models.GetErrorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_module):
            body['BizModule'] = request.biz_module
        if not UtilClient.is_unset(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        body_flat = {}
        if not UtilClient.is_unset(request.time_range):
            body_flat['TimeRange'] = request.time_range
        if not UtilClient.is_unset(request.utdid):
            body['Utdid'] = request.utdid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErrors',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetErrorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_errors_with_options_async(
        self,
        tmp_req: emas_appmonitor_20190611_models.GetErrorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetErrorsResponse:
        """
        @summary 获取某一聚合错误下所有的错误事件列表
        
        @param tmp_req: GetErrorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErrorsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emas_appmonitor_20190611_models.GetErrorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_module):
            body['BizModule'] = request.biz_module
        if not UtilClient.is_unset(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        body_flat = {}
        if not UtilClient.is_unset(request.time_range):
            body_flat['TimeRange'] = request.time_range
        if not UtilClient.is_unset(request.utdid):
            body['Utdid'] = request.utdid
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErrors',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetErrorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_errors(
        self,
        request: emas_appmonitor_20190611_models.GetErrorsRequest,
    ) -> emas_appmonitor_20190611_models.GetErrorsResponse:
        """
        @summary 获取某一聚合错误下所有的错误事件列表
        
        @param request: GetErrorsRequest
        @return: GetErrorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_errors_with_options(request, runtime)

    async def get_errors_async(
        self,
        request: emas_appmonitor_20190611_models.GetErrorsRequest,
    ) -> emas_appmonitor_20190611_models.GetErrorsResponse:
        """
        @summary 获取某一聚合错误下所有的错误事件列表
        
        @param request: GetErrorsRequest
        @return: GetErrorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_errors_with_options_async(request, runtime)

    def get_issue_with_options(
        self,
        tmp_req: emas_appmonitor_20190611_models.GetIssueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetIssueResponse:
        """
        @summary 获取聚合错误详情
        
        @param tmp_req: GetIssueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIssueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emas_appmonitor_20190611_models.GetIssueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_module):
            body['BizModule'] = request.biz_module
        if not UtilClient.is_unset(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        body_flat = {}
        if not UtilClient.is_unset(request.time_range):
            body_flat['TimeRange'] = request.time_range
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIssue',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetIssueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_issue_with_options_async(
        self,
        tmp_req: emas_appmonitor_20190611_models.GetIssueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetIssueResponse:
        """
        @summary 获取聚合错误详情
        
        @param tmp_req: GetIssueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIssueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emas_appmonitor_20190611_models.GetIssueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_module):
            body['BizModule'] = request.biz_module
        if not UtilClient.is_unset(request.digest_hash):
            body['DigestHash'] = request.digest_hash
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        body_flat = {}
        if not UtilClient.is_unset(request.time_range):
            body_flat['TimeRange'] = request.time_range
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIssue',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetIssueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_issue(
        self,
        request: emas_appmonitor_20190611_models.GetIssueRequest,
    ) -> emas_appmonitor_20190611_models.GetIssueResponse:
        """
        @summary 获取聚合错误详情
        
        @param request: GetIssueRequest
        @return: GetIssueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_issue_with_options(request, runtime)

    async def get_issue_async(
        self,
        request: emas_appmonitor_20190611_models.GetIssueRequest,
    ) -> emas_appmonitor_20190611_models.GetIssueResponse:
        """
        @summary 获取聚合错误详情
        
        @param request: GetIssueRequest
        @return: GetIssueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_issue_with_options_async(request, runtime)

    def get_issues_with_options(
        self,
        tmp_req: emas_appmonitor_20190611_models.GetIssuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetIssuesResponse:
        """
        @summary 获取聚合错误列表
        
        @param tmp_req: GetIssuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIssuesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emas_appmonitor_20190611_models.GetIssuesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_module):
            body['BizModule'] = request.biz_module
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not UtilClient.is_unset(request.time_range):
            body_flat['TimeRange'] = request.time_range
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIssues',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetIssuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_issues_with_options_async(
        self,
        tmp_req: emas_appmonitor_20190611_models.GetIssuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetIssuesResponse:
        """
        @summary 获取聚合错误列表
        
        @param tmp_req: GetIssuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIssuesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emas_appmonitor_20190611_models.GetIssuesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_module):
            body['BizModule'] = request.biz_module
        if not UtilClient.is_unset(request.filter_shrink):
            body['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not UtilClient.is_unset(request.time_range):
            body_flat['TimeRange'] = request.time_range
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIssues',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetIssuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_issues(
        self,
        request: emas_appmonitor_20190611_models.GetIssuesRequest,
    ) -> emas_appmonitor_20190611_models.GetIssuesResponse:
        """
        @summary 获取聚合错误列表
        
        @param request: GetIssuesRequest
        @return: GetIssuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_issues_with_options(request, runtime)

    async def get_issues_async(
        self,
        request: emas_appmonitor_20190611_models.GetIssuesRequest,
    ) -> emas_appmonitor_20190611_models.GetIssuesResponse:
        """
        @summary 获取聚合错误列表
        
        @param request: GetIssuesRequest
        @return: GetIssuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_issues_with_options_async(request, runtime)

    def get_symbolic_files_with_options(
        self,
        request: emas_appmonitor_20190611_models.GetSymbolicFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetSymbolicFilesResponse:
        """
        @summary 获取符号表文件列表
        
        @param request: GetSymbolicFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSymbolicFilesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.export_status):
            body['ExportStatus'] = request.export_status
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSymbolicFiles',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetSymbolicFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_symbolic_files_with_options_async(
        self,
        request: emas_appmonitor_20190611_models.GetSymbolicFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.GetSymbolicFilesResponse:
        """
        @summary 获取符号表文件列表
        
        @param request: GetSymbolicFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSymbolicFilesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.export_status):
            body['ExportStatus'] = request.export_status
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSymbolicFiles',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.GetSymbolicFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_symbolic_files(
        self,
        request: emas_appmonitor_20190611_models.GetSymbolicFilesRequest,
    ) -> emas_appmonitor_20190611_models.GetSymbolicFilesResponse:
        """
        @summary 获取符号表文件列表
        
        @param request: GetSymbolicFilesRequest
        @return: GetSymbolicFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_symbolic_files_with_options(request, runtime)

    async def get_symbolic_files_async(
        self,
        request: emas_appmonitor_20190611_models.GetSymbolicFilesRequest,
    ) -> emas_appmonitor_20190611_models.GetSymbolicFilesResponse:
        """
        @summary 获取符号表文件列表
        
        @param request: GetSymbolicFilesRequest
        @return: GetSymbolicFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_symbolic_files_with_options_async(request, runtime)

    def request_upload_token_with_options(
        self,
        request: emas_appmonitor_20190611_models.RequestUploadTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.RequestUploadTokenResponse:
        """
        @param request: RequestUploadTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RequestUploadTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RequestUploadToken',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.RequestUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def request_upload_token_with_options_async(
        self,
        request: emas_appmonitor_20190611_models.RequestUploadTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.RequestUploadTokenResponse:
        """
        @param request: RequestUploadTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RequestUploadTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RequestUploadToken',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.RequestUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def request_upload_token(
        self,
        request: emas_appmonitor_20190611_models.RequestUploadTokenRequest,
    ) -> emas_appmonitor_20190611_models.RequestUploadTokenResponse:
        """
        @param request: RequestUploadTokenRequest
        @return: RequestUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.request_upload_token_with_options(request, runtime)

    async def request_upload_token_async(
        self,
        request: emas_appmonitor_20190611_models.RequestUploadTokenRequest,
    ) -> emas_appmonitor_20190611_models.RequestUploadTokenResponse:
        """
        @param request: RequestUploadTokenRequest
        @return: RequestUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.request_upload_token_with_options_async(request, runtime)

    def submit_symbolic_with_options(
        self,
        request: emas_appmonitor_20190611_models.SubmitSymbolicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.SubmitSymbolicResponse:
        """
        @param request: SubmitSymbolicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSymbolicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSymbolic',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.SubmitSymbolicResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_symbolic_with_options_async(
        self,
        request: emas_appmonitor_20190611_models.SubmitSymbolicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emas_appmonitor_20190611_models.SubmitSymbolicResponse:
        """
        @param request: SubmitSymbolicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSymbolicResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.build_id):
            body['BuildId'] = request.build_id
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.os):
            body['Os'] = request.os
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSymbolic',
            version='2019-06-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emas_appmonitor_20190611_models.SubmitSymbolicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_symbolic(
        self,
        request: emas_appmonitor_20190611_models.SubmitSymbolicRequest,
    ) -> emas_appmonitor_20190611_models.SubmitSymbolicResponse:
        """
        @param request: SubmitSymbolicRequest
        @return: SubmitSymbolicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_symbolic_with_options(request, runtime)

    async def submit_symbolic_async(
        self,
        request: emas_appmonitor_20190611_models.SubmitSymbolicRequest,
    ) -> emas_appmonitor_20190611_models.SubmitSymbolicResponse:
        """
        @param request: SubmitSymbolicRequest
        @return: SubmitSymbolicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_symbolic_with_options_async(request, runtime)
