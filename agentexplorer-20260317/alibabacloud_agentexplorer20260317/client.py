# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentexplorer20260317 import models as main_models
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
        self._endpoint = self.get_endpoint('agentexplorer', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_skill_content_with_options(
        self,
        skill_name: str,
        request: main_models.GetSkillContentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillContentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSkillContent',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = f'/openapi/skills/{DaraURL.percent_encode(skill_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_content_with_options_async(
        self,
        skill_name: str,
        request: main_models.GetSkillContentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillContentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSkillContent',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = f'/openapi/skills/{DaraURL.percent_encode(skill_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_content(
        self,
        skill_name: str,
        request: main_models.GetSkillContentRequest,
    ) -> main_models.GetSkillContentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_skill_content_with_options(skill_name, request, headers, runtime)

    async def get_skill_content_async(
        self,
        skill_name: str,
        request: main_models.GetSkillContentRequest,
    ) -> main_models.GetSkillContentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_skill_content_with_options_async(skill_name, request, headers, runtime)

    def list_categories_with_options(
        self,
        request: main_models.ListCategoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoriesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = f'/openapi/categories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_categories_with_options_async(
        self,
        request: main_models.ListCategoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoriesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = f'/openapi/categories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_categories(
        self,
        request: main_models.ListCategoriesRequest,
    ) -> main_models.ListCategoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_categories_with_options(request, headers, runtime)

    async def list_categories_async(
        self,
        request: main_models.ListCategoriesRequest,
    ) -> main_models.ListCategoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_categories_with_options_async(request, headers, runtime)

    def search_skills_with_options(
        self,
        request: main_models.SearchSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_code):
            query['categoryCode'] = request.category_code
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchSkills',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = f'/openapi/skills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchSkillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_skills_with_options_async(
        self,
        request: main_models.SearchSkillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_code):
            query['categoryCode'] = request.category_code
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.skip):
            query['skip'] = request.skip
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchSkills',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = f'/openapi/skills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchSkillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_skills(
        self,
        request: main_models.SearchSkillsRequest,
    ) -> main_models.SearchSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_skills_with_options(request, headers, runtime)

    async def search_skills_async(
        self,
        request: main_models.SearchSkillsRequest,
    ) -> main_models.SearchSkillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_skills_with_options_async(request, headers, runtime)
