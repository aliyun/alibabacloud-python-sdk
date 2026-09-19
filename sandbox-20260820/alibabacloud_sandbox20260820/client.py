# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sandbox20260820 import models as main_models
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
        self._endpoint = self.get_endpoint('sandbox', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_template_with_options(
        self,
        request: main_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: main_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    async def create_template_async(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(request, headers, runtime)

    def create_template_cache_with_options(
        self,
        request: main_models.CreateTemplateCacheRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateCacheResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplateCache',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/template-caches',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_cache_with_options_async(
        self,
        request: main_models.CreateTemplateCacheRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateCacheResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplateCache',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/template-caches',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template_cache(
        self,
        request: main_models.CreateTemplateCacheRequest,
    ) -> main_models.CreateTemplateCacheResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_template_cache_with_options(request, headers, runtime)

    async def create_template_cache_async(
        self,
        request: main_models.CreateTemplateCacheRequest,
    ) -> main_models.CreateTemplateCacheResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_template_cache_with_options_async(request, headers, runtime)

    def delete_template_with_options(
        self,
        template_id: str,
        request: main_models.DeleteTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        template_id: str,
        request: main_models.DeleteTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        template_id: str,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(template_id, request, headers, runtime)

    async def delete_template_async(
        self,
        template_id: str,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(template_id, request, headers, runtime)

    def delete_template_cache_with_options(
        self,
        template_id: str,
        request: main_models.DeleteTemplateCacheRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplateCache',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/template-caches/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_cache_with_options_async(
        self,
        template_id: str,
        request: main_models.DeleteTemplateCacheRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplateCache',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/template-caches/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template_cache(
        self,
        template_id: str,
        request: main_models.DeleteTemplateCacheRequest,
    ) -> main_models.DeleteTemplateCacheResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_template_cache_with_options(template_id, request, headers, runtime)

    async def delete_template_cache_async(
        self,
        template_id: str,
        request: main_models.DeleteTemplateCacheRequest,
    ) -> main_models.DeleteTemplateCacheResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_template_cache_with_options_async(template_id, request, headers, runtime)

    def describe_template_cache_with_options(
        self,
        template_id: str,
        request: main_models.DescribeTemplateCacheRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateCache',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/template-caches/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_cache_with_options_async(
        self,
        template_id: str,
        request: main_models.DescribeTemplateCacheRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateCache',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/template-caches/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_cache(
        self,
        template_id: str,
        request: main_models.DescribeTemplateCacheRequest,
    ) -> main_models.DescribeTemplateCacheResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_template_cache_with_options(template_id, request, headers, runtime)

    async def describe_template_cache_async(
        self,
        template_id: str,
        request: main_models.DescribeTemplateCacheRequest,
    ) -> main_models.DescribeTemplateCacheResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_template_cache_with_options_async(template_id, request, headers, runtime)

    def get_template_with_options(
        self,
        template_id: str,
        request: main_models.GetTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        template_id: str,
        request: main_models.GetTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        template_id: str,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_template_with_options(template_id, request, headers, runtime)

    async def get_template_async(
        self,
        template_id: str,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(template_id, request, headers, runtime)

    def list_template_cache_with_options(
        self,
        request: main_models.ListTemplateCacheRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        if not DaraCore.is_null(request.template_id):
            query['templateID'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateCache',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/template-caches',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_cache_with_options_async(
        self,
        request: main_models.ListTemplateCacheRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateCacheResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        if not DaraCore.is_null(request.template_id):
            query['templateID'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateCache',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/template-caches',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_cache(
        self,
        request: main_models.ListTemplateCacheRequest,
    ) -> main_models.ListTemplateCacheResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_template_cache_with_options(request, headers, runtime)

    async def list_template_cache_async(
        self,
        request: main_models.ListTemplateCacheRequest,
    ) -> main_models.ListTemplateCacheResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_template_cache_with_options_async(request, headers, runtime)

    def list_templates_with_options(
        self,
        request: main_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: main_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    async def list_templates_async(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(request, headers, runtime)

    def update_template_with_options(
        self,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates/{DaraURL.percent_encode(template_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2026-08-20',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-08-20/templates/{DaraURL.percent_encode(template_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_template_with_options(template_id, request, headers, runtime)

    async def update_template_async(
        self,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(template_id, request, headers, runtime)
