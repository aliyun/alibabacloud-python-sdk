# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aisc20260101 import models as main_models
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
        self._endpoint = self.get_endpoint('aisc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_skill_file_check_with_options(
        self,
        request: main_models.CreateSkillFileCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillFileCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.files):
            query['Files'] = request.files
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillFileCheck',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillFileCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_file_check_with_options_async(
        self,
        request: main_models.CreateSkillFileCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillFileCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.files):
            query['Files'] = request.files
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillFileCheck',
            version = '2026-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillFileCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_file_check(
        self,
        request: main_models.CreateSkillFileCheckRequest,
    ) -> main_models.CreateSkillFileCheckResponse:
        runtime = RuntimeOptions()
        return self.create_skill_file_check_with_options(request, runtime)

    async def create_skill_file_check_async(
        self,
        request: main_models.CreateSkillFileCheckRequest,
    ) -> main_models.CreateSkillFileCheckResponse:
        runtime = RuntimeOptions()
        return await self.create_skill_file_check_with_options_async(request, runtime)
