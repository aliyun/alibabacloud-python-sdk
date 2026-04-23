# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_vod20170321 import models as main_models
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
            'cn-hangzhou': 'vod.cn-shanghai.aliyuncs.com',
            'ap-northeast-2-pop': 'vod.aliyuncs.com',
            'ap-southeast-2': 'vod.aliyuncs.com',
            'ap-southeast-3': 'vod.aliyuncs.com',
            'cn-beijing-finance-1': 'vod.aliyuncs.com',
            'cn-beijing-finance-pop': 'vod.aliyuncs.com',
            'cn-beijing-gov-1': 'vod.aliyuncs.com',
            'cn-beijing-nu16-b01': 'vod.aliyuncs.com',
            'cn-chengdu': 'vod.aliyuncs.com',
            'cn-edge-1': 'vod.aliyuncs.com',
            'cn-fujian': 'vod.aliyuncs.com',
            'cn-haidian-cm12-c01': 'vod.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'vod.aliyuncs.com',
            'cn-hangzhou-finance': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'vod.aliyuncs.com',
            'cn-hangzhou-test-306': 'vod.aliyuncs.com',
            'cn-hongkong-finance-pop': 'vod.aliyuncs.com',
            'cn-huhehaote': 'vod.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'vod.aliyuncs.com',
            'cn-qingdao': 'vod.aliyuncs.com',
            'cn-qingdao-nebula': 'vod.aliyuncs.com',
            'cn-shanghai-et15-b01': 'vod.aliyuncs.com',
            'cn-shanghai-et2-b01': 'vod.aliyuncs.com',
            'cn-shanghai-finance-1': 'vod.aliyuncs.com',
            'cn-shanghai-inner': 'vod.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'vod.aliyuncs.com',
            'cn-shenzhen-finance-1': 'vod.aliyuncs.com',
            'cn-shenzhen-inner': 'vod.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'vod.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'vod.aliyuncs.com',
            'cn-wuhan': 'vod.aliyuncs.com',
            'cn-wulanchabu': 'vod.aliyuncs.com',
            'cn-yushanfang': 'vod.aliyuncs.com',
            'cn-zhangbei': 'vod.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'vod.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'vod.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'vod.aliyuncs.com',
            'eu-west-1-oxs': 'vod.aliyuncs.com',
            'me-east-1': 'vod.aliyuncs.com',
            'rus-west-1-pop': 'vod.aliyuncs.com',
            'us-east-1': 'vod.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('vod', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_aitemplate_with_options(
        self,
        request: main_models.AddAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_aitemplate_with_options_async(
        self,
        request: main_models.AddAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAITemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_aitemplate(
        self,
        request: main_models.AddAITemplateRequest,
    ) -> main_models.AddAITemplateResponse:
        runtime = RuntimeOptions()
        return self.add_aitemplate_with_options(request, runtime)

    async def add_aitemplate_async(
        self,
        request: main_models.AddAITemplateRequest,
    ) -> main_models.AddAITemplateResponse:
        runtime = RuntimeOptions()
        return await self.add_aitemplate_with_options_async(request, runtime)

    def add_category_with_options(
        self,
        request: main_models.AddCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_name):
            query['CateName'] = request.cate_name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCategory',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_category_with_options_async(
        self,
        request: main_models.AddCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_name):
            query['CateName'] = request.cate_name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCategory',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_category(
        self,
        request: main_models.AddCategoryRequest,
    ) -> main_models.AddCategoryResponse:
        runtime = RuntimeOptions()
        return self.add_category_with_options(request, runtime)

    async def add_category_async(
        self,
        request: main_models.AddCategoryRequest,
    ) -> main_models.AddCategoryResponse:
        runtime = RuntimeOptions()
        return await self.add_category_with_options_async(request, runtime)

    def add_editing_project_with_options(
        self,
        request: main_models.AddEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.division):
            query['Division'] = request.division
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.timeline):
            query['Timeline'] = request.timeline
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_editing_project_with_options_async(
        self,
        request: main_models.AddEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.division):
            query['Division'] = request.division
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.timeline):
            query['Timeline'] = request.timeline
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEditingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_editing_project(
        self,
        request: main_models.AddEditingProjectRequest,
    ) -> main_models.AddEditingProjectResponse:
        runtime = RuntimeOptions()
        return self.add_editing_project_with_options(request, runtime)

    async def add_editing_project_async(
        self,
        request: main_models.AddEditingProjectRequest,
    ) -> main_models.AddEditingProjectResponse:
        runtime = RuntimeOptions()
        return await self.add_editing_project_with_options_async(request, runtime)

    def add_editing_project_materials_with_options(
        self,
        request: main_models.AddEditingProjectMaterialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEditingProjectMaterialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not DaraCore.is_null(request.material_type):
            query['MaterialType'] = request.material_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEditingProjectMaterials',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_editing_project_materials_with_options_async(
        self,
        request: main_models.AddEditingProjectMaterialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddEditingProjectMaterialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not DaraCore.is_null(request.material_type):
            query['MaterialType'] = request.material_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEditingProjectMaterials',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddEditingProjectMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_editing_project_materials(
        self,
        request: main_models.AddEditingProjectMaterialsRequest,
    ) -> main_models.AddEditingProjectMaterialsResponse:
        runtime = RuntimeOptions()
        return self.add_editing_project_materials_with_options(request, runtime)

    async def add_editing_project_materials_async(
        self,
        request: main_models.AddEditingProjectMaterialsRequest,
    ) -> main_models.AddEditingProjectMaterialsResponse:
        runtime = RuntimeOptions()
        return await self.add_editing_project_materials_with_options_async(request, runtime)

    def add_transcode_template_group_with_options(
        self,
        request: main_models.AddTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        if not DaraCore.is_null(request.transcode_template_list):
            query['TranscodeTemplateList'] = request.transcode_template_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_transcode_template_group_with_options_async(
        self,
        request: main_models.AddTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        if not DaraCore.is_null(request.transcode_template_list):
            query['TranscodeTemplateList'] = request.transcode_template_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTranscodeTemplateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_transcode_template_group(
        self,
        request: main_models.AddTranscodeTemplateGroupRequest,
    ) -> main_models.AddTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return self.add_transcode_template_group_with_options(request, runtime)

    async def add_transcode_template_group_async(
        self,
        request: main_models.AddTranscodeTemplateGroupRequest,
    ) -> main_models.AddTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_transcode_template_group_with_options_async(request, runtime)

    def add_vod_domain_with_options(
        self,
        request: main_models.AddVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vod_domain_with_options_async(
        self,
        request: main_models.AddVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_url):
            query['CheckUrl'] = request.check_url
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVodDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vod_domain(
        self,
        request: main_models.AddVodDomainRequest,
    ) -> main_models.AddVodDomainResponse:
        runtime = RuntimeOptions()
        return self.add_vod_domain_with_options(request, runtime)

    async def add_vod_domain_async(
        self,
        request: main_models.AddVodDomainRequest,
    ) -> main_models.AddVodDomainResponse:
        runtime = RuntimeOptions()
        return await self.add_vod_domain_with_options_async(request, runtime)

    def add_vod_storage_for_app_with_options(
        self,
        request: main_models.AddVodStorageForAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVodStorageForAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVodStorageForApp',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVodStorageForAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vod_storage_for_app_with_options_async(
        self,
        request: main_models.AddVodStorageForAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVodStorageForAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVodStorageForApp',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVodStorageForAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vod_storage_for_app(
        self,
        request: main_models.AddVodStorageForAppRequest,
    ) -> main_models.AddVodStorageForAppResponse:
        runtime = RuntimeOptions()
        return self.add_vod_storage_for_app_with_options(request, runtime)

    async def add_vod_storage_for_app_async(
        self,
        request: main_models.AddVodStorageForAppRequest,
    ) -> main_models.AddVodStorageForAppResponse:
        runtime = RuntimeOptions()
        return await self.add_vod_storage_for_app_with_options_async(request, runtime)

    def add_vod_template_with_options(
        self,
        request: main_models.AddVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vod_template_with_options_async(
        self,
        request: main_models.AddVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVodTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vod_template(
        self,
        request: main_models.AddVodTemplateRequest,
    ) -> main_models.AddVodTemplateResponse:
        runtime = RuntimeOptions()
        return self.add_vod_template_with_options(request, runtime)

    async def add_vod_template_async(
        self,
        request: main_models.AddVodTemplateRequest,
    ) -> main_models.AddVodTemplateResponse:
        runtime = RuntimeOptions()
        return await self.add_vod_template_with_options_async(request, runtime)

    def add_watermark_with_options(
        self,
        request: main_models.AddWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.watermark_config):
            query['WatermarkConfig'] = request.watermark_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_watermark_with_options_async(
        self,
        request: main_models.AddWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.file_url):
            query['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.watermark_config):
            query['WatermarkConfig'] = request.watermark_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_watermark(
        self,
        request: main_models.AddWatermarkRequest,
    ) -> main_models.AddWatermarkResponse:
        runtime = RuntimeOptions()
        return self.add_watermark_with_options(request, runtime)

    async def add_watermark_async(
        self,
        request: main_models.AddWatermarkRequest,
    ) -> main_models.AddWatermarkResponse:
        runtime = RuntimeOptions()
        return await self.add_watermark_with_options_async(request, runtime)

    def attach_app_policy_to_identity_with_options(
        self,
        request: main_models.AttachAppPolicyToIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachAppPolicyToIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.identity_name):
            query['IdentityName'] = request.identity_name
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachAppPolicyToIdentity',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachAppPolicyToIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_app_policy_to_identity_with_options_async(
        self,
        request: main_models.AttachAppPolicyToIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachAppPolicyToIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.identity_name):
            query['IdentityName'] = request.identity_name
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachAppPolicyToIdentity',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachAppPolicyToIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_app_policy_to_identity(
        self,
        request: main_models.AttachAppPolicyToIdentityRequest,
    ) -> main_models.AttachAppPolicyToIdentityResponse:
        runtime = RuntimeOptions()
        return self.attach_app_policy_to_identity_with_options(request, runtime)

    async def attach_app_policy_to_identity_async(
        self,
        request: main_models.AttachAppPolicyToIdentityRequest,
    ) -> main_models.AttachAppPolicyToIdentityResponse:
        runtime = RuntimeOptions()
        return await self.attach_app_policy_to_identity_with_options_async(request, runtime)

    def batch_get_media_infos_with_options(
        self,
        request: main_models.BatchGetMediaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetMediaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetMediaInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetMediaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_media_infos_with_options_async(
        self,
        request: main_models.BatchGetMediaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetMediaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetMediaInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetMediaInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_media_infos(
        self,
        request: main_models.BatchGetMediaInfosRequest,
    ) -> main_models.BatchGetMediaInfosResponse:
        runtime = RuntimeOptions()
        return self.batch_get_media_infos_with_options(request, runtime)

    async def batch_get_media_infos_async(
        self,
        request: main_models.BatchGetMediaInfosRequest,
    ) -> main_models.BatchGetMediaInfosResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_media_infos_with_options_async(request, runtime)

    def batch_set_vod_domain_configs_with_options(
        self,
        request: main_models.BatchSetVodDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetVodDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetVodDomainConfigs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetVodDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_vod_domain_configs_with_options_async(
        self,
        request: main_models.BatchSetVodDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetVodDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetVodDomainConfigs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetVodDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_vod_domain_configs(
        self,
        request: main_models.BatchSetVodDomainConfigsRequest,
    ) -> main_models.BatchSetVodDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.batch_set_vod_domain_configs_with_options(request, runtime)

    async def batch_set_vod_domain_configs_async(
        self,
        request: main_models.BatchSetVodDomainConfigsRequest,
    ) -> main_models.BatchSetVodDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.batch_set_vod_domain_configs_with_options_async(request, runtime)

    def batch_start_vod_domain_with_options(
        self,
        request: main_models.BatchStartVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_vod_domain_with_options_async(
        self,
        request: main_models.BatchStartVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartVodDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_vod_domain(
        self,
        request: main_models.BatchStartVodDomainRequest,
    ) -> main_models.BatchStartVodDomainResponse:
        runtime = RuntimeOptions()
        return self.batch_start_vod_domain_with_options(request, runtime)

    async def batch_start_vod_domain_async(
        self,
        request: main_models.BatchStartVodDomainRequest,
    ) -> main_models.BatchStartVodDomainResponse:
        runtime = RuntimeOptions()
        return await self.batch_start_vod_domain_with_options_async(request, runtime)

    def batch_stop_vod_domain_with_options(
        self,
        request: main_models.BatchStopVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_vod_domain_with_options_async(
        self,
        request: main_models.BatchStopVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopVodDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_vod_domain(
        self,
        request: main_models.BatchStopVodDomainRequest,
    ) -> main_models.BatchStopVodDomainResponse:
        runtime = RuntimeOptions()
        return self.batch_stop_vod_domain_with_options(request, runtime)

    async def batch_stop_vod_domain_async(
        self,
        request: main_models.BatchStopVodDomainRequest,
    ) -> main_models.BatchStopVodDomainResponse:
        runtime = RuntimeOptions()
        return await self.batch_stop_vod_domain_with_options_async(request, runtime)

    def cancel_url_upload_jobs_with_options(
        self,
        request: main_models.CancelUrlUploadJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUrlUploadJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.upload_urls):
            query['UploadUrls'] = request.upload_urls
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelUrlUploadJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUrlUploadJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_url_upload_jobs_with_options_async(
        self,
        request: main_models.CancelUrlUploadJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUrlUploadJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.upload_urls):
            query['UploadUrls'] = request.upload_urls
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelUrlUploadJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUrlUploadJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_url_upload_jobs(
        self,
        request: main_models.CancelUrlUploadJobsRequest,
    ) -> main_models.CancelUrlUploadJobsResponse:
        runtime = RuntimeOptions()
        return self.cancel_url_upload_jobs_with_options(request, runtime)

    async def cancel_url_upload_jobs_async(
        self,
        request: main_models.CancelUrlUploadJobsRequest,
    ) -> main_models.CancelUrlUploadJobsResponse:
        runtime = RuntimeOptions()
        return await self.cancel_url_upload_jobs_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_app_info_with_options(
        self,
        request: main_models.CreateAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_info_with_options_async(
        self,
        request: main_models.CreateAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_info(
        self,
        request: main_models.CreateAppInfoRequest,
    ) -> main_models.CreateAppInfoResponse:
        runtime = RuntimeOptions()
        return self.create_app_info_with_options(request, runtime)

    async def create_app_info_async(
        self,
        request: main_models.CreateAppInfoRequest,
    ) -> main_models.CreateAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.create_app_info_with_options_async(request, runtime)

    def create_audit_with_options(
        self,
        request: main_models.CreateAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_content):
            query['AuditContent'] = request.audit_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAudit',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_audit_with_options_async(
        self,
        request: main_models.CreateAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_content):
            query['AuditContent'] = request.audit_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAudit',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_audit(
        self,
        request: main_models.CreateAuditRequest,
    ) -> main_models.CreateAuditResponse:
        runtime = RuntimeOptions()
        return self.create_audit_with_options(request, runtime)

    async def create_audit_async(
        self,
        request: main_models.CreateAuditRequest,
    ) -> main_models.CreateAuditResponse:
        runtime = RuntimeOptions()
        return await self.create_audit_with_options_async(request, runtime)

    def create_upload_attached_media_with_options(
        self,
        request: main_models.CreateUploadAttachedMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUploadAttachedMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.cate_ids):
            query['CateIds'] = request.cate_ids
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_size):
            query['FileSize'] = request.file_size
        if not DaraCore.is_null(request.media_ext):
            query['MediaExt'] = request.media_ext
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUploadAttachedMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUploadAttachedMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_upload_attached_media_with_options_async(
        self,
        request: main_models.CreateUploadAttachedMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUploadAttachedMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.cate_ids):
            query['CateIds'] = request.cate_ids
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_size):
            query['FileSize'] = request.file_size
        if not DaraCore.is_null(request.media_ext):
            query['MediaExt'] = request.media_ext
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUploadAttachedMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUploadAttachedMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_upload_attached_media(
        self,
        request: main_models.CreateUploadAttachedMediaRequest,
    ) -> main_models.CreateUploadAttachedMediaResponse:
        runtime = RuntimeOptions()
        return self.create_upload_attached_media_with_options(request, runtime)

    async def create_upload_attached_media_async(
        self,
        request: main_models.CreateUploadAttachedMediaRequest,
    ) -> main_models.CreateUploadAttachedMediaResponse:
        runtime = RuntimeOptions()
        return await self.create_upload_attached_media_with_options_async(request, runtime)

    def create_upload_image_with_options(
        self,
        request: main_models.CreateUploadImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUploadImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.image_ext):
            query['ImageExt'] = request.image_ext
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.original_file_name):
            query['OriginalFileName'] = request.original_file_name
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUploadImage',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUploadImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_upload_image_with_options_async(
        self,
        request: main_models.CreateUploadImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUploadImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.image_ext):
            query['ImageExt'] = request.image_ext
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.original_file_name):
            query['OriginalFileName'] = request.original_file_name
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUploadImage',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUploadImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_upload_image(
        self,
        request: main_models.CreateUploadImageRequest,
    ) -> main_models.CreateUploadImageResponse:
        runtime = RuntimeOptions()
        return self.create_upload_image_with_options(request, runtime)

    async def create_upload_image_async(
        self,
        request: main_models.CreateUploadImageRequest,
    ) -> main_models.CreateUploadImageResponse:
        runtime = RuntimeOptions()
        return await self.create_upload_image_with_options_async(request, runtime)

    def create_upload_video_with_options(
        self,
        request: main_models.CreateUploadVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUploadVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_size):
            query['FileSize'] = request.file_size
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUploadVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUploadVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_upload_video_with_options_async(
        self,
        request: main_models.CreateUploadVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUploadVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.file_size):
            query['FileSize'] = request.file_size
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUploadVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUploadVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_upload_video(
        self,
        request: main_models.CreateUploadVideoRequest,
    ) -> main_models.CreateUploadVideoResponse:
        runtime = RuntimeOptions()
        return self.create_upload_video_with_options(request, runtime)

    async def create_upload_video_async(
        self,
        request: main_models.CreateUploadVideoRequest,
    ) -> main_models.CreateUploadVideoResponse:
        runtime = RuntimeOptions()
        return await self.create_upload_video_with_options_async(request, runtime)

    def decrypt_kmsdata_key_with_options(
        self,
        request: main_models.DecryptKMSDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecryptKMSDataKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cipher_text):
            query['CipherText'] = request.cipher_text
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DecryptKMSDataKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecryptKMSDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def decrypt_kmsdata_key_with_options_async(
        self,
        request: main_models.DecryptKMSDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecryptKMSDataKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cipher_text):
            query['CipherText'] = request.cipher_text
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DecryptKMSDataKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecryptKMSDataKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decrypt_kmsdata_key(
        self,
        request: main_models.DecryptKMSDataKeyRequest,
    ) -> main_models.DecryptKMSDataKeyResponse:
        runtime = RuntimeOptions()
        return self.decrypt_kmsdata_key_with_options(request, runtime)

    async def decrypt_kmsdata_key_async(
        self,
        request: main_models.DecryptKMSDataKeyRequest,
    ) -> main_models.DecryptKMSDataKeyResponse:
        runtime = RuntimeOptions()
        return await self.decrypt_kmsdata_key_with_options_async(request, runtime)

    def delete_aiimage_infos_with_options(
        self,
        request: main_models.DeleteAIImageInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAIImageInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aiimage_info_ids):
            query['AIImageInfoIds'] = request.aiimage_info_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAIImageInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAIImageInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aiimage_infos_with_options_async(
        self,
        request: main_models.DeleteAIImageInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAIImageInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aiimage_info_ids):
            query['AIImageInfoIds'] = request.aiimage_info_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAIImageInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAIImageInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aiimage_infos(
        self,
        request: main_models.DeleteAIImageInfosRequest,
    ) -> main_models.DeleteAIImageInfosResponse:
        runtime = RuntimeOptions()
        return self.delete_aiimage_infos_with_options(request, runtime)

    async def delete_aiimage_infos_async(
        self,
        request: main_models.DeleteAIImageInfosRequest,
    ) -> main_models.DeleteAIImageInfosResponse:
        runtime = RuntimeOptions()
        return await self.delete_aiimage_infos_with_options_async(request, runtime)

    def delete_aitemplate_with_options(
        self,
        request: main_models.DeleteAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aitemplate_with_options_async(
        self,
        request: main_models.DeleteAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAITemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aitemplate(
        self,
        request: main_models.DeleteAITemplateRequest,
    ) -> main_models.DeleteAITemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_aitemplate_with_options(request, runtime)

    async def delete_aitemplate_async(
        self,
        request: main_models.DeleteAITemplateRequest,
    ) -> main_models.DeleteAITemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_aitemplate_with_options_async(request, runtime)

    def delete_app_info_with_options(
        self,
        request: main_models.DeleteAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_info_with_options_async(
        self,
        request: main_models.DeleteAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_info(
        self,
        request: main_models.DeleteAppInfoRequest,
    ) -> main_models.DeleteAppInfoResponse:
        runtime = RuntimeOptions()
        return self.delete_app_info_with_options(request, runtime)

    async def delete_app_info_async(
        self,
        request: main_models.DeleteAppInfoRequest,
    ) -> main_models.DeleteAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_info_with_options_async(request, runtime)

    def delete_attached_media_with_options(
        self,
        request: main_models.DeleteAttachedMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAttachedMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAttachedMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAttachedMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_attached_media_with_options_async(
        self,
        request: main_models.DeleteAttachedMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAttachedMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAttachedMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAttachedMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_attached_media(
        self,
        request: main_models.DeleteAttachedMediaRequest,
    ) -> main_models.DeleteAttachedMediaResponse:
        runtime = RuntimeOptions()
        return self.delete_attached_media_with_options(request, runtime)

    async def delete_attached_media_async(
        self,
        request: main_models.DeleteAttachedMediaRequest,
    ) -> main_models.DeleteAttachedMediaResponse:
        runtime = RuntimeOptions()
        return await self.delete_attached_media_with_options_async(request, runtime)

    def delete_category_with_options(
        self,
        request: main_models.DeleteCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCategory',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: main_models.DeleteCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCategory',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_category(
        self,
        request: main_models.DeleteCategoryRequest,
    ) -> main_models.DeleteCategoryResponse:
        runtime = RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    async def delete_category_async(
        self,
        request: main_models.DeleteCategoryRequest,
    ) -> main_models.DeleteCategoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_category_with_options_async(request, runtime)

    def delete_dynamic_image_with_options(
        self,
        request: main_models.DeleteDynamicImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDynamicImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_image_ids):
            query['DynamicImageIds'] = request.dynamic_image_ids
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDynamicImage',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDynamicImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dynamic_image_with_options_async(
        self,
        request: main_models.DeleteDynamicImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDynamicImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_image_ids):
            query['DynamicImageIds'] = request.dynamic_image_ids
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDynamicImage',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDynamicImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dynamic_image(
        self,
        request: main_models.DeleteDynamicImageRequest,
    ) -> main_models.DeleteDynamicImageResponse:
        runtime = RuntimeOptions()
        return self.delete_dynamic_image_with_options(request, runtime)

    async def delete_dynamic_image_async(
        self,
        request: main_models.DeleteDynamicImageRequest,
    ) -> main_models.DeleteDynamicImageResponse:
        runtime = RuntimeOptions()
        return await self.delete_dynamic_image_with_options_async(request, runtime)

    def delete_editing_project_with_options(
        self,
        request: main_models.DeleteEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_ids):
            query['ProjectIds'] = request.project_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_editing_project_with_options_async(
        self,
        request: main_models.DeleteEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_ids):
            query['ProjectIds'] = request.project_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEditingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_editing_project(
        self,
        request: main_models.DeleteEditingProjectRequest,
    ) -> main_models.DeleteEditingProjectResponse:
        runtime = RuntimeOptions()
        return self.delete_editing_project_with_options(request, runtime)

    async def delete_editing_project_async(
        self,
        request: main_models.DeleteEditingProjectRequest,
    ) -> main_models.DeleteEditingProjectResponse:
        runtime = RuntimeOptions()
        return await self.delete_editing_project_with_options_async(request, runtime)

    def delete_editing_project_materials_with_options(
        self,
        request: main_models.DeleteEditingProjectMaterialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEditingProjectMaterialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not DaraCore.is_null(request.material_type):
            query['MaterialType'] = request.material_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEditingProjectMaterials',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_editing_project_materials_with_options_async(
        self,
        request: main_models.DeleteEditingProjectMaterialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEditingProjectMaterialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not DaraCore.is_null(request.material_type):
            query['MaterialType'] = request.material_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEditingProjectMaterials',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEditingProjectMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_editing_project_materials(
        self,
        request: main_models.DeleteEditingProjectMaterialsRequest,
    ) -> main_models.DeleteEditingProjectMaterialsResponse:
        runtime = RuntimeOptions()
        return self.delete_editing_project_materials_with_options(request, runtime)

    async def delete_editing_project_materials_async(
        self,
        request: main_models.DeleteEditingProjectMaterialsRequest,
    ) -> main_models.DeleteEditingProjectMaterialsResponse:
        runtime = RuntimeOptions()
        return await self.delete_editing_project_materials_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: main_models.DeleteImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_image_type):
            query['DeleteImageType'] = request.delete_image_type
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.image_urls):
            query['ImageURLs'] = request.image_urls
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImage',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: main_models.DeleteImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_image_type):
            query['DeleteImageType'] = request.delete_image_type
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.image_type):
            query['ImageType'] = request.image_type
        if not DaraCore.is_null(request.image_urls):
            query['ImageURLs'] = request.image_urls
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImage',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image(
        self,
        request: main_models.DeleteImageRequest,
    ) -> main_models.DeleteImageResponse:
        runtime = RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: main_models.DeleteImageRequest,
    ) -> main_models.DeleteImageResponse:
        runtime = RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_message_callback_with_options(
        self,
        request: main_models.DeleteMessageCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessageCallback',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_message_callback_with_options_async(
        self,
        request: main_models.DeleteMessageCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMessageCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMessageCallback',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMessageCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_message_callback(
        self,
        request: main_models.DeleteMessageCallbackRequest,
    ) -> main_models.DeleteMessageCallbackResponse:
        runtime = RuntimeOptions()
        return self.delete_message_callback_with_options(request, runtime)

    async def delete_message_callback_async(
        self,
        request: main_models.DeleteMessageCallbackRequest,
    ) -> main_models.DeleteMessageCallbackResponse:
        runtime = RuntimeOptions()
        return await self.delete_message_callback_with_options_async(request, runtime)

    def delete_mezzanines_with_options(
        self,
        request: main_models.DeleteMezzaninesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMezzaninesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        if not DaraCore.is_null(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMezzanines',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMezzaninesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mezzanines_with_options_async(
        self,
        request: main_models.DeleteMezzaninesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMezzaninesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        if not DaraCore.is_null(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMezzanines',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMezzaninesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mezzanines(
        self,
        request: main_models.DeleteMezzaninesRequest,
    ) -> main_models.DeleteMezzaninesResponse:
        runtime = RuntimeOptions()
        return self.delete_mezzanines_with_options(request, runtime)

    async def delete_mezzanines_async(
        self,
        request: main_models.DeleteMezzaninesRequest,
    ) -> main_models.DeleteMezzaninesResponse:
        runtime = RuntimeOptions()
        return await self.delete_mezzanines_with_options_async(request, runtime)

    def delete_multipart_upload_with_options(
        self,
        request: main_models.DeleteMultipartUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultipartUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultipartUpload',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultipartUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_multipart_upload_with_options_async(
        self,
        request: main_models.DeleteMultipartUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultipartUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultipartUpload',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultipartUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_multipart_upload(
        self,
        request: main_models.DeleteMultipartUploadRequest,
    ) -> main_models.DeleteMultipartUploadResponse:
        runtime = RuntimeOptions()
        return self.delete_multipart_upload_with_options(request, runtime)

    async def delete_multipart_upload_async(
        self,
        request: main_models.DeleteMultipartUploadRequest,
    ) -> main_models.DeleteMultipartUploadResponse:
        runtime = RuntimeOptions()
        return await self.delete_multipart_upload_with_options_async(request, runtime)

    def delete_stream_with_options(
        self,
        request: main_models.DeleteStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStream',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stream_with_options_async(
        self,
        request: main_models.DeleteStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStream',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stream(
        self,
        request: main_models.DeleteStreamRequest,
    ) -> main_models.DeleteStreamResponse:
        runtime = RuntimeOptions()
        return self.delete_stream_with_options(request, runtime)

    async def delete_stream_async(
        self,
        request: main_models.DeleteStreamRequest,
    ) -> main_models.DeleteStreamResponse:
        runtime = RuntimeOptions()
        return await self.delete_stream_with_options_async(request, runtime)

    def delete_transcode_template_group_with_options(
        self,
        request: main_models.DeleteTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_del_group):
            query['ForceDelGroup'] = request.force_del_group
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        if not DaraCore.is_null(request.transcode_template_ids):
            query['TranscodeTemplateIds'] = request.transcode_template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_transcode_template_group_with_options_async(
        self,
        request: main_models.DeleteTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force_del_group):
            query['ForceDelGroup'] = request.force_del_group
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        if not DaraCore.is_null(request.transcode_template_ids):
            query['TranscodeTemplateIds'] = request.transcode_template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTranscodeTemplateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_transcode_template_group(
        self,
        request: main_models.DeleteTranscodeTemplateGroupRequest,
    ) -> main_models.DeleteTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_transcode_template_group_with_options(request, runtime)

    async def delete_transcode_template_group_async(
        self,
        request: main_models.DeleteTranscodeTemplateGroupRequest,
    ) -> main_models.DeleteTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_transcode_template_group_with_options_async(request, runtime)

    def delete_video_with_options(
        self,
        request: main_models.DeleteVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        if not DaraCore.is_null(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_video_with_options_async(
        self,
        request: main_models.DeleteVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        if not DaraCore.is_null(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_video(
        self,
        request: main_models.DeleteVideoRequest,
    ) -> main_models.DeleteVideoResponse:
        runtime = RuntimeOptions()
        return self.delete_video_with_options(request, runtime)

    async def delete_video_async(
        self,
        request: main_models.DeleteVideoRequest,
    ) -> main_models.DeleteVideoResponse:
        runtime = RuntimeOptions()
        return await self.delete_video_with_options_async(request, runtime)

    def delete_vod_domain_with_options(
        self,
        request: main_models.DeleteVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vod_domain_with_options_async(
        self,
        request: main_models.DeleteVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVodDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vod_domain(
        self,
        request: main_models.DeleteVodDomainRequest,
    ) -> main_models.DeleteVodDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_vod_domain_with_options(request, runtime)

    async def delete_vod_domain_async(
        self,
        request: main_models.DeleteVodDomainRequest,
    ) -> main_models.DeleteVodDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_vod_domain_with_options_async(request, runtime)

    def delete_vod_specific_config_with_options(
        self,
        request: main_models.DeleteVodSpecificConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVodSpecificConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVodSpecificConfig',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVodSpecificConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vod_specific_config_with_options_async(
        self,
        request: main_models.DeleteVodSpecificConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVodSpecificConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['ConfigId'] = request.config_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVodSpecificConfig',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVodSpecificConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vod_specific_config(
        self,
        request: main_models.DeleteVodSpecificConfigRequest,
    ) -> main_models.DeleteVodSpecificConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_vod_specific_config_with_options(request, runtime)

    async def delete_vod_specific_config_async(
        self,
        request: main_models.DeleteVodSpecificConfigRequest,
    ) -> main_models.DeleteVodSpecificConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_vod_specific_config_with_options_async(request, runtime)

    def delete_vod_template_with_options(
        self,
        request: main_models.DeleteVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vod_template_id):
            query['VodTemplateId'] = request.vod_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vod_template_with_options_async(
        self,
        request: main_models.DeleteVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vod_template_id):
            query['VodTemplateId'] = request.vod_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVodTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vod_template(
        self,
        request: main_models.DeleteVodTemplateRequest,
    ) -> main_models.DeleteVodTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_vod_template_with_options(request, runtime)

    async def delete_vod_template_async(
        self,
        request: main_models.DeleteVodTemplateRequest,
    ) -> main_models.DeleteVodTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_vod_template_with_options_async(request, runtime)

    def delete_watermark_with_options(
        self,
        request: main_models.DeleteWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_watermark_with_options_async(
        self,
        request: main_models.DeleteWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_watermark(
        self,
        request: main_models.DeleteWatermarkRequest,
    ) -> main_models.DeleteWatermarkResponse:
        runtime = RuntimeOptions()
        return self.delete_watermark_with_options(request, runtime)

    async def delete_watermark_async(
        self,
        request: main_models.DeleteWatermarkRequest,
    ) -> main_models.DeleteWatermarkResponse:
        runtime = RuntimeOptions()
        return await self.delete_watermark_with_options_async(request, runtime)

    def describe_media_distribution_with_options(
        self,
        request: main_models.DescribeMediaDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMediaDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMediaDistribution',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMediaDistributionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_media_distribution_with_options_async(
        self,
        request: main_models.DescribeMediaDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMediaDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMediaDistribution',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMediaDistributionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_media_distribution(
        self,
        request: main_models.DescribeMediaDistributionRequest,
    ) -> main_models.DescribeMediaDistributionResponse:
        runtime = RuntimeOptions()
        return self.describe_media_distribution_with_options(request, runtime)

    async def describe_media_distribution_async(
        self,
        request: main_models.DescribeMediaDistributionRequest,
    ) -> main_models.DescribeMediaDistributionResponse:
        runtime = RuntimeOptions()
        return await self.describe_media_distribution_with_options_async(request, runtime)

    def describe_play_top_videos_with_options(
        self,
        request: main_models.DescribePlayTopVideosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlayTopVideosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_date):
            query['BizDate'] = request.biz_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlayTopVideos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlayTopVideosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_top_videos_with_options_async(
        self,
        request: main_models.DescribePlayTopVideosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlayTopVideosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_date):
            query['BizDate'] = request.biz_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlayTopVideos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlayTopVideosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_top_videos(
        self,
        request: main_models.DescribePlayTopVideosRequest,
    ) -> main_models.DescribePlayTopVideosResponse:
        runtime = RuntimeOptions()
        return self.describe_play_top_videos_with_options(request, runtime)

    async def describe_play_top_videos_async(
        self,
        request: main_models.DescribePlayTopVideosRequest,
    ) -> main_models.DescribePlayTopVideosResponse:
        runtime = RuntimeOptions()
        return await self.describe_play_top_videos_with_options_async(request, runtime)

    def describe_play_user_avg_with_options(
        self,
        request: main_models.DescribePlayUserAvgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlayUserAvgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlayUserAvg',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlayUserAvgResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_user_avg_with_options_async(
        self,
        request: main_models.DescribePlayUserAvgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlayUserAvgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlayUserAvg',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlayUserAvgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_user_avg(
        self,
        request: main_models.DescribePlayUserAvgRequest,
    ) -> main_models.DescribePlayUserAvgResponse:
        runtime = RuntimeOptions()
        return self.describe_play_user_avg_with_options(request, runtime)

    async def describe_play_user_avg_async(
        self,
        request: main_models.DescribePlayUserAvgRequest,
    ) -> main_models.DescribePlayUserAvgResponse:
        runtime = RuntimeOptions()
        return await self.describe_play_user_avg_with_options_async(request, runtime)

    def describe_play_user_total_with_options(
        self,
        request: main_models.DescribePlayUserTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlayUserTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlayUserTotal',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlayUserTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_user_total_with_options_async(
        self,
        request: main_models.DescribePlayUserTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlayUserTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlayUserTotal',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlayUserTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_user_total(
        self,
        request: main_models.DescribePlayUserTotalRequest,
    ) -> main_models.DescribePlayUserTotalResponse:
        runtime = RuntimeOptions()
        return self.describe_play_user_total_with_options(request, runtime)

    async def describe_play_user_total_async(
        self,
        request: main_models.DescribePlayUserTotalRequest,
    ) -> main_models.DescribePlayUserTotalResponse:
        runtime = RuntimeOptions()
        return await self.describe_play_user_total_with_options_async(request, runtime)

    def describe_play_video_statis_with_options(
        self,
        request: main_models.DescribePlayVideoStatisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlayVideoStatisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlayVideoStatis',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlayVideoStatisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_video_statis_with_options_async(
        self,
        request: main_models.DescribePlayVideoStatisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePlayVideoStatisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePlayVideoStatis',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePlayVideoStatisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_video_statis(
        self,
        request: main_models.DescribePlayVideoStatisRequest,
    ) -> main_models.DescribePlayVideoStatisResponse:
        runtime = RuntimeOptions()
        return self.describe_play_video_statis_with_options(request, runtime)

    async def describe_play_video_statis_async(
        self,
        request: main_models.DescribePlayVideoStatisRequest,
    ) -> main_models.DescribePlayVideoStatisResponse:
        runtime = RuntimeOptions()
        return await self.describe_play_video_statis_with_options_async(request, runtime)

    def describe_vod_aidata_with_options(
        self,
        request: main_models.DescribeVodAIDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodAIDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aitype):
            query['AIType'] = request.aitype
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodAIData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodAIDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_aidata_with_options_async(
        self,
        request: main_models.DescribeVodAIDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodAIDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aitype):
            query['AIType'] = request.aitype
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodAIData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodAIDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_aidata(
        self,
        request: main_models.DescribeVodAIDataRequest,
    ) -> main_models.DescribeVodAIDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_aidata_with_options(request, runtime)

    async def describe_vod_aidata_async(
        self,
        request: main_models.DescribeVodAIDataRequest,
    ) -> main_models.DescribeVodAIDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_aidata_with_options_async(request, runtime)

    def describe_vod_certificate_list_with_options(
        self,
        request: main_models.DescribeVodCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodCertificateList',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_certificate_list_with_options_async(
        self,
        request: main_models.DescribeVodCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodCertificateList',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_certificate_list(
        self,
        request: main_models.DescribeVodCertificateListRequest,
    ) -> main_models.DescribeVodCertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_certificate_list_with_options(request, runtime)

    async def describe_vod_certificate_list_async(
        self,
        request: main_models.DescribeVodCertificateListRequest,
    ) -> main_models.DescribeVodCertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_certificate_list_with_options_async(request, runtime)

    def describe_vod_domain_bps_data_with_options(
        self,
        request: main_models.DescribeVodDomainBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainBpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_bps_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainBpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_bps_data(
        self,
        request: main_models.DescribeVodDomainBpsDataRequest,
    ) -> main_models.DescribeVodDomainBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_bps_data_with_options(request, runtime)

    async def describe_vod_domain_bps_data_async(
        self,
        request: main_models.DescribeVodDomainBpsDataRequest,
    ) -> main_models.DescribeVodDomainBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_bps_data_with_options_async(request, runtime)

    def describe_vod_domain_bps_data_by_layer_with_options(
        self,
        request: main_models.DescribeVodDomainBpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainBpsDataByLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.layer):
            query['Layer'] = request.layer
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainBpsDataByLayer',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainBpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_bps_data_by_layer_with_options_async(
        self,
        request: main_models.DescribeVodDomainBpsDataByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainBpsDataByLayerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.layer):
            query['Layer'] = request.layer
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainBpsDataByLayer',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainBpsDataByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_bps_data_by_layer(
        self,
        request: main_models.DescribeVodDomainBpsDataByLayerRequest,
    ) -> main_models.DescribeVodDomainBpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_bps_data_by_layer_with_options(request, runtime)

    async def describe_vod_domain_bps_data_by_layer_async(
        self,
        request: main_models.DescribeVodDomainBpsDataByLayerRequest,
    ) -> main_models.DescribeVodDomainBpsDataByLayerResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_bps_data_by_layer_with_options_async(request, runtime)

    def describe_vod_domain_certificate_info_with_options(
        self,
        request: main_models.DescribeVodDomainCertificateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainCertificateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.hera_api_auto_version):
            query['HeraApiAutoVersion'] = request.hera_api_auto_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainCertificateInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_certificate_info_with_options_async(
        self,
        request: main_models.DescribeVodDomainCertificateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainCertificateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.hera_api_auto_version):
            query['HeraApiAutoVersion'] = request.hera_api_auto_version
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainCertificateInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainCertificateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_certificate_info(
        self,
        request: main_models.DescribeVodDomainCertificateInfoRequest,
    ) -> main_models.DescribeVodDomainCertificateInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_certificate_info_with_options(request, runtime)

    async def describe_vod_domain_certificate_info_async(
        self,
        request: main_models.DescribeVodDomainCertificateInfoRequest,
    ) -> main_models.DescribeVodDomainCertificateInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_certificate_info_with_options_async(request, runtime)

    def describe_vod_domain_configs_with_options(
        self,
        request: main_models.DescribeVodDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainConfigs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_configs_with_options_async(
        self,
        request: main_models.DescribeVodDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainConfigs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_configs(
        self,
        request: main_models.DescribeVodDomainConfigsRequest,
    ) -> main_models.DescribeVodDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_configs_with_options(request, runtime)

    async def describe_vod_domain_configs_async(
        self,
        request: main_models.DescribeVodDomainConfigsRequest,
    ) -> main_models.DescribeVodDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_configs_with_options_async(request, runtime)

    def describe_vod_domain_detail_with_options(
        self,
        request: main_models.DescribeVodDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainDetail',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_detail_with_options_async(
        self,
        request: main_models.DescribeVodDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainDetail',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_detail(
        self,
        request: main_models.DescribeVodDomainDetailRequest,
    ) -> main_models.DescribeVodDomainDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_detail_with_options(request, runtime)

    async def describe_vod_domain_detail_async(
        self,
        request: main_models.DescribeVodDomainDetailRequest,
    ) -> main_models.DescribeVodDomainDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_detail_with_options_async(request, runtime)

    def describe_vod_domain_hit_rate_data_with_options(
        self,
        request: main_models.DescribeVodDomainHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainHitRateDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainHitRateData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainHitRateDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainHitRateData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_hit_rate_data(
        self,
        request: main_models.DescribeVodDomainHitRateDataRequest,
    ) -> main_models.DescribeVodDomainHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_hit_rate_data_with_options(request, runtime)

    async def describe_vod_domain_hit_rate_data_async(
        self,
        request: main_models.DescribeVodDomainHitRateDataRequest,
    ) -> main_models.DescribeVodDomainHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_vod_domain_log_with_options(
        self,
        request: main_models.DescribeVodDomainLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainLog',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_log_with_options_async(
        self,
        request: main_models.DescribeVodDomainLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainLog',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_log(
        self,
        request: main_models.DescribeVodDomainLogRequest,
    ) -> main_models.DescribeVodDomainLogResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_log_with_options(request, runtime)

    async def describe_vod_domain_log_async(
        self,
        request: main_models.DescribeVodDomainLogRequest,
    ) -> main_models.DescribeVodDomainLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_log_with_options_async(request, runtime)

    def describe_vod_domain_max_95bps_data_with_options(
        self,
        request: main_models.DescribeVodDomainMax95BpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainMax95BpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainMax95BpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainMax95BpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_max_95bps_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainMax95BpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainMax95BpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainMax95BpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainMax95BpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_max_95bps_data(
        self,
        request: main_models.DescribeVodDomainMax95BpsDataRequest,
    ) -> main_models.DescribeVodDomainMax95BpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_max_95bps_data_with_options(request, runtime)

    async def describe_vod_domain_max_95bps_data_async(
        self,
        request: main_models.DescribeVodDomainMax95BpsDataRequest,
    ) -> main_models.DescribeVodDomainMax95BpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_max_95bps_data_with_options_async(request, runtime)

    def describe_vod_domain_qps_data_with_options(
        self,
        request: main_models.DescribeVodDomainQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainQpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainQpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_qps_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainQpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainQpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_qps_data(
        self,
        request: main_models.DescribeVodDomainQpsDataRequest,
    ) -> main_models.DescribeVodDomainQpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_qps_data_with_options(request, runtime)

    async def describe_vod_domain_qps_data_async(
        self,
        request: main_models.DescribeVodDomainQpsDataRequest,
    ) -> main_models.DescribeVodDomainQpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_qps_data_with_options_async(request, runtime)

    def describe_vod_domain_real_time_bps_data_with_options(
        self,
        request: main_models.DescribeVodDomainRealTimeBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeBpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeBpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_real_time_bps_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainRealTimeBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeBpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeBpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_real_time_bps_data(
        self,
        request: main_models.DescribeVodDomainRealTimeBpsDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_real_time_bps_data_with_options(request, runtime)

    async def describe_vod_domain_real_time_bps_data_async(
        self,
        request: main_models.DescribeVodDomainRealTimeBpsDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_real_time_bps_data_with_options_async(request, runtime)

    def describe_vod_domain_real_time_byte_hit_rate_data_with_options(
        self,
        request: main_models.DescribeVodDomainRealTimeByteHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeByteHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeByteHitRateData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeByteHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_real_time_byte_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainRealTimeByteHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeByteHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeByteHitRateData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeByteHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_real_time_byte_hit_rate_data(
        self,
        request: main_models.DescribeVodDomainRealTimeByteHitRateDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeByteHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_real_time_byte_hit_rate_data_with_options(request, runtime)

    async def describe_vod_domain_real_time_byte_hit_rate_data_async(
        self,
        request: main_models.DescribeVodDomainRealTimeByteHitRateDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeByteHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_real_time_byte_hit_rate_data_with_options_async(request, runtime)

    def describe_vod_domain_real_time_detail_data_with_options(
        self,
        request: main_models.DescribeVodDomainRealTimeDetailDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeDetailDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeDetailData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_real_time_detail_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainRealTimeDetailDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeDetailDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeDetailData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeDetailDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_real_time_detail_data(
        self,
        request: main_models.DescribeVodDomainRealTimeDetailDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeDetailDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_real_time_detail_data_with_options(request, runtime)

    async def describe_vod_domain_real_time_detail_data_async(
        self,
        request: main_models.DescribeVodDomainRealTimeDetailDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeDetailDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_real_time_detail_data_with_options_async(request, runtime)

    def describe_vod_domain_real_time_http_code_data_with_options(
        self,
        request: main_models.DescribeVodDomainRealTimeHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeHttpCodeData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_real_time_http_code_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainRealTimeHttpCodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeHttpCodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeHttpCodeData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_real_time_http_code_data(
        self,
        request: main_models.DescribeVodDomainRealTimeHttpCodeDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_real_time_http_code_data_with_options(request, runtime)

    async def describe_vod_domain_real_time_http_code_data_async(
        self,
        request: main_models.DescribeVodDomainRealTimeHttpCodeDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeHttpCodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_real_time_http_code_data_with_options_async(request, runtime)

    def describe_vod_domain_real_time_qps_data_with_options(
        self,
        request: main_models.DescribeVodDomainRealTimeQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeQpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeQpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_real_time_qps_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainRealTimeQpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeQpsDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeQpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_real_time_qps_data(
        self,
        request: main_models.DescribeVodDomainRealTimeQpsDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeQpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_real_time_qps_data_with_options(request, runtime)

    async def describe_vod_domain_real_time_qps_data_async(
        self,
        request: main_models.DescribeVodDomainRealTimeQpsDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeQpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_real_time_qps_data_with_options_async(request, runtime)

    def describe_vod_domain_real_time_req_hit_rate_data_with_options(
        self,
        request: main_models.DescribeVodDomainRealTimeReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeReqHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeReqHitRateData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_real_time_req_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainRealTimeReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeReqHitRateDataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeReqHitRateData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_real_time_req_hit_rate_data(
        self,
        request: main_models.DescribeVodDomainRealTimeReqHitRateDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_real_time_req_hit_rate_data_with_options(request, runtime)

    async def describe_vod_domain_real_time_req_hit_rate_data_async(
        self,
        request: main_models.DescribeVodDomainRealTimeReqHitRateDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_real_time_req_hit_rate_data_with_options_async(request, runtime)

    def describe_vod_domain_real_time_traffic_data_with_options(
        self,
        request: main_models.DescribeVodDomainRealTimeTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeTrafficData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_real_time_traffic_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainRealTimeTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainRealTimeTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainRealTimeTrafficData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainRealTimeTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_real_time_traffic_data(
        self,
        request: main_models.DescribeVodDomainRealTimeTrafficDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_real_time_traffic_data_with_options(request, runtime)

    async def describe_vod_domain_real_time_traffic_data_async(
        self,
        request: main_models.DescribeVodDomainRealTimeTrafficDataRequest,
    ) -> main_models.DescribeVodDomainRealTimeTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_real_time_traffic_data_with_options_async(request, runtime)

    def describe_vod_domain_req_hit_rate_data_with_options(
        self,
        request: main_models.DescribeVodDomainReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainReqHitRateDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainReqHitRateData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_req_hit_rate_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainReqHitRateDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainReqHitRateDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainReqHitRateData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_req_hit_rate_data(
        self,
        request: main_models.DescribeVodDomainReqHitRateDataRequest,
    ) -> main_models.DescribeVodDomainReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_req_hit_rate_data_with_options(request, runtime)

    async def describe_vod_domain_req_hit_rate_data_async(
        self,
        request: main_models.DescribeVodDomainReqHitRateDataRequest,
    ) -> main_models.DescribeVodDomainReqHitRateDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_req_hit_rate_data_with_options_async(request, runtime)

    def describe_vod_domain_src_bps_data_with_options(
        self,
        request: main_models.DescribeVodDomainSrcBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainSrcBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainSrcBpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_src_bps_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainSrcBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainSrcBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainSrcBpsData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainSrcBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_src_bps_data(
        self,
        request: main_models.DescribeVodDomainSrcBpsDataRequest,
    ) -> main_models.DescribeVodDomainSrcBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_src_bps_data_with_options(request, runtime)

    async def describe_vod_domain_src_bps_data_async(
        self,
        request: main_models.DescribeVodDomainSrcBpsDataRequest,
    ) -> main_models.DescribeVodDomainSrcBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_src_bps_data_with_options_async(request, runtime)

    def describe_vod_domain_src_traffic_data_with_options(
        self,
        request: main_models.DescribeVodDomainSrcTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainSrcTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainSrcTrafficData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainSrcTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_src_traffic_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainSrcTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainSrcTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainSrcTrafficData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainSrcTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_src_traffic_data(
        self,
        request: main_models.DescribeVodDomainSrcTrafficDataRequest,
    ) -> main_models.DescribeVodDomainSrcTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_src_traffic_data_with_options(request, runtime)

    async def describe_vod_domain_src_traffic_data_async(
        self,
        request: main_models.DescribeVodDomainSrcTrafficDataRequest,
    ) -> main_models.DescribeVodDomainSrcTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_src_traffic_data_with_options_async(request, runtime)

    def describe_vod_domain_traffic_data_with_options(
        self,
        request: main_models.DescribeVodDomainTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainTrafficData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_traffic_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainTrafficData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_traffic_data(
        self,
        request: main_models.DescribeVodDomainTrafficDataRequest,
    ) -> main_models.DescribeVodDomainTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_traffic_data_with_options(request, runtime)

    async def describe_vod_domain_traffic_data_async(
        self,
        request: main_models.DescribeVodDomainTrafficDataRequest,
    ) -> main_models.DescribeVodDomainTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_traffic_data_with_options_async(request, runtime)

    def describe_vod_domain_usage_data_with_options(
        self,
        request: main_models.DescribeVodDomainUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.field):
            query['Field'] = request.field
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainUsageData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_domain_usage_data_with_options_async(
        self,
        request: main_models.DescribeVodDomainUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodDomainUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.field):
            query['Field'] = request.field
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodDomainUsageData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodDomainUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_domain_usage_data(
        self,
        request: main_models.DescribeVodDomainUsageDataRequest,
    ) -> main_models.DescribeVodDomainUsageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_domain_usage_data_with_options(request, runtime)

    async def describe_vod_domain_usage_data_async(
        self,
        request: main_models.DescribeVodDomainUsageDataRequest,
    ) -> main_models.DescribeVodDomainUsageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_domain_usage_data_with_options_async(request, runtime)

    def describe_vod_editing_usage_data_with_options(
        self,
        request: main_models.DescribeVodEditingUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodEditingUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodEditingUsageData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodEditingUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_editing_usage_data_with_options_async(
        self,
        request: main_models.DescribeVodEditingUsageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodEditingUsageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodEditingUsageData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodEditingUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_editing_usage_data(
        self,
        request: main_models.DescribeVodEditingUsageDataRequest,
    ) -> main_models.DescribeVodEditingUsageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_editing_usage_data_with_options(request, runtime)

    async def describe_vod_editing_usage_data_async(
        self,
        request: main_models.DescribeVodEditingUsageDataRequest,
    ) -> main_models.DescribeVodEditingUsageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_editing_usage_data_with_options_async(request, runtime)

    def describe_vod_media_play_data_with_options(
        self,
        request: main_models.DescribeVodMediaPlayDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodMediaPlayDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.order_name):
            query['OrderName'] = request.order_name
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.os):
            query['Os'] = request.os
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.play_date):
            query['PlayDate'] = request.play_date
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodMediaPlayData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodMediaPlayDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_media_play_data_with_options_async(
        self,
        request: main_models.DescribeVodMediaPlayDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodMediaPlayDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.order_name):
            query['OrderName'] = request.order_name
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.os):
            query['Os'] = request.os
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.play_date):
            query['PlayDate'] = request.play_date
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodMediaPlayData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodMediaPlayDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_media_play_data(
        self,
        request: main_models.DescribeVodMediaPlayDataRequest,
    ) -> main_models.DescribeVodMediaPlayDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_media_play_data_with_options(request, runtime)

    async def describe_vod_media_play_data_async(
        self,
        request: main_models.DescribeVodMediaPlayDataRequest,
    ) -> main_models.DescribeVodMediaPlayDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_media_play_data_with_options_async(request, runtime)

    def describe_vod_player_collect_data_with_options(
        self,
        request: main_models.DescribeVodPlayerCollectDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodPlayerCollectDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.os):
            query['Os'] = request.os
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodPlayerCollectData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodPlayerCollectDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_player_collect_data_with_options_async(
        self,
        request: main_models.DescribeVodPlayerCollectDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodPlayerCollectDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.os):
            query['Os'] = request.os
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodPlayerCollectData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodPlayerCollectDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_player_collect_data(
        self,
        request: main_models.DescribeVodPlayerCollectDataRequest,
    ) -> main_models.DescribeVodPlayerCollectDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_player_collect_data_with_options(request, runtime)

    async def describe_vod_player_collect_data_async(
        self,
        request: main_models.DescribeVodPlayerCollectDataRequest,
    ) -> main_models.DescribeVodPlayerCollectDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_player_collect_data_with_options_async(request, runtime)

    def describe_vod_player_dimension_data_with_options(
        self,
        request: main_models.DescribeVodPlayerDimensionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodPlayerDimensionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodPlayerDimensionData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodPlayerDimensionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_player_dimension_data_with_options_async(
        self,
        request: main_models.DescribeVodPlayerDimensionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodPlayerDimensionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodPlayerDimensionData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodPlayerDimensionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_player_dimension_data(
        self,
        request: main_models.DescribeVodPlayerDimensionDataRequest,
    ) -> main_models.DescribeVodPlayerDimensionDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_player_dimension_data_with_options(request, runtime)

    async def describe_vod_player_dimension_data_async(
        self,
        request: main_models.DescribeVodPlayerDimensionDataRequest,
    ) -> main_models.DescribeVodPlayerDimensionDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_player_dimension_data_with_options_async(request, runtime)

    def describe_vod_player_metric_data_with_options(
        self,
        request: main_models.DescribeVodPlayerMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodPlayerMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.os):
            query['Os'] = request.os
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        if not DaraCore.is_null(request.top):
            query['Top'] = request.top
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodPlayerMetricData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodPlayerMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_player_metric_data_with_options_async(
        self,
        request: main_models.DescribeVodPlayerMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodPlayerMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.os):
            query['Os'] = request.os
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        if not DaraCore.is_null(request.top):
            query['Top'] = request.top
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodPlayerMetricData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodPlayerMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_player_metric_data(
        self,
        request: main_models.DescribeVodPlayerMetricDataRequest,
    ) -> main_models.DescribeVodPlayerMetricDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_player_metric_data_with_options(request, runtime)

    async def describe_vod_player_metric_data_async(
        self,
        request: main_models.DescribeVodPlayerMetricDataRequest,
    ) -> main_models.DescribeVodPlayerMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_player_metric_data_with_options_async(request, runtime)

    def describe_vod_range_data_by_locate_and_isp_service_with_options(
        self,
        request: main_models.DescribeVodRangeDataByLocateAndIspServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodRangeDataByLocateAndIspServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodRangeDataByLocateAndIspService',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodRangeDataByLocateAndIspServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_range_data_by_locate_and_isp_service_with_options_async(
        self,
        request: main_models.DescribeVodRangeDataByLocateAndIspServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodRangeDataByLocateAndIspServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodRangeDataByLocateAndIspService',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodRangeDataByLocateAndIspServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_range_data_by_locate_and_isp_service(
        self,
        request: main_models.DescribeVodRangeDataByLocateAndIspServiceRequest,
    ) -> main_models.DescribeVodRangeDataByLocateAndIspServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_range_data_by_locate_and_isp_service_with_options(request, runtime)

    async def describe_vod_range_data_by_locate_and_isp_service_async(
        self,
        request: main_models.DescribeVodRangeDataByLocateAndIspServiceRequest,
    ) -> main_models.DescribeVodRangeDataByLocateAndIspServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_range_data_by_locate_and_isp_service_with_options_async(request, runtime)

    def describe_vod_refresh_quota_with_options(
        self,
        request: main_models.DescribeVodRefreshQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodRefreshQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodRefreshQuota',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_refresh_quota_with_options_async(
        self,
        request: main_models.DescribeVodRefreshQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodRefreshQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodRefreshQuota',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodRefreshQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_refresh_quota(
        self,
        request: main_models.DescribeVodRefreshQuotaRequest,
    ) -> main_models.DescribeVodRefreshQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_refresh_quota_with_options(request, runtime)

    async def describe_vod_refresh_quota_async(
        self,
        request: main_models.DescribeVodRefreshQuotaRequest,
    ) -> main_models.DescribeVodRefreshQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_refresh_quota_with_options_async(request, runtime)

    def describe_vod_refresh_tasks_with_options(
        self,
        request: main_models.DescribeVodRefreshTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodRefreshTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodRefreshTasks',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodRefreshTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_refresh_tasks_with_options_async(
        self,
        request: main_models.DescribeVodRefreshTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodRefreshTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodRefreshTasks',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodRefreshTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_refresh_tasks(
        self,
        request: main_models.DescribeVodRefreshTasksRequest,
    ) -> main_models.DescribeVodRefreshTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_refresh_tasks_with_options(request, runtime)

    async def describe_vod_refresh_tasks_async(
        self,
        request: main_models.DescribeVodRefreshTasksRequest,
    ) -> main_models.DescribeVodRefreshTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_refresh_tasks_with_options_async(request, runtime)

    def describe_vod_sslcertificate_list_with_options(
        self,
        request: main_models.DescribeVodSSLCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodSSLCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_keyword):
            query['SearchKeyword'] = request.search_keyword
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodSSLCertificateList',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodSSLCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_sslcertificate_list_with_options_async(
        self,
        request: main_models.DescribeVodSSLCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodSSLCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_keyword):
            query['SearchKeyword'] = request.search_keyword
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodSSLCertificateList',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodSSLCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_sslcertificate_list(
        self,
        request: main_models.DescribeVodSSLCertificateListRequest,
    ) -> main_models.DescribeVodSSLCertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_sslcertificate_list_with_options(request, runtime)

    async def describe_vod_sslcertificate_list_async(
        self,
        request: main_models.DescribeVodSSLCertificateListRequest,
    ) -> main_models.DescribeVodSSLCertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_sslcertificate_list_with_options_async(request, runtime)

    def describe_vod_storage_data_with_options(
        self,
        request: main_models.DescribeVodStorageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodStorageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage):
            query['Storage'] = request.storage
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodStorageData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodStorageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_storage_data_with_options_async(
        self,
        request: main_models.DescribeVodStorageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodStorageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage):
            query['Storage'] = request.storage
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodStorageData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodStorageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_storage_data(
        self,
        request: main_models.DescribeVodStorageDataRequest,
    ) -> main_models.DescribeVodStorageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_storage_data_with_options(request, runtime)

    async def describe_vod_storage_data_async(
        self,
        request: main_models.DescribeVodStorageDataRequest,
    ) -> main_models.DescribeVodStorageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_storage_data_with_options_async(request, runtime)

    def describe_vod_tiering_storage_data_with_options(
        self,
        request: main_models.DescribeVodTieringStorageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodTieringStorageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodTieringStorageData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodTieringStorageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_tiering_storage_data_with_options_async(
        self,
        request: main_models.DescribeVodTieringStorageDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodTieringStorageDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodTieringStorageData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodTieringStorageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_tiering_storage_data(
        self,
        request: main_models.DescribeVodTieringStorageDataRequest,
    ) -> main_models.DescribeVodTieringStorageDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_tiering_storage_data_with_options(request, runtime)

    async def describe_vod_tiering_storage_data_async(
        self,
        request: main_models.DescribeVodTieringStorageDataRequest,
    ) -> main_models.DescribeVodTieringStorageDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_tiering_storage_data_with_options_async(request, runtime)

    def describe_vod_tiering_storage_retrieval_data_with_options(
        self,
        request: main_models.DescribeVodTieringStorageRetrievalDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodTieringStorageRetrievalDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodTieringStorageRetrievalData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodTieringStorageRetrievalDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_tiering_storage_retrieval_data_with_options_async(
        self,
        request: main_models.DescribeVodTieringStorageRetrievalDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodTieringStorageRetrievalDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodTieringStorageRetrievalData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodTieringStorageRetrievalDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_tiering_storage_retrieval_data(
        self,
        request: main_models.DescribeVodTieringStorageRetrievalDataRequest,
    ) -> main_models.DescribeVodTieringStorageRetrievalDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_tiering_storage_retrieval_data_with_options(request, runtime)

    async def describe_vod_tiering_storage_retrieval_data_async(
        self,
        request: main_models.DescribeVodTieringStorageRetrievalDataRequest,
    ) -> main_models.DescribeVodTieringStorageRetrievalDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_tiering_storage_retrieval_data_with_options_async(request, runtime)

    def describe_vod_transcode_data_with_options(
        self,
        request: main_models.DescribeVodTranscodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodTranscodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage):
            query['Storage'] = request.storage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodTranscodeData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodTranscodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_transcode_data_with_options_async(
        self,
        request: main_models.DescribeVodTranscodeDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodTranscodeDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.storage):
            query['Storage'] = request.storage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodTranscodeData',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodTranscodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_transcode_data(
        self,
        request: main_models.DescribeVodTranscodeDataRequest,
    ) -> main_models.DescribeVodTranscodeDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_transcode_data_with_options(request, runtime)

    async def describe_vod_transcode_data_async(
        self,
        request: main_models.DescribeVodTranscodeDataRequest,
    ) -> main_models.DescribeVodTranscodeDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_transcode_data_with_options_async(request, runtime)

    def describe_vod_user_domains_with_options(
        self,
        request: main_models.DescribeVodUserDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodUserDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodUserDomains',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_user_domains_with_options_async(
        self,
        request: main_models.DescribeVodUserDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodUserDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not DaraCore.is_null(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodUserDomains',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_user_domains(
        self,
        request: main_models.DescribeVodUserDomainsRequest,
    ) -> main_models.DescribeVodUserDomainsResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_user_domains_with_options(request, runtime)

    async def describe_vod_user_domains_async(
        self,
        request: main_models.DescribeVodUserDomainsRequest,
    ) -> main_models.DescribeVodUserDomainsResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_user_domains_with_options_async(request, runtime)

    def describe_vod_user_vips_by_domain_with_options(
        self,
        request: main_models.DescribeVodUserVipsByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodUserVipsByDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.available):
            query['Available'] = request.available
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodUserVipsByDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodUserVipsByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_user_vips_by_domain_with_options_async(
        self,
        request: main_models.DescribeVodUserVipsByDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodUserVipsByDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.available):
            query['Available'] = request.available
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodUserVipsByDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodUserVipsByDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_user_vips_by_domain(
        self,
        request: main_models.DescribeVodUserVipsByDomainRequest,
    ) -> main_models.DescribeVodUserVipsByDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_user_vips_by_domain_with_options(request, runtime)

    async def describe_vod_user_vips_by_domain_async(
        self,
        request: main_models.DescribeVodUserVipsByDomainRequest,
    ) -> main_models.DescribeVodUserVipsByDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_user_vips_by_domain_with_options_async(request, runtime)

    def describe_vod_verify_content_with_options(
        self,
        request: main_models.DescribeVodVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodVerifyContent',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_verify_content_with_options_async(
        self,
        request: main_models.DescribeVodVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodVerifyContent',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodVerifyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_verify_content(
        self,
        request: main_models.DescribeVodVerifyContentRequest,
    ) -> main_models.DescribeVodVerifyContentResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_verify_content_with_options(request, runtime)

    async def describe_vod_verify_content_async(
        self,
        request: main_models.DescribeVodVerifyContentRequest,
    ) -> main_models.DescribeVodVerifyContentResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_verify_content_with_options_async(request, runtime)

    def detach_app_policy_from_identity_with_options(
        self,
        request: main_models.DetachAppPolicyFromIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachAppPolicyFromIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.identity_name):
            query['IdentityName'] = request.identity_name
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachAppPolicyFromIdentity',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachAppPolicyFromIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_app_policy_from_identity_with_options_async(
        self,
        request: main_models.DetachAppPolicyFromIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachAppPolicyFromIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.identity_name):
            query['IdentityName'] = request.identity_name
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachAppPolicyFromIdentity',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachAppPolicyFromIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_app_policy_from_identity(
        self,
        request: main_models.DetachAppPolicyFromIdentityRequest,
    ) -> main_models.DetachAppPolicyFromIdentityResponse:
        runtime = RuntimeOptions()
        return self.detach_app_policy_from_identity_with_options(request, runtime)

    async def detach_app_policy_from_identity_async(
        self,
        request: main_models.DetachAppPolicyFromIdentityRequest,
    ) -> main_models.DetachAppPolicyFromIdentityResponse:
        runtime = RuntimeOptions()
        return await self.detach_app_policy_from_identity_with_options_async(request, runtime)

    def generate_download_secret_key_with_options(
        self,
        request: main_models.GenerateDownloadSecretKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDownloadSecretKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_decrypt_key):
            query['AppDecryptKey'] = request.app_decrypt_key
        if not DaraCore.is_null(request.app_identification):
            query['AppIdentification'] = request.app_identification
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDownloadSecretKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDownloadSecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_download_secret_key_with_options_async(
        self,
        request: main_models.GenerateDownloadSecretKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDownloadSecretKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_decrypt_key):
            query['AppDecryptKey'] = request.app_decrypt_key
        if not DaraCore.is_null(request.app_identification):
            query['AppIdentification'] = request.app_identification
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDownloadSecretKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDownloadSecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_download_secret_key(
        self,
        request: main_models.GenerateDownloadSecretKeyRequest,
    ) -> main_models.GenerateDownloadSecretKeyResponse:
        runtime = RuntimeOptions()
        return self.generate_download_secret_key_with_options(request, runtime)

    async def generate_download_secret_key_async(
        self,
        request: main_models.GenerateDownloadSecretKeyRequest,
    ) -> main_models.GenerateDownloadSecretKeyResponse:
        runtime = RuntimeOptions()
        return await self.generate_download_secret_key_with_options_async(request, runtime)

    def generate_kmsdata_key_with_options(
        self,
        request: main_models.GenerateKMSDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateKMSDataKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateKMSDataKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateKMSDataKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_kmsdata_key_with_options_async(
        self,
        request: main_models.GenerateKMSDataKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateKMSDataKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateKMSDataKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateKMSDataKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_kmsdata_key(
        self,
        request: main_models.GenerateKMSDataKeyRequest,
    ) -> main_models.GenerateKMSDataKeyResponse:
        runtime = RuntimeOptions()
        return self.generate_kmsdata_key_with_options(request, runtime)

    async def generate_kmsdata_key_async(
        self,
        request: main_models.GenerateKMSDataKeyRequest,
    ) -> main_models.GenerateKMSDataKeyResponse:
        runtime = RuntimeOptions()
        return await self.generate_kmsdata_key_with_options_async(request, runtime)

    def get_aiimage_jobs_with_options(
        self,
        request: main_models.GetAIImageJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAIImageJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAIImageJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIImageJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiimage_jobs_with_options_async(
        self,
        request: main_models.GetAIImageJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAIImageJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAIImageJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIImageJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aiimage_jobs(
        self,
        request: main_models.GetAIImageJobsRequest,
    ) -> main_models.GetAIImageJobsResponse:
        runtime = RuntimeOptions()
        return self.get_aiimage_jobs_with_options(request, runtime)

    async def get_aiimage_jobs_async(
        self,
        request: main_models.GetAIImageJobsRequest,
    ) -> main_models.GetAIImageJobsResponse:
        runtime = RuntimeOptions()
        return await self.get_aiimage_jobs_with_options_async(request, runtime)

    def get_aimedia_audit_job_with_options(
        self,
        request: main_models.GetAIMediaAuditJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAIMediaAuditJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAIMediaAuditJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIMediaAuditJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aimedia_audit_job_with_options_async(
        self,
        request: main_models.GetAIMediaAuditJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAIMediaAuditJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAIMediaAuditJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIMediaAuditJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aimedia_audit_job(
        self,
        request: main_models.GetAIMediaAuditJobRequest,
    ) -> main_models.GetAIMediaAuditJobResponse:
        runtime = RuntimeOptions()
        return self.get_aimedia_audit_job_with_options(request, runtime)

    async def get_aimedia_audit_job_async(
        self,
        request: main_models.GetAIMediaAuditJobRequest,
    ) -> main_models.GetAIMediaAuditJobResponse:
        runtime = RuntimeOptions()
        return await self.get_aimedia_audit_job_with_options_async(request, runtime)

    def get_aitemplate_with_options(
        self,
        request: main_models.GetAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aitemplate_with_options_async(
        self,
        request: main_models.GetAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAITemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aitemplate(
        self,
        request: main_models.GetAITemplateRequest,
    ) -> main_models.GetAITemplateResponse:
        runtime = RuntimeOptions()
        return self.get_aitemplate_with_options(request, runtime)

    async def get_aitemplate_async(
        self,
        request: main_models.GetAITemplateRequest,
    ) -> main_models.GetAITemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_aitemplate_with_options_async(request, runtime)

    def get_aivideo_tag_result_with_options(
        self,
        request: main_models.GetAIVideoTagResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAIVideoTagResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAIVideoTagResult',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIVideoTagResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aivideo_tag_result_with_options_async(
        self,
        request: main_models.GetAIVideoTagResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAIVideoTagResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAIVideoTagResult',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAIVideoTagResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aivideo_tag_result(
        self,
        request: main_models.GetAIVideoTagResultRequest,
    ) -> main_models.GetAIVideoTagResultResponse:
        runtime = RuntimeOptions()
        return self.get_aivideo_tag_result_with_options(request, runtime)

    async def get_aivideo_tag_result_async(
        self,
        request: main_models.GetAIVideoTagResultRequest,
    ) -> main_models.GetAIVideoTagResultResponse:
        runtime = RuntimeOptions()
        return await self.get_aivideo_tag_result_with_options_async(request, runtime)

    def get_app_infos_with_options(
        self,
        request: main_models.GetAppInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_infos_with_options_async(
        self,
        request: main_models.GetAppInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_infos(
        self,
        request: main_models.GetAppInfosRequest,
    ) -> main_models.GetAppInfosResponse:
        runtime = RuntimeOptions()
        return self.get_app_infos_with_options(request, runtime)

    async def get_app_infos_async(
        self,
        request: main_models.GetAppInfosRequest,
    ) -> main_models.GetAppInfosResponse:
        runtime = RuntimeOptions()
        return await self.get_app_infos_with_options_async(request, runtime)

    def get_app_play_key_with_options(
        self,
        request: main_models.GetAppPlayKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppPlayKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppPlayKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppPlayKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_play_key_with_options_async(
        self,
        request: main_models.GetAppPlayKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppPlayKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppPlayKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppPlayKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_play_key(
        self,
        request: main_models.GetAppPlayKeyRequest,
    ) -> main_models.GetAppPlayKeyResponse:
        runtime = RuntimeOptions()
        return self.get_app_play_key_with_options(request, runtime)

    async def get_app_play_key_async(
        self,
        request: main_models.GetAppPlayKeyRequest,
    ) -> main_models.GetAppPlayKeyResponse:
        runtime = RuntimeOptions()
        return await self.get_app_play_key_with_options_async(request, runtime)

    def get_attached_media_info_with_options(
        self,
        request: main_models.GetAttachedMediaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAttachedMediaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAttachedMediaInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAttachedMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_attached_media_info_with_options_async(
        self,
        request: main_models.GetAttachedMediaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAttachedMediaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAttachedMediaInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAttachedMediaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_attached_media_info(
        self,
        request: main_models.GetAttachedMediaInfoRequest,
    ) -> main_models.GetAttachedMediaInfoResponse:
        runtime = RuntimeOptions()
        return self.get_attached_media_info_with_options(request, runtime)

    async def get_attached_media_info_async(
        self,
        request: main_models.GetAttachedMediaInfoRequest,
    ) -> main_models.GetAttachedMediaInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_attached_media_info_with_options_async(request, runtime)

    def get_audit_history_with_options(
        self,
        request: main_models.GetAuditHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditHistory',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_history_with_options_async(
        self,
        request: main_models.GetAuditHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditHistory',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_history(
        self,
        request: main_models.GetAuditHistoryRequest,
    ) -> main_models.GetAuditHistoryResponse:
        runtime = RuntimeOptions()
        return self.get_audit_history_with_options(request, runtime)

    async def get_audit_history_async(
        self,
        request: main_models.GetAuditHistoryRequest,
    ) -> main_models.GetAuditHistoryResponse:
        runtime = RuntimeOptions()
        return await self.get_audit_history_with_options_async(request, runtime)

    def get_categories_with_options(
        self,
        request: main_models.GetCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCategories',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_categories_with_options_async(
        self,
        request: main_models.GetCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCategories',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_categories(
        self,
        request: main_models.GetCategoriesRequest,
    ) -> main_models.GetCategoriesResponse:
        runtime = RuntimeOptions()
        return self.get_categories_with_options(request, runtime)

    async def get_categories_async(
        self,
        request: main_models.GetCategoriesRequest,
    ) -> main_models.GetCategoriesResponse:
        runtime = RuntimeOptions()
        return await self.get_categories_with_options_async(request, runtime)

    def get_daily_play_region_statis_with_options(
        self,
        request: main_models.GetDailyPlayRegionStatisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDailyPlayRegionStatisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        if not DaraCore.is_null(request.media_region):
            query['MediaRegion'] = request.media_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDailyPlayRegionStatis',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDailyPlayRegionStatisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_daily_play_region_statis_with_options_async(
        self,
        request: main_models.GetDailyPlayRegionStatisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDailyPlayRegionStatisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        if not DaraCore.is_null(request.media_region):
            query['MediaRegion'] = request.media_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDailyPlayRegionStatis',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDailyPlayRegionStatisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_daily_play_region_statis(
        self,
        request: main_models.GetDailyPlayRegionStatisRequest,
    ) -> main_models.GetDailyPlayRegionStatisResponse:
        runtime = RuntimeOptions()
        return self.get_daily_play_region_statis_with_options(request, runtime)

    async def get_daily_play_region_statis_async(
        self,
        request: main_models.GetDailyPlayRegionStatisRequest,
    ) -> main_models.GetDailyPlayRegionStatisResponse:
        runtime = RuntimeOptions()
        return await self.get_daily_play_region_statis_with_options_async(request, runtime)

    def get_default_aitemplate_with_options(
        self,
        request: main_models.GetDefaultAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDefaultAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_aitemplate_with_options_async(
        self,
        request: main_models.GetDefaultAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDefaultAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultAITemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_aitemplate(
        self,
        request: main_models.GetDefaultAITemplateRequest,
    ) -> main_models.GetDefaultAITemplateResponse:
        runtime = RuntimeOptions()
        return self.get_default_aitemplate_with_options(request, runtime)

    async def get_default_aitemplate_async(
        self,
        request: main_models.GetDefaultAITemplateRequest,
    ) -> main_models.GetDefaultAITemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_default_aitemplate_with_options_async(request, runtime)

    def get_digital_watermark_extract_result_with_options(
        self,
        request: main_models.GetDigitalWatermarkExtractResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDigitalWatermarkExtractResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extract_type):
            query['ExtractType'] = request.extract_type
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDigitalWatermarkExtractResult',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDigitalWatermarkExtractResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_digital_watermark_extract_result_with_options_async(
        self,
        request: main_models.GetDigitalWatermarkExtractResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDigitalWatermarkExtractResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extract_type):
            query['ExtractType'] = request.extract_type
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDigitalWatermarkExtractResult',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDigitalWatermarkExtractResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_digital_watermark_extract_result(
        self,
        request: main_models.GetDigitalWatermarkExtractResultRequest,
    ) -> main_models.GetDigitalWatermarkExtractResultResponse:
        runtime = RuntimeOptions()
        return self.get_digital_watermark_extract_result_with_options(request, runtime)

    async def get_digital_watermark_extract_result_async(
        self,
        request: main_models.GetDigitalWatermarkExtractResultRequest,
    ) -> main_models.GetDigitalWatermarkExtractResultResponse:
        runtime = RuntimeOptions()
        return await self.get_digital_watermark_extract_result_with_options_async(request, runtime)

    def get_editing_project_with_options(
        self,
        request: main_models.GetEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_editing_project_with_options_async(
        self,
        request: main_models.GetEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEditingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_editing_project(
        self,
        request: main_models.GetEditingProjectRequest,
    ) -> main_models.GetEditingProjectResponse:
        runtime = RuntimeOptions()
        return self.get_editing_project_with_options(request, runtime)

    async def get_editing_project_async(
        self,
        request: main_models.GetEditingProjectRequest,
    ) -> main_models.GetEditingProjectResponse:
        runtime = RuntimeOptions()
        return await self.get_editing_project_with_options_async(request, runtime)

    def get_editing_project_materials_with_options(
        self,
        request: main_models.GetEditingProjectMaterialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEditingProjectMaterialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.material_type):
            query['MaterialType'] = request.material_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEditingProjectMaterials',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_editing_project_materials_with_options_async(
        self,
        request: main_models.GetEditingProjectMaterialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEditingProjectMaterialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.material_type):
            query['MaterialType'] = request.material_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEditingProjectMaterials',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEditingProjectMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_editing_project_materials(
        self,
        request: main_models.GetEditingProjectMaterialsRequest,
    ) -> main_models.GetEditingProjectMaterialsResponse:
        runtime = RuntimeOptions()
        return self.get_editing_project_materials_with_options(request, runtime)

    async def get_editing_project_materials_async(
        self,
        request: main_models.GetEditingProjectMaterialsRequest,
    ) -> main_models.GetEditingProjectMaterialsResponse:
        runtime = RuntimeOptions()
        return await self.get_editing_project_materials_with_options_async(request, runtime)

    def get_image_info_with_options(
        self,
        request: main_models.GetImageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_info_with_options_async(
        self,
        request: main_models.GetImageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.image_id):
            query['ImageId'] = request.image_id
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_info(
        self,
        request: main_models.GetImageInfoRequest,
    ) -> main_models.GetImageInfoResponse:
        runtime = RuntimeOptions()
        return self.get_image_info_with_options(request, runtime)

    async def get_image_info_async(
        self,
        request: main_models.GetImageInfoRequest,
    ) -> main_models.GetImageInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_image_info_with_options_async(request, runtime)

    def get_image_infos_with_options(
        self,
        request: main_models.GetImageInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_infos_with_options_async(
        self,
        request: main_models.GetImageInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_infos(
        self,
        request: main_models.GetImageInfosRequest,
    ) -> main_models.GetImageInfosResponse:
        runtime = RuntimeOptions()
        return self.get_image_infos_with_options(request, runtime)

    async def get_image_infos_async(
        self,
        request: main_models.GetImageInfosRequest,
    ) -> main_models.GetImageInfosResponse:
        runtime = RuntimeOptions()
        return await self.get_image_infos_with_options_async(request, runtime)

    def get_job_detail_with_options(
        self,
        request: main_models.GetJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobDetail',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_detail_with_options_async(
        self,
        request: main_models.GetJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobDetail',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_detail(
        self,
        request: main_models.GetJobDetailRequest,
    ) -> main_models.GetJobDetailResponse:
        runtime = RuntimeOptions()
        return self.get_job_detail_with_options(request, runtime)

    async def get_job_detail_async(
        self,
        request: main_models.GetJobDetailRequest,
    ) -> main_models.GetJobDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_job_detail_with_options_async(request, runtime)

    def get_media_audit_audio_result_detail_with_options(
        self,
        request: main_models.GetMediaAuditAudioResultDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaAuditAudioResultDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaAuditAudioResultDetail',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaAuditAudioResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_audit_audio_result_detail_with_options_async(
        self,
        request: main_models.GetMediaAuditAudioResultDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaAuditAudioResultDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaAuditAudioResultDetail',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaAuditAudioResultDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_audit_audio_result_detail(
        self,
        request: main_models.GetMediaAuditAudioResultDetailRequest,
    ) -> main_models.GetMediaAuditAudioResultDetailResponse:
        runtime = RuntimeOptions()
        return self.get_media_audit_audio_result_detail_with_options(request, runtime)

    async def get_media_audit_audio_result_detail_async(
        self,
        request: main_models.GetMediaAuditAudioResultDetailRequest,
    ) -> main_models.GetMediaAuditAudioResultDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_media_audit_audio_result_detail_with_options_async(request, runtime)

    def get_media_audit_result_with_options(
        self,
        request: main_models.GetMediaAuditResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaAuditResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaAuditResult',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaAuditResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_audit_result_with_options_async(
        self,
        request: main_models.GetMediaAuditResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaAuditResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaAuditResult',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaAuditResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_audit_result(
        self,
        request: main_models.GetMediaAuditResultRequest,
    ) -> main_models.GetMediaAuditResultResponse:
        runtime = RuntimeOptions()
        return self.get_media_audit_result_with_options(request, runtime)

    async def get_media_audit_result_async(
        self,
        request: main_models.GetMediaAuditResultRequest,
    ) -> main_models.GetMediaAuditResultResponse:
        runtime = RuntimeOptions()
        return await self.get_media_audit_result_with_options_async(request, runtime)

    def get_media_audit_result_detail_with_options(
        self,
        request: main_models.GetMediaAuditResultDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaAuditResultDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaAuditResultDetail',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaAuditResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_audit_result_detail_with_options_async(
        self,
        request: main_models.GetMediaAuditResultDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaAuditResultDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaAuditResultDetail',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaAuditResultDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_audit_result_detail(
        self,
        request: main_models.GetMediaAuditResultDetailRequest,
    ) -> main_models.GetMediaAuditResultDetailResponse:
        runtime = RuntimeOptions()
        return self.get_media_audit_result_detail_with_options(request, runtime)

    async def get_media_audit_result_detail_async(
        self,
        request: main_models.GetMediaAuditResultDetailRequest,
    ) -> main_models.GetMediaAuditResultDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_media_audit_result_detail_with_options_async(request, runtime)

    def get_media_audit_result_timeline_with_options(
        self,
        request: main_models.GetMediaAuditResultTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaAuditResultTimelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaAuditResultTimeline',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaAuditResultTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_audit_result_timeline_with_options_async(
        self,
        request: main_models.GetMediaAuditResultTimelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaAuditResultTimelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaAuditResultTimeline',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaAuditResultTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_audit_result_timeline(
        self,
        request: main_models.GetMediaAuditResultTimelineRequest,
    ) -> main_models.GetMediaAuditResultTimelineResponse:
        runtime = RuntimeOptions()
        return self.get_media_audit_result_timeline_with_options(request, runtime)

    async def get_media_audit_result_timeline_async(
        self,
        request: main_models.GetMediaAuditResultTimelineRequest,
    ) -> main_models.GetMediaAuditResultTimelineResponse:
        runtime = RuntimeOptions()
        return await self.get_media_audit_result_timeline_with_options_async(request, runtime)

    def get_media_dnaresult_with_options(
        self,
        request: main_models.GetMediaDNAResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaDNAResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaDNAResult',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaDNAResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_dnaresult_with_options_async(
        self,
        request: main_models.GetMediaDNAResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaDNAResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaDNAResult',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaDNAResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_dnaresult(
        self,
        request: main_models.GetMediaDNAResultRequest,
    ) -> main_models.GetMediaDNAResultResponse:
        runtime = RuntimeOptions()
        return self.get_media_dnaresult_with_options(request, runtime)

    async def get_media_dnaresult_async(
        self,
        request: main_models.GetMediaDNAResultRequest,
    ) -> main_models.GetMediaDNAResultResponse:
        runtime = RuntimeOptions()
        return await self.get_media_dnaresult_with_options_async(request, runtime)

    def get_media_refresh_jobs_with_options(
        self,
        request: main_models.GetMediaRefreshJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaRefreshJobsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaRefreshJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaRefreshJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_refresh_jobs_with_options_async(
        self,
        request: main_models.GetMediaRefreshJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMediaRefreshJobsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMediaRefreshJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMediaRefreshJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_refresh_jobs(
        self,
        request: main_models.GetMediaRefreshJobsRequest,
    ) -> main_models.GetMediaRefreshJobsResponse:
        runtime = RuntimeOptions()
        return self.get_media_refresh_jobs_with_options(request, runtime)

    async def get_media_refresh_jobs_async(
        self,
        request: main_models.GetMediaRefreshJobsRequest,
    ) -> main_models.GetMediaRefreshJobsResponse:
        runtime = RuntimeOptions()
        return await self.get_media_refresh_jobs_with_options_async(request, runtime)

    def get_message_callback_with_options(
        self,
        request: main_models.GetMessageCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessageCallback',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_callback_with_options_async(
        self,
        request: main_models.GetMessageCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMessageCallback',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_callback(
        self,
        request: main_models.GetMessageCallbackRequest,
    ) -> main_models.GetMessageCallbackResponse:
        runtime = RuntimeOptions()
        return self.get_message_callback_with_options(request, runtime)

    async def get_message_callback_async(
        self,
        request: main_models.GetMessageCallbackRequest,
    ) -> main_models.GetMessageCallbackResponse:
        runtime = RuntimeOptions()
        return await self.get_message_callback_with_options_async(request, runtime)

    def get_mezzanine_info_with_options(
        self,
        request: main_models.GetMezzanineInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMezzanineInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addition_type):
            query['AdditionType'] = request.addition_type
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMezzanineInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMezzanineInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mezzanine_info_with_options_async(
        self,
        request: main_models.GetMezzanineInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMezzanineInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addition_type):
            query['AdditionType'] = request.addition_type
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMezzanineInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMezzanineInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mezzanine_info(
        self,
        request: main_models.GetMezzanineInfoRequest,
    ) -> main_models.GetMezzanineInfoResponse:
        runtime = RuntimeOptions()
        return self.get_mezzanine_info_with_options(request, runtime)

    async def get_mezzanine_info_async(
        self,
        request: main_models.GetMezzanineInfoRequest,
    ) -> main_models.GetMezzanineInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_mezzanine_info_with_options_async(request, runtime)

    def get_play_info_with_options(
        self,
        request: main_models.GetPlayInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPlayInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addition_type):
            query['AdditionType'] = request.addition_type
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.codec_name):
            query['CodecName'] = request.codec_name
        if not DaraCore.is_null(request.definition):
            query['Definition'] = request.definition
        if not DaraCore.is_null(request.digital_watermark_type):
            query['DigitalWatermarkType'] = request.digital_watermark_type
        if not DaraCore.is_null(request.formats):
            query['Formats'] = request.formats
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.play_config):
            query['PlayConfig'] = request.play_config
        if not DaraCore.is_null(request.re_auth_info):
            query['ReAuthInfo'] = request.re_auth_info
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.trace):
            query['Trace'] = request.trace
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPlayInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_play_info_with_options_async(
        self,
        request: main_models.GetPlayInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPlayInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addition_type):
            query['AdditionType'] = request.addition_type
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.codec_name):
            query['CodecName'] = request.codec_name
        if not DaraCore.is_null(request.definition):
            query['Definition'] = request.definition
        if not DaraCore.is_null(request.digital_watermark_type):
            query['DigitalWatermarkType'] = request.digital_watermark_type
        if not DaraCore.is_null(request.formats):
            query['Formats'] = request.formats
        if not DaraCore.is_null(request.output_type):
            query['OutputType'] = request.output_type
        if not DaraCore.is_null(request.play_config):
            query['PlayConfig'] = request.play_config
        if not DaraCore.is_null(request.re_auth_info):
            query['ReAuthInfo'] = request.re_auth_info
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.trace):
            query['Trace'] = request.trace
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPlayInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPlayInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_play_info(
        self,
        request: main_models.GetPlayInfoRequest,
    ) -> main_models.GetPlayInfoResponse:
        runtime = RuntimeOptions()
        return self.get_play_info_with_options(request, runtime)

    async def get_play_info_async(
        self,
        request: main_models.GetPlayInfoRequest,
    ) -> main_models.GetPlayInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_play_info_with_options_async(request, runtime)

    def get_transcode_summary_with_options(
        self,
        request: main_models.GetTranscodeSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranscodeSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTranscodeSummary',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranscodeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transcode_summary_with_options_async(
        self,
        request: main_models.GetTranscodeSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranscodeSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTranscodeSummary',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranscodeSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transcode_summary(
        self,
        request: main_models.GetTranscodeSummaryRequest,
    ) -> main_models.GetTranscodeSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_transcode_summary_with_options(request, runtime)

    async def get_transcode_summary_async(
        self,
        request: main_models.GetTranscodeSummaryRequest,
    ) -> main_models.GetTranscodeSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_transcode_summary_with_options_async(request, runtime)

    def get_transcode_task_with_options(
        self,
        request: main_models.GetTranscodeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranscodeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.transcode_task_id):
            query['TranscodeTaskId'] = request.transcode_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTranscodeTask',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranscodeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transcode_task_with_options_async(
        self,
        request: main_models.GetTranscodeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranscodeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.transcode_task_id):
            query['TranscodeTaskId'] = request.transcode_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTranscodeTask',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranscodeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transcode_task(
        self,
        request: main_models.GetTranscodeTaskRequest,
    ) -> main_models.GetTranscodeTaskResponse:
        runtime = RuntimeOptions()
        return self.get_transcode_task_with_options(request, runtime)

    async def get_transcode_task_async(
        self,
        request: main_models.GetTranscodeTaskRequest,
    ) -> main_models.GetTranscodeTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_transcode_task_with_options_async(request, runtime)

    def get_transcode_template_group_with_options(
        self,
        request: main_models.GetTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transcode_template_group_with_options_async(
        self,
        request: main_models.GetTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTranscodeTemplateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transcode_template_group(
        self,
        request: main_models.GetTranscodeTemplateGroupRequest,
    ) -> main_models.GetTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return self.get_transcode_template_group_with_options(request, runtime)

    async def get_transcode_template_group_async(
        self,
        request: main_models.GetTranscodeTemplateGroupRequest,
    ) -> main_models.GetTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_transcode_template_group_with_options_async(request, runtime)

    def get_urlupload_infos_with_options(
        self,
        request: main_models.GetURLUploadInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetURLUploadInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetURLUploadInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetURLUploadInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_urlupload_infos_with_options_async(
        self,
        request: main_models.GetURLUploadInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetURLUploadInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetURLUploadInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetURLUploadInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_urlupload_infos(
        self,
        request: main_models.GetURLUploadInfosRequest,
    ) -> main_models.GetURLUploadInfosResponse:
        runtime = RuntimeOptions()
        return self.get_urlupload_infos_with_options(request, runtime)

    async def get_urlupload_infos_async(
        self,
        request: main_models.GetURLUploadInfosRequest,
    ) -> main_models.GetURLUploadInfosResponse:
        runtime = RuntimeOptions()
        return await self.get_urlupload_infos_with_options_async(request, runtime)

    def get_upload_details_with_options(
        self,
        request: main_models.GetUploadDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadDetails',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_details_with_options_async(
        self,
        request: main_models.GetUploadDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadDetails',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_details(
        self,
        request: main_models.GetUploadDetailsRequest,
    ) -> main_models.GetUploadDetailsResponse:
        runtime = RuntimeOptions()
        return self.get_upload_details_with_options(request, runtime)

    async def get_upload_details_async(
        self,
        request: main_models.GetUploadDetailsRequest,
    ) -> main_models.GetUploadDetailsResponse:
        runtime = RuntimeOptions()
        return await self.get_upload_details_with_options_async(request, runtime)

    def get_video_info_with_options(
        self,
        request: main_models.GetVideoInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_info_with_options_async(
        self,
        request: main_models.GetVideoInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_info(
        self,
        request: main_models.GetVideoInfoRequest,
    ) -> main_models.GetVideoInfoResponse:
        runtime = RuntimeOptions()
        return self.get_video_info_with_options(request, runtime)

    async def get_video_info_async(
        self,
        request: main_models.GetVideoInfoRequest,
    ) -> main_models.GetVideoInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_video_info_with_options_async(request, runtime)

    def get_video_infos_with_options(
        self,
        request: main_models.GetVideoInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        if not DaraCore.is_null(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_infos_with_options_async(
        self,
        request: main_models.GetVideoInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        if not DaraCore.is_null(request.video_ids):
            query['VideoIds'] = request.video_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_infos(
        self,
        request: main_models.GetVideoInfosRequest,
    ) -> main_models.GetVideoInfosResponse:
        runtime = RuntimeOptions()
        return self.get_video_infos_with_options(request, runtime)

    async def get_video_infos_async(
        self,
        request: main_models.GetVideoInfosRequest,
    ) -> main_models.GetVideoInfosResponse:
        runtime = RuntimeOptions()
        return await self.get_video_infos_with_options_async(request, runtime)

    def get_video_list_with_options(
        self,
        request: main_models.GetVideoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoList',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_list_with_options_async(
        self,
        request: main_models.GetVideoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reference_ids):
            query['ReferenceIds'] = request.reference_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoList',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_list(
        self,
        request: main_models.GetVideoListRequest,
    ) -> main_models.GetVideoListResponse:
        runtime = RuntimeOptions()
        return self.get_video_list_with_options(request, runtime)

    async def get_video_list_async(
        self,
        request: main_models.GetVideoListRequest,
    ) -> main_models.GetVideoListResponse:
        runtime = RuntimeOptions()
        return await self.get_video_list_with_options_async(request, runtime)

    def get_video_play_auth_with_options(
        self,
        request: main_models.GetVideoPlayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoPlayAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_version):
            query['ApiVersion'] = request.api_version
        if not DaraCore.is_null(request.auth_info_timeout):
            query['AuthInfoTimeout'] = request.auth_info_timeout
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoPlayAuth',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoPlayAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_play_auth_with_options_async(
        self,
        request: main_models.GetVideoPlayAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoPlayAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_version):
            query['ApiVersion'] = request.api_version
        if not DaraCore.is_null(request.auth_info_timeout):
            query['AuthInfoTimeout'] = request.auth_info_timeout
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoPlayAuth',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoPlayAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_play_auth(
        self,
        request: main_models.GetVideoPlayAuthRequest,
    ) -> main_models.GetVideoPlayAuthResponse:
        runtime = RuntimeOptions()
        return self.get_video_play_auth_with_options(request, runtime)

    async def get_video_play_auth_async(
        self,
        request: main_models.GetVideoPlayAuthRequest,
    ) -> main_models.GetVideoPlayAuthResponse:
        runtime = RuntimeOptions()
        return await self.get_video_play_auth_with_options_async(request, runtime)

    def get_vod_template_with_options(
        self,
        request: main_models.GetVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vod_template_id):
            query['VodTemplateId'] = request.vod_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vod_template_with_options_async(
        self,
        request: main_models.GetVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vod_template_id):
            query['VodTemplateId'] = request.vod_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVodTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vod_template(
        self,
        request: main_models.GetVodTemplateRequest,
    ) -> main_models.GetVodTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_vod_template_with_options(request, runtime)

    async def get_vod_template_async(
        self,
        request: main_models.GetVodTemplateRequest,
    ) -> main_models.GetVodTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_vod_template_with_options_async(request, runtime)

    def get_watermark_with_options(
        self,
        request: main_models.GetWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_watermark_with_options_async(
        self,
        request: main_models.GetWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_watermark(
        self,
        request: main_models.GetWatermarkRequest,
    ) -> main_models.GetWatermarkResponse:
        runtime = RuntimeOptions()
        return self.get_watermark_with_options(request, runtime)

    async def get_watermark_async(
        self,
        request: main_models.GetWatermarkRequest,
    ) -> main_models.GetWatermarkResponse:
        runtime = RuntimeOptions()
        return await self.get_watermark_with_options_async(request, runtime)

    def list_aiimage_info_with_options(
        self,
        request: main_models.ListAIImageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIImageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAIImageInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIImageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aiimage_info_with_options_async(
        self,
        request: main_models.ListAIImageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIImageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAIImageInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIImageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aiimage_info(
        self,
        request: main_models.ListAIImageInfoRequest,
    ) -> main_models.ListAIImageInfoResponse:
        runtime = RuntimeOptions()
        return self.list_aiimage_info_with_options(request, runtime)

    async def list_aiimage_info_async(
        self,
        request: main_models.ListAIImageInfoRequest,
    ) -> main_models.ListAIImageInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_aiimage_info_with_options_async(request, runtime)

    def list_aijob_with_options(
        self,
        request: main_models.ListAIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAIJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aijob_with_options_async(
        self,
        request: main_models.ListAIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAIJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAIJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aijob(
        self,
        request: main_models.ListAIJobRequest,
    ) -> main_models.ListAIJobResponse:
        runtime = RuntimeOptions()
        return self.list_aijob_with_options(request, runtime)

    async def list_aijob_async(
        self,
        request: main_models.ListAIJobRequest,
    ) -> main_models.ListAIJobResponse:
        runtime = RuntimeOptions()
        return await self.list_aijob_with_options_async(request, runtime)

    def list_aitemplate_with_options(
        self,
        request: main_models.ListAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aitemplate_with_options_async(
        self,
        request: main_models.ListAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAITemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aitemplate(
        self,
        request: main_models.ListAITemplateRequest,
    ) -> main_models.ListAITemplateResponse:
        runtime = RuntimeOptions()
        return self.list_aitemplate_with_options(request, runtime)

    async def list_aitemplate_async(
        self,
        request: main_models.ListAITemplateRequest,
    ) -> main_models.ListAITemplateResponse:
        runtime = RuntimeOptions()
        return await self.list_aitemplate_with_options_async(request, runtime)

    def list_app_info_with_options(
        self,
        request: main_models.ListAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_info_with_options_async(
        self,
        request: main_models.ListAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_info(
        self,
        request: main_models.ListAppInfoRequest,
    ) -> main_models.ListAppInfoResponse:
        runtime = RuntimeOptions()
        return self.list_app_info_with_options(request, runtime)

    async def list_app_info_async(
        self,
        request: main_models.ListAppInfoRequest,
    ) -> main_models.ListAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_app_info_with_options_async(request, runtime)

    def list_app_policies_for_identity_with_options(
        self,
        request: main_models.ListAppPoliciesForIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppPoliciesForIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.identity_name):
            query['IdentityName'] = request.identity_name
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppPoliciesForIdentity',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppPoliciesForIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_policies_for_identity_with_options_async(
        self,
        request: main_models.ListAppPoliciesForIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppPoliciesForIdentityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.identity_name):
            query['IdentityName'] = request.identity_name
        if not DaraCore.is_null(request.identity_type):
            query['IdentityType'] = request.identity_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppPoliciesForIdentity',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppPoliciesForIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_policies_for_identity(
        self,
        request: main_models.ListAppPoliciesForIdentityRequest,
    ) -> main_models.ListAppPoliciesForIdentityResponse:
        runtime = RuntimeOptions()
        return self.list_app_policies_for_identity_with_options(request, runtime)

    async def list_app_policies_for_identity_async(
        self,
        request: main_models.ListAppPoliciesForIdentityRequest,
    ) -> main_models.ListAppPoliciesForIdentityResponse:
        runtime = RuntimeOptions()
        return await self.list_app_policies_for_identity_with_options_async(request, runtime)

    def list_audit_security_ip_with_options(
        self,
        request: main_models.ListAuditSecurityIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuditSecurityIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuditSecurityIp',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuditSecurityIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_audit_security_ip_with_options_async(
        self,
        request: main_models.ListAuditSecurityIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuditSecurityIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuditSecurityIp',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuditSecurityIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_audit_security_ip(
        self,
        request: main_models.ListAuditSecurityIpRequest,
    ) -> main_models.ListAuditSecurityIpResponse:
        runtime = RuntimeOptions()
        return self.list_audit_security_ip_with_options(request, runtime)

    async def list_audit_security_ip_async(
        self,
        request: main_models.ListAuditSecurityIpRequest,
    ) -> main_models.ListAuditSecurityIpResponse:
        runtime = RuntimeOptions()
        return await self.list_audit_security_ip_with_options_async(request, runtime)

    def list_dynamic_image_with_options(
        self,
        request: main_models.ListDynamicImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDynamicImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDynamicImage',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDynamicImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dynamic_image_with_options_async(
        self,
        request: main_models.ListDynamicImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDynamicImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDynamicImage',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDynamicImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dynamic_image(
        self,
        request: main_models.ListDynamicImageRequest,
    ) -> main_models.ListDynamicImageResponse:
        runtime = RuntimeOptions()
        return self.list_dynamic_image_with_options(request, runtime)

    async def list_dynamic_image_async(
        self,
        request: main_models.ListDynamicImageRequest,
    ) -> main_models.ListDynamicImageResponse:
        runtime = RuntimeOptions()
        return await self.list_dynamic_image_with_options_async(request, runtime)

    def list_job_info_with_options(
        self,
        request: main_models.ListJobInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_info_with_options_async(
        self,
        request: main_models.ListJobInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_info(
        self,
        request: main_models.ListJobInfoRequest,
    ) -> main_models.ListJobInfoResponse:
        runtime = RuntimeOptions()
        return self.list_job_info_with_options(request, runtime)

    async def list_job_info_async(
        self,
        request: main_models.ListJobInfoRequest,
    ) -> main_models.ListJobInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_job_info_with_options_async(request, runtime)

    def list_live_record_video_with_options(
        self,
        request: main_models.ListLiveRecordVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLiveRecordVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLiveRecordVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLiveRecordVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_record_video_with_options_async(
        self,
        request: main_models.ListLiveRecordVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLiveRecordVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLiveRecordVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLiveRecordVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_record_video(
        self,
        request: main_models.ListLiveRecordVideoRequest,
    ) -> main_models.ListLiveRecordVideoResponse:
        runtime = RuntimeOptions()
        return self.list_live_record_video_with_options(request, runtime)

    async def list_live_record_video_async(
        self,
        request: main_models.ListLiveRecordVideoRequest,
    ) -> main_models.ListLiveRecordVideoResponse:
        runtime = RuntimeOptions()
        return await self.list_live_record_video_with_options_async(request, runtime)

    def list_snapshots_with_options(
        self,
        request: main_models.ListSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSnapshots',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshots_with_options_async(
        self,
        request: main_models.ListSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_timeout):
            query['AuthTimeout'] = request.auth_timeout
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSnapshots',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_snapshots(
        self,
        request: main_models.ListSnapshotsRequest,
    ) -> main_models.ListSnapshotsResponse:
        runtime = RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    async def list_snapshots_async(
        self,
        request: main_models.ListSnapshotsRequest,
    ) -> main_models.ListSnapshotsResponse:
        runtime = RuntimeOptions()
        return await self.list_snapshots_with_options_async(request, runtime)

    def list_transcode_task_with_options(
        self,
        request: main_models.ListTranscodeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTranscodeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTranscodeTask',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTranscodeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transcode_task_with_options_async(
        self,
        request: main_models.ListTranscodeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTranscodeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTranscodeTask',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTranscodeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transcode_task(
        self,
        request: main_models.ListTranscodeTaskRequest,
    ) -> main_models.ListTranscodeTaskResponse:
        runtime = RuntimeOptions()
        return self.list_transcode_task_with_options(request, runtime)

    async def list_transcode_task_async(
        self,
        request: main_models.ListTranscodeTaskRequest,
    ) -> main_models.ListTranscodeTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_transcode_task_with_options_async(request, runtime)

    def list_transcode_template_group_with_options(
        self,
        request: main_models.ListTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transcode_template_group_with_options_async(
        self,
        request: main_models.ListTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTranscodeTemplateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transcode_template_group(
        self,
        request: main_models.ListTranscodeTemplateGroupRequest,
    ) -> main_models.ListTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return self.list_transcode_template_group_with_options(request, runtime)

    async def list_transcode_template_group_async(
        self,
        request: main_models.ListTranscodeTemplateGroupRequest,
    ) -> main_models.ListTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_transcode_template_group_with_options_async(request, runtime)

    def list_vod_template_with_options(
        self,
        request: main_models.ListVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vod_template_with_options_async(
        self,
        request: main_models.ListVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVodTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vod_template(
        self,
        request: main_models.ListVodTemplateRequest,
    ) -> main_models.ListVodTemplateResponse:
        runtime = RuntimeOptions()
        return self.list_vod_template_with_options(request, runtime)

    async def list_vod_template_async(
        self,
        request: main_models.ListVodTemplateRequest,
    ) -> main_models.ListVodTemplateResponse:
        runtime = RuntimeOptions()
        return await self.list_vod_template_with_options_async(request, runtime)

    def list_watermark_with_options(
        self,
        request: main_models.ListWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_watermark_with_options_async(
        self,
        request: main_models.ListWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_watermark(
        self,
        request: main_models.ListWatermarkRequest,
    ) -> main_models.ListWatermarkResponse:
        runtime = RuntimeOptions()
        return self.list_watermark_with_options(request, runtime)

    async def list_watermark_async(
        self,
        request: main_models.ListWatermarkRequest,
    ) -> main_models.ListWatermarkResponse:
        runtime = RuntimeOptions()
        return await self.list_watermark_with_options_async(request, runtime)

    def move_app_resource_with_options(
        self,
        request: main_models.MoveAppResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveAppResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.target_app_id):
            query['TargetAppId'] = request.target_app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveAppResource',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveAppResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_app_resource_with_options_async(
        self,
        request: main_models.MoveAppResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveAppResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.target_app_id):
            query['TargetAppId'] = request.target_app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveAppResource',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveAppResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_app_resource(
        self,
        request: main_models.MoveAppResourceRequest,
    ) -> main_models.MoveAppResourceResponse:
        runtime = RuntimeOptions()
        return self.move_app_resource_with_options(request, runtime)

    async def move_app_resource_async(
        self,
        request: main_models.MoveAppResourceRequest,
    ) -> main_models.MoveAppResourceResponse:
        runtime = RuntimeOptions()
        return await self.move_app_resource_with_options_async(request, runtime)

    def preload_vod_object_caches_with_options(
        self,
        request: main_models.PreloadVodObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreloadVodObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.l_2preload):
            query['L2Preload'] = request.l_2preload
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.with_header):
            query['WithHeader'] = request.with_header
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreloadVodObjectCaches',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreloadVodObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def preload_vod_object_caches_with_options_async(
        self,
        request: main_models.PreloadVodObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreloadVodObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.area):
            query['Area'] = request.area
        if not DaraCore.is_null(request.l_2preload):
            query['L2Preload'] = request.l_2preload
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.with_header):
            query['WithHeader'] = request.with_header
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreloadVodObjectCaches',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreloadVodObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preload_vod_object_caches(
        self,
        request: main_models.PreloadVodObjectCachesRequest,
    ) -> main_models.PreloadVodObjectCachesResponse:
        runtime = RuntimeOptions()
        return self.preload_vod_object_caches_with_options(request, runtime)

    async def preload_vod_object_caches_async(
        self,
        request: main_models.PreloadVodObjectCachesRequest,
    ) -> main_models.PreloadVodObjectCachesResponse:
        runtime = RuntimeOptions()
        return await self.preload_vod_object_caches_with_options_async(request, runtime)

    def produce_editing_project_video_with_options(
        self,
        request: main_models.ProduceEditingProjectVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProduceEditingProjectVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.media_metadata):
            query['MediaMetadata'] = request.media_metadata
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.produce_config):
            query['ProduceConfig'] = request.produce_config
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.timeline):
            query['Timeline'] = request.timeline
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProduceEditingProjectVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProduceEditingProjectVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def produce_editing_project_video_with_options_async(
        self,
        request: main_models.ProduceEditingProjectVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProduceEditingProjectVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.media_metadata):
            query['MediaMetadata'] = request.media_metadata
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.produce_config):
            query['ProduceConfig'] = request.produce_config
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.timeline):
            query['Timeline'] = request.timeline
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProduceEditingProjectVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProduceEditingProjectVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def produce_editing_project_video(
        self,
        request: main_models.ProduceEditingProjectVideoRequest,
    ) -> main_models.ProduceEditingProjectVideoResponse:
        runtime = RuntimeOptions()
        return self.produce_editing_project_video_with_options(request, runtime)

    async def produce_editing_project_video_async(
        self,
        request: main_models.ProduceEditingProjectVideoRequest,
    ) -> main_models.ProduceEditingProjectVideoResponse:
        runtime = RuntimeOptions()
        return await self.produce_editing_project_video_with_options_async(request, runtime)

    def refresh_media_play_urls_with_options(
        self,
        request: main_models.RefreshMediaPlayUrlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshMediaPlayUrlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.definitions):
            query['Definitions'] = request.definitions
        if not DaraCore.is_null(request.formats):
            query['Formats'] = request.formats
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.slice_count):
            query['SliceCount'] = request.slice_count
        if not DaraCore.is_null(request.slice_flag):
            query['SliceFlag'] = request.slice_flag
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshMediaPlayUrls',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshMediaPlayUrlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_media_play_urls_with_options_async(
        self,
        request: main_models.RefreshMediaPlayUrlsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshMediaPlayUrlsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.definitions):
            query['Definitions'] = request.definitions
        if not DaraCore.is_null(request.formats):
            query['Formats'] = request.formats
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.result_type):
            query['ResultType'] = request.result_type
        if not DaraCore.is_null(request.slice_count):
            query['SliceCount'] = request.slice_count
        if not DaraCore.is_null(request.slice_flag):
            query['SliceFlag'] = request.slice_flag
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshMediaPlayUrls',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshMediaPlayUrlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_media_play_urls(
        self,
        request: main_models.RefreshMediaPlayUrlsRequest,
    ) -> main_models.RefreshMediaPlayUrlsResponse:
        runtime = RuntimeOptions()
        return self.refresh_media_play_urls_with_options(request, runtime)

    async def refresh_media_play_urls_async(
        self,
        request: main_models.RefreshMediaPlayUrlsRequest,
    ) -> main_models.RefreshMediaPlayUrlsResponse:
        runtime = RuntimeOptions()
        return await self.refresh_media_play_urls_with_options_async(request, runtime)

    def refresh_upload_video_with_options(
        self,
        request: main_models.RefreshUploadVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshUploadVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshUploadVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshUploadVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_upload_video_with_options_async(
        self,
        request: main_models.RefreshUploadVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshUploadVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshUploadVideo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshUploadVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_upload_video(
        self,
        request: main_models.RefreshUploadVideoRequest,
    ) -> main_models.RefreshUploadVideoResponse:
        runtime = RuntimeOptions()
        return self.refresh_upload_video_with_options(request, runtime)

    async def refresh_upload_video_async(
        self,
        request: main_models.RefreshUploadVideoRequest,
    ) -> main_models.RefreshUploadVideoResponse:
        runtime = RuntimeOptions()
        return await self.refresh_upload_video_with_options_async(request, runtime)

    def refresh_vod_object_caches_with_options(
        self,
        request: main_models.RefreshVodObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshVodObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshVodObjectCaches',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshVodObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_vod_object_caches_with_options_async(
        self,
        request: main_models.RefreshVodObjectCachesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshVodObjectCachesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.object_path):
            query['ObjectPath'] = request.object_path
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshVodObjectCaches',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshVodObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_vod_object_caches(
        self,
        request: main_models.RefreshVodObjectCachesRequest,
    ) -> main_models.RefreshVodObjectCachesResponse:
        runtime = RuntimeOptions()
        return self.refresh_vod_object_caches_with_options(request, runtime)

    async def refresh_vod_object_caches_async(
        self,
        request: main_models.RefreshVodObjectCachesRequest,
    ) -> main_models.RefreshVodObjectCachesResponse:
        runtime = RuntimeOptions()
        return await self.refresh_vod_object_caches_with_options_async(request, runtime)

    def register_media_with_options(
        self,
        request: main_models.RegisterMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.register_metadatas):
            query['RegisterMetadatas'] = request.register_metadatas
        if not DaraCore.is_null(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_media_with_options_async(
        self,
        request: main_models.RegisterMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.register_metadatas):
            query['RegisterMetadatas'] = request.register_metadatas
        if not DaraCore.is_null(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_media(
        self,
        request: main_models.RegisterMediaRequest,
    ) -> main_models.RegisterMediaResponse:
        runtime = RuntimeOptions()
        return self.register_media_with_options(request, runtime)

    async def register_media_async(
        self,
        request: main_models.RegisterMediaRequest,
    ) -> main_models.RegisterMediaResponse:
        runtime = RuntimeOptions()
        return await self.register_media_with_options_async(request, runtime)

    def restore_media_with_options(
        self,
        request: main_models.RestoreMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.restore_days):
            query['RestoreDays'] = request.restore_days
        if not DaraCore.is_null(request.restore_tier):
            query['RestoreTier'] = request.restore_tier
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_media_with_options_async(
        self,
        request: main_models.RestoreMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.restore_days):
            query['RestoreDays'] = request.restore_days
        if not DaraCore.is_null(request.restore_tier):
            query['RestoreTier'] = request.restore_tier
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_media(
        self,
        request: main_models.RestoreMediaRequest,
    ) -> main_models.RestoreMediaResponse:
        runtime = RuntimeOptions()
        return self.restore_media_with_options(request, runtime)

    async def restore_media_async(
        self,
        request: main_models.RestoreMediaRequest,
    ) -> main_models.RestoreMediaResponse:
        runtime = RuntimeOptions()
        return await self.restore_media_with_options_async(request, runtime)

    def search_editing_project_with_options(
        self,
        request: main_models.SearchEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_editing_project_with_options_async(
        self,
        request: main_models.SearchEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchEditingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_editing_project(
        self,
        request: main_models.SearchEditingProjectRequest,
    ) -> main_models.SearchEditingProjectResponse:
        runtime = RuntimeOptions()
        return self.search_editing_project_with_options(request, runtime)

    async def search_editing_project_async(
        self,
        request: main_models.SearchEditingProjectRequest,
    ) -> main_models.SearchEditingProjectResponse:
        runtime = RuntimeOptions()
        return await self.search_editing_project_with_options_async(request, runtime)

    def search_media_with_options(
        self,
        request: main_models.SearchMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.match):
            query['Match'] = request.match
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scroll_token):
            query['ScrollToken'] = request.scroll_token
        if not DaraCore.is_null(request.search_type):
            query['SearchType'] = request.search_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_media_with_options_async(
        self,
        request: main_models.SearchMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fields):
            query['Fields'] = request.fields
        if not DaraCore.is_null(request.match):
            query['Match'] = request.match
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scroll_token):
            query['ScrollToken'] = request.scroll_token
        if not DaraCore.is_null(request.search_type):
            query['SearchType'] = request.search_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchMedia',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_media(
        self,
        request: main_models.SearchMediaRequest,
    ) -> main_models.SearchMediaResponse:
        runtime = RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    async def search_media_async(
        self,
        request: main_models.SearchMediaRequest,
    ) -> main_models.SearchMediaResponse:
        runtime = RuntimeOptions()
        return await self.search_media_with_options_async(request, runtime)

    def set_app_play_key_with_options(
        self,
        request: main_models.SetAppPlayKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppPlayKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_key):
            query['PlayKey'] = request.play_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppPlayKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppPlayKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_app_play_key_with_options_async(
        self,
        request: main_models.SetAppPlayKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppPlayKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_key):
            query['PlayKey'] = request.play_key
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppPlayKey',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppPlayKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_app_play_key(
        self,
        request: main_models.SetAppPlayKeyRequest,
    ) -> main_models.SetAppPlayKeyResponse:
        runtime = RuntimeOptions()
        return self.set_app_play_key_with_options(request, runtime)

    async def set_app_play_key_async(
        self,
        request: main_models.SetAppPlayKeyRequest,
    ) -> main_models.SetAppPlayKeyResponse:
        runtime = RuntimeOptions()
        return await self.set_app_play_key_with_options_async(request, runtime)

    def set_audit_security_ip_with_options(
        self,
        request: main_models.SetAuditSecurityIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAuditSecurityIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ips):
            query['Ips'] = request.ips
        if not DaraCore.is_null(request.operate_mode):
            query['OperateMode'] = request.operate_mode
        if not DaraCore.is_null(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAuditSecurityIp',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAuditSecurityIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_audit_security_ip_with_options_async(
        self,
        request: main_models.SetAuditSecurityIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAuditSecurityIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ips):
            query['Ips'] = request.ips
        if not DaraCore.is_null(request.operate_mode):
            query['OperateMode'] = request.operate_mode
        if not DaraCore.is_null(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAuditSecurityIp',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAuditSecurityIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_audit_security_ip(
        self,
        request: main_models.SetAuditSecurityIpRequest,
    ) -> main_models.SetAuditSecurityIpResponse:
        runtime = RuntimeOptions()
        return self.set_audit_security_ip_with_options(request, runtime)

    async def set_audit_security_ip_async(
        self,
        request: main_models.SetAuditSecurityIpRequest,
    ) -> main_models.SetAuditSecurityIpResponse:
        runtime = RuntimeOptions()
        return await self.set_audit_security_ip_with_options_async(request, runtime)

    def set_crossdomain_content_with_options(
        self,
        request: main_models.SetCrossdomainContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCrossdomainContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_real_owner_id):
            query['ResourceRealOwnerId'] = request.resource_real_owner_id
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetCrossdomainContent',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCrossdomainContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_crossdomain_content_with_options_async(
        self,
        request: main_models.SetCrossdomainContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCrossdomainContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_real_owner_id):
            query['ResourceRealOwnerId'] = request.resource_real_owner_id
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetCrossdomainContent',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCrossdomainContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_crossdomain_content(
        self,
        request: main_models.SetCrossdomainContentRequest,
    ) -> main_models.SetCrossdomainContentResponse:
        runtime = RuntimeOptions()
        return self.set_crossdomain_content_with_options(request, runtime)

    async def set_crossdomain_content_async(
        self,
        request: main_models.SetCrossdomainContentRequest,
    ) -> main_models.SetCrossdomainContentResponse:
        runtime = RuntimeOptions()
        return await self.set_crossdomain_content_with_options_async(request, runtime)

    def set_default_aitemplate_with_options(
        self,
        request: main_models.SetDefaultAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_aitemplate_with_options_async(
        self,
        request: main_models.SetDefaultAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultAITemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_aitemplate(
        self,
        request: main_models.SetDefaultAITemplateRequest,
    ) -> main_models.SetDefaultAITemplateResponse:
        runtime = RuntimeOptions()
        return self.set_default_aitemplate_with_options(request, runtime)

    async def set_default_aitemplate_async(
        self,
        request: main_models.SetDefaultAITemplateRequest,
    ) -> main_models.SetDefaultAITemplateResponse:
        runtime = RuntimeOptions()
        return await self.set_default_aitemplate_with_options_async(request, runtime)

    def set_default_transcode_template_group_with_options(
        self,
        request: main_models.SetDefaultTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_transcode_template_group_with_options_async(
        self,
        request: main_models.SetDefaultTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultTranscodeTemplateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_transcode_template_group(
        self,
        request: main_models.SetDefaultTranscodeTemplateGroupRequest,
    ) -> main_models.SetDefaultTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return self.set_default_transcode_template_group_with_options(request, runtime)

    async def set_default_transcode_template_group_async(
        self,
        request: main_models.SetDefaultTranscodeTemplateGroupRequest,
    ) -> main_models.SetDefaultTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return await self.set_default_transcode_template_group_with_options_async(request, runtime)

    def set_default_watermark_with_options(
        self,
        request: main_models.SetDefaultWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_watermark_with_options_async(
        self,
        request: main_models.SetDefaultWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_watermark(
        self,
        request: main_models.SetDefaultWatermarkRequest,
    ) -> main_models.SetDefaultWatermarkResponse:
        runtime = RuntimeOptions()
        return self.set_default_watermark_with_options(request, runtime)

    async def set_default_watermark_async(
        self,
        request: main_models.SetDefaultWatermarkRequest,
    ) -> main_models.SetDefaultWatermarkResponse:
        runtime = RuntimeOptions()
        return await self.set_default_watermark_with_options_async(request, runtime)

    def set_editing_project_materials_with_options(
        self,
        request: main_models.SetEditingProjectMaterialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetEditingProjectMaterialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetEditingProjectMaterials',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_editing_project_materials_with_options_async(
        self,
        request: main_models.SetEditingProjectMaterialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetEditingProjectMaterialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetEditingProjectMaterials',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetEditingProjectMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_editing_project_materials(
        self,
        request: main_models.SetEditingProjectMaterialsRequest,
    ) -> main_models.SetEditingProjectMaterialsResponse:
        runtime = RuntimeOptions()
        return self.set_editing_project_materials_with_options(request, runtime)

    async def set_editing_project_materials_async(
        self,
        request: main_models.SetEditingProjectMaterialsRequest,
    ) -> main_models.SetEditingProjectMaterialsResponse:
        runtime = RuntimeOptions()
        return await self.set_editing_project_materials_with_options_async(request, runtime)

    def set_message_callback_with_options(
        self,
        request: main_models.SetMessageCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetMessageCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.auth_switch):
            query['AuthSwitch'] = request.auth_switch
        if not DaraCore.is_null(request.callback_type):
            query['CallbackType'] = request.callback_type
        if not DaraCore.is_null(request.callback_url):
            query['CallbackURL'] = request.callback_url
        if not DaraCore.is_null(request.event_type_list):
            query['EventTypeList'] = request.event_type_list
        if not DaraCore.is_null(request.mns_endpoint):
            query['MnsEndpoint'] = request.mns_endpoint
        if not DaraCore.is_null(request.mns_queue_name):
            query['MnsQueueName'] = request.mns_queue_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetMessageCallback',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetMessageCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_message_callback_with_options_async(
        self,
        request: main_models.SetMessageCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetMessageCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.auth_switch):
            query['AuthSwitch'] = request.auth_switch
        if not DaraCore.is_null(request.callback_type):
            query['CallbackType'] = request.callback_type
        if not DaraCore.is_null(request.callback_url):
            query['CallbackURL'] = request.callback_url
        if not DaraCore.is_null(request.event_type_list):
            query['EventTypeList'] = request.event_type_list
        if not DaraCore.is_null(request.mns_endpoint):
            query['MnsEndpoint'] = request.mns_endpoint
        if not DaraCore.is_null(request.mns_queue_name):
            query['MnsQueueName'] = request.mns_queue_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetMessageCallback',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetMessageCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_message_callback(
        self,
        request: main_models.SetMessageCallbackRequest,
    ) -> main_models.SetMessageCallbackResponse:
        runtime = RuntimeOptions()
        return self.set_message_callback_with_options(request, runtime)

    async def set_message_callback_async(
        self,
        request: main_models.SetMessageCallbackRequest,
    ) -> main_models.SetMessageCallbackResponse:
        runtime = RuntimeOptions()
        return await self.set_message_callback_with_options_async(request, runtime)

    def set_vod_domain_certificate_with_options(
        self,
        request: main_models.SetVodDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVodDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVodDomainCertificate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVodDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vod_domain_certificate_with_options_async(
        self,
        request: main_models.SetVodDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVodDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVodDomainCertificate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVodDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_vod_domain_certificate(
        self,
        request: main_models.SetVodDomainCertificateRequest,
    ) -> main_models.SetVodDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_vod_domain_certificate_with_options(request, runtime)

    async def set_vod_domain_certificate_async(
        self,
        request: main_models.SetVodDomainCertificateRequest,
    ) -> main_models.SetVodDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_vod_domain_certificate_with_options_async(request, runtime)

    def set_vod_domain_sslcertificate_with_options(
        self,
        request: main_models.SetVodDomainSSLCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVodDomainSSLCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVodDomainSSLCertificate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVodDomainSSLCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vod_domain_sslcertificate_with_options_async(
        self,
        request: main_models.SetVodDomainSSLCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVodDomainSSLCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_region):
            query['CertRegion'] = request.cert_region
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVodDomainSSLCertificate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVodDomainSSLCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_vod_domain_sslcertificate(
        self,
        request: main_models.SetVodDomainSSLCertificateRequest,
    ) -> main_models.SetVodDomainSSLCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_vod_domain_sslcertificate_with_options(request, runtime)

    async def set_vod_domain_sslcertificate_async(
        self,
        request: main_models.SetVodDomainSSLCertificateRequest,
    ) -> main_models.SetVodDomainSSLCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_vod_domain_sslcertificate_with_options_async(request, runtime)

    def submit_aiimage_audit_job_with_options(
        self,
        request: main_models.SubmitAIImageAuditJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAIImageAuditJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_audit_configuration):
            query['MediaAuditConfiguration'] = request.media_audit_configuration
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAIImageAuditJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAIImageAuditJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_aiimage_audit_job_with_options_async(
        self,
        request: main_models.SubmitAIImageAuditJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAIImageAuditJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_audit_configuration):
            query['MediaAuditConfiguration'] = request.media_audit_configuration
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAIImageAuditJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAIImageAuditJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_aiimage_audit_job(
        self,
        request: main_models.SubmitAIImageAuditJobRequest,
    ) -> main_models.SubmitAIImageAuditJobResponse:
        runtime = RuntimeOptions()
        return self.submit_aiimage_audit_job_with_options(request, runtime)

    async def submit_aiimage_audit_job_async(
        self,
        request: main_models.SubmitAIImageAuditJobRequest,
    ) -> main_models.SubmitAIImageAuditJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_aiimage_audit_job_with_options_async(request, runtime)

    def submit_aiimage_job_with_options(
        self,
        request: main_models.SubmitAIImageJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAIImageJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aipipeline_id):
            query['AIPipelineId'] = request.aipipeline_id
        if not DaraCore.is_null(request.aitemplate_id):
            query['AITemplateId'] = request.aitemplate_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAIImageJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAIImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_aiimage_job_with_options_async(
        self,
        request: main_models.SubmitAIImageJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAIImageJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aipipeline_id):
            query['AIPipelineId'] = request.aipipeline_id
        if not DaraCore.is_null(request.aitemplate_id):
            query['AITemplateId'] = request.aitemplate_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAIImageJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAIImageJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_aiimage_job(
        self,
        request: main_models.SubmitAIImageJobRequest,
    ) -> main_models.SubmitAIImageJobResponse:
        runtime = RuntimeOptions()
        return self.submit_aiimage_job_with_options(request, runtime)

    async def submit_aiimage_job_async(
        self,
        request: main_models.SubmitAIImageJobRequest,
    ) -> main_models.SubmitAIImageJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_aiimage_job_with_options_async(request, runtime)

    def submit_aijob_with_options(
        self,
        request: main_models.SubmitAIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAIJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAIJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAIJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_aijob_with_options_async(
        self,
        request: main_models.SubmitAIJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAIJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAIJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAIJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_aijob(
        self,
        request: main_models.SubmitAIJobRequest,
    ) -> main_models.SubmitAIJobResponse:
        runtime = RuntimeOptions()
        return self.submit_aijob_with_options(request, runtime)

    async def submit_aijob_async(
        self,
        request: main_models.SubmitAIJobRequest,
    ) -> main_models.SubmitAIJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_aijob_with_options_async(request, runtime)

    def submit_aimedia_audit_job_with_options(
        self,
        request: main_models.SubmitAIMediaAuditJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAIMediaAuditJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_audit_configuration):
            query['MediaAuditConfiguration'] = request.media_audit_configuration
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAIMediaAuditJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAIMediaAuditJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_aimedia_audit_job_with_options_async(
        self,
        request: main_models.SubmitAIMediaAuditJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAIMediaAuditJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_audit_configuration):
            query['MediaAuditConfiguration'] = request.media_audit_configuration
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAIMediaAuditJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAIMediaAuditJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_aimedia_audit_job(
        self,
        request: main_models.SubmitAIMediaAuditJobRequest,
    ) -> main_models.SubmitAIMediaAuditJobResponse:
        runtime = RuntimeOptions()
        return self.submit_aimedia_audit_job_with_options(request, runtime)

    async def submit_aimedia_audit_job_async(
        self,
        request: main_models.SubmitAIMediaAuditJobRequest,
    ) -> main_models.SubmitAIMediaAuditJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_aimedia_audit_job_with_options_async(request, runtime)

    def submit_digital_watermark_extract_job_with_options(
        self,
        request: main_models.SubmitDigitalWatermarkExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDigitalWatermarkExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extract_type):
            query['ExtractType'] = request.extract_type
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDigitalWatermarkExtractJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDigitalWatermarkExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_digital_watermark_extract_job_with_options_async(
        self,
        request: main_models.SubmitDigitalWatermarkExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDigitalWatermarkExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extract_type):
            query['ExtractType'] = request.extract_type
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDigitalWatermarkExtractJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDigitalWatermarkExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_digital_watermark_extract_job(
        self,
        request: main_models.SubmitDigitalWatermarkExtractJobRequest,
    ) -> main_models.SubmitDigitalWatermarkExtractJobResponse:
        runtime = RuntimeOptions()
        return self.submit_digital_watermark_extract_job_with_options(request, runtime)

    async def submit_digital_watermark_extract_job_async(
        self,
        request: main_models.SubmitDigitalWatermarkExtractJobRequest,
    ) -> main_models.SubmitDigitalWatermarkExtractJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_digital_watermark_extract_job_with_options_async(request, runtime)

    def submit_dynamic_image_job_with_options(
        self,
        request: main_models.SubmitDynamicImageJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDynamicImageJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_image_template_id):
            query['DynamicImageTemplateId'] = request.dynamic_image_template_id
        if not DaraCore.is_null(request.override_params):
            query['OverrideParams'] = request.override_params
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDynamicImageJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDynamicImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_dynamic_image_job_with_options_async(
        self,
        request: main_models.SubmitDynamicImageJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitDynamicImageJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_image_template_id):
            query['DynamicImageTemplateId'] = request.dynamic_image_template_id
        if not DaraCore.is_null(request.override_params):
            query['OverrideParams'] = request.override_params
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitDynamicImageJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitDynamicImageJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_dynamic_image_job(
        self,
        request: main_models.SubmitDynamicImageJobRequest,
    ) -> main_models.SubmitDynamicImageJobResponse:
        runtime = RuntimeOptions()
        return self.submit_dynamic_image_job_with_options(request, runtime)

    async def submit_dynamic_image_job_async(
        self,
        request: main_models.SubmitDynamicImageJobRequest,
    ) -> main_models.SubmitDynamicImageJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_dynamic_image_job_with_options_async(request, runtime)

    def submit_media_dnadelete_job_with_options(
        self,
        request: main_models.SubmitMediaDNADeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaDNADeleteJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaDNADeleteJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaDNADeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_dnadelete_job_with_options_async(
        self,
        request: main_models.SubmitMediaDNADeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaDNADeleteJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaDNADeleteJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaDNADeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_dnadelete_job(
        self,
        request: main_models.SubmitMediaDNADeleteJobRequest,
    ) -> main_models.SubmitMediaDNADeleteJobResponse:
        runtime = RuntimeOptions()
        return self.submit_media_dnadelete_job_with_options(request, runtime)

    async def submit_media_dnadelete_job_async(
        self,
        request: main_models.SubmitMediaDNADeleteJobRequest,
    ) -> main_models.SubmitMediaDNADeleteJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_media_dnadelete_job_with_options_async(request, runtime)

    def submit_preprocess_jobs_with_options(
        self,
        request: main_models.SubmitPreprocessJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitPreprocessJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.preprocess_type):
            query['PreprocessType'] = request.preprocess_type
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitPreprocessJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitPreprocessJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_preprocess_jobs_with_options_async(
        self,
        request: main_models.SubmitPreprocessJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitPreprocessJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.preprocess_type):
            query['PreprocessType'] = request.preprocess_type
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitPreprocessJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitPreprocessJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_preprocess_jobs(
        self,
        request: main_models.SubmitPreprocessJobsRequest,
    ) -> main_models.SubmitPreprocessJobsResponse:
        runtime = RuntimeOptions()
        return self.submit_preprocess_jobs_with_options(request, runtime)

    async def submit_preprocess_jobs_async(
        self,
        request: main_models.SubmitPreprocessJobsRequest,
    ) -> main_models.SubmitPreprocessJobsResponse:
        runtime = RuntimeOptions()
        return await self.submit_preprocess_jobs_with_options_async(request, runtime)

    def submit_snapshot_job_with_options(
        self,
        tmp_req: main_models.SubmitSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSnapshotJobResponse:
        tmp_req.validate()
        request = main_models.SubmitSnapshotJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.specified_offset_times):
            request.specified_offset_times_shrink = Utils.array_to_string_with_specified_style(tmp_req.specified_offset_times, 'SpecifiedOffsetTimes', 'json')
        query = {}
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.height):
            query['Height'] = request.height
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.snapshot_template_id):
            query['SnapshotTemplateId'] = request.snapshot_template_id
        if not DaraCore.is_null(request.specified_offset_time):
            query['SpecifiedOffsetTime'] = request.specified_offset_time
        if not DaraCore.is_null(request.specified_offset_times_shrink):
            query['SpecifiedOffsetTimes'] = request.specified_offset_times_shrink
        if not DaraCore.is_null(request.sprite_snapshot_config):
            query['SpriteSnapshotConfig'] = request.sprite_snapshot_config
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        if not DaraCore.is_null(request.width):
            query['Width'] = request.width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSnapshotJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_snapshot_job_with_options_async(
        self,
        tmp_req: main_models.SubmitSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSnapshotJobResponse:
        tmp_req.validate()
        request = main_models.SubmitSnapshotJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.specified_offset_times):
            request.specified_offset_times_shrink = Utils.array_to_string_with_specified_style(tmp_req.specified_offset_times, 'SpecifiedOffsetTimes', 'json')
        query = {}
        if not DaraCore.is_null(request.count):
            query['Count'] = request.count
        if not DaraCore.is_null(request.height):
            query['Height'] = request.height
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.snapshot_template_id):
            query['SnapshotTemplateId'] = request.snapshot_template_id
        if not DaraCore.is_null(request.specified_offset_time):
            query['SpecifiedOffsetTime'] = request.specified_offset_time
        if not DaraCore.is_null(request.specified_offset_times_shrink):
            query['SpecifiedOffsetTimes'] = request.specified_offset_times_shrink
        if not DaraCore.is_null(request.sprite_snapshot_config):
            query['SpriteSnapshotConfig'] = request.sprite_snapshot_config
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        if not DaraCore.is_null(request.width):
            query['Width'] = request.width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSnapshotJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_snapshot_job(
        self,
        request: main_models.SubmitSnapshotJobRequest,
    ) -> main_models.SubmitSnapshotJobResponse:
        runtime = RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    async def submit_snapshot_job_async(
        self,
        request: main_models.SubmitSnapshotJobRequest,
    ) -> main_models.SubmitSnapshotJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_snapshot_job_with_options_async(request, runtime)

    def submit_transcode_jobs_with_options(
        self,
        request: main_models.SubmitTranscodeJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTranscodeJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_config):
            query['EncryptConfig'] = request.encrypt_config
        if not DaraCore.is_null(request.override_params):
            query['OverrideParams'] = request.override_params
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTranscodeJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTranscodeJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_transcode_jobs_with_options_async(
        self,
        request: main_models.SubmitTranscodeJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTranscodeJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_config):
            query['EncryptConfig'] = request.encrypt_config
        if not DaraCore.is_null(request.override_params):
            query['OverrideParams'] = request.override_params
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTranscodeJobs',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTranscodeJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_transcode_jobs(
        self,
        request: main_models.SubmitTranscodeJobsRequest,
    ) -> main_models.SubmitTranscodeJobsResponse:
        runtime = RuntimeOptions()
        return self.submit_transcode_jobs_with_options(request, runtime)

    async def submit_transcode_jobs_async(
        self,
        request: main_models.SubmitTranscodeJobsRequest,
    ) -> main_models.SubmitTranscodeJobsResponse:
        runtime = RuntimeOptions()
        return await self.submit_transcode_jobs_with_options_async(request, runtime)

    def submit_workflow_job_with_options(
        self,
        request: main_models.SubmitWorkflowJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitWorkflowJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitWorkflowJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitWorkflowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_workflow_job_with_options_async(
        self,
        request: main_models.SubmitWorkflowJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitWorkflowJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitWorkflowJob',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitWorkflowJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_workflow_job(
        self,
        request: main_models.SubmitWorkflowJobRequest,
    ) -> main_models.SubmitWorkflowJobResponse:
        runtime = RuntimeOptions()
        return self.submit_workflow_job_with_options(request, runtime)

    async def submit_workflow_job_async(
        self,
        request: main_models.SubmitWorkflowJobRequest,
    ) -> main_models.SubmitWorkflowJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_workflow_job_with_options_async(request, runtime)

    def update_aitemplate_with_options(
        self,
        request: main_models.UpdateAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAITemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aitemplate_with_options_async(
        self,
        request: main_models.UpdateAITemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAITemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAITemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAITemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aitemplate(
        self,
        request: main_models.UpdateAITemplateRequest,
    ) -> main_models.UpdateAITemplateResponse:
        runtime = RuntimeOptions()
        return self.update_aitemplate_with_options(request, runtime)

    async def update_aitemplate_async(
        self,
        request: main_models.UpdateAITemplateRequest,
    ) -> main_models.UpdateAITemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_aitemplate_with_options_async(request, runtime)

    def update_app_info_with_options(
        self,
        request: main_models.UpdateAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_info_with_options_async(
        self,
        request: main_models.UpdateAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAppInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_info(
        self,
        request: main_models.UpdateAppInfoRequest,
    ) -> main_models.UpdateAppInfoResponse:
        runtime = RuntimeOptions()
        return self.update_app_info_with_options(request, runtime)

    async def update_app_info_async(
        self,
        request: main_models.UpdateAppInfoRequest,
    ) -> main_models.UpdateAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_app_info_with_options_async(request, runtime)

    def update_attached_media_infos_with_options(
        self,
        request: main_models.UpdateAttachedMediaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAttachedMediaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.update_content):
            query['UpdateContent'] = request.update_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAttachedMediaInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAttachedMediaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_attached_media_infos_with_options_async(
        self,
        request: main_models.UpdateAttachedMediaInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAttachedMediaInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.update_content):
            query['UpdateContent'] = request.update_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAttachedMediaInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAttachedMediaInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_attached_media_infos(
        self,
        request: main_models.UpdateAttachedMediaInfosRequest,
    ) -> main_models.UpdateAttachedMediaInfosResponse:
        runtime = RuntimeOptions()
        return self.update_attached_media_infos_with_options(request, runtime)

    async def update_attached_media_infos_async(
        self,
        request: main_models.UpdateAttachedMediaInfosRequest,
    ) -> main_models.UpdateAttachedMediaInfosResponse:
        runtime = RuntimeOptions()
        return await self.update_attached_media_infos_with_options_async(request, runtime)

    def update_category_with_options(
        self,
        request: main_models.UpdateCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cate_name):
            query['CateName'] = request.cate_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCategory',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_category_with_options_async(
        self,
        request: main_models.UpdateCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cate_name):
            query['CateName'] = request.cate_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCategory',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_category(
        self,
        request: main_models.UpdateCategoryRequest,
    ) -> main_models.UpdateCategoryResponse:
        runtime = RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    async def update_category_async(
        self,
        request: main_models.UpdateCategoryRequest,
    ) -> main_models.UpdateCategoryResponse:
        runtime = RuntimeOptions()
        return await self.update_category_with_options_async(request, runtime)

    def update_editing_project_with_options(
        self,
        request: main_models.UpdateEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.timeline):
            query['Timeline'] = request.timeline
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_editing_project_with_options_async(
        self,
        request: main_models.UpdateEditingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEditingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.timeline):
            query['Timeline'] = request.timeline
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEditingProject',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEditingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_editing_project(
        self,
        request: main_models.UpdateEditingProjectRequest,
    ) -> main_models.UpdateEditingProjectResponse:
        runtime = RuntimeOptions()
        return self.update_editing_project_with_options(request, runtime)

    async def update_editing_project_async(
        self,
        request: main_models.UpdateEditingProjectRequest,
    ) -> main_models.UpdateEditingProjectResponse:
        runtime = RuntimeOptions()
        return await self.update_editing_project_with_options_async(request, runtime)

    def update_image_infos_with_options(
        self,
        request: main_models.UpdateImageInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.update_content):
            query['UpdateContent'] = request.update_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImageInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_infos_with_options_async(
        self,
        request: main_models.UpdateImageInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.update_content):
            query['UpdateContent'] = request.update_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImageInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image_infos(
        self,
        request: main_models.UpdateImageInfosRequest,
    ) -> main_models.UpdateImageInfosResponse:
        runtime = RuntimeOptions()
        return self.update_image_infos_with_options(request, runtime)

    async def update_image_infos_async(
        self,
        request: main_models.UpdateImageInfosRequest,
    ) -> main_models.UpdateImageInfosResponse:
        runtime = RuntimeOptions()
        return await self.update_image_infos_with_options_async(request, runtime)

    def update_media_storage_class_with_options(
        self,
        request: main_models.UpdateMediaStorageClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaStorageClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_update_without_time_limit):
            query['AllowUpdateWithoutTimeLimit'] = request.allow_update_without_time_limit
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.restore_tier):
            query['RestoreTier'] = request.restore_tier
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaStorageClass',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaStorageClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_storage_class_with_options_async(
        self,
        request: main_models.UpdateMediaStorageClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaStorageClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_update_without_time_limit):
            query['AllowUpdateWithoutTimeLimit'] = request.allow_update_without_time_limit
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.restore_tier):
            query['RestoreTier'] = request.restore_tier
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaStorageClass',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaStorageClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_storage_class(
        self,
        request: main_models.UpdateMediaStorageClassRequest,
    ) -> main_models.UpdateMediaStorageClassResponse:
        runtime = RuntimeOptions()
        return self.update_media_storage_class_with_options(request, runtime)

    async def update_media_storage_class_async(
        self,
        request: main_models.UpdateMediaStorageClassRequest,
    ) -> main_models.UpdateMediaStorageClassResponse:
        runtime = RuntimeOptions()
        return await self.update_media_storage_class_with_options_async(request, runtime)

    def update_transcode_template_group_with_options(
        self,
        request: main_models.UpdateTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.locked):
            query['Locked'] = request.locked
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        if not DaraCore.is_null(request.transcode_template_list):
            query['TranscodeTemplateList'] = request.transcode_template_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTranscodeTemplateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_transcode_template_group_with_options_async(
        self,
        request: main_models.UpdateTranscodeTemplateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTranscodeTemplateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.locked):
            query['Locked'] = request.locked
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.transcode_template_group_id):
            query['TranscodeTemplateGroupId'] = request.transcode_template_group_id
        if not DaraCore.is_null(request.transcode_template_list):
            query['TranscodeTemplateList'] = request.transcode_template_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTranscodeTemplateGroup',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTranscodeTemplateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_transcode_template_group(
        self,
        request: main_models.UpdateTranscodeTemplateGroupRequest,
    ) -> main_models.UpdateTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return self.update_transcode_template_group_with_options(request, runtime)

    async def update_transcode_template_group_async(
        self,
        request: main_models.UpdateTranscodeTemplateGroupRequest,
    ) -> main_models.UpdateTranscodeTemplateGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_transcode_template_group_with_options_async(request, runtime)

    def update_video_info_with_options(
        self,
        request: main_models.UpdateVideoInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_video_info_with_options_async(
        self,
        request: main_models.UpdateVideoInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoInfo',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_video_info(
        self,
        request: main_models.UpdateVideoInfoRequest,
    ) -> main_models.UpdateVideoInfoResponse:
        runtime = RuntimeOptions()
        return self.update_video_info_with_options(request, runtime)

    async def update_video_info_async(
        self,
        request: main_models.UpdateVideoInfoRequest,
    ) -> main_models.UpdateVideoInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_video_info_with_options_async(request, runtime)

    def update_video_infos_with_options(
        self,
        request: main_models.UpdateVideoInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.update_content):
            query['UpdateContent'] = request.update_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_video_infos_with_options_async(
        self,
        request: main_models.UpdateVideoInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVideoInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.update_content):
            query['UpdateContent'] = request.update_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVideoInfos',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVideoInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_video_infos(
        self,
        request: main_models.UpdateVideoInfosRequest,
    ) -> main_models.UpdateVideoInfosResponse:
        runtime = RuntimeOptions()
        return self.update_video_infos_with_options(request, runtime)

    async def update_video_infos_async(
        self,
        request: main_models.UpdateVideoInfosRequest,
    ) -> main_models.UpdateVideoInfosResponse:
        runtime = RuntimeOptions()
        return await self.update_video_infos_with_options_async(request, runtime)

    def update_vod_domain_with_options(
        self,
        request: main_models.UpdateVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVodDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vod_domain_with_options_async(
        self,
        request: main_models.UpdateVodDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVodDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.sources):
            query['Sources'] = request.sources
        if not DaraCore.is_null(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVodDomain',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVodDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vod_domain(
        self,
        request: main_models.UpdateVodDomainRequest,
    ) -> main_models.UpdateVodDomainResponse:
        runtime = RuntimeOptions()
        return self.update_vod_domain_with_options(request, runtime)

    async def update_vod_domain_async(
        self,
        request: main_models.UpdateVodDomainRequest,
    ) -> main_models.UpdateVodDomainResponse:
        runtime = RuntimeOptions()
        return await self.update_vod_domain_with_options_async(request, runtime)

    def update_vod_template_with_options(
        self,
        request: main_models.UpdateVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.vod_template_id):
            query['VodTemplateId'] = request.vod_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVodTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vod_template_with_options_async(
        self,
        request: main_models.UpdateVodTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVodTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.vod_template_id):
            query['VodTemplateId'] = request.vod_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVodTemplate',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVodTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vod_template(
        self,
        request: main_models.UpdateVodTemplateRequest,
    ) -> main_models.UpdateVodTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_vod_template_with_options(request, runtime)

    async def update_vod_template_async(
        self,
        request: main_models.UpdateVodTemplateRequest,
    ) -> main_models.UpdateVodTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_vod_template_with_options_async(request, runtime)

    def update_watermark_with_options(
        self,
        request: main_models.UpdateWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.watermark_config):
            query['WatermarkConfig'] = request.watermark_config
        if not DaraCore.is_null(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_watermark_with_options_async(
        self,
        request: main_models.UpdateWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.watermark_config):
            query['WatermarkConfig'] = request.watermark_config
        if not DaraCore.is_null(request.watermark_id):
            query['WatermarkId'] = request.watermark_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWatermark',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_watermark(
        self,
        request: main_models.UpdateWatermarkRequest,
    ) -> main_models.UpdateWatermarkResponse:
        runtime = RuntimeOptions()
        return self.update_watermark_with_options(request, runtime)

    async def update_watermark_async(
        self,
        request: main_models.UpdateWatermarkRequest,
    ) -> main_models.UpdateWatermarkResponse:
        runtime = RuntimeOptions()
        return await self.update_watermark_with_options_async(request, runtime)

    def upload_media_by_urlwith_options(
        self,
        request: main_models.UploadMediaByURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadMediaByURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not DaraCore.is_null(request.upload_metadatas):
            query['UploadMetadatas'] = request.upload_metadatas
        if not DaraCore.is_null(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadMediaByURL',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadMediaByURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_media_by_urlwith_options_async(
        self,
        request: main_models.UploadMediaByURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadMediaByURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not DaraCore.is_null(request.template_group_id):
            query['TemplateGroupId'] = request.template_group_id
        if not DaraCore.is_null(request.upload_metadatas):
            query['UploadMetadatas'] = request.upload_metadatas
        if not DaraCore.is_null(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadMediaByURL',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadMediaByURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_media_by_url(
        self,
        request: main_models.UploadMediaByURLRequest,
    ) -> main_models.UploadMediaByURLResponse:
        runtime = RuntimeOptions()
        return self.upload_media_by_urlwith_options(request, runtime)

    async def upload_media_by_url_async(
        self,
        request: main_models.UploadMediaByURLRequest,
    ) -> main_models.UploadMediaByURLResponse:
        runtime = RuntimeOptions()
        return await self.upload_media_by_urlwith_options_async(request, runtime)

    def upload_stream_by_urlwith_options(
        self,
        request: main_models.UploadStreamByURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadStreamByURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.definition):
            query['Definition'] = request.definition
        if not DaraCore.is_null(request.file_extension):
            query['FileExtension'] = request.file_extension
        if not DaraCore.is_null(request.hdrtype):
            query['HDRType'] = request.hdrtype
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not DaraCore.is_null(request.upload_metadata):
            query['UploadMetadata'] = request.upload_metadata
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadStreamByURL',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadStreamByURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_stream_by_urlwith_options_async(
        self,
        request: main_models.UploadStreamByURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadStreamByURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.definition):
            query['Definition'] = request.definition
        if not DaraCore.is_null(request.file_extension):
            query['FileExtension'] = request.file_extension
        if not DaraCore.is_null(request.hdrtype):
            query['HDRType'] = request.hdrtype
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not DaraCore.is_null(request.upload_metadata):
            query['UploadMetadata'] = request.upload_metadata
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadStreamByURL',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadStreamByURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_stream_by_url(
        self,
        request: main_models.UploadStreamByURLRequest,
    ) -> main_models.UploadStreamByURLResponse:
        runtime = RuntimeOptions()
        return self.upload_stream_by_urlwith_options(request, runtime)

    async def upload_stream_by_url_async(
        self,
        request: main_models.UploadStreamByURLRequest,
    ) -> main_models.UploadStreamByURLResponse:
        runtime = RuntimeOptions()
        return await self.upload_stream_by_urlwith_options_async(request, runtime)

    def verify_vod_domain_owner_with_options(
        self,
        request: main_models.VerifyVodDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyVodDomainOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyVodDomainOwner',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyVodDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_vod_domain_owner_with_options_async(
        self,
        request: main_models.VerifyVodDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyVodDomainOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyVodDomainOwner',
            version = '2017-03-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyVodDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_vod_domain_owner(
        self,
        request: main_models.VerifyVodDomainOwnerRequest,
    ) -> main_models.VerifyVodDomainOwnerResponse:
        runtime = RuntimeOptions()
        return self.verify_vod_domain_owner_with_options(request, runtime)

    async def verify_vod_domain_owner_async(
        self,
        request: main_models.VerifyVodDomainOwnerRequest,
    ) -> main_models.VerifyVodDomainOwnerResponse:
        runtime = RuntimeOptions()
        return await self.verify_vod_domain_owner_with_options_async(request, runtime)
