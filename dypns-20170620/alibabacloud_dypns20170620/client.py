# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dypns20170620 import models as main_models
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
        self._endpoint = self.get_endpoint('dypns', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def config_verify_scene_app_info_with_options(
        self,
        request: main_models.ConfigVerifySceneAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigVerifySceneAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cm):
            query['CM'] = request.cm
        if not DaraCore.is_null(request.ct):
            query['CT'] = request.ct
        if not DaraCore.is_null(request.cu):
            query['CU'] = request.cu
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigVerifySceneAppInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigVerifySceneAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_verify_scene_app_info_with_options_async(
        self,
        request: main_models.ConfigVerifySceneAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigVerifySceneAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cm):
            query['CM'] = request.cm
        if not DaraCore.is_null(request.ct):
            query['CT'] = request.ct
        if not DaraCore.is_null(request.cu):
            query['CU'] = request.cu
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigVerifySceneAppInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigVerifySceneAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_verify_scene_app_info(
        self,
        request: main_models.ConfigVerifySceneAppInfoRequest,
    ) -> main_models.ConfigVerifySceneAppInfoResponse:
        runtime = RuntimeOptions()
        return self.config_verify_scene_app_info_with_options(request, runtime)

    async def config_verify_scene_app_info_async(
        self,
        request: main_models.ConfigVerifySceneAppInfoRequest,
    ) -> main_models.ConfigVerifySceneAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.config_verify_scene_app_info_with_options_async(request, runtime)

    def copy_scheme_with_options(
        self,
        request: main_models.CopySchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopySchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_scheme_with_options_async(
        self,
        request: main_models.CopySchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopySchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CopyScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopySchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_scheme(
        self,
        request: main_models.CopySchemeRequest,
    ) -> main_models.CopySchemeResponse:
        runtime = RuntimeOptions()
        return self.copy_scheme_with_options(request, runtime)

    async def copy_scheme_async(
        self,
        request: main_models.CopySchemeRequest,
    ) -> main_models.CopySchemeResponse:
        runtime = RuntimeOptions()
        return await self.copy_scheme_with_options_async(request, runtime)

    def copy_verify_scheme_with_options(
        self,
        request: main_models.CopyVerifySchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyVerifySchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cm_api_code):
            query['CmApiCode'] = request.cm_api_code
        if not DaraCore.is_null(request.cm_new_flag):
            query['CmNewFlag'] = request.cm_new_flag
        if not DaraCore.is_null(request.ct_api_code):
            query['CtApiCode'] = request.ct_api_code
        if not DaraCore.is_null(request.ct_new_flag):
            query['CtNewFlag'] = request.ct_new_flag
        if not DaraCore.is_null(request.cu_api_code):
            query['CuApiCode'] = request.cu_api_code
        if not DaraCore.is_null(request.cu_new_flag):
            query['CuNewFlag'] = request.cu_new_flag
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.model_scene_code):
            query['ModelSceneCode'] = request.model_scene_code
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
            action = 'CopyVerifyScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyVerifySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_verify_scheme_with_options_async(
        self,
        request: main_models.CopyVerifySchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyVerifySchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cm_api_code):
            query['CmApiCode'] = request.cm_api_code
        if not DaraCore.is_null(request.cm_new_flag):
            query['CmNewFlag'] = request.cm_new_flag
        if not DaraCore.is_null(request.ct_api_code):
            query['CtApiCode'] = request.ct_api_code
        if not DaraCore.is_null(request.ct_new_flag):
            query['CtNewFlag'] = request.ct_new_flag
        if not DaraCore.is_null(request.cu_api_code):
            query['CuApiCode'] = request.cu_api_code
        if not DaraCore.is_null(request.cu_new_flag):
            query['CuNewFlag'] = request.cu_new_flag
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.model_scene_code):
            query['ModelSceneCode'] = request.model_scene_code
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
            action = 'CopyVerifyScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyVerifySchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_verify_scheme(
        self,
        request: main_models.CopyVerifySchemeRequest,
    ) -> main_models.CopyVerifySchemeResponse:
        runtime = RuntimeOptions()
        return self.copy_verify_scheme_with_options(request, runtime)

    async def copy_verify_scheme_async(
        self,
        request: main_models.CopyVerifySchemeRequest,
    ) -> main_models.CopyVerifySchemeResponse:
        runtime = RuntimeOptions()
        return await self.copy_verify_scheme_with_options_async(request, runtime)

    def create_dypns_sms_verify_call_back_test_with_options(
        self,
        request: main_models.CreateDypnsSmsVerifyCallBackTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDypnsSmsVerifyCallBackTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDypnsSmsVerifyCallBackTest',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDypnsSmsVerifyCallBackTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dypns_sms_verify_call_back_test_with_options_async(
        self,
        request: main_models.CreateDypnsSmsVerifyCallBackTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDypnsSmsVerifyCallBackTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDypnsSmsVerifyCallBackTest',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDypnsSmsVerifyCallBackTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dypns_sms_verify_call_back_test(
        self,
        request: main_models.CreateDypnsSmsVerifyCallBackTestRequest,
    ) -> main_models.CreateDypnsSmsVerifyCallBackTestResponse:
        runtime = RuntimeOptions()
        return self.create_dypns_sms_verify_call_back_test_with_options(request, runtime)

    async def create_dypns_sms_verify_call_back_test_async(
        self,
        request: main_models.CreateDypnsSmsVerifyCallBackTestRequest,
    ) -> main_models.CreateDypnsSmsVerifyCallBackTestResponse:
        runtime = RuntimeOptions()
        return await self.create_dypns_sms_verify_call_back_test_with_options_async(request, runtime)

    def create_dypns_sms_verify_message_call_back_with_options(
        self,
        request: main_models.CreateDypnsSmsVerifyMessageCallBackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDypnsSmsVerifyMessageCallBackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDypnsSmsVerifyMessageCallBack',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDypnsSmsVerifyMessageCallBackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dypns_sms_verify_message_call_back_with_options_async(
        self,
        request: main_models.CreateDypnsSmsVerifyMessageCallBackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDypnsSmsVerifyMessageCallBackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDypnsSmsVerifyMessageCallBack',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDypnsSmsVerifyMessageCallBackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dypns_sms_verify_message_call_back(
        self,
        request: main_models.CreateDypnsSmsVerifyMessageCallBackRequest,
    ) -> main_models.CreateDypnsSmsVerifyMessageCallBackResponse:
        runtime = RuntimeOptions()
        return self.create_dypns_sms_verify_message_call_back_with_options(request, runtime)

    async def create_dypns_sms_verify_message_call_back_async(
        self,
        request: main_models.CreateDypnsSmsVerifyMessageCallBackRequest,
    ) -> main_models.CreateDypnsSmsVerifyMessageCallBackResponse:
        runtime = RuntimeOptions()
        return await self.create_dypns_sms_verify_message_call_back_with_options_async(request, runtime)

    def create_dypns_sms_verify_message_queue_with_options(
        self,
        request: main_models.CreateDypnsSmsVerifyMessageQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDypnsSmsVerifyMessageQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_queue_types):
            query['QueryQueueTypes'] = request.query_queue_types
        if not DaraCore.is_null(request.queue_type):
            query['QueueType'] = request.queue_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDypnsSmsVerifyMessageQueue',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDypnsSmsVerifyMessageQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dypns_sms_verify_message_queue_with_options_async(
        self,
        request: main_models.CreateDypnsSmsVerifyMessageQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDypnsSmsVerifyMessageQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_queue_types):
            query['QueryQueueTypes'] = request.query_queue_types
        if not DaraCore.is_null(request.queue_type):
            query['QueueType'] = request.queue_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDypnsSmsVerifyMessageQueue',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDypnsSmsVerifyMessageQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dypns_sms_verify_message_queue(
        self,
        request: main_models.CreateDypnsSmsVerifyMessageQueueRequest,
    ) -> main_models.CreateDypnsSmsVerifyMessageQueueResponse:
        runtime = RuntimeOptions()
        return self.create_dypns_sms_verify_message_queue_with_options(request, runtime)

    async def create_dypns_sms_verify_message_queue_async(
        self,
        request: main_models.CreateDypnsSmsVerifyMessageQueueRequest,
    ) -> main_models.CreateDypnsSmsVerifyMessageQueueResponse:
        runtime = RuntimeOptions()
        return await self.create_dypns_sms_verify_message_queue_with_options_async(request, runtime)

    def create_file_by_biz_with_options(
        self,
        request: main_models.CreateFileByBizRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileByBizResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.save_oss_file_name):
            query['SaveOssFileName'] = request.save_oss_file_name
        if not DaraCore.is_null(request.user_view_file_name):
            query['UserViewFileName'] = request.user_view_file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileByBiz',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileByBizResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_by_biz_with_options_async(
        self,
        request: main_models.CreateFileByBizRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileByBizResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.save_oss_file_name):
            query['SaveOssFileName'] = request.save_oss_file_name
        if not DaraCore.is_null(request.user_view_file_name):
            query['UserViewFileName'] = request.user_view_file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileByBiz',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileByBizResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_by_biz(
        self,
        request: main_models.CreateFileByBizRequest,
    ) -> main_models.CreateFileByBizResponse:
        runtime = RuntimeOptions()
        return self.create_file_by_biz_with_options(request, runtime)

    async def create_file_by_biz_async(
        self,
        request: main_models.CreateFileByBizRequest,
    ) -> main_models.CreateFileByBizResponse:
        runtime = RuntimeOptions()
        return await self.create_file_by_biz_with_options_async(request, runtime)

    def create_gate_verify_export_log_with_options(
        self,
        request: main_models.CreateGateVerifyExportLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGateVerifyExportLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_month):
            query['QueryMonth'] = request.query_month
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGateVerifyExportLog',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGateVerifyExportLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gate_verify_export_log_with_options_async(
        self,
        request: main_models.CreateGateVerifyExportLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGateVerifyExportLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_month):
            query['QueryMonth'] = request.query_month
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGateVerifyExportLog',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGateVerifyExportLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gate_verify_export_log(
        self,
        request: main_models.CreateGateVerifyExportLogRequest,
    ) -> main_models.CreateGateVerifyExportLogResponse:
        runtime = RuntimeOptions()
        return self.create_gate_verify_export_log_with_options(request, runtime)

    async def create_gate_verify_export_log_async(
        self,
        request: main_models.CreateGateVerifyExportLogRequest,
    ) -> main_models.CreateGateVerifyExportLogResponse:
        runtime = RuntimeOptions()
        return await self.create_gate_verify_export_log_with_options_async(request, runtime)

    def create_graphic_auth_scheme_config_with_options(
        self,
        request: main_models.CreateGraphicAuthSchemeConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGraphicAuthSchemeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGraphicAuthSchemeConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGraphicAuthSchemeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_graphic_auth_scheme_config_with_options_async(
        self,
        request: main_models.CreateGraphicAuthSchemeConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGraphicAuthSchemeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGraphicAuthSchemeConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGraphicAuthSchemeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_graphic_auth_scheme_config(
        self,
        request: main_models.CreateGraphicAuthSchemeConfigRequest,
    ) -> main_models.CreateGraphicAuthSchemeConfigResponse:
        runtime = RuntimeOptions()
        return self.create_graphic_auth_scheme_config_with_options(request, runtime)

    async def create_graphic_auth_scheme_config_async(
        self,
        request: main_models.CreateGraphicAuthSchemeConfigRequest,
    ) -> main_models.CreateGraphicAuthSchemeConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_graphic_auth_scheme_config_with_options_async(request, runtime)

    def create_product_with_options(
        self,
        request: main_models.CreateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.prod_id):
            query['ProdId'] = request.prod_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduct',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: main_models.CreateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.prod_id):
            query['ProdId'] = request.prod_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduct',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product(
        self,
        request: main_models.CreateProductRequest,
    ) -> main_models.CreateProductResponse:
        runtime = RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    async def create_product_async(
        self,
        request: main_models.CreateProductRequest,
    ) -> main_models.CreateProductResponse:
        runtime = RuntimeOptions()
        return await self.create_product_with_options_async(request, runtime)

    def create_scheme_config_with_options(
        self,
        request: main_models.CreateSchemeConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchemeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_package_name):
            query['AndroidPackageName'] = request.android_package_name
        if not DaraCore.is_null(request.android_package_sign):
            query['AndroidPackageSign'] = request.android_package_sign
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.h_5origin):
            query['H5Origin'] = request.h_5origin
        if not DaraCore.is_null(request.h_5url):
            query['H5Url'] = request.h_5url
        if not DaraCore.is_null(request.ios_bundle_id):
            query['IosBundleId'] = request.ios_bundle_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchemeConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchemeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheme_config_with_options_async(
        self,
        request: main_models.CreateSchemeConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchemeConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.android_package_name):
            query['AndroidPackageName'] = request.android_package_name
        if not DaraCore.is_null(request.android_package_sign):
            query['AndroidPackageSign'] = request.android_package_sign
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.h_5origin):
            query['H5Origin'] = request.h_5origin
        if not DaraCore.is_null(request.h_5url):
            query['H5Url'] = request.h_5url
        if not DaraCore.is_null(request.ios_bundle_id):
            query['IosBundleId'] = request.ios_bundle_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchemeConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchemeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheme_config(
        self,
        request: main_models.CreateSchemeConfigRequest,
    ) -> main_models.CreateSchemeConfigResponse:
        runtime = RuntimeOptions()
        return self.create_scheme_config_with_options(request, runtime)

    async def create_scheme_config_async(
        self,
        request: main_models.CreateSchemeConfigRequest,
    ) -> main_models.CreateSchemeConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_scheme_config_with_options_async(request, runtime)

    def create_sms_sign_with_options(
        self,
        request: main_models.CreateSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_url):
            query['AppUrl'] = request.app_url
        if not DaraCore.is_null(request.business_license_cert):
            query['BusinessLicenseCert'] = request.business_license_cert
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.extend_message):
            query['ExtendMessage'] = request.extend_message
        if not DaraCore.is_null(request.old_sms_sign_name):
            query['OldSmsSignName'] = request.old_sms_sign_name
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.organization_code_cert):
            query['OrganizationCodeCert'] = request.organization_code_cert
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.sms_sign_remark):
            query['SmsSignRemark'] = request.sms_sign_remark
        if not DaraCore.is_null(request.sms_sign_source):
            query['SmsSignSource'] = request.sms_sign_source
        if not DaraCore.is_null(request.tax_registration_cert):
            query['TaxRegistrationCert'] = request.tax_registration_cert
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsSign',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_sign_with_options_async(
        self,
        request: main_models.CreateSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_url):
            query['AppUrl'] = request.app_url
        if not DaraCore.is_null(request.business_license_cert):
            query['BusinessLicenseCert'] = request.business_license_cert
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.extend_message):
            query['ExtendMessage'] = request.extend_message
        if not DaraCore.is_null(request.old_sms_sign_name):
            query['OldSmsSignName'] = request.old_sms_sign_name
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.organization_code_cert):
            query['OrganizationCodeCert'] = request.organization_code_cert
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.sms_sign_remark):
            query['SmsSignRemark'] = request.sms_sign_remark
        if not DaraCore.is_null(request.sms_sign_source):
            query['SmsSignSource'] = request.sms_sign_source
        if not DaraCore.is_null(request.tax_registration_cert):
            query['TaxRegistrationCert'] = request.tax_registration_cert
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsSign',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_sign(
        self,
        request: main_models.CreateSmsSignRequest,
    ) -> main_models.CreateSmsSignResponse:
        runtime = RuntimeOptions()
        return self.create_sms_sign_with_options(request, runtime)

    async def create_sms_sign_async(
        self,
        request: main_models.CreateSmsSignRequest,
    ) -> main_models.CreateSmsSignResponse:
        runtime = RuntimeOptions()
        return await self.create_sms_sign_with_options_async(request, runtime)

    def create_sms_template_with_options(
        self,
        request: main_models.CreateSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_url):
            query['BizUrl'] = request.biz_url
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sms_template_content):
            query['SmsTemplateContent'] = request.sms_template_content
        if not DaraCore.is_null(request.sms_template_name):
            query['SmsTemplateName'] = request.sms_template_name
        if not DaraCore.is_null(request.sms_template_rule):
            query['SmsTemplateRule'] = request.sms_template_rule
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsTemplate',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_template_with_options_async(
        self,
        request: main_models.CreateSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_url):
            query['BizUrl'] = request.biz_url
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sms_template_content):
            query['SmsTemplateContent'] = request.sms_template_content
        if not DaraCore.is_null(request.sms_template_name):
            query['SmsTemplateName'] = request.sms_template_name
        if not DaraCore.is_null(request.sms_template_rule):
            query['SmsTemplateRule'] = request.sms_template_rule
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsTemplate',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_template(
        self,
        request: main_models.CreateSmsTemplateRequest,
    ) -> main_models.CreateSmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_sms_template_with_options(request, runtime)

    async def create_sms_template_async(
        self,
        request: main_models.CreateSmsTemplateRequest,
    ) -> main_models.CreateSmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_sms_template_with_options_async(request, runtime)

    def create_sms_verify_statistic_records_export_task_with_options(
        self,
        request: main_models.CreateSmsVerifyStatisticRecordsExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsVerifyStatisticRecordsExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_date):
            query['FromDate'] = request.from_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not DaraCore.is_null(request.to_date):
            query['ToDate'] = request.to_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsVerifyStatisticRecordsExportTask',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsVerifyStatisticRecordsExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sms_verify_statistic_records_export_task_with_options_async(
        self,
        request: main_models.CreateSmsVerifyStatisticRecordsExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSmsVerifyStatisticRecordsExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_date):
            query['FromDate'] = request.from_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not DaraCore.is_null(request.to_date):
            query['ToDate'] = request.to_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSmsVerifyStatisticRecordsExportTask',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSmsVerifyStatisticRecordsExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sms_verify_statistic_records_export_task(
        self,
        request: main_models.CreateSmsVerifyStatisticRecordsExportTaskRequest,
    ) -> main_models.CreateSmsVerifyStatisticRecordsExportTaskResponse:
        runtime = RuntimeOptions()
        return self.create_sms_verify_statistic_records_export_task_with_options(request, runtime)

    async def create_sms_verify_statistic_records_export_task_async(
        self,
        request: main_models.CreateSmsVerifyStatisticRecordsExportTaskRequest,
    ) -> main_models.CreateSmsVerifyStatisticRecordsExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_sms_verify_statistic_records_export_task_with_options_async(request, runtime)

    def create_verify_scheme_with_options(
        self,
        request: main_models.CreateVerifySchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVerifySchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not DaraCore.is_null(request.cm_api_code):
            query['CmApiCode'] = request.cm_api_code
        if not DaraCore.is_null(request.ct_api_code):
            query['CtApiCode'] = request.ct_api_code
        if not DaraCore.is_null(request.cu_api_code):
            query['CuApiCode'] = request.cu_api_code
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.hm_app_identifier):
            query['HmAppIdentifier'] = request.hm_app_identifier
        if not DaraCore.is_null(request.hm_package_name):
            query['HmPackageName'] = request.hm_package_name
        if not DaraCore.is_null(request.hm_sign_name):
            query['HmSignName'] = request.hm_sign_name
        if not DaraCore.is_null(request.ip_white_list):
            query['IpWhiteList'] = request.ip_white_list
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pack_name):
            query['PackName'] = request.pack_name
        if not DaraCore.is_null(request.pack_sign):
            query['PackSign'] = request.pack_sign
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not DaraCore.is_null(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVerifyScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVerifySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_verify_scheme_with_options_async(
        self,
        request: main_models.CreateVerifySchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVerifySchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not DaraCore.is_null(request.cm_api_code):
            query['CmApiCode'] = request.cm_api_code
        if not DaraCore.is_null(request.ct_api_code):
            query['CtApiCode'] = request.ct_api_code
        if not DaraCore.is_null(request.cu_api_code):
            query['CuApiCode'] = request.cu_api_code
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.hm_app_identifier):
            query['HmAppIdentifier'] = request.hm_app_identifier
        if not DaraCore.is_null(request.hm_package_name):
            query['HmPackageName'] = request.hm_package_name
        if not DaraCore.is_null(request.hm_sign_name):
            query['HmSignName'] = request.hm_sign_name
        if not DaraCore.is_null(request.ip_white_list):
            query['IpWhiteList'] = request.ip_white_list
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pack_name):
            query['PackName'] = request.pack_name
        if not DaraCore.is_null(request.pack_sign):
            query['PackSign'] = request.pack_sign
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not DaraCore.is_null(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVerifyScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVerifySchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_verify_scheme(
        self,
        request: main_models.CreateVerifySchemeRequest,
    ) -> main_models.CreateVerifySchemeResponse:
        runtime = RuntimeOptions()
        return self.create_verify_scheme_with_options(request, runtime)

    async def create_verify_scheme_async(
        self,
        request: main_models.CreateVerifySchemeRequest,
    ) -> main_models.CreateVerifySchemeResponse:
        runtime = RuntimeOptions()
        return await self.create_verify_scheme_with_options_async(request, runtime)

    def createt_verify_sms_export_task_with_options(
        self,
        request: main_models.CreatetVerifySmsExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatetVerifySmsExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not DaraCore.is_null(request.send_status):
            query['SendStatus'] = request.send_status
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatetVerifySmsExportTask',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatetVerifySmsExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def createt_verify_sms_export_task_with_options_async(
        self,
        request: main_models.CreatetVerifySmsExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatetVerifySmsExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_name):
            query['SchemeName'] = request.scheme_name
        if not DaraCore.is_null(request.send_status):
            query['SendStatus'] = request.send_status
        if not DaraCore.is_null(request.sign_name):
            query['SignName'] = request.sign_name
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatetVerifySmsExportTask',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatetVerifySmsExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def createt_verify_sms_export_task(
        self,
        request: main_models.CreatetVerifySmsExportTaskRequest,
    ) -> main_models.CreatetVerifySmsExportTaskResponse:
        runtime = RuntimeOptions()
        return self.createt_verify_sms_export_task_with_options(request, runtime)

    async def createt_verify_sms_export_task_async(
        self,
        request: main_models.CreatetVerifySmsExportTaskRequest,
    ) -> main_models.CreatetVerifySmsExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.createt_verify_sms_export_task_with_options_async(request, runtime)

    def delete_scene_with_options(
        self,
        request: main_models.DeleteSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScene',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scene_with_options_async(
        self,
        request: main_models.DeleteSceneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSceneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScene',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scene(
        self,
        request: main_models.DeleteSceneRequest,
    ) -> main_models.DeleteSceneResponse:
        runtime = RuntimeOptions()
        return self.delete_scene_with_options(request, runtime)

    async def delete_scene_async(
        self,
        request: main_models.DeleteSceneRequest,
    ) -> main_models.DeleteSceneResponse:
        runtime = RuntimeOptions()
        return await self.delete_scene_with_options_async(request, runtime)

    def delete_scheme_with_options(
        self,
        request: main_models.DeleteSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheme_with_options_async(
        self,
        request: main_models.DeleteSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheme(
        self,
        request: main_models.DeleteSchemeRequest,
    ) -> main_models.DeleteSchemeResponse:
        runtime = RuntimeOptions()
        return self.delete_scheme_with_options(request, runtime)

    async def delete_scheme_async(
        self,
        request: main_models.DeleteSchemeRequest,
    ) -> main_models.DeleteSchemeResponse:
        runtime = RuntimeOptions()
        return await self.delete_scheme_with_options_async(request, runtime)

    def get_down_load_file_url_with_options(
        self,
        request: main_models.GetDownLoadFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDownLoadFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acct_id):
            query['AcctId'] = request.acct_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
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
            action = 'GetDownLoadFileUrl',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDownLoadFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_down_load_file_url_with_options_async(
        self,
        request: main_models.GetDownLoadFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDownLoadFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acct_id):
            query['AcctId'] = request.acct_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
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
            action = 'GetDownLoadFileUrl',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDownLoadFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_down_load_file_url(
        self,
        request: main_models.GetDownLoadFileUrlRequest,
    ) -> main_models.GetDownLoadFileUrlResponse:
        runtime = RuntimeOptions()
        return self.get_down_load_file_url_with_options(request, runtime)

    async def get_down_load_file_url_async(
        self,
        request: main_models.GetDownLoadFileUrlRequest,
    ) -> main_models.GetDownLoadFileUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_down_load_file_url_with_options_async(request, runtime)

    def get_enterprise_info_with_options(
        self,
        request: main_models.GetEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['EnterpriseId'] = request.enterprise_id
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
            action = 'GetEnterpriseInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_info_with_options_async(
        self,
        request: main_models.GetEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['EnterpriseId'] = request.enterprise_id
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
            action = 'GetEnterpriseInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_info(
        self,
        request: main_models.GetEnterpriseInfoRequest,
    ) -> main_models.GetEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return self.get_enterprise_info_with_options(request, runtime)

    async def get_enterprise_info_async(
        self,
        request: main_models.GetEnterpriseInfoRequest,
    ) -> main_models.GetEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_enterprise_info_with_options_async(request, runtime)

    def get_open_sub_product_status_with_options(
        self,
        request: main_models.GetOpenSubProductStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOpenSubProductStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOpenSubProductStatus',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOpenSubProductStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_open_sub_product_status_with_options_async(
        self,
        request: main_models.GetOpenSubProductStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOpenSubProductStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOpenSubProductStatus',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOpenSubProductStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_open_sub_product_status(
        self,
        request: main_models.GetOpenSubProductStatusRequest,
    ) -> main_models.GetOpenSubProductStatusResponse:
        runtime = RuntimeOptions()
        return self.get_open_sub_product_status_with_options(request, runtime)

    async def get_open_sub_product_status_async(
        self,
        request: main_models.GetOpenSubProductStatusRequest,
    ) -> main_models.GetOpenSubProductStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_open_sub_product_status_with_options_async(request, runtime)

    def get_oss_upload_for_enterprise_with_options(
        self,
        request: main_models.GetOssUploadForEnterpriseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssUploadForEnterpriseResponse:
        request.validate()
        query = {}
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
            action = 'GetOssUploadForEnterprise',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssUploadForEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_upload_for_enterprise_with_options_async(
        self,
        request: main_models.GetOssUploadForEnterpriseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssUploadForEnterpriseResponse:
        request.validate()
        query = {}
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
            action = 'GetOssUploadForEnterprise',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssUploadForEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_upload_for_enterprise(
        self,
        request: main_models.GetOssUploadForEnterpriseRequest,
    ) -> main_models.GetOssUploadForEnterpriseResponse:
        runtime = RuntimeOptions()
        return self.get_oss_upload_for_enterprise_with_options(request, runtime)

    async def get_oss_upload_for_enterprise_async(
        self,
        request: main_models.GetOssUploadForEnterpriseRequest,
    ) -> main_models.GetOssUploadForEnterpriseResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_upload_for_enterprise_with_options_async(request, runtime)

    def get_oss_upload_sign_with_options(
        self,
        request: main_models.GetOssUploadSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssUploadSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
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
            action = 'GetOssUploadSign',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssUploadSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_upload_sign_with_options_async(
        self,
        request: main_models.GetOssUploadSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssUploadSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
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
            action = 'GetOssUploadSign',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssUploadSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_upload_sign(
        self,
        request: main_models.GetOssUploadSignRequest,
    ) -> main_models.GetOssUploadSignResponse:
        runtime = RuntimeOptions()
        return self.get_oss_upload_sign_with_options(request, runtime)

    async def get_oss_upload_sign_async(
        self,
        request: main_models.GetOssUploadSignRequest,
    ) -> main_models.GetOssUploadSignResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_upload_sign_with_options_async(request, runtime)

    def get_scheme_with_options(
        self,
        request: main_models.GetSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scheme_with_options_async(
        self,
        request: main_models.GetSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scheme_id):
            query['SchemeId'] = request.scheme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scheme(
        self,
        request: main_models.GetSchemeRequest,
    ) -> main_models.GetSchemeResponse:
        runtime = RuntimeOptions()
        return self.get_scheme_with_options(request, runtime)

    async def get_scheme_async(
        self,
        request: main_models.GetSchemeRequest,
    ) -> main_models.GetSchemeResponse:
        runtime = RuntimeOptions()
        return await self.get_scheme_with_options_async(request, runtime)

    def get_sms_code_limit_config_with_options(
        self,
        request: main_models.GetSmsCodeLimitConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsCodeLimitConfigResponse:
        request.validate()
        query = {}
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
            action = 'GetSmsCodeLimitConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsCodeLimitConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_code_limit_config_with_options_async(
        self,
        request: main_models.GetSmsCodeLimitConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsCodeLimitConfigResponse:
        request.validate()
        query = {}
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
            action = 'GetSmsCodeLimitConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsCodeLimitConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_code_limit_config(
        self,
        request: main_models.GetSmsCodeLimitConfigRequest,
    ) -> main_models.GetSmsCodeLimitConfigResponse:
        runtime = RuntimeOptions()
        return self.get_sms_code_limit_config_with_options(request, runtime)

    async def get_sms_code_limit_config_async(
        self,
        request: main_models.GetSmsCodeLimitConfigRequest,
    ) -> main_models.GetSmsCodeLimitConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_sms_code_limit_config_with_options_async(request, runtime)

    def get_sms_sign_with_options(
        self,
        request: main_models.GetSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsSign',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sms_sign_with_options_async(
        self,
        request: main_models.GetSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSmsSign',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sms_sign(
        self,
        request: main_models.GetSmsSignRequest,
    ) -> main_models.GetSmsSignResponse:
        runtime = RuntimeOptions()
        return self.get_sms_sign_with_options(request, runtime)

    async def get_sms_sign_async(
        self,
        request: main_models.GetSmsSignRequest,
    ) -> main_models.GetSmsSignResponse:
        runtime = RuntimeOptions()
        return await self.get_sms_sign_with_options_async(request, runtime)

    def list_audit_pass_enterprise_info_with_options(
        self,
        request: main_models.ListAuditPassEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuditPassEnterpriseInfoResponse:
        request.validate()
        query = {}
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
            action = 'ListAuditPassEnterpriseInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuditPassEnterpriseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_audit_pass_enterprise_info_with_options_async(
        self,
        request: main_models.ListAuditPassEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuditPassEnterpriseInfoResponse:
        request.validate()
        query = {}
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
            action = 'ListAuditPassEnterpriseInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuditPassEnterpriseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_audit_pass_enterprise_info(
        self,
        request: main_models.ListAuditPassEnterpriseInfoRequest,
    ) -> main_models.ListAuditPassEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return self.list_audit_pass_enterprise_info_with_options(request, runtime)

    async def list_audit_pass_enterprise_info_async(
        self,
        request: main_models.ListAuditPassEnterpriseInfoRequest,
    ) -> main_models.ListAuditPassEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_audit_pass_enterprise_info_with_options_async(request, runtime)

    def list_certificate_with_options(
        self,
        request: main_models.ListCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCertificate',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_certificate_with_options_async(
        self,
        request: main_models.ListCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_no):
            query['PhoneNo'] = request.phone_no
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCertificate',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_certificate(
        self,
        request: main_models.ListCertificateRequest,
    ) -> main_models.ListCertificateResponse:
        runtime = RuntimeOptions()
        return self.list_certificate_with_options(request, runtime)

    async def list_certificate_async(
        self,
        request: main_models.ListCertificateRequest,
    ) -> main_models.ListCertificateResponse:
        runtime = RuntimeOptions()
        return await self.list_certificate_with_options_async(request, runtime)

    def list_enterprise_info_with_options(
        self,
        request: main_models.ListEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enterprise_info_with_options_async(
        self,
        request: main_models.ListEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enterprise_info(
        self,
        request: main_models.ListEnterpriseInfoRequest,
    ) -> main_models.ListEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return self.list_enterprise_info_with_options(request, runtime)

    async def list_enterprise_info_async(
        self,
        request: main_models.ListEnterpriseInfoRequest,
    ) -> main_models.ListEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_enterprise_info_with_options_async(request, runtime)

    def list_scheme_with_options(
        self,
        request: main_models.ListSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheme_with_options_async(
        self,
        request: main_models.ListSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScheme',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheme(
        self,
        request: main_models.ListSchemeRequest,
    ) -> main_models.ListSchemeResponse:
        runtime = RuntimeOptions()
        return self.list_scheme_with_options(request, runtime)

    async def list_scheme_async(
        self,
        request: main_models.ListSchemeRequest,
    ) -> main_models.ListSchemeResponse:
        runtime = RuntimeOptions()
        return await self.list_scheme_with_options_async(request, runtime)

    def list_sms_sign_with_options(
        self,
        request: main_models.ListSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.query_sms_sign):
            query['QuerySmsSign'] = request.query_sms_sign
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmsSign',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmsSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sms_sign_with_options_async(
        self,
        request: main_models.ListSmsSignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmsSignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.query_sms_sign):
            query['QuerySmsSign'] = request.query_sms_sign
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmsSign',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmsSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sms_sign(
        self,
        request: main_models.ListSmsSignRequest,
    ) -> main_models.ListSmsSignResponse:
        runtime = RuntimeOptions()
        return self.list_sms_sign_with_options(request, runtime)

    async def list_sms_sign_async(
        self,
        request: main_models.ListSmsSignRequest,
    ) -> main_models.ListSmsSignResponse:
        runtime = RuntimeOptions()
        return await self.list_sms_sign_with_options_async(request, runtime)

    def list_sms_template_with_options(
        self,
        request: main_models.ListSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.query_template):
            query['QueryTemplate'] = request.query_template
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmsTemplate',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmsTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sms_template_with_options_async(
        self,
        request: main_models.ListSmsTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSmsTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.query_template):
            query['QueryTemplate'] = request.query_template
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSmsTemplate',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSmsTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sms_template(
        self,
        request: main_models.ListSmsTemplateRequest,
    ) -> main_models.ListSmsTemplateResponse:
        runtime = RuntimeOptions()
        return self.list_sms_template_with_options(request, runtime)

    async def list_sms_template_async(
        self,
        request: main_models.ListSmsTemplateRequest,
    ) -> main_models.ListSmsTemplateResponse:
        runtime = RuntimeOptions()
        return await self.list_sms_template_with_options_async(request, runtime)

    def open_common_product_with_options(
        self,
        request: main_models.OpenCommonProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenCommonProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenCommonProduct',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenCommonProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_common_product_with_options_async(
        self,
        request: main_models.OpenCommonProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenCommonProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenCommonProduct',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenCommonProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_common_product(
        self,
        request: main_models.OpenCommonProductRequest,
    ) -> main_models.OpenCommonProductResponse:
        runtime = RuntimeOptions()
        return self.open_common_product_with_options(request, runtime)

    async def open_common_product_async(
        self,
        request: main_models.OpenCommonProductRequest,
    ) -> main_models.OpenCommonProductResponse:
        runtime = RuntimeOptions()
        return await self.open_common_product_with_options_async(request, runtime)

    def query_common_billing_with_options(
        self,
        request: main_models.QueryCommonBillingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommonBillingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.month):
            query['Month'] = request.month
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommonBilling',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommonBillingResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_common_billing_with_options_async(
        self,
        request: main_models.QueryCommonBillingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommonBillingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.month):
            query['Month'] = request.month
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommonBilling',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommonBillingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_common_billing(
        self,
        request: main_models.QueryCommonBillingRequest,
    ) -> main_models.QueryCommonBillingResponse:
        runtime = RuntimeOptions()
        return self.query_common_billing_with_options(request, runtime)

    async def query_common_billing_async(
        self,
        request: main_models.QueryCommonBillingRequest,
    ) -> main_models.QueryCommonBillingResponse:
        runtime = RuntimeOptions()
        return await self.query_common_billing_with_options_async(request, runtime)

    def query_common_cust_info_with_options(
        self,
        request: main_models.QueryCommonCustInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommonCustInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommonCustInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommonCustInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_common_cust_info_with_options_async(
        self,
        request: main_models.QueryCommonCustInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommonCustInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommonCustInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommonCustInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_common_cust_info(
        self,
        request: main_models.QueryCommonCustInfoRequest,
    ) -> main_models.QueryCommonCustInfoResponse:
        runtime = RuntimeOptions()
        return self.query_common_cust_info_with_options(request, runtime)

    async def query_common_cust_info_async(
        self,
        request: main_models.QueryCommonCustInfoRequest,
    ) -> main_models.QueryCommonCustInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_common_cust_info_with_options_async(request, runtime)

    def query_common_statistic_with_options(
        self,
        request: main_models.QueryCommonStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommonStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommonStatistic',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommonStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_common_statistic_with_options_async(
        self,
        request: main_models.QueryCommonStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommonStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommonStatistic',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommonStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_common_statistic(
        self,
        request: main_models.QueryCommonStatisticRequest,
    ) -> main_models.QueryCommonStatisticResponse:
        runtime = RuntimeOptions()
        return self.query_common_statistic_with_options(request, runtime)

    async def query_common_statistic_async(
        self,
        request: main_models.QueryCommonStatisticRequest,
    ) -> main_models.QueryCommonStatisticResponse:
        runtime = RuntimeOptions()
        return await self.query_common_statistic_with_options_async(request, runtime)

    def query_common_statistic_preview_with_options(
        self,
        request: main_models.QueryCommonStatisticPreviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommonStatisticPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommonStatisticPreview',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommonStatisticPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_common_statistic_preview_with_options_async(
        self,
        request: main_models.QueryCommonStatisticPreviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommonStatisticPreviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommonStatisticPreview',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommonStatisticPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_common_statistic_preview(
        self,
        request: main_models.QueryCommonStatisticPreviewRequest,
    ) -> main_models.QueryCommonStatisticPreviewResponse:
        runtime = RuntimeOptions()
        return self.query_common_statistic_preview_with_options(request, runtime)

    async def query_common_statistic_preview_async(
        self,
        request: main_models.QueryCommonStatisticPreviewRequest,
    ) -> main_models.QueryCommonStatisticPreviewResponse:
        runtime = RuntimeOptions()
        return await self.query_common_statistic_preview_with_options_async(request, runtime)

    def query_dayu_migrate_status_with_options(
        self,
        request: main_models.QueryDayuMigrateStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDayuMigrateStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDayuMigrateStatus',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDayuMigrateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dayu_migrate_status_with_options_async(
        self,
        request: main_models.QueryDayuMigrateStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDayuMigrateStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDayuMigrateStatus',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDayuMigrateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dayu_migrate_status(
        self,
        request: main_models.QueryDayuMigrateStatusRequest,
    ) -> main_models.QueryDayuMigrateStatusResponse:
        runtime = RuntimeOptions()
        return self.query_dayu_migrate_status_with_options(request, runtime)

    async def query_dayu_migrate_status_async(
        self,
        request: main_models.QueryDayuMigrateStatusRequest,
    ) -> main_models.QueryDayuMigrateStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_dayu_migrate_status_with_options_async(request, runtime)

    def query_dict_data_item_with_options(
        self,
        request: main_models.QueryDictDataItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDictDataItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.classify_item_code):
            query['ClassifyItemCode'] = request.classify_item_code
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
            action = 'QueryDictDataItem',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDictDataItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dict_data_item_with_options_async(
        self,
        request: main_models.QueryDictDataItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDictDataItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.classify_item_code):
            query['ClassifyItemCode'] = request.classify_item_code
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
            action = 'QueryDictDataItem',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDictDataItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dict_data_item(
        self,
        request: main_models.QueryDictDataItemRequest,
    ) -> main_models.QueryDictDataItemResponse:
        runtime = RuntimeOptions()
        return self.query_dict_data_item_with_options(request, runtime)

    async def query_dict_data_item_async(
        self,
        request: main_models.QueryDictDataItemRequest,
    ) -> main_models.QueryDictDataItemResponse:
        runtime = RuntimeOptions()
        return await self.query_dict_data_item_with_options_async(request, runtime)

    def query_gate_verify_billing_with_options(
        self,
        request: main_models.QueryGateVerifyBillingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGateVerifyBillingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.month):
            query['Month'] = request.month
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGateVerifyBilling',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGateVerifyBillingResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gate_verify_billing_with_options_async(
        self,
        request: main_models.QueryGateVerifyBillingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGateVerifyBillingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.month):
            query['Month'] = request.month
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGateVerifyBilling',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGateVerifyBillingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gate_verify_billing(
        self,
        request: main_models.QueryGateVerifyBillingRequest,
    ) -> main_models.QueryGateVerifyBillingResponse:
        runtime = RuntimeOptions()
        return self.query_gate_verify_billing_with_options(request, runtime)

    async def query_gate_verify_billing_async(
        self,
        request: main_models.QueryGateVerifyBillingRequest,
    ) -> main_models.QueryGateVerifyBillingResponse:
        runtime = RuntimeOptions()
        return await self.query_gate_verify_billing_with_options_async(request, runtime)

    def query_gate_verify_record_list_with_options(
        self,
        request: main_models.QueryGateVerifyRecordListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGateVerifyRecordListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGateVerifyRecordList',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGateVerifyRecordListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gate_verify_record_list_with_options_async(
        self,
        request: main_models.QueryGateVerifyRecordListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGateVerifyRecordListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGateVerifyRecordList',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGateVerifyRecordListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gate_verify_record_list(
        self,
        request: main_models.QueryGateVerifyRecordListRequest,
    ) -> main_models.QueryGateVerifyRecordListResponse:
        runtime = RuntimeOptions()
        return self.query_gate_verify_record_list_with_options(request, runtime)

    async def query_gate_verify_record_list_async(
        self,
        request: main_models.QueryGateVerifyRecordListRequest,
    ) -> main_models.QueryGateVerifyRecordListResponse:
        runtime = RuntimeOptions()
        return await self.query_gate_verify_record_list_with_options_async(request, runtime)

    def query_gate_verify_statistic_with_options(
        self,
        request: main_models.QueryGateVerifyStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGateVerifyStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGateVerifyStatistic',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGateVerifyStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gate_verify_statistic_with_options_async(
        self,
        request: main_models.QueryGateVerifyStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryGateVerifyStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_type):
            query['AuthenticationType'] = request.authentication_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryGateVerifyStatistic',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryGateVerifyStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gate_verify_statistic(
        self,
        request: main_models.QueryGateVerifyStatisticRequest,
    ) -> main_models.QueryGateVerifyStatisticResponse:
        runtime = RuntimeOptions()
        return self.query_gate_verify_statistic_with_options(request, runtime)

    async def query_gate_verify_statistic_async(
        self,
        request: main_models.QueryGateVerifyStatisticRequest,
    ) -> main_models.QueryGateVerifyStatisticResponse:
        runtime = RuntimeOptions()
        return await self.query_gate_verify_statistic_with_options_async(request, runtime)

    def query_pns_config_with_options(
        self,
        request: main_models.QueryPnsConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPnsConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPnsConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPnsConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pns_config_with_options_async(
        self,
        request: main_models.QueryPnsConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPnsConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPnsConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPnsConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pns_config(
        self,
        request: main_models.QueryPnsConfigRequest,
    ) -> main_models.QueryPnsConfigResponse:
        runtime = RuntimeOptions()
        return self.query_pns_config_with_options(request, runtime)

    async def query_pns_config_async(
        self,
        request: main_models.QueryPnsConfigRequest,
    ) -> main_models.QueryPnsConfigResponse:
        runtime = RuntimeOptions()
        return await self.query_pns_config_with_options_async(request, runtime)

    def query_pns_package_detail_with_options(
        self,
        request: main_models.QueryPnsPackageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPnsPackageDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPnsPackageDetail',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPnsPackageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pns_package_detail_with_options_async(
        self,
        request: main_models.QueryPnsPackageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPnsPackageDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPnsPackageDetail',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPnsPackageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pns_package_detail(
        self,
        request: main_models.QueryPnsPackageDetailRequest,
    ) -> main_models.QueryPnsPackageDetailResponse:
        runtime = RuntimeOptions()
        return self.query_pns_package_detail_with_options(request, runtime)

    async def query_pns_package_detail_async(
        self,
        request: main_models.QueryPnsPackageDetailRequest,
    ) -> main_models.QueryPnsPackageDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_pns_package_detail_with_options_async(request, runtime)

    def query_pns_package_list_with_options(
        self,
        request: main_models.QueryPnsPackageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPnsPackageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPnsPackageList',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPnsPackageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pns_package_list_with_options_async(
        self,
        request: main_models.QueryPnsPackageListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPnsPackageListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPnsPackageList',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPnsPackageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pns_package_list(
        self,
        request: main_models.QueryPnsPackageListRequest,
    ) -> main_models.QueryPnsPackageListResponse:
        runtime = RuntimeOptions()
        return self.query_pns_package_list_with_options(request, runtime)

    async def query_pns_package_list_async(
        self,
        request: main_models.QueryPnsPackageListRequest,
    ) -> main_models.QueryPnsPackageListResponse:
        runtime = RuntimeOptions()
        return await self.query_pns_package_list_with_options_async(request, runtime)

    def query_pns_package_statistics_with_options(
        self,
        request: main_models.QueryPnsPackageStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPnsPackageStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPnsPackageStatistics',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPnsPackageStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pns_package_statistics_with_options_async(
        self,
        request: main_models.QueryPnsPackageStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPnsPackageStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPnsPackageStatistics',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPnsPackageStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pns_package_statistics(
        self,
        request: main_models.QueryPnsPackageStatisticsRequest,
    ) -> main_models.QueryPnsPackageStatisticsResponse:
        runtime = RuntimeOptions()
        return self.query_pns_package_statistics_with_options(request, runtime)

    async def query_pns_package_statistics_async(
        self,
        request: main_models.QueryPnsPackageStatisticsRequest,
    ) -> main_models.QueryPnsPackageStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.query_pns_package_statistics_with_options_async(request, runtime)

    def query_scene_list_with_options(
        self,
        request: main_models.QuerySceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySceneList',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySceneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_scene_list_with_options_async(
        self,
        request: main_models.QuerySceneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySceneListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySceneList',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySceneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_scene_list(
        self,
        request: main_models.QuerySceneListRequest,
    ) -> main_models.QuerySceneListResponse:
        runtime = RuntimeOptions()
        return self.query_scene_list_with_options(request, runtime)

    async def query_scene_list_async(
        self,
        request: main_models.QuerySceneListRequest,
    ) -> main_models.QuerySceneListResponse:
        runtime = RuntimeOptions()
        return await self.query_scene_list_with_options_async(request, runtime)

    def query_sdk_version_with_options(
        self,
        request: main_models.QuerySdkVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySdkVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.customer_id):
            query['customerId'] = request.customer_id
        if not DaraCore.is_null(request.prod_code):
            query['prodCode'] = request.prod_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySdkVersion',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySdkVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sdk_version_with_options_async(
        self,
        request: main_models.QuerySdkVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySdkVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.customer_id):
            query['customerId'] = request.customer_id
        if not DaraCore.is_null(request.prod_code):
            query['prodCode'] = request.prod_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySdkVersion',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySdkVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sdk_version(
        self,
        request: main_models.QuerySdkVersionRequest,
    ) -> main_models.QuerySdkVersionResponse:
        runtime = RuntimeOptions()
        return self.query_sdk_version_with_options(request, runtime)

    async def query_sdk_version_async(
        self,
        request: main_models.QuerySdkVersionRequest,
    ) -> main_models.QuerySdkVersionResponse:
        runtime = RuntimeOptions()
        return await self.query_sdk_version_with_options_async(request, runtime)

    def query_tag_status_with_options(
        self,
        request: main_models.QueryTagStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attr_key):
            query['AttrKey'] = request.attr_key
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagStatus',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_status_with_options_async(
        self,
        request: main_models.QueryTagStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTagStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attr_key):
            query['AttrKey'] = request.attr_key
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTagStatus',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTagStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tag_status(
        self,
        request: main_models.QueryTagStatusRequest,
    ) -> main_models.QueryTagStatusResponse:
        runtime = RuntimeOptions()
        return self.query_tag_status_with_options(request, runtime)

    async def query_tag_status_async(
        self,
        request: main_models.QueryTagStatusRequest,
    ) -> main_models.QueryTagStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_tag_status_with_options_async(request, runtime)

    def remove_gate_verify_export_log_with_options(
        self,
        request: main_models.RemoveGateVerifyExportLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveGateVerifyExportLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
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
            action = 'RemoveGateVerifyExportLog',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveGateVerifyExportLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_gate_verify_export_log_with_options_async(
        self,
        request: main_models.RemoveGateVerifyExportLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveGateVerifyExportLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
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
            action = 'RemoveGateVerifyExportLog',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveGateVerifyExportLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_gate_verify_export_log(
        self,
        request: main_models.RemoveGateVerifyExportLogRequest,
    ) -> main_models.RemoveGateVerifyExportLogResponse:
        runtime = RuntimeOptions()
        return self.remove_gate_verify_export_log_with_options(request, runtime)

    async def remove_gate_verify_export_log_async(
        self,
        request: main_models.RemoveGateVerifyExportLogRequest,
    ) -> main_models.RemoveGateVerifyExportLogResponse:
        runtime = RuntimeOptions()
        return await self.remove_gate_verify_export_log_with_options_async(request, runtime)

    def submit_enterprise_info_with_options(
        self,
        request: main_models.SubmitEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEnterpriseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_license_address):
            query['BusinessLicenseAddress'] = request.business_license_address
        if not DaraCore.is_null(request.business_license_picture):
            query['BusinessLicensePicture'] = request.business_license_picture
        if not DaraCore.is_null(request.enterprise_id):
            query['EnterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.enterprise_name):
            query['EnterpriseName'] = request.enterprise_name
        if not DaraCore.is_null(request.legal_person_cert_number):
            query['LegalPersonCertNumber'] = request.legal_person_cert_number
        if not DaraCore.is_null(request.legal_person_cert_picture):
            query['LegalPersonCertPicture'] = request.legal_person_cert_picture
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.manager_cert_number):
            query['ManagerCertNumber'] = request.manager_cert_number
        if not DaraCore.is_null(request.manager_cert_picture):
            query['ManagerCertPicture'] = request.manager_cert_picture
        if not DaraCore.is_null(request.manager_contact_number):
            query['ManagerContactNumber'] = request.manager_contact_number
        if not DaraCore.is_null(request.manager_name):
            query['ManagerName'] = request.manager_name
        if not DaraCore.is_null(request.number_application_letter_picture):
            query['NumberApplicationLetterPicture'] = request.number_application_letter_picture
        if not DaraCore.is_null(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.undertaking_picture):
            query['UndertakingPicture'] = request.undertaking_picture
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEnterpriseInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEnterpriseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_enterprise_info_with_options_async(
        self,
        request: main_models.SubmitEnterpriseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitEnterpriseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_license_address):
            query['BusinessLicenseAddress'] = request.business_license_address
        if not DaraCore.is_null(request.business_license_picture):
            query['BusinessLicensePicture'] = request.business_license_picture
        if not DaraCore.is_null(request.enterprise_id):
            query['EnterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.enterprise_name):
            query['EnterpriseName'] = request.enterprise_name
        if not DaraCore.is_null(request.legal_person_cert_number):
            query['LegalPersonCertNumber'] = request.legal_person_cert_number
        if not DaraCore.is_null(request.legal_person_cert_picture):
            query['LegalPersonCertPicture'] = request.legal_person_cert_picture
        if not DaraCore.is_null(request.legal_person_name):
            query['LegalPersonName'] = request.legal_person_name
        if not DaraCore.is_null(request.manager_cert_number):
            query['ManagerCertNumber'] = request.manager_cert_number
        if not DaraCore.is_null(request.manager_cert_picture):
            query['ManagerCertPicture'] = request.manager_cert_picture
        if not DaraCore.is_null(request.manager_contact_number):
            query['ManagerContactNumber'] = request.manager_contact_number
        if not DaraCore.is_null(request.manager_name):
            query['ManagerName'] = request.manager_name
        if not DaraCore.is_null(request.number_application_letter_picture):
            query['NumberApplicationLetterPicture'] = request.number_application_letter_picture
        if not DaraCore.is_null(request.organization_code):
            query['OrganizationCode'] = request.organization_code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.undertaking_picture):
            query['UndertakingPicture'] = request.undertaking_picture
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitEnterpriseInfo',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitEnterpriseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_enterprise_info(
        self,
        request: main_models.SubmitEnterpriseInfoRequest,
    ) -> main_models.SubmitEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return self.submit_enterprise_info_with_options(request, runtime)

    async def submit_enterprise_info_async(
        self,
        request: main_models.SubmitEnterpriseInfoRequest,
    ) -> main_models.SubmitEnterpriseInfoResponse:
        runtime = RuntimeOptions()
        return await self.submit_enterprise_info_with_options_async(request, runtime)

    def update_export_log_state_with_options(
        self,
        request: main_models.UpdateExportLogStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExportLogStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExportLogState',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExportLogStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_export_log_state_with_options_async(
        self,
        request: main_models.UpdateExportLogStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExportLogStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExportLogState',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExportLogStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_export_log_state(
        self,
        request: main_models.UpdateExportLogStateRequest,
    ) -> main_models.UpdateExportLogStateResponse:
        runtime = RuntimeOptions()
        return self.update_export_log_state_with_options(request, runtime)

    async def update_export_log_state_async(
        self,
        request: main_models.UpdateExportLogStateRequest,
    ) -> main_models.UpdateExportLogStateResponse:
        runtime = RuntimeOptions()
        return await self.update_export_log_state_with_options_async(request, runtime)

    def update_sms_code_limit_config_with_options(
        self,
        request: main_models.UpdateSmsCodeLimitConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmsCodeLimitConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit_day):
            query['LimitDay'] = request.limit_day
        if not DaraCore.is_null(request.limit_hour):
            query['LimitHour'] = request.limit_hour
        if not DaraCore.is_null(request.limit_id):
            query['LimitId'] = request.limit_id
        if not DaraCore.is_null(request.limit_minute):
            query['LimitMinute'] = request.limit_minute
        if not DaraCore.is_null(request.limit_other):
            query['LimitOther'] = request.limit_other
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
            action = 'UpdateSmsCodeLimitConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmsCodeLimitConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sms_code_limit_config_with_options_async(
        self,
        request: main_models.UpdateSmsCodeLimitConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmsCodeLimitConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.limit_day):
            query['LimitDay'] = request.limit_day
        if not DaraCore.is_null(request.limit_hour):
            query['LimitHour'] = request.limit_hour
        if not DaraCore.is_null(request.limit_id):
            query['LimitId'] = request.limit_id
        if not DaraCore.is_null(request.limit_minute):
            query['LimitMinute'] = request.limit_minute
        if not DaraCore.is_null(request.limit_other):
            query['LimitOther'] = request.limit_other
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
            action = 'UpdateSmsCodeLimitConfig',
            version = '2017-06-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmsCodeLimitConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sms_code_limit_config(
        self,
        request: main_models.UpdateSmsCodeLimitConfigRequest,
    ) -> main_models.UpdateSmsCodeLimitConfigResponse:
        runtime = RuntimeOptions()
        return self.update_sms_code_limit_config_with_options(request, runtime)

    async def update_sms_code_limit_config_async(
        self,
        request: main_models.UpdateSmsCodeLimitConfigRequest,
    ) -> main_models.UpdateSmsCodeLimitConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_sms_code_limit_config_with_options_async(request, runtime)
