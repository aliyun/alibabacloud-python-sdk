# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aliding20230426 import models as aliding_20230426_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aliding', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_sheet_with_options(
        self,
        tmp_req: aliding_20230426_models.CreateSheetRequest,
        tmp_header: aliding_20230426_models.CreateSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateSheetResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/createSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateSheetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sheet_with_options_async(
        self,
        tmp_req: aliding_20230426_models.CreateSheetRequest,
        tmp_header: aliding_20230426_models.CreateSheetHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.CreateSheetResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.CreateSheetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.CreateSheetShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSheet',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/createSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.CreateSheetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sheet(
        self,
        request: aliding_20230426_models.CreateSheetRequest,
    ) -> aliding_20230426_models.CreateSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateSheetHeaders()
        return self.create_sheet_with_options(request, headers, runtime)

    async def create_sheet_async(
        self,
        request: aliding_20230426_models.CreateSheetRequest,
    ) -> aliding_20230426_models.CreateSheetResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.CreateSheetHeaders()
        return await self.create_sheet_with_options_async(request, headers, runtime)

    def insert_rows_before_with_options(
        self,
        tmp_req: aliding_20230426_models.InsertRowsBeforeRequest,
        tmp_header: aliding_20230426_models.InsertRowsBeforeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.InsertRowsBeforeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InsertRowsBeforeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InsertRowsBeforeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.row):
            body['Row'] = request.row
        if not UtilClient.is_unset(request.row_count):
            body['RowCount'] = request.row_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertRowsBefore',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/insertRowsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InsertRowsBeforeResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_rows_before_with_options_async(
        self,
        tmp_req: aliding_20230426_models.InsertRowsBeforeRequest,
        tmp_header: aliding_20230426_models.InsertRowsBeforeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> aliding_20230426_models.InsertRowsBeforeResponse:
        UtilClient.validate_model(tmp_req)
        request = aliding_20230426_models.InsertRowsBeforeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        headers = aliding_20230426_models.InsertRowsBeforeShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.account_context):
            headers.account_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.account_context, 'AccountContext', 'json')
        if not UtilClient.is_unset(tmp_req.tenant_context):
            request.tenant_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tenant_context, 'TenantContext', 'json')
        body = {}
        if not UtilClient.is_unset(request.row):
            body['Row'] = request.row
        if not UtilClient.is_unset(request.row_count):
            body['RowCount'] = request.row_count
        if not UtilClient.is_unset(request.sheet_id):
            body['SheetId'] = request.sheet_id
        if not UtilClient.is_unset(request.tenant_context_shrink):
            body['TenantContext'] = request.tenant_context_shrink
        if not UtilClient.is_unset(request.workbook_id):
            body['WorkbookId'] = request.workbook_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.account_context_shrink):
            real_headers['AccountContext'] = UtilClient.to_jsonstring(headers.account_context_shrink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InsertRowsBefore',
            version='2023-04-26',
            protocol='HTTPS',
            pathname=f'/dingtalk/v1/documents/insertRowsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aliding_20230426_models.InsertRowsBeforeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_rows_before(
        self,
        request: aliding_20230426_models.InsertRowsBeforeRequest,
    ) -> aliding_20230426_models.InsertRowsBeforeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InsertRowsBeforeHeaders()
        return self.insert_rows_before_with_options(request, headers, runtime)

    async def insert_rows_before_async(
        self,
        request: aliding_20230426_models.InsertRowsBeforeRequest,
    ) -> aliding_20230426_models.InsertRowsBeforeResponse:
        runtime = util_models.RuntimeOptions()
        headers = aliding_20230426_models.InsertRowsBeforeHeaders()
        return await self.insert_rows_before_with_options_async(request, headers, runtime)
