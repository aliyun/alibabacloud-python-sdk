# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_umeng_verify_agent20240131 import models as umeng_verify_agent_20240131_models
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
        self._endpoint = self.get_endpoint('umeng-verify-agent', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_with_options(
        self,
        request: umeng_verify_agent_20240131_models.CreateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_verify_agent_20240131_models.CreateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.pack_name):
            body['packName'] = request.pack_name
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.scheme_name):
            body['schemeName'] = request.scheme_name
        if not UtilClient.is_unset(request.sign_name):
            body['signName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Create',
            version='2024-01-31',
            protocol='HTTPS',
            pathname=f'/Create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_verify_agent_20240131_models.CreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_with_options_async(
        self,
        request: umeng_verify_agent_20240131_models.CreateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_verify_agent_20240131_models.CreateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.bundle_id):
            body['bundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.pack_name):
            body['packName'] = request.pack_name
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.scheme_name):
            body['schemeName'] = request.scheme_name
        if not UtilClient.is_unset(request.sign_name):
            body['signName'] = request.sign_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Create',
            version='2024-01-31',
            protocol='HTTPS',
            pathname=f'/Create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_verify_agent_20240131_models.CreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create(
        self,
        request: umeng_verify_agent_20240131_models.CreateRequest,
    ) -> umeng_verify_agent_20240131_models.CreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_with_options(request, headers, runtime)

    async def create_async(
        self,
        request: umeng_verify_agent_20240131_models.CreateRequest,
    ) -> umeng_verify_agent_20240131_models.CreateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_with_options_async(request, headers, runtime)

    def get_mobile_with_token_with_options(
        self,
        request: umeng_verify_agent_20240131_models.GetMobileWithTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_verify_agent_20240131_models.GetMobileWithTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_code):
            body['apiCode'] = request.api_code
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.os_type):
            body['osType'] = request.os_type
        if not UtilClient.is_unset(request.scheme_code):
            body['schemeCode'] = request.scheme_code
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMobileWithToken',
            version='2024-01-31',
            protocol='HTTPS',
            pathname=f'/GetMobileWithToken',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_verify_agent_20240131_models.GetMobileWithTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mobile_with_token_with_options_async(
        self,
        request: umeng_verify_agent_20240131_models.GetMobileWithTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_verify_agent_20240131_models.GetMobileWithTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_code):
            body['apiCode'] = request.api_code
        if not UtilClient.is_unset(request.operator_id):
            body['operatorId'] = request.operator_id
        if not UtilClient.is_unset(request.os_type):
            body['osType'] = request.os_type
        if not UtilClient.is_unset(request.scheme_code):
            body['schemeCode'] = request.scheme_code
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMobileWithToken',
            version='2024-01-31',
            protocol='HTTPS',
            pathname=f'/GetMobileWithToken',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_verify_agent_20240131_models.GetMobileWithTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mobile_with_token(
        self,
        request: umeng_verify_agent_20240131_models.GetMobileWithTokenRequest,
    ) -> umeng_verify_agent_20240131_models.GetMobileWithTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mobile_with_token_with_options(request, headers, runtime)

    async def get_mobile_with_token_async(
        self,
        request: umeng_verify_agent_20240131_models.GetMobileWithTokenRequest,
    ) -> umeng_verify_agent_20240131_models.GetMobileWithTokenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mobile_with_token_with_options_async(request, headers, runtime)

    def query_app_info_by_scheme_with_options(
        self,
        request: umeng_verify_agent_20240131_models.QueryAppInfoBySchemeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_verify_agent_20240131_models.QueryAppInfoBySchemeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scheme_code):
            body['schemeCode'] = request.scheme_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAppInfoByScheme',
            version='2024-01-31',
            protocol='HTTPS',
            pathname=f'/QueryAppInfoByScheme',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_verify_agent_20240131_models.QueryAppInfoBySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_app_info_by_scheme_with_options_async(
        self,
        request: umeng_verify_agent_20240131_models.QueryAppInfoBySchemeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_verify_agent_20240131_models.QueryAppInfoBySchemeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scheme_code):
            body['schemeCode'] = request.scheme_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAppInfoByScheme',
            version='2024-01-31',
            protocol='HTTPS',
            pathname=f'/QueryAppInfoByScheme',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_verify_agent_20240131_models.QueryAppInfoBySchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_app_info_by_scheme(
        self,
        request: umeng_verify_agent_20240131_models.QueryAppInfoBySchemeRequest,
    ) -> umeng_verify_agent_20240131_models.QueryAppInfoBySchemeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_app_info_by_scheme_with_options(request, headers, runtime)

    async def query_app_info_by_scheme_async(
        self,
        request: umeng_verify_agent_20240131_models.QueryAppInfoBySchemeRequest,
    ) -> umeng_verify_agent_20240131_models.QueryAppInfoBySchemeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_app_info_by_scheme_with_options_async(request, headers, runtime)
