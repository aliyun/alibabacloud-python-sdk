# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agenticbas20260630 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('agenticbas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_pentest_task_with_options(
        self,
        tmp_req: main_models.CreatePentestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePentestTaskResponse:
        tmp_req.validate()
        request = main_models.CreatePentestTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_input):
            request.operation_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_input, 'OperationInput', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_input_shrink):
            query['OperationInput'] = request.operation_input_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePentestTask',
            version = '2026-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePentestTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pentest_task_with_options_async(
        self,
        tmp_req: main_models.CreatePentestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePentestTaskResponse:
        tmp_req.validate()
        request = main_models.CreatePentestTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_input):
            request.operation_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_input, 'OperationInput', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_input_shrink):
            query['OperationInput'] = request.operation_input_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePentestTask',
            version = '2026-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePentestTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pentest_task(
        self,
        request: main_models.CreatePentestTaskRequest,
    ) -> main_models.CreatePentestTaskResponse:
        runtime = RuntimeOptions()
        return self.create_pentest_task_with_options(request, runtime)

    async def create_pentest_task_async(
        self,
        request: main_models.CreatePentestTaskRequest,
    ) -> main_models.CreatePentestTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_pentest_task_with_options_async(request, runtime)

    def describe_pentest_report_content_with_options(
        self,
        tmp_req: main_models.DescribePentestReportContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePentestReportContentResponse:
        tmp_req.validate()
        request = main_models.DescribePentestReportContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_input):
            request.operation_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_input, 'OperationInput', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_input_shrink):
            query['OperationInput'] = request.operation_input_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePentestReportContent',
            version = '2026-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePentestReportContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pentest_report_content_with_options_async(
        self,
        tmp_req: main_models.DescribePentestReportContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePentestReportContentResponse:
        tmp_req.validate()
        request = main_models.DescribePentestReportContentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_input):
            request.operation_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_input, 'OperationInput', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_input_shrink):
            query['OperationInput'] = request.operation_input_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePentestReportContent',
            version = '2026-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePentestReportContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pentest_report_content(
        self,
        request: main_models.DescribePentestReportContentRequest,
    ) -> main_models.DescribePentestReportContentResponse:
        runtime = RuntimeOptions()
        return self.describe_pentest_report_content_with_options(request, runtime)

    async def describe_pentest_report_content_async(
        self,
        request: main_models.DescribePentestReportContentRequest,
    ) -> main_models.DescribePentestReportContentResponse:
        runtime = RuntimeOptions()
        return await self.describe_pentest_report_content_with_options_async(request, runtime)

    def describe_pentest_task_list_with_options(
        self,
        tmp_req: main_models.DescribePentestTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePentestTaskListResponse:
        tmp_req.validate()
        request = main_models.DescribePentestTaskListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_input):
            request.operation_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_input, 'OperationInput', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_input_shrink):
            query['OperationInput'] = request.operation_input_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePentestTaskList',
            version = '2026-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePentestTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pentest_task_list_with_options_async(
        self,
        tmp_req: main_models.DescribePentestTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePentestTaskListResponse:
        tmp_req.validate()
        request = main_models.DescribePentestTaskListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_input):
            request.operation_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_input, 'OperationInput', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_input_shrink):
            query['OperationInput'] = request.operation_input_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePentestTaskList',
            version = '2026-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePentestTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pentest_task_list(
        self,
        request: main_models.DescribePentestTaskListRequest,
    ) -> main_models.DescribePentestTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_pentest_task_list_with_options(request, runtime)

    async def describe_pentest_task_list_async(
        self,
        request: main_models.DescribePentestTaskListRequest,
    ) -> main_models.DescribePentestTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_pentest_task_list_with_options_async(request, runtime)

    def describe_pentest_vuln_list_with_options(
        self,
        tmp_req: main_models.DescribePentestVulnListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePentestVulnListResponse:
        tmp_req.validate()
        request = main_models.DescribePentestVulnListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_input):
            request.operation_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_input, 'OperationInput', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_input_shrink):
            query['OperationInput'] = request.operation_input_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePentestVulnList',
            version = '2026-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePentestVulnListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pentest_vuln_list_with_options_async(
        self,
        tmp_req: main_models.DescribePentestVulnListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePentestVulnListResponse:
        tmp_req.validate()
        request = main_models.DescribePentestVulnListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_input):
            request.operation_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_input, 'OperationInput', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_input_shrink):
            query['OperationInput'] = request.operation_input_shrink
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePentestVulnList',
            version = '2026-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePentestVulnListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pentest_vuln_list(
        self,
        request: main_models.DescribePentestVulnListRequest,
    ) -> main_models.DescribePentestVulnListResponse:
        runtime = RuntimeOptions()
        return self.describe_pentest_vuln_list_with_options(request, runtime)

    async def describe_pentest_vuln_list_async(
        self,
        request: main_models.DescribePentestVulnListRequest,
    ) -> main_models.DescribePentestVulnListResponse:
        runtime = RuntimeOptions()
        return await self.describe_pentest_vuln_list_with_options_async(request, runtime)
