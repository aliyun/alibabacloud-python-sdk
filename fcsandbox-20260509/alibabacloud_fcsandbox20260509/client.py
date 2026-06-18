# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_fcsandbox20260509 import models as main_models
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
        self._endpoint = self.get_endpoint('fcsandbox', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def delete_quota_with_options(
        self,
        request: main_models.DeleteQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_value):
            query['tagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQuota',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/quotas/tag',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quota_with_options_async(
        self,
        request: main_models.DeleteQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_value):
            query['tagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQuota',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/quotas/tag',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quota(
        self,
        request: main_models.DeleteQuotaRequest,
    ) -> main_models.DeleteQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_quota_with_options(request, headers, runtime)

    async def delete_quota_async(
        self,
        request: main_models.DeleteQuotaRequest,
    ) -> main_models.DeleteQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_quota_with_options_async(request, headers, runtime)

    def describe_quota_with_options(
        self,
        request: main_models.DescribeQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_value):
            query['tagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQuota',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/quotas/tag',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_quota_with_options_async(
        self,
        request: main_models.DescribeQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_value):
            query['tagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeQuota',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/quotas/tag',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_quota(
        self,
        request: main_models.DescribeQuotaRequest,
    ) -> main_models.DescribeQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_quota_with_options(request, headers, runtime)

    async def describe_quota_async(
        self,
        request: main_models.DescribeQuotaRequest,
    ) -> main_models.DescribeQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_quota_with_options_async(request, headers, runtime)

    def list_quota_with_options(
        self,
        request: main_models.ListQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuota',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/quotas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quota_with_options_async(
        self,
        request: main_models.ListQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuota',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/quotas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quota(
        self,
        request: main_models.ListQuotaRequest,
    ) -> main_models.ListQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_quota_with_options(request, headers, runtime)

    async def list_quota_async(
        self,
        request: main_models.ListQuotaRequest,
    ) -> main_models.ListQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_quota_with_options_async(request, headers, runtime)

    def update_quota_with_options(
        self,
        request: main_models.UpdateQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuota',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/quotas/tag',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_with_options_async(
        self,
        request: main_models.UpdateQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuota',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/quotas/tag',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota(
        self,
        request: main_models.UpdateQuotaRequest,
    ) -> main_models.UpdateQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_quota_with_options(request, headers, runtime)

    async def update_quota_async(
        self,
        request: main_models.UpdateQuotaRequest,
    ) -> main_models.UpdateQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_quota_with_options_async(request, headers, runtime)
