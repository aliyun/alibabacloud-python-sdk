# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_bsn20150512 import models as main_models
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
        self._endpoint = self.get_endpoint('bsn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_bsn_by_resource_with_options(
        self,
        request: main_models.GetBsnByResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBsnByResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliuid):
            query['aliuid'] = request.aliuid
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBsnByResource',
            version = '2015-05-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBsnByResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bsn_by_resource_with_options_async(
        self,
        request: main_models.GetBsnByResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBsnByResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliuid):
            query['aliuid'] = request.aliuid
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBsnByResource',
            version = '2015-05-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBsnByResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bsn_by_resource(
        self,
        request: main_models.GetBsnByResourceRequest,
    ) -> main_models.GetBsnByResourceResponse:
        runtime = RuntimeOptions()
        return self.get_bsn_by_resource_with_options(request, runtime)

    async def get_bsn_by_resource_async(
        self,
        request: main_models.GetBsnByResourceRequest,
    ) -> main_models.GetBsnByResourceResponse:
        runtime = RuntimeOptions()
        return await self.get_bsn_by_resource_with_options_async(request, runtime)

    def grant_bsn_code_with_options(
        self,
        request: main_models.GrantBsnCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantBsnCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.grant_to_aliuid):
            query['GrantToAliuid'] = request.grant_to_aliuid
        if not DaraCore.is_null(request.notes):
            query['Notes'] = request.notes
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantBsnCode',
            version = '2015-05-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantBsnCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_bsn_code_with_options_async(
        self,
        request: main_models.GrantBsnCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantBsnCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.grant_to_aliuid):
            query['GrantToAliuid'] = request.grant_to_aliuid
        if not DaraCore.is_null(request.notes):
            query['Notes'] = request.notes
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GrantBsnCode',
            version = '2015-05-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantBsnCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_bsn_code(
        self,
        request: main_models.GrantBsnCodeRequest,
    ) -> main_models.GrantBsnCodeResponse:
        runtime = RuntimeOptions()
        return self.grant_bsn_code_with_options(request, runtime)

    async def grant_bsn_code_async(
        self,
        request: main_models.GrantBsnCodeRequest,
    ) -> main_models.GrantBsnCodeResponse:
        runtime = RuntimeOptions()
        return await self.grant_bsn_code_with_options_async(request, runtime)

    def product_bind_bsn_with_options(
        self,
        request: main_models.ProductBindBsnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProductBindBsnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliuid):
            query['aliuid'] = request.aliuid
        if not DaraCore.is_null(request.num):
            query['num'] = request.num
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProductBindBsn',
            version = '2015-05-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProductBindBsnResponse(),
            self.call_api(params, req, runtime)
        )

    async def product_bind_bsn_with_options_async(
        self,
        request: main_models.ProductBindBsnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProductBindBsnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliuid):
            query['aliuid'] = request.aliuid
        if not DaraCore.is_null(request.num):
            query['num'] = request.num
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProductBindBsn',
            version = '2015-05-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProductBindBsnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def product_bind_bsn(
        self,
        request: main_models.ProductBindBsnRequest,
    ) -> main_models.ProductBindBsnResponse:
        runtime = RuntimeOptions()
        return self.product_bind_bsn_with_options(request, runtime)

    async def product_bind_bsn_async(
        self,
        request: main_models.ProductBindBsnRequest,
    ) -> main_models.ProductBindBsnResponse:
        runtime = RuntimeOptions()
        return await self.product_bind_bsn_with_options_async(request, runtime)
