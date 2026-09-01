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
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-shenzhen': 'fcsandbox.cn-shenzhen.aliyuncs.com',
            'cn-beijing': 'fcsandbox.cn-beijing.aliyuncs.com',
            'cn-shanghai': 'fcsandbox.cn-shanghai.aliyuncs.com',
            'cn-hongkong': 'fcsandbox.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'fcsandbox.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou': 'fcsandbox.cn-hangzhou.aliyuncs.com',
            'us-west-1': 'fcsandbox.us-west-1.aliyuncs.com',
            'us-east-1': 'fcsandbox.us-east-1.aliyuncs.com'
        }
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

    def create_api_key_with_options(
        self,
        request: main_models.CreateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_key_with_options_async(
        self,
        request: main_models.CreateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_key(
        self,
        request: main_models.CreateApiKeyRequest,
    ) -> main_models.CreateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_api_key_with_options(request, headers, runtime)

    async def create_api_key_async(
        self,
        request: main_models.CreateApiKeyRequest,
    ) -> main_models.CreateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_api_key_with_options_async(request, headers, runtime)

    def create_team_with_options(
        self,
        request: main_models.CreateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTeam',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_team_with_options_async(
        self,
        request: main_models.CreateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTeam',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_team(
        self,
        request: main_models.CreateTeamRequest,
    ) -> main_models.CreateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_team_with_options(request, headers, runtime)

    async def create_team_async(
        self,
        request: main_models.CreateTeamRequest,
    ) -> main_models.CreateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_team_with_options_async(request, headers, runtime)

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
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/templates',
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
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/templates',
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

    def create_volume_with_options(
        self,
        request: main_models.CreateVolumeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVolumeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVolume',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_volume_with_options_async(
        self,
        request: main_models.CreateVolumeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVolumeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVolume',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_volume(
        self,
        request: main_models.CreateVolumeRequest,
    ) -> main_models.CreateVolumeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_volume_with_options(request, headers, runtime)

    async def create_volume_async(
        self,
        request: main_models.CreateVolumeRequest,
    ) -> main_models.CreateVolumeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_volume_with_options_async(request, headers, runtime)

    def delete_api_key_with_options(
        self,
        api_key_id: str,
        request: main_models.DeleteApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys/{DaraURL.percent_encode(api_key_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_key_with_options_async(
        self,
        api_key_id: str,
        request: main_models.DeleteApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys/{DaraURL.percent_encode(api_key_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_key(
        self,
        api_key_id: str,
        request: main_models.DeleteApiKeyRequest,
    ) -> main_models.DeleteApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_api_key_with_options(api_key_id, request, headers, runtime)

    async def delete_api_key_async(
        self,
        api_key_id: str,
        request: main_models.DeleteApiKeyRequest,
    ) -> main_models.DeleteApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_api_key_with_options_async(api_key_id, request, headers, runtime)

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

    def delete_team_with_options(
        self,
        team_id: str,
        request: main_models.DeleteTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTeam',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams/{DaraURL.percent_encode(team_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_team_with_options_async(
        self,
        team_id: str,
        request: main_models.DeleteTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTeam',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams/{DaraURL.percent_encode(team_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_team(
        self,
        team_id: str,
        request: main_models.DeleteTeamRequest,
    ) -> main_models.DeleteTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_team_with_options(team_id, request, headers, runtime)

    async def delete_team_async(
        self,
        team_id: str,
        request: main_models.DeleteTeamRequest,
    ) -> main_models.DeleteTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_team_with_options_async(team_id, request, headers, runtime)

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
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/templates/{DaraURL.percent_encode(template_id)}',
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
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/templates/{DaraURL.percent_encode(template_id)}',
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

    def delete_volume_with_options(
        self,
        volume_id: str,
        request: main_models.DeleteVolumeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVolume',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes/{DaraURL.percent_encode(volume_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_volume_with_options_async(
        self,
        volume_id: str,
        request: main_models.DeleteVolumeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVolume',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes/{DaraURL.percent_encode(volume_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_volume(
        self,
        volume_id: str,
        request: main_models.DeleteVolumeRequest,
    ) -> main_models.DeleteVolumeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_volume_with_options(volume_id, request, headers, runtime)

    async def delete_volume_async(
        self,
        volume_id: str,
        request: main_models.DeleteVolumeRequest,
    ) -> main_models.DeleteVolumeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_volume_with_options_async(volume_id, request, headers, runtime)

    def describe_api_key_with_options(
        self,
        api_key_id: str,
        request: main_models.DescribeApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys/{DaraURL.percent_encode(api_key_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_key_with_options_async(
        self,
        api_key_id: str,
        request: main_models.DescribeApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys/{DaraURL.percent_encode(api_key_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_key(
        self,
        api_key_id: str,
        request: main_models.DescribeApiKeyRequest,
    ) -> main_models.DescribeApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_api_key_with_options(api_key_id, request, headers, runtime)

    async def describe_api_key_async(
        self,
        api_key_id: str,
        request: main_models.DescribeApiKeyRequest,
    ) -> main_models.DescribeApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_api_key_with_options_async(api_key_id, request, headers, runtime)

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

    def get_team_with_options(
        self,
        team_id: str,
        request: main_models.GetTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTeam',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams/{DaraURL.percent_encode(team_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_team_with_options_async(
        self,
        team_id: str,
        request: main_models.GetTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTeam',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams/{DaraURL.percent_encode(team_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_team(
        self,
        team_id: str,
        request: main_models.GetTeamRequest,
    ) -> main_models.GetTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_team_with_options(team_id, request, headers, runtime)

    async def get_team_async(
        self,
        team_id: str,
        request: main_models.GetTeamRequest,
    ) -> main_models.GetTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_team_with_options_async(team_id, request, headers, runtime)

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
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/templates/{DaraURL.percent_encode(template_id)}',
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
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/templates/{DaraURL.percent_encode(template_id)}',
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

    def get_volume_with_options(
        self,
        volume_id: str,
        request: main_models.GetVolumeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVolume',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes/{DaraURL.percent_encode(volume_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_volume_with_options_async(
        self,
        volume_id: str,
        request: main_models.GetVolumeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVolume',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes/{DaraURL.percent_encode(volume_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_volume(
        self,
        volume_id: str,
        request: main_models.GetVolumeRequest,
    ) -> main_models.GetVolumeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_volume_with_options(volume_id, request, headers, runtime)

    async def get_volume_async(
        self,
        volume_id: str,
        request: main_models.GetVolumeRequest,
    ) -> main_models.GetVolumeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_volume_with_options_async(volume_id, request, headers, runtime)

    def list_api_keys_with_options(
        self,
        request: main_models.ListApiKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_name):
            query['apiKeyName'] = request.api_key_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupID'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        if not DaraCore.is_null(request.user_id):
            query['userID'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiKeys',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_keys_with_options_async(
        self,
        request: main_models.ListApiKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_name):
            query['apiKeyName'] = request.api_key_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupID'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        if not DaraCore.is_null(request.user_id):
            query['userID'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiKeys',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_keys(
        self,
        request: main_models.ListApiKeysRequest,
    ) -> main_models.ListApiKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_api_keys_with_options(request, headers, runtime)

    async def list_api_keys_async(
        self,
        request: main_models.ListApiKeysRequest,
    ) -> main_models.ListApiKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_api_keys_with_options_async(request, headers, runtime)

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

    def list_teams_with_options(
        self,
        request: main_models.ListTeamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plan):
            query['plan'] = request.plan
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupID'] = request.resource_group_id
        if not DaraCore.is_null(request.team_name):
            query['teamName'] = request.team_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeams',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_teams_with_options_async(
        self,
        request: main_models.ListTeamsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTeamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plan):
            query['plan'] = request.plan
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupID'] = request.resource_group_id
        if not DaraCore.is_null(request.team_name):
            query['teamName'] = request.team_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTeams',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTeamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_teams(
        self,
        request: main_models.ListTeamsRequest,
    ) -> main_models.ListTeamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_teams_with_options(request, headers, runtime)

    async def list_teams_async(
        self,
        request: main_models.ListTeamsRequest,
    ) -> main_models.ListTeamsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_teams_with_options_async(request, headers, runtime)

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
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/templates',
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
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/templates',
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

    def list_volumes_with_options(
        self,
        request: main_models.ListVolumesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVolumesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupID'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        if not DaraCore.is_null(request.user_id):
            query['userID'] = request.user_id
        if not DaraCore.is_null(request.volume_name):
            query['volumeName'] = request.volume_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVolumes',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_volumes_with_options_async(
        self,
        request: main_models.ListVolumesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVolumesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupID'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.team_id):
            query['teamID'] = request.team_id
        if not DaraCore.is_null(request.user_id):
            query['userID'] = request.user_id
        if not DaraCore.is_null(request.volume_name):
            query['volumeName'] = request.volume_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVolumes',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_volumes(
        self,
        request: main_models.ListVolumesRequest,
    ) -> main_models.ListVolumesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_volumes_with_options(request, headers, runtime)

    async def list_volumes_async(
        self,
        request: main_models.ListVolumesRequest,
    ) -> main_models.ListVolumesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_volumes_with_options_async(request, headers, runtime)

    def reset_api_key_with_options(
        self,
        api_key_id: str,
        request: main_models.ResetApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResetApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys/{DaraURL.percent_encode(api_key_id)}/reset',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_api_key_with_options_async(
        self,
        api_key_id: str,
        request: main_models.ResetApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResetApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys/{DaraURL.percent_encode(api_key_id)}/reset',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_api_key(
        self,
        api_key_id: str,
        request: main_models.ResetApiKeyRequest,
    ) -> main_models.ResetApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reset_api_key_with_options(api_key_id, request, headers, runtime)

    async def reset_api_key_async(
        self,
        api_key_id: str,
        request: main_models.ResetApiKeyRequest,
    ) -> main_models.ResetApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reset_api_key_with_options_async(api_key_id, request, headers, runtime)

    def update_api_key_with_options(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys/{DaraURL.percent_encode(api_key_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_key_with_options_async(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiKey',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/api-keys/{DaraURL.percent_encode(api_key_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_key(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
    ) -> main_models.UpdateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_api_key_with_options(api_key_id, request, headers, runtime)

    async def update_api_key_async(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
    ) -> main_models.UpdateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_api_key_with_options_async(api_key_id, request, headers, runtime)

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

    def update_team_with_options(
        self,
        team_id: str,
        request: main_models.UpdateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTeam',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams/{DaraURL.percent_encode(team_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTeamResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_team_with_options_async(
        self,
        team_id: str,
        request: main_models.UpdateTeamRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTeamResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTeam',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/teams/{DaraURL.percent_encode(team_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTeamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_team(
        self,
        team_id: str,
        request: main_models.UpdateTeamRequest,
    ) -> main_models.UpdateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_team_with_options(team_id, request, headers, runtime)

    async def update_team_async(
        self,
        team_id: str,
        request: main_models.UpdateTeamRequest,
    ) -> main_models.UpdateTeamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_team_with_options_async(team_id, request, headers, runtime)

    def update_volume_with_options(
        self,
        volume_id: str,
        request: main_models.UpdateVolumeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVolumeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVolume',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes/{DaraURL.percent_encode(volume_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_volume_with_options_async(
        self,
        volume_id: str,
        request: main_models.UpdateVolumeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVolumeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVolume',
            version = '2026-05-09',
            protocol = 'HTTPS',
            pathname = f'/pop/2026-05-09/volumes/{DaraURL.percent_encode(volume_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_volume(
        self,
        volume_id: str,
        request: main_models.UpdateVolumeRequest,
    ) -> main_models.UpdateVolumeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_volume_with_options(volume_id, request, headers, runtime)

    async def update_volume_async(
        self,
        volume_id: str,
        request: main_models.UpdateVolumeRequest,
    ) -> main_models.UpdateVolumeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_volume_with_options_async(volume_id, request, headers, runtime)
