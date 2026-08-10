# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_codesec20260401 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('codesec', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_projects_with_options(
        self,
        request: main_models.DescribeProjectsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjects',
            version = '2026-04-01',
            protocol = 'HTTPS',
            pathname = f'/v1/projects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_projects_with_options_async(
        self,
        request: main_models.DescribeProjectsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjects',
            version = '2026-04-01',
            protocol = 'HTTPS',
            pathname = f'/v1/projects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_projects(
        self,
        request: main_models.DescribeProjectsRequest,
    ) -> main_models.DescribeProjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_projects_with_options(request, headers, runtime)

    async def describe_projects_async(
        self,
        request: main_models.DescribeProjectsRequest,
    ) -> main_models.DescribeProjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_projects_with_options_async(request, headers, runtime)

    def describe_scan_results_by_engine_with_options(
        self,
        project_id: str,
        scan_id: str,
        engine: str,
        request: main_models.DescribeScanResultsByEngineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScanResultsByEngineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_state):
            query['baselineState'] = request.baseline_state
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.package_name):
            query['packageName'] = request.package_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScanResultsByEngine',
            version = '2026-04-01',
            protocol = 'HTTPS',
            pathname = f'/v1/projects/{DaraURL.percent_encode(project_id)}/scans/{DaraURL.percent_encode(scan_id)}/results/{DaraURL.percent_encode(engine)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScanResultsByEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scan_results_by_engine_with_options_async(
        self,
        project_id: str,
        scan_id: str,
        engine: str,
        request: main_models.DescribeScanResultsByEngineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScanResultsByEngineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_state):
            query['baselineState'] = request.baseline_state
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.package_name):
            query['packageName'] = request.package_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScanResultsByEngine',
            version = '2026-04-01',
            protocol = 'HTTPS',
            pathname = f'/v1/projects/{DaraURL.percent_encode(project_id)}/scans/{DaraURL.percent_encode(scan_id)}/results/{DaraURL.percent_encode(engine)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScanResultsByEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scan_results_by_engine(
        self,
        project_id: str,
        scan_id: str,
        engine: str,
        request: main_models.DescribeScanResultsByEngineRequest,
    ) -> main_models.DescribeScanResultsByEngineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_scan_results_by_engine_with_options(project_id, scan_id, engine, request, headers, runtime)

    async def describe_scan_results_by_engine_async(
        self,
        project_id: str,
        scan_id: str,
        engine: str,
        request: main_models.DescribeScanResultsByEngineRequest,
    ) -> main_models.DescribeScanResultsByEngineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_scan_results_by_engine_with_options_async(project_id, scan_id, engine, request, headers, runtime)

    def describe_scans_with_options(
        self,
        project_id: str,
        request: main_models.DescribeScansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScans',
            version = '2026-04-01',
            protocol = 'HTTPS',
            pathname = f'/v1/projects/{DaraURL.percent_encode(project_id)}/scans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scans_with_options_async(
        self,
        project_id: str,
        request: main_models.DescribeScansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeScans',
            version = '2026-04-01',
            protocol = 'HTTPS',
            pathname = f'/v1/projects/{DaraURL.percent_encode(project_id)}/scans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scans(
        self,
        project_id: str,
        request: main_models.DescribeScansRequest,
    ) -> main_models.DescribeScansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_scans_with_options(project_id, request, headers, runtime)

    async def describe_scans_async(
        self,
        project_id: str,
        request: main_models.DescribeScansRequest,
    ) -> main_models.DescribeScansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_scans_with_options_async(project_id, request, headers, runtime)
