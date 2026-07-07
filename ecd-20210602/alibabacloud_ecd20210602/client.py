# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ecd20210602 import models as main_models
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
        self._endpoint_map = {
            'us-west-1': 'ecd.us-west-1.aliyuncs.com',
            'us-east-1': 'ecd.us-east-1.aliyuncs.com',
            'me-east-1': 'ecd.me-east-1.aliyuncs.com',
            'me-central-1': 'ecd.me-central-1.aliyuncs.com',
            'eu-west-1': 'ecd.eu-west-1.aliyuncs.com',
            'eu-central-1': 'ecd.eu-central-1.aliyuncs.com',
            'cn-zhangjiakou': 'ecd.cn-zhangjiakou.aliyuncs.com',
            'cn-wulanchabu': 'ecd.cn-wulanchabu.aliyuncs.com',
            'cn-shenzhen': 'ecd.cn-shenzhen.aliyuncs.com',
            'cn-shanghai-finance-1': 'ecd.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shanghai': 'ecd.cn-shanghai.aliyuncs.com',
            'cn-qingdao': 'ecd.cn-qingdao.aliyuncs.com',
            'cn-nanjing': 'ecd.cn-nanjing.aliyuncs.com',
            'cn-hongkong': 'ecd.cn-hongkong.aliyuncs.com',
            'cn-hangzhou-finance': 'ecd.cn-hangzhou-finance.aliyuncs.com',
            'cn-hangzhou': 'ecd.cn-hangzhou.aliyuncs.com',
            'cn-guangzhou': 'ecd.cn-guangzhou.aliyuncs.com',
            'cn-chengdu': 'ecd.cn-chengdu.aliyuncs.com',
            'cn-beijing': 'ecd.cn-beijing.aliyuncs.com',
            'ap-southeast-7': 'ecd.ap-southeast-7.aliyuncs.com',
            'ap-southeast-6': 'ecd.ap-southeast-6.aliyuncs.com',
            'ap-southeast-5': 'ecd.ap-southeast-5.aliyuncs.com',
            'ap-southeast-1': 'ecd.ap-southeast-1.aliyuncs.com',
            'ap-northeast-1': 'ecd.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_tenant_skill_with_options(
        self,
        tmp_req: main_models.CreateTenantSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTenantSkillResponse:
        tmp_req.validate()
        request = main_models.CreateTenantSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.env_vars):
            request.env_vars_shrink = Utils.array_to_string_with_specified_style(tmp_req.env_vars, 'EnvVars', 'json')
        query = {}
        if not DaraCore.is_null(request.api_key):
            query['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.env_vars_shrink):
            query['EnvVars'] = request.env_vars_shrink
        if not DaraCore.is_null(request.icon_etag):
            query['IconETag'] = request.icon_etag
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_icon):
            query['SkillIcon'] = request.skill_icon
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        if not DaraCore.is_null(request.slug):
            query['Slug'] = request.slug
        if not DaraCore.is_null(request.task_key):
            query['TaskKey'] = request.task_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTenantSkill',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTenantSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tenant_skill_with_options_async(
        self,
        tmp_req: main_models.CreateTenantSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTenantSkillResponse:
        tmp_req.validate()
        request = main_models.CreateTenantSkillShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.env_vars):
            request.env_vars_shrink = Utils.array_to_string_with_specified_style(tmp_req.env_vars, 'EnvVars', 'json')
        query = {}
        if not DaraCore.is_null(request.api_key):
            query['ApiKey'] = request.api_key
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.env_vars_shrink):
            query['EnvVars'] = request.env_vars_shrink
        if not DaraCore.is_null(request.icon_etag):
            query['IconETag'] = request.icon_etag
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_icon):
            query['SkillIcon'] = request.skill_icon
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        if not DaraCore.is_null(request.slug):
            query['Slug'] = request.slug
        if not DaraCore.is_null(request.task_key):
            query['TaskKey'] = request.task_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTenantSkill',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTenantSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tenant_skill(
        self,
        request: main_models.CreateTenantSkillRequest,
    ) -> main_models.CreateTenantSkillResponse:
        runtime = RuntimeOptions()
        return self.create_tenant_skill_with_options(request, runtime)

    async def create_tenant_skill_async(
        self,
        request: main_models.CreateTenantSkillRequest,
    ) -> main_models.CreateTenantSkillResponse:
        runtime = RuntimeOptions()
        return await self.create_tenant_skill_with_options_async(request, runtime)

    def delete_tenant_skills_with_options(
        self,
        request: main_models.DeleteTenantSkillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTenantSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_ids):
            query['SkillIds'] = request.skill_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTenantSkills',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTenantSkillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tenant_skills_with_options_async(
        self,
        request: main_models.DeleteTenantSkillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTenantSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_ids):
            query['SkillIds'] = request.skill_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTenantSkills',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTenantSkillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tenant_skills(
        self,
        request: main_models.DeleteTenantSkillsRequest,
    ) -> main_models.DeleteTenantSkillsResponse:
        runtime = RuntimeOptions()
        return self.delete_tenant_skills_with_options(request, runtime)

    async def delete_tenant_skills_async(
        self,
        request: main_models.DeleteTenantSkillsRequest,
    ) -> main_models.DeleteTenantSkillsResponse:
        runtime = RuntimeOptions()
        return await self.delete_tenant_skills_with_options_async(request, runtime)

    def get_oss_sts_token_with_options(
        self,
        request: main_models.GetOssStsTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssStsTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssStsToken',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssStsTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_sts_token_with_options_async(
        self,
        request: main_models.GetOssStsTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssStsTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssStsToken',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssStsTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_sts_token(
        self,
        request: main_models.GetOssStsTokenRequest,
    ) -> main_models.GetOssStsTokenResponse:
        runtime = RuntimeOptions()
        return self.get_oss_sts_token_with_options(request, runtime)

    async def get_oss_sts_token_async(
        self,
        request: main_models.GetOssStsTokenRequest,
    ) -> main_models.GetOssStsTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_sts_token_with_options_async(request, runtime)

    def get_parse_progress_with_options(
        self,
        request: main_models.GetParseProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParseProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_key):
            query['TaskKey'] = request.task_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParseProgress',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParseProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parse_progress_with_options_async(
        self,
        request: main_models.GetParseProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParseProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_key):
            query['TaskKey'] = request.task_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParseProgress',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParseProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parse_progress(
        self,
        request: main_models.GetParseProgressRequest,
    ) -> main_models.GetParseProgressResponse:
        runtime = RuntimeOptions()
        return self.get_parse_progress_with_options(request, runtime)

    async def get_parse_progress_async(
        self,
        request: main_models.GetParseProgressRequest,
    ) -> main_models.GetParseProgressResponse:
        runtime = RuntimeOptions()
        return await self.get_parse_progress_with_options_async(request, runtime)

    def list_secure_skill_identities_with_options(
        self,
        request: main_models.ListSecureSkillIdentitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecureSkillIdentitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecureSkillIdentities',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecureSkillIdentitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secure_skill_identities_with_options_async(
        self,
        request: main_models.ListSecureSkillIdentitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecureSkillIdentitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecureSkillIdentities',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecureSkillIdentitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secure_skill_identities(
        self,
        request: main_models.ListSecureSkillIdentitiesRequest,
    ) -> main_models.ListSecureSkillIdentitiesResponse:
        runtime = RuntimeOptions()
        return self.list_secure_skill_identities_with_options(request, runtime)

    async def list_secure_skill_identities_async(
        self,
        request: main_models.ListSecureSkillIdentitiesRequest,
    ) -> main_models.ListSecureSkillIdentitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_secure_skill_identities_with_options_async(request, runtime)

    def list_skill_authed_identities_with_options(
        self,
        request: main_models.ListSkillAuthedIdentitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillAuthedIdentitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillAuthedIdentities',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillAuthedIdentitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_authed_identities_with_options_async(
        self,
        request: main_models.ListSkillAuthedIdentitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillAuthedIdentitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillAuthedIdentities',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillAuthedIdentitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_authed_identities(
        self,
        request: main_models.ListSkillAuthedIdentitiesRequest,
    ) -> main_models.ListSkillAuthedIdentitiesResponse:
        runtime = RuntimeOptions()
        return self.list_skill_authed_identities_with_options(request, runtime)

    async def list_skill_authed_identities_async(
        self,
        request: main_models.ListSkillAuthedIdentitiesRequest,
    ) -> main_models.ListSkillAuthedIdentitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_skill_authed_identities_with_options_async(request, runtime)

    def list_skills_with_options(
        self,
        request: main_models.ListSkillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_ids):
            query['SkillIds'] = request.skill_ids
        if not DaraCore.is_null(request.supplier_type):
            query['SupplierType'] = request.supplier_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skills_with_options_async(
        self,
        request: main_models.ListSkillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_ids):
            query['SkillIds'] = request.skill_ids
        if not DaraCore.is_null(request.supplier_type):
            query['SupplierType'] = request.supplier_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skills(
        self,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        return self.list_skills_with_options(request, runtime)

    async def list_skills_async(
        self,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        return await self.list_skills_with_options_async(request, runtime)

    def parse_skill_package_with_options(
        self,
        request: main_models.ParseSkillPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ParseSkillPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oss_object_etag):
            query['OssObjectETag'] = request.oss_object_etag
        if not DaraCore.is_null(request.oss_object_key):
            query['OssObjectKey'] = request.oss_object_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ParseSkillPackage',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ParseSkillPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def parse_skill_package_with_options_async(
        self,
        request: main_models.ParseSkillPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ParseSkillPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.oss_object_etag):
            query['OssObjectETag'] = request.oss_object_etag
        if not DaraCore.is_null(request.oss_object_key):
            query['OssObjectKey'] = request.oss_object_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ParseSkillPackage',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ParseSkillPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def parse_skill_package(
        self,
        request: main_models.ParseSkillPackageRequest,
    ) -> main_models.ParseSkillPackageResponse:
        runtime = RuntimeOptions()
        return self.parse_skill_package_with_options(request, runtime)

    async def parse_skill_package_async(
        self,
        request: main_models.ParseSkillPackageRequest,
    ) -> main_models.ParseSkillPackageResponse:
        runtime = RuntimeOptions()
        return await self.parse_skill_package_with_options_async(request, runtime)

    def set_identity_skill_auth_with_options(
        self,
        request: main_models.SetIdentitySkillAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetIdentitySkillAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_install):
            query['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.identities):
            query['Identities'] = request.identities
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_ids):
            query['SkillIds'] = request.skill_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetIdentitySkillAuth',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetIdentitySkillAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_identity_skill_auth_with_options_async(
        self,
        request: main_models.SetIdentitySkillAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetIdentitySkillAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_install):
            query['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.identities):
            query['Identities'] = request.identities
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_ids):
            query['SkillIds'] = request.skill_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetIdentitySkillAuth',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetIdentitySkillAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_identity_skill_auth(
        self,
        request: main_models.SetIdentitySkillAuthRequest,
    ) -> main_models.SetIdentitySkillAuthResponse:
        runtime = RuntimeOptions()
        return self.set_identity_skill_auth_with_options(request, runtime)

    async def set_identity_skill_auth_async(
        self,
        request: main_models.SetIdentitySkillAuthRequest,
    ) -> main_models.SetIdentitySkillAuthResponse:
        runtime = RuntimeOptions()
        return await self.set_identity_skill_auth_with_options_async(request, runtime)

    def set_identity_skill_security_with_options(
        self,
        request: main_models.SetIdentitySkillSecurityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetIdentitySkillSecurityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.identity_ids):
            query['IdentityIds'] = request.identity_ids
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetIdentitySkillSecurity',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetIdentitySkillSecurityResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_identity_skill_security_with_options_async(
        self,
        request: main_models.SetIdentitySkillSecurityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetIdentitySkillSecurityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.identity_ids):
            query['IdentityIds'] = request.identity_ids
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetIdentitySkillSecurity',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetIdentitySkillSecurityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_identity_skill_security(
        self,
        request: main_models.SetIdentitySkillSecurityRequest,
    ) -> main_models.SetIdentitySkillSecurityResponse:
        runtime = RuntimeOptions()
        return self.set_identity_skill_security_with_options(request, runtime)

    async def set_identity_skill_security_async(
        self,
        request: main_models.SetIdentitySkillSecurityRequest,
    ) -> main_models.SetIdentitySkillSecurityResponse:
        runtime = RuntimeOptions()
        return await self.set_identity_skill_security_with_options_async(request, runtime)

    def set_tenant_skill_enabled_with_options(
        self,
        request: main_models.SetTenantSkillEnabledRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTenantSkillEnabledResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_ids):
            query['SkillIds'] = request.skill_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTenantSkillEnabled',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTenantSkillEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_tenant_skill_enabled_with_options_async(
        self,
        request: main_models.SetTenantSkillEnabledRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTenantSkillEnabledResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.skill_channel):
            query['SkillChannel'] = request.skill_channel
        if not DaraCore.is_null(request.skill_ids):
            query['SkillIds'] = request.skill_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTenantSkillEnabled',
            version = '2021-06-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTenantSkillEnabledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_tenant_skill_enabled(
        self,
        request: main_models.SetTenantSkillEnabledRequest,
    ) -> main_models.SetTenantSkillEnabledResponse:
        runtime = RuntimeOptions()
        return self.set_tenant_skill_enabled_with_options(request, runtime)

    async def set_tenant_skill_enabled_async(
        self,
        request: main_models.SetTenantSkillEnabledRequest,
    ) -> main_models.SetTenantSkillEnabledResponse:
        runtime = RuntimeOptions()
        return await self.set_tenant_skill_enabled_with_options_async(request, runtime)
