# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_holowatcher20200730 import models as holowatcher_20200730_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-hangzhou': 'holowatcher.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('holowatcher', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_user_with_options(
        self,
        request: holowatcher_20200730_models.ActivateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ActivateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ActivateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_user_with_options_async(
        self,
        request: holowatcher_20200730_models.ActivateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ActivateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ActivateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_user(
        self,
        request: holowatcher_20200730_models.ActivateUserRequest,
    ) -> holowatcher_20200730_models.ActivateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_user_with_options(request, runtime)

    async def activate_user_async(
        self,
        request: holowatcher_20200730_models.ActivateUserRequest,
    ) -> holowatcher_20200730_models.ActivateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_user_with_options_async(request, runtime)

    def add_qrcode_with_options(
        self,
        request: holowatcher_20200730_models.AddQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AddQRCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddQRCode',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AddQRCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_qrcode_with_options_async(
        self,
        request: holowatcher_20200730_models.AddQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AddQRCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddQRCode',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AddQRCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_qrcode(
        self,
        request: holowatcher_20200730_models.AddQRCodeRequest,
    ) -> holowatcher_20200730_models.AddQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_qrcode_with_options(request, runtime)

    async def add_qrcode_async(
        self,
        request: holowatcher_20200730_models.AddQRCodeRequest,
    ) -> holowatcher_20200730_models.AddQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_qrcode_with_options_async(request, runtime)

    def aliyun_jwt_create_common_with_options(
        self,
        request: holowatcher_20200730_models.AliyunJwtCreateCommonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunJwtCreateCommonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_account_name):
            query['AliyunAccountName'] = request.aliyun_account_name
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.aliyun_uid_type):
            query['AliyunUidType'] = request.aliyun_uid_type
        if not UtilClient.is_unset(request.parent_uid):
            query['ParentUid'] = request.parent_uid
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunJwtCreateCommon',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunJwtCreateCommonResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_jwt_create_common_with_options_async(
        self,
        request: holowatcher_20200730_models.AliyunJwtCreateCommonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunJwtCreateCommonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_account_name):
            query['AliyunAccountName'] = request.aliyun_account_name
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.aliyun_uid_type):
            query['AliyunUidType'] = request.aliyun_uid_type
        if not UtilClient.is_unset(request.parent_uid):
            query['ParentUid'] = request.parent_uid
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunJwtCreateCommon',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunJwtCreateCommonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_jwt_create_common(
        self,
        request: holowatcher_20200730_models.AliyunJwtCreateCommonRequest,
    ) -> holowatcher_20200730_models.AliyunJwtCreateCommonResponse:
        runtime = util_models.RuntimeOptions()
        return self.aliyun_jwt_create_common_with_options(request, runtime)

    async def aliyun_jwt_create_common_async(
        self,
        request: holowatcher_20200730_models.AliyunJwtCreateCommonRequest,
    ) -> holowatcher_20200730_models.AliyunJwtCreateCommonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.aliyun_jwt_create_common_with_options_async(request, runtime)

    def aliyun_main_jwt_create_with_options(
        self,
        request: holowatcher_20200730_models.AliyunMainJwtCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunMainJwtCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.aliyun_uid_type):
            query['AliyunUidType'] = request.aliyun_uid_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunMainJwtCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunMainJwtCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_main_jwt_create_with_options_async(
        self,
        request: holowatcher_20200730_models.AliyunMainJwtCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunMainJwtCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        if not UtilClient.is_unset(request.aliyun_uid_type):
            query['AliyunUidType'] = request.aliyun_uid_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunMainJwtCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunMainJwtCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_main_jwt_create(
        self,
        request: holowatcher_20200730_models.AliyunMainJwtCreateRequest,
    ) -> holowatcher_20200730_models.AliyunMainJwtCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.aliyun_main_jwt_create_with_options(request, runtime)

    async def aliyun_main_jwt_create_async(
        self,
        request: holowatcher_20200730_models.AliyunMainJwtCreateRequest,
    ) -> holowatcher_20200730_models.AliyunMainJwtCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.aliyun_main_jwt_create_with_options_async(request, runtime)

    def aliyun_ram_jwt_create_with_options(
        self,
        request: holowatcher_20200730_models.AliyunRamJwtCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunRamJwtCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid_type):
            query['AliyunUidType'] = request.aliyun_uid_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_uid):
            query['ParentUid'] = request.parent_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunRamJwtCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunRamJwtCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_ram_jwt_create_with_options_async(
        self,
        request: holowatcher_20200730_models.AliyunRamJwtCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunRamJwtCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid_type):
            query['AliyunUidType'] = request.aliyun_uid_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_uid):
            query['ParentUid'] = request.parent_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunRamJwtCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunRamJwtCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_ram_jwt_create(
        self,
        request: holowatcher_20200730_models.AliyunRamJwtCreateRequest,
    ) -> holowatcher_20200730_models.AliyunRamJwtCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.aliyun_ram_jwt_create_with_options(request, runtime)

    async def aliyun_ram_jwt_create_async(
        self,
        request: holowatcher_20200730_models.AliyunRamJwtCreateRequest,
    ) -> holowatcher_20200730_models.AliyunRamJwtCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.aliyun_ram_jwt_create_with_options_async(request, runtime)

    def aliyun_ticket_jwt_create_with_options(
        self,
        request: holowatcher_20200730_models.AliyunTicketJwtCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunTicketJwtCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunTicketJwtCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunTicketJwtCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_ticket_jwt_create_with_options_async(
        self,
        request: holowatcher_20200730_models.AliyunTicketJwtCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunTicketJwtCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunTicketJwtCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunTicketJwtCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_ticket_jwt_create(
        self,
        request: holowatcher_20200730_models.AliyunTicketJwtCreateRequest,
    ) -> holowatcher_20200730_models.AliyunTicketJwtCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.aliyun_ticket_jwt_create_with_options(request, runtime)

    async def aliyun_ticket_jwt_create_async(
        self,
        request: holowatcher_20200730_models.AliyunTicketJwtCreateRequest,
    ) -> holowatcher_20200730_models.AliyunTicketJwtCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.aliyun_ticket_jwt_create_with_options_async(request, runtime)

    def aliyun_uid_white_list_with_options(
        self,
        request: holowatcher_20200730_models.AliyunUidWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunUidWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunUidWhiteList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunUidWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_uid_white_list_with_options_async(
        self,
        request: holowatcher_20200730_models.AliyunUidWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.AliyunUidWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AliyunUidWhiteList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.AliyunUidWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_uid_white_list(
        self,
        request: holowatcher_20200730_models.AliyunUidWhiteListRequest,
    ) -> holowatcher_20200730_models.AliyunUidWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.aliyun_uid_white_list_with_options(request, runtime)

    async def aliyun_uid_white_list_async(
        self,
        request: holowatcher_20200730_models.AliyunUidWhiteListRequest,
    ) -> holowatcher_20200730_models.AliyunUidWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.aliyun_uid_white_list_with_options_async(request, runtime)

    def bim_build_model_with_options(
        self,
        request: holowatcher_20200730_models.BimBuildModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimBuildModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimBuildModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimBuildModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_build_model_with_options_async(
        self,
        request: holowatcher_20200730_models.BimBuildModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimBuildModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimBuildModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimBuildModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_build_model(
        self,
        request: holowatcher_20200730_models.BimBuildModelRequest,
    ) -> holowatcher_20200730_models.BimBuildModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_build_model_with_options(request, runtime)

    async def bim_build_model_async(
        self,
        request: holowatcher_20200730_models.BimBuildModelRequest,
    ) -> holowatcher_20200730_models.BimBuildModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_build_model_with_options_async(request, runtime)

    def bim_get_sts_token_with_options(
        self,
        request: holowatcher_20200730_models.BimGetStsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimGetStsTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimGetStsToken',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimGetStsTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_get_sts_token_with_options_async(
        self,
        request: holowatcher_20200730_models.BimGetStsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimGetStsTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimGetStsToken',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimGetStsTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_get_sts_token(
        self,
        request: holowatcher_20200730_models.BimGetStsTokenRequest,
    ) -> holowatcher_20200730_models.BimGetStsTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_get_sts_token_with_options(request, runtime)

    async def bim_get_sts_token_async(
        self,
        request: holowatcher_20200730_models.BimGetStsTokenRequest,
    ) -> holowatcher_20200730_models.BimGetStsTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_get_sts_token_with_options_async(request, runtime)

    def bim_pre_step_with_options(
        self,
        request: holowatcher_20200730_models.BimPreStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimPreStepResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimPreStep',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimPreStepResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_pre_step_with_options_async(
        self,
        request: holowatcher_20200730_models.BimPreStepRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimPreStepResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimPreStep',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimPreStepResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_pre_step(
        self,
        request: holowatcher_20200730_models.BimPreStepRequest,
    ) -> holowatcher_20200730_models.BimPreStepResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_pre_step_with_options(request, runtime)

    async def bim_pre_step_async(
        self,
        request: holowatcher_20200730_models.BimPreStepRequest,
    ) -> holowatcher_20200730_models.BimPreStepResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_pre_step_with_options_async(request, runtime)

    def bim_pro_again_build_mode_with_options(
        self,
        request: holowatcher_20200730_models.BimProAgainBuildModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimProAgainBuildModeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimProAgainBuildMode',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimProAgainBuildModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_pro_again_build_mode_with_options_async(
        self,
        request: holowatcher_20200730_models.BimProAgainBuildModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimProAgainBuildModeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimProAgainBuildMode',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimProAgainBuildModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_pro_again_build_mode(
        self,
        request: holowatcher_20200730_models.BimProAgainBuildModeRequest,
    ) -> holowatcher_20200730_models.BimProAgainBuildModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_pro_again_build_mode_with_options(request, runtime)

    async def bim_pro_again_build_mode_async(
        self,
        request: holowatcher_20200730_models.BimProAgainBuildModeRequest,
    ) -> holowatcher_20200730_models.BimProAgainBuildModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_pro_again_build_mode_with_options_async(request, runtime)

    def bim_project_delete_file_with_options(
        self,
        request: holowatcher_20200730_models.BimProjectDeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimProjectDeleteFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimProjectDeleteFile',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimProjectDeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_project_delete_file_with_options_async(
        self,
        request: holowatcher_20200730_models.BimProjectDeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimProjectDeleteFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimProjectDeleteFile',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimProjectDeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_project_delete_file(
        self,
        request: holowatcher_20200730_models.BimProjectDeleteFileRequest,
    ) -> holowatcher_20200730_models.BimProjectDeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_project_delete_file_with_options(request, runtime)

    async def bim_project_delete_file_async(
        self,
        request: holowatcher_20200730_models.BimProjectDeleteFileRequest,
    ) -> holowatcher_20200730_models.BimProjectDeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_project_delete_file_with_options_async(request, runtime)

    def bim_project_share_model_with_options(
        self,
        request: holowatcher_20200730_models.BimProjectShareModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimProjectShareModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimProjectShareModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimProjectShareModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_project_share_model_with_options_async(
        self,
        request: holowatcher_20200730_models.BimProjectShareModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimProjectShareModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimProjectShareModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimProjectShareModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_project_share_model(
        self,
        request: holowatcher_20200730_models.BimProjectShareModelRequest,
    ) -> holowatcher_20200730_models.BimProjectShareModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_project_share_model_with_options(request, runtime)

    async def bim_project_share_model_async(
        self,
        request: holowatcher_20200730_models.BimProjectShareModelRequest,
    ) -> holowatcher_20200730_models.BimProjectShareModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_project_share_model_with_options_async(request, runtime)

    def bim_retry_trans_with_options(
        self,
        request: holowatcher_20200730_models.BimRetryTransRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimRetryTransResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimRetryTrans',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimRetryTransResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_retry_trans_with_options_async(
        self,
        request: holowatcher_20200730_models.BimRetryTransRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimRetryTransResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimRetryTrans',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimRetryTransResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_retry_trans(
        self,
        request: holowatcher_20200730_models.BimRetryTransRequest,
    ) -> holowatcher_20200730_models.BimRetryTransResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_retry_trans_with_options(request, runtime)

    async def bim_retry_trans_async(
        self,
        request: holowatcher_20200730_models.BimRetryTransRequest,
    ) -> holowatcher_20200730_models.BimRetryTransResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_retry_trans_with_options_async(request, runtime)

    def bim_standard_auto_salb_info_with_options(
        self,
        request: holowatcher_20200730_models.BimStandardAutoSalbInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimStandardAutoSalbInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimStandardAutoSalbInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimStandardAutoSalbInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_standard_auto_salb_info_with_options_async(
        self,
        request: holowatcher_20200730_models.BimStandardAutoSalbInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimStandardAutoSalbInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimStandardAutoSalbInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimStandardAutoSalbInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_standard_auto_salb_info(
        self,
        request: holowatcher_20200730_models.BimStandardAutoSalbInfoRequest,
    ) -> holowatcher_20200730_models.BimStandardAutoSalbInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_standard_auto_salb_info_with_options(request, runtime)

    async def bim_standard_auto_salb_info_async(
        self,
        request: holowatcher_20200730_models.BimStandardAutoSalbInfoRequest,
    ) -> holowatcher_20200730_models.BimStandardAutoSalbInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_standard_auto_salb_info_with_options_async(request, runtime)

    def bim_standard_detail_with_options(
        self,
        request: holowatcher_20200730_models.BimStandardDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimStandardDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimStandardDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimStandardDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_standard_detail_with_options_async(
        self,
        request: holowatcher_20200730_models.BimStandardDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimStandardDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimStandardDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimStandardDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_standard_detail(
        self,
        request: holowatcher_20200730_models.BimStandardDetailRequest,
    ) -> holowatcher_20200730_models.BimStandardDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_standard_detail_with_options(request, runtime)

    async def bim_standard_detail_async(
        self,
        request: holowatcher_20200730_models.BimStandardDetailRequest,
    ) -> holowatcher_20200730_models.BimStandardDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_standard_detail_with_options_async(request, runtime)

    def bim_standard_elevation_with_options(
        self,
        request: holowatcher_20200730_models.BimStandardElevationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimStandardElevationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimStandardElevation',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimStandardElevationResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_standard_elevation_with_options_async(
        self,
        request: holowatcher_20200730_models.BimStandardElevationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimStandardElevationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimStandardElevation',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimStandardElevationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_standard_elevation(
        self,
        request: holowatcher_20200730_models.BimStandardElevationRequest,
    ) -> holowatcher_20200730_models.BimStandardElevationResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_standard_elevation_with_options(request, runtime)

    async def bim_standard_elevation_async(
        self,
        request: holowatcher_20200730_models.BimStandardElevationRequest,
    ) -> holowatcher_20200730_models.BimStandardElevationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_standard_elevation_with_options_async(request, runtime)

    def bim_trans_model_with_options(
        self,
        request: holowatcher_20200730_models.BimTransModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimTransModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimTransModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimTransModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_trans_model_with_options_async(
        self,
        request: holowatcher_20200730_models.BimTransModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimTransModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimTransModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimTransModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_trans_model(
        self,
        request: holowatcher_20200730_models.BimTransModelRequest,
    ) -> holowatcher_20200730_models.BimTransModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_trans_model_with_options(request, runtime)

    async def bim_trans_model_async(
        self,
        request: holowatcher_20200730_models.BimTransModelRequest,
    ) -> holowatcher_20200730_models.BimTransModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_trans_model_with_options_async(request, runtime)

    def bim_trans_model_status_with_options(
        self,
        tmp_req: holowatcher_20200730_models.BimTransModelStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimTransModelStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.BimTransModelStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimTransModelStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimTransModelStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_trans_model_status_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.BimTransModelStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimTransModelStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.BimTransModelStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimTransModelStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimTransModelStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_trans_model_status(
        self,
        request: holowatcher_20200730_models.BimTransModelStatusRequest,
    ) -> holowatcher_20200730_models.BimTransModelStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_trans_model_status_with_options(request, runtime)

    async def bim_trans_model_status_async(
        self,
        request: holowatcher_20200730_models.BimTransModelStatusRequest,
    ) -> holowatcher_20200730_models.BimTransModelStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_trans_model_status_with_options_async(request, runtime)

    def bim_update_project_with_options(
        self,
        tmp_req: holowatcher_20200730_models.BimUpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimUpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.BimUpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component):
            request.component_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component, 'Component', 'json')
        query = {}
        if not UtilClient.is_unset(request.component_shrink):
            query['Component'] = request.component_shrink
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            query['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimUpdateProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimUpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def bim_update_project_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.BimUpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.BimUpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.BimUpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component):
            request.component_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component, 'Component', 'json')
        query = {}
        if not UtilClient.is_unset(request.component_shrink):
            query['Component'] = request.component_shrink
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            query['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BimUpdateProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.BimUpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bim_update_project(
        self,
        request: holowatcher_20200730_models.BimUpdateProjectRequest,
    ) -> holowatcher_20200730_models.BimUpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.bim_update_project_with_options(request, runtime)

    async def bim_update_project_async(
        self,
        request: holowatcher_20200730_models.BimUpdateProjectRequest,
    ) -> holowatcher_20200730_models.BimUpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bim_update_project_with_options_async(request, runtime)

    def check_image_with_options(
        self,
        request: holowatcher_20200730_models.CheckImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CheckImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_path):
            query['ImagePath'] = request.image_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckImage',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CheckImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_image_with_options_async(
        self,
        request: holowatcher_20200730_models.CheckImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CheckImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_path):
            query['ImagePath'] = request.image_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckImage',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CheckImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_image(
        self,
        request: holowatcher_20200730_models.CheckImageRequest,
    ) -> holowatcher_20200730_models.CheckImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_image_with_options(request, runtime)

    async def check_image_async(
        self,
        request: holowatcher_20200730_models.CheckImageRequest,
    ) -> holowatcher_20200730_models.CheckImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_image_with_options_async(request, runtime)

    def common_request_with_options(
        self,
        request: holowatcher_20200730_models.CommonRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CommonRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommonRequest',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CommonRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def common_request_with_options_async(
        self,
        request: holowatcher_20200730_models.CommonRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CommonRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api):
            query['Api'] = request.api
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommonRequest',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CommonRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def common_request(
        self,
        request: holowatcher_20200730_models.CommonRequestRequest,
    ) -> holowatcher_20200730_models.CommonRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.common_request_with_options(request, runtime)

    async def common_request_async(
        self,
        request: holowatcher_20200730_models.CommonRequestRequest,
    ) -> holowatcher_20200730_models.CommonRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.common_request_with_options_async(request, runtime)

    def company_activate_one_with_options(
        self,
        request: holowatcher_20200730_models.CompanyActivateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyActivateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyActivateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyActivateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_activate_one_with_options_async(
        self,
        request: holowatcher_20200730_models.CompanyActivateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyActivateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyActivateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyActivateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_activate_one(
        self,
        request: holowatcher_20200730_models.CompanyActivateOneRequest,
    ) -> holowatcher_20200730_models.CompanyActivateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.company_activate_one_with_options(request, runtime)

    async def company_activate_one_async(
        self,
        request: holowatcher_20200730_models.CompanyActivateOneRequest,
    ) -> holowatcher_20200730_models.CompanyActivateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.company_activate_one_with_options_async(request, runtime)

    def company_and_main_user_create_with_options(
        self,
        request: holowatcher_20200730_models.CompanyAndMainUserCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyAndMainUserCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.company_params):
            query['CompanyParams'] = request.company_params
        if not UtilClient.is_unset(request.user_params):
            query['UserParams'] = request.user_params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyAndMainUserCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyAndMainUserCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_and_main_user_create_with_options_async(
        self,
        request: holowatcher_20200730_models.CompanyAndMainUserCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyAndMainUserCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.company_params):
            query['CompanyParams'] = request.company_params
        if not UtilClient.is_unset(request.user_params):
            query['UserParams'] = request.user_params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyAndMainUserCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyAndMainUserCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_and_main_user_create(
        self,
        request: holowatcher_20200730_models.CompanyAndMainUserCreateRequest,
    ) -> holowatcher_20200730_models.CompanyAndMainUserCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.company_and_main_user_create_with_options(request, runtime)

    async def company_and_main_user_create_async(
        self,
        request: holowatcher_20200730_models.CompanyAndMainUserCreateRequest,
    ) -> holowatcher_20200730_models.CompanyAndMainUserCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.company_and_main_user_create_with_options_async(request, runtime)

    def company_create_one_with_options(
        self,
        request: holowatcher_20200730_models.CompanyCreateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyCreateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyCreateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyCreateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_create_one_with_options_async(
        self,
        request: holowatcher_20200730_models.CompanyCreateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyCreateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyCreateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyCreateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_create_one(
        self,
        request: holowatcher_20200730_models.CompanyCreateOneRequest,
    ) -> holowatcher_20200730_models.CompanyCreateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.company_create_one_with_options(request, runtime)

    async def company_create_one_async(
        self,
        request: holowatcher_20200730_models.CompanyCreateOneRequest,
    ) -> holowatcher_20200730_models.CompanyCreateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.company_create_one_with_options_async(request, runtime)

    def company_disable_one_with_options(
        self,
        request: holowatcher_20200730_models.CompanyDisableOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyDisableOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyDisableOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyDisableOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_disable_one_with_options_async(
        self,
        request: holowatcher_20200730_models.CompanyDisableOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyDisableOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyDisableOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyDisableOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_disable_one(
        self,
        request: holowatcher_20200730_models.CompanyDisableOneRequest,
    ) -> holowatcher_20200730_models.CompanyDisableOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.company_disable_one_with_options(request, runtime)

    async def company_disable_one_async(
        self,
        request: holowatcher_20200730_models.CompanyDisableOneRequest,
    ) -> holowatcher_20200730_models.CompanyDisableOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.company_disable_one_with_options_async(request, runtime)

    def company_find_all_with_options(
        self,
        request: holowatcher_20200730_models.CompanyFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyFindAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_find_all_with_options_async(
        self,
        request: holowatcher_20200730_models.CompanyFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyFindAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_find_all(
        self,
        request: holowatcher_20200730_models.CompanyFindAllRequest,
    ) -> holowatcher_20200730_models.CompanyFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.company_find_all_with_options(request, runtime)

    async def company_find_all_async(
        self,
        request: holowatcher_20200730_models.CompanyFindAllRequest,
    ) -> holowatcher_20200730_models.CompanyFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.company_find_all_with_options_async(request, runtime)

    def company_find_by_isv_type_with_options(
        self,
        request: holowatcher_20200730_models.CompanyFindByIsvTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyFindByIsvTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.isv_type):
            query['IsvType'] = request.isv_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyFindByIsvType',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyFindByIsvTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_find_by_isv_type_with_options_async(
        self,
        request: holowatcher_20200730_models.CompanyFindByIsvTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyFindByIsvTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.isv_type):
            query['IsvType'] = request.isv_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyFindByIsvType',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyFindByIsvTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_find_by_isv_type(
        self,
        request: holowatcher_20200730_models.CompanyFindByIsvTypeRequest,
    ) -> holowatcher_20200730_models.CompanyFindByIsvTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.company_find_by_isv_type_with_options(request, runtime)

    async def company_find_by_isv_type_async(
        self,
        request: holowatcher_20200730_models.CompanyFindByIsvTypeRequest,
    ) -> holowatcher_20200730_models.CompanyFindByIsvTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.company_find_by_isv_type_with_options_async(request, runtime)

    def company_find_one_with_options(
        self,
        request: holowatcher_20200730_models.CompanyFindOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyFindOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.company_id):
            query['CompanyId'] = request.company_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyFindOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyFindOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_find_one_with_options_async(
        self,
        request: holowatcher_20200730_models.CompanyFindOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyFindOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.company_id):
            query['CompanyId'] = request.company_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyFindOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyFindOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_find_one(
        self,
        request: holowatcher_20200730_models.CompanyFindOneRequest,
    ) -> holowatcher_20200730_models.CompanyFindOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.company_find_one_with_options(request, runtime)

    async def company_find_one_async(
        self,
        request: holowatcher_20200730_models.CompanyFindOneRequest,
    ) -> holowatcher_20200730_models.CompanyFindOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.company_find_one_with_options_async(request, runtime)

    def company_list_by_condition_with_options(
        self,
        request: holowatcher_20200730_models.CompanyListByConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyListByConditionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.custom_see_self):
            query['CustomSeeSelf'] = request.custom_see_self
        if not UtilClient.is_unset(request.isv_type):
            query['IsvType'] = request.isv_type
        if not UtilClient.is_unset(request.support_type):
            query['SupportType'] = request.support_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyListByCondition',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyListByConditionResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_list_by_condition_with_options_async(
        self,
        request: holowatcher_20200730_models.CompanyListByConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyListByConditionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.custom_see_self):
            query['CustomSeeSelf'] = request.custom_see_self
        if not UtilClient.is_unset(request.isv_type):
            query['IsvType'] = request.isv_type
        if not UtilClient.is_unset(request.support_type):
            query['SupportType'] = request.support_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyListByCondition',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyListByConditionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_list_by_condition(
        self,
        request: holowatcher_20200730_models.CompanyListByConditionRequest,
    ) -> holowatcher_20200730_models.CompanyListByConditionResponse:
        runtime = util_models.RuntimeOptions()
        return self.company_list_by_condition_with_options(request, runtime)

    async def company_list_by_condition_async(
        self,
        request: holowatcher_20200730_models.CompanyListByConditionRequest,
    ) -> holowatcher_20200730_models.CompanyListByConditionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.company_list_by_condition_with_options_async(request, runtime)

    def company_update_one_with_options(
        self,
        request: holowatcher_20200730_models.CompanyUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyUpdateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def company_update_one_with_options_async(
        self,
        request: holowatcher_20200730_models.CompanyUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CompanyUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompanyUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CompanyUpdateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def company_update_one(
        self,
        request: holowatcher_20200730_models.CompanyUpdateOneRequest,
    ) -> holowatcher_20200730_models.CompanyUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.company_update_one_with_options(request, runtime)

    async def company_update_one_async(
        self,
        request: holowatcher_20200730_models.CompanyUpdateOneRequest,
    ) -> holowatcher_20200730_models.CompanyUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.company_update_one_with_options_async(request, runtime)

    def create_bim_project_with_options(
        self,
        tmp_req: holowatcher_20200730_models.CreateBimProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateBimProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.CreateBimProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component):
            request.component_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component, 'Component', 'json')
        query = {}
        if not UtilClient.is_unset(request.component_shrink):
            query['Component'] = request.component_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            query['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBimProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateBimProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_bim_project_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.CreateBimProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateBimProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.CreateBimProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component):
            request.component_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component, 'Component', 'json')
        query = {}
        if not UtilClient.is_unset(request.component_shrink):
            query['Component'] = request.component_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            query['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBimProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateBimProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_bim_project(
        self,
        request: holowatcher_20200730_models.CreateBimProjectRequest,
    ) -> holowatcher_20200730_models.CreateBimProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_bim_project_with_options(request, runtime)

    async def create_bim_project_async(
        self,
        request: holowatcher_20200730_models.CreateBimProjectRequest,
    ) -> holowatcher_20200730_models.CreateBimProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_bim_project_with_options_async(request, runtime)

    def create_main_user_with_options(
        self,
        request: holowatcher_20200730_models.CreateMainUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateMainUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMainUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateMainUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_main_user_with_options_async(
        self,
        request: holowatcher_20200730_models.CreateMainUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateMainUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMainUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateMainUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_main_user(
        self,
        request: holowatcher_20200730_models.CreateMainUserRequest,
    ) -> holowatcher_20200730_models.CreateMainUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_main_user_with_options(request, runtime)

    async def create_main_user_async(
        self,
        request: holowatcher_20200730_models.CreateMainUserRequest,
    ) -> holowatcher_20200730_models.CreateMainUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_main_user_with_options_async(request, runtime)

    def create_material_with_options(
        self,
        request: holowatcher_20200730_models.CreateMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateMaterialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMaterial',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_material_with_options_async(
        self,
        request: holowatcher_20200730_models.CreateMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateMaterialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMaterial',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_material(
        self,
        request: holowatcher_20200730_models.CreateMaterialRequest,
    ) -> holowatcher_20200730_models.CreateMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_material_with_options(request, runtime)

    async def create_material_async(
        self,
        request: holowatcher_20200730_models.CreateMaterialRequest,
    ) -> holowatcher_20200730_models.CreateMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_material_with_options_async(request, runtime)

    def create_or_update_ext_info_with_options(
        self,
        request: holowatcher_20200730_models.CreateOrUpdateExtInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateOrUpdateExtInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateExtInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateOrUpdateExtInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_ext_info_with_options_async(
        self,
        request: holowatcher_20200730_models.CreateOrUpdateExtInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateOrUpdateExtInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateExtInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateOrUpdateExtInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_ext_info(
        self,
        request: holowatcher_20200730_models.CreateOrUpdateExtInfoRequest,
    ) -> holowatcher_20200730_models.CreateOrUpdateExtInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_ext_info_with_options(request, runtime)

    async def create_or_update_ext_info_async(
        self,
        request: holowatcher_20200730_models.CreateOrUpdateExtInfoRequest,
    ) -> holowatcher_20200730_models.CreateOrUpdateExtInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_ext_info_with_options_async(request, runtime)

    def create_pipeline_node_instance_with_options(
        self,
        request: holowatcher_20200730_models.CreatePipelineNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreatePipelineNodeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipelineNodeInstance',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreatePipelineNodeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_node_instance_with_options_async(
        self,
        request: holowatcher_20200730_models.CreatePipelineNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreatePipelineNodeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipelineNodeInstance',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreatePipelineNodeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_node_instance(
        self,
        request: holowatcher_20200730_models.CreatePipelineNodeInstanceRequest,
    ) -> holowatcher_20200730_models.CreatePipelineNodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pipeline_node_instance_with_options(request, runtime)

    async def create_pipeline_node_instance_async(
        self,
        request: holowatcher_20200730_models.CreatePipelineNodeInstanceRequest,
    ) -> holowatcher_20200730_models.CreatePipelineNodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pipeline_node_instance_with_options_async(request, runtime)

    def create_ram_user_with_options(
        self,
        request: holowatcher_20200730_models.CreateRamUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateRamUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRamUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateRamUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ram_user_with_options_async(
        self,
        request: holowatcher_20200730_models.CreateRamUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CreateRamUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRamUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CreateRamUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ram_user(
        self,
        request: holowatcher_20200730_models.CreateRamUserRequest,
    ) -> holowatcher_20200730_models.CreateRamUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ram_user_with_options(request, runtime)

    async def create_ram_user_async(
        self,
        request: holowatcher_20200730_models.CreateRamUserRequest,
    ) -> holowatcher_20200730_models.CreateRamUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ram_user_with_options_async(request, runtime)

    def custom_create_order_with_options(
        self,
        request: holowatcher_20200730_models.CustomCreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CustomCreateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_type):
            query['ItemType'] = request.item_type
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_photo_contact):
            query['OrderPhotoContact'] = request.order_photo_contact
        if not UtilClient.is_unset(request.photo_address):
            query['PhotoAddress'] = request.photo_address
        if not UtilClient.is_unset(request.photo_environment):
            query['PhotoEnvironment'] = request.photo_environment
        if not UtilClient.is_unset(request.photo_floor_num):
            query['PhotoFloorNum'] = request.photo_floor_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CustomCreateOrder',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CustomCreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def custom_create_order_with_options_async(
        self,
        request: holowatcher_20200730_models.CustomCreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CustomCreateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_type):
            query['ItemType'] = request.item_type
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_photo_contact):
            query['OrderPhotoContact'] = request.order_photo_contact
        if not UtilClient.is_unset(request.photo_address):
            query['PhotoAddress'] = request.photo_address
        if not UtilClient.is_unset(request.photo_environment):
            query['PhotoEnvironment'] = request.photo_environment
        if not UtilClient.is_unset(request.photo_floor_num):
            query['PhotoFloorNum'] = request.photo_floor_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CustomCreateOrder',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CustomCreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def custom_create_order(
        self,
        request: holowatcher_20200730_models.CustomCreateOrderRequest,
    ) -> holowatcher_20200730_models.CustomCreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.custom_create_order_with_options(request, runtime)

    async def custom_create_order_async(
        self,
        request: holowatcher_20200730_models.CustomCreateOrderRequest,
    ) -> holowatcher_20200730_models.CustomCreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.custom_create_order_with_options_async(request, runtime)

    def custom_find_order_with_options(
        self,
        request: holowatcher_20200730_models.CustomFindOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CustomFindOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id_cipher):
            query['OrderIdCipher'] = request.order_id_cipher
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_state):
            query['OrderState'] = request.order_state
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CustomFindOrder',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CustomFindOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def custom_find_order_with_options_async(
        self,
        request: holowatcher_20200730_models.CustomFindOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CustomFindOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id_cipher):
            query['OrderIdCipher'] = request.order_id_cipher
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_state):
            query['OrderState'] = request.order_state
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CustomFindOrder',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CustomFindOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def custom_find_order(
        self,
        request: holowatcher_20200730_models.CustomFindOrderRequest,
    ) -> holowatcher_20200730_models.CustomFindOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.custom_find_order_with_options(request, runtime)

    async def custom_find_order_async(
        self,
        request: holowatcher_20200730_models.CustomFindOrderRequest,
    ) -> holowatcher_20200730_models.CustomFindOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.custom_find_order_with_options_async(request, runtime)

    def custom_find_order_status_with_options(
        self,
        request: holowatcher_20200730_models.CustomFindOrderStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CustomFindOrderStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id_cipher):
            query['OrderIdCipher'] = request.order_id_cipher
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CustomFindOrderStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CustomFindOrderStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def custom_find_order_status_with_options_async(
        self,
        request: holowatcher_20200730_models.CustomFindOrderStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CustomFindOrderStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id_cipher):
            query['OrderIdCipher'] = request.order_id_cipher
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CustomFindOrderStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CustomFindOrderStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def custom_find_order_status(
        self,
        request: holowatcher_20200730_models.CustomFindOrderStatusRequest,
    ) -> holowatcher_20200730_models.CustomFindOrderStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.custom_find_order_status_with_options(request, runtime)

    async def custom_find_order_status_async(
        self,
        request: holowatcher_20200730_models.CustomFindOrderStatusRequest,
    ) -> holowatcher_20200730_models.CustomFindOrderStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.custom_find_order_status_with_options_async(request, runtime)

    def custom_get_cdn_model_path_with_options(
        self,
        request: holowatcher_20200730_models.CustomGetCdnModelPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CustomGetCdnModelPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id_cipher):
            query['OrderIdCipher'] = request.order_id_cipher
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CustomGetCdnModelPath',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CustomGetCdnModelPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def custom_get_cdn_model_path_with_options_async(
        self,
        request: holowatcher_20200730_models.CustomGetCdnModelPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.CustomGetCdnModelPathResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id_cipher):
            query['OrderIdCipher'] = request.order_id_cipher
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CustomGetCdnModelPath',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.CustomGetCdnModelPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def custom_get_cdn_model_path(
        self,
        request: holowatcher_20200730_models.CustomGetCdnModelPathRequest,
    ) -> holowatcher_20200730_models.CustomGetCdnModelPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.custom_get_cdn_model_path_with_options(request, runtime)

    async def custom_get_cdn_model_path_async(
        self,
        request: holowatcher_20200730_models.CustomGetCdnModelPathRequest,
    ) -> holowatcher_20200730_models.CustomGetCdnModelPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.custom_get_cdn_model_path_with_options_async(request, runtime)

    def data_store_credential_with_options(
        self,
        request: holowatcher_20200730_models.DataStoreCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DataStoreCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DataStoreCredential',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DataStoreCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def data_store_credential_with_options_async(
        self,
        request: holowatcher_20200730_models.DataStoreCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DataStoreCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DataStoreCredential',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DataStoreCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def data_store_credential(
        self,
        request: holowatcher_20200730_models.DataStoreCredentialRequest,
    ) -> holowatcher_20200730_models.DataStoreCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.data_store_credential_with_options(request, runtime)

    async def data_store_credential_async(
        self,
        request: holowatcher_20200730_models.DataStoreCredentialRequest,
    ) -> holowatcher_20200730_models.DataStoreCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.data_store_credential_with_options_async(request, runtime)

    def dataset_config_find_all_with_options(
        self,
        request: holowatcher_20200730_models.DatasetConfigFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetConfigFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetConfigFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetConfigFindAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_config_find_all_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetConfigFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetConfigFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetConfigFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetConfigFindAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_config_find_all(
        self,
        request: holowatcher_20200730_models.DatasetConfigFindAllRequest,
    ) -> holowatcher_20200730_models.DatasetConfigFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_config_find_all_with_options(request, runtime)

    async def dataset_config_find_all_async(
        self,
        request: holowatcher_20200730_models.DatasetConfigFindAllRequest,
    ) -> holowatcher_20200730_models.DatasetConfigFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_config_find_all_with_options_async(request, runtime)

    def dataset_config_find_one_with_options(
        self,
        request: holowatcher_20200730_models.DatasetConfigFindOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetConfigFindOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetConfigFindOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetConfigFindOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_config_find_one_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetConfigFindOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetConfigFindOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetConfigFindOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetConfigFindOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_config_find_one(
        self,
        request: holowatcher_20200730_models.DatasetConfigFindOneRequest,
    ) -> holowatcher_20200730_models.DatasetConfigFindOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_config_find_one_with_options(request, runtime)

    async def dataset_config_find_one_async(
        self,
        request: holowatcher_20200730_models.DatasetConfigFindOneRequest,
    ) -> holowatcher_20200730_models.DatasetConfigFindOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_config_find_one_with_options_async(request, runtime)

    def dataset_config_update_one_with_options(
        self,
        request: holowatcher_20200730_models.DatasetConfigUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetConfigUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetConfigUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetConfigUpdateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_config_update_one_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetConfigUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetConfigUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetConfigUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetConfigUpdateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_config_update_one(
        self,
        request: holowatcher_20200730_models.DatasetConfigUpdateOneRequest,
    ) -> holowatcher_20200730_models.DatasetConfigUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_config_update_one_with_options(request, runtime)

    async def dataset_config_update_one_async(
        self,
        request: holowatcher_20200730_models.DatasetConfigUpdateOneRequest,
    ) -> holowatcher_20200730_models.DatasetConfigUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_config_update_one_with_options_async(request, runtime)

    def dataset_create_one_with_options(
        self,
        request: holowatcher_20200730_models.DatasetCreateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetCreateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetCreateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetCreateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_create_one_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetCreateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetCreateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetCreateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetCreateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_create_one(
        self,
        request: holowatcher_20200730_models.DatasetCreateOneRequest,
    ) -> holowatcher_20200730_models.DatasetCreateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_create_one_with_options(request, runtime)

    async def dataset_create_one_async(
        self,
        request: holowatcher_20200730_models.DatasetCreateOneRequest,
    ) -> holowatcher_20200730_models.DatasetCreateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_create_one_with_options_async(request, runtime)

    def dataset_detele_one_with_options(
        self,
        request: holowatcher_20200730_models.DatasetDeteleOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetDeteleOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DatasetDeteleOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetDeteleOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_detele_one_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetDeteleOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetDeteleOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DatasetDeteleOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetDeteleOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_detele_one(
        self,
        request: holowatcher_20200730_models.DatasetDeteleOneRequest,
    ) -> holowatcher_20200730_models.DatasetDeteleOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_detele_one_with_options(request, runtime)

    async def dataset_detele_one_async(
        self,
        request: holowatcher_20200730_models.DatasetDeteleOneRequest,
    ) -> holowatcher_20200730_models.DatasetDeteleOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_detele_one_with_options_async(request, runtime)

    def dataset_find_all_with_options(
        self,
        request: holowatcher_20200730_models.DatasetFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.no_project):
            query['NoProject'] = request.no_project
        if not UtilClient.is_unset(request.not_project_id):
            query['NotProjectId'] = request.not_project_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetFindAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_find_all_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.no_project):
            query['NoProject'] = request.no_project
        if not UtilClient.is_unset(request.not_project_id):
            query['NotProjectId'] = request.not_project_id
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetFindAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_find_all(
        self,
        request: holowatcher_20200730_models.DatasetFindAllRequest,
    ) -> holowatcher_20200730_models.DatasetFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_find_all_with_options(request, runtime)

    async def dataset_find_all_async(
        self,
        request: holowatcher_20200730_models.DatasetFindAllRequest,
    ) -> holowatcher_20200730_models.DatasetFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_find_all_with_options_async(request, runtime)

    def dataset_publish_publish_with_options(
        self,
        request: holowatcher_20200730_models.DatasetPublishPublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetPublishPublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.overwrite_latest):
            query['OverwriteLatest'] = request.overwrite_latest
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetPublishPublish',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetPublishPublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_publish_publish_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetPublishPublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetPublishPublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.overwrite_latest):
            query['OverwriteLatest'] = request.overwrite_latest
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetPublishPublish',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetPublishPublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_publish_publish(
        self,
        request: holowatcher_20200730_models.DatasetPublishPublishRequest,
    ) -> holowatcher_20200730_models.DatasetPublishPublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_publish_publish_with_options(request, runtime)

    async def dataset_publish_publish_async(
        self,
        request: holowatcher_20200730_models.DatasetPublishPublishRequest,
    ) -> holowatcher_20200730_models.DatasetPublishPublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_publish_publish_with_options_async(request, runtime)

    def dataset_type_find_all_with_options(
        self,
        request: holowatcher_20200730_models.DatasetTypeFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetTypeFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetTypeFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetTypeFindAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_type_find_all_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetTypeFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetTypeFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetTypeFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetTypeFindAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_type_find_all(
        self,
        request: holowatcher_20200730_models.DatasetTypeFindAllRequest,
    ) -> holowatcher_20200730_models.DatasetTypeFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_type_find_all_with_options(request, runtime)

    async def dataset_type_find_all_async(
        self,
        request: holowatcher_20200730_models.DatasetTypeFindAllRequest,
    ) -> holowatcher_20200730_models.DatasetTypeFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_type_find_all_with_options_async(request, runtime)

    def dataset_unbind_project_with_options(
        self,
        request: holowatcher_20200730_models.DatasetUnbindProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUnbindProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUnbindProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUnbindProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_unbind_project_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetUnbindProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUnbindProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUnbindProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUnbindProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_unbind_project(
        self,
        request: holowatcher_20200730_models.DatasetUnbindProjectRequest,
    ) -> holowatcher_20200730_models.DatasetUnbindProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_unbind_project_with_options(request, runtime)

    async def dataset_unbind_project_async(
        self,
        request: holowatcher_20200730_models.DatasetUnbindProjectRequest,
    ) -> holowatcher_20200730_models.DatasetUnbindProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_unbind_project_with_options_async(request, runtime)

    def dataset_update_one_with_options(
        self,
        request: holowatcher_20200730_models.DatasetUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUpdateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_update_one_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUpdateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_update_one(
        self,
        request: holowatcher_20200730_models.DatasetUpdateOneRequest,
    ) -> holowatcher_20200730_models.DatasetUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_update_one_with_options(request, runtime)

    async def dataset_update_one_async(
        self,
        request: holowatcher_20200730_models.DatasetUpdateOneRequest,
    ) -> holowatcher_20200730_models.DatasetUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_update_one_with_options_async(request, runtime)

    def dataset_upload_create_one_with_options(
        self,
        request: holowatcher_20200730_models.DatasetUploadCreateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadCreateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.device_key):
            query['DeviceKey'] = request.device_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadCreateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadCreateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_upload_create_one_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadCreateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadCreateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.device_key):
            query['DeviceKey'] = request.device_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadCreateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadCreateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_upload_create_one(
        self,
        request: holowatcher_20200730_models.DatasetUploadCreateOneRequest,
    ) -> holowatcher_20200730_models.DatasetUploadCreateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_upload_create_one_with_options(request, runtime)

    async def dataset_upload_create_one_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadCreateOneRequest,
    ) -> holowatcher_20200730_models.DatasetUploadCreateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_upload_create_one_with_options_async(request, runtime)

    def dataset_upload_delete_one_with_options(
        self,
        request: holowatcher_20200730_models.DatasetUploadDeleteOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadDeleteOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.upload_id):
            query['UploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadDeleteOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadDeleteOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_upload_delete_one_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadDeleteOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadDeleteOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.upload_id):
            query['UploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadDeleteOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadDeleteOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_upload_delete_one(
        self,
        request: holowatcher_20200730_models.DatasetUploadDeleteOneRequest,
    ) -> holowatcher_20200730_models.DatasetUploadDeleteOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_upload_delete_one_with_options(request, runtime)

    async def dataset_upload_delete_one_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadDeleteOneRequest,
    ) -> holowatcher_20200730_models.DatasetUploadDeleteOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_upload_delete_one_with_options_async(request, runtime)

    def dataset_upload_delete_oss_file_with_options(
        self,
        request: holowatcher_20200730_models.DatasetUploadDeleteOssFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadDeleteOssFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.upload_id):
            query['UploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadDeleteOssFile',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadDeleteOssFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_upload_delete_oss_file_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadDeleteOssFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadDeleteOssFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.upload_id):
            query['UploadId'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadDeleteOssFile',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadDeleteOssFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_upload_delete_oss_file(
        self,
        request: holowatcher_20200730_models.DatasetUploadDeleteOssFileRequest,
    ) -> holowatcher_20200730_models.DatasetUploadDeleteOssFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_upload_delete_oss_file_with_options(request, runtime)

    async def dataset_upload_delete_oss_file_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadDeleteOssFileRequest,
    ) -> holowatcher_20200730_models.DatasetUploadDeleteOssFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_upload_delete_oss_file_with_options_async(request, runtime)

    def dataset_upload_find_by_dataset_id_with_options(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByDatasetIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadFindByDatasetIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadFindByDatasetId',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadFindByDatasetIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_upload_find_by_dataset_id_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByDatasetIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadFindByDatasetIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadFindByDatasetId',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadFindByDatasetIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_upload_find_by_dataset_id(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByDatasetIdRequest,
    ) -> holowatcher_20200730_models.DatasetUploadFindByDatasetIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_upload_find_by_dataset_id_with_options(request, runtime)

    async def dataset_upload_find_by_dataset_id_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByDatasetIdRequest,
    ) -> holowatcher_20200730_models.DatasetUploadFindByDatasetIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_upload_find_by_dataset_id_with_options_async(request, runtime)

    def dataset_upload_find_by_project_id_with_options(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByProjectIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadFindByProjectIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadFindByProjectId',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadFindByProjectIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_upload_find_by_project_id_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByProjectIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadFindByProjectIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadFindByProjectId',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadFindByProjectIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_upload_find_by_project_id(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByProjectIdRequest,
    ) -> holowatcher_20200730_models.DatasetUploadFindByProjectIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_upload_find_by_project_id_with_options(request, runtime)

    async def dataset_upload_find_by_project_id_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByProjectIdRequest,
    ) -> holowatcher_20200730_models.DatasetUploadFindByProjectIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_upload_find_by_project_id_with_options_async(request, runtime)

    def dataset_upload_find_by_project_id_app_with_options(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByProjectIdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadFindByProjectIdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadFindByProjectIdApp',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadFindByProjectIdAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def dataset_upload_find_by_project_id_app_with_options_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByProjectIdAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DatasetUploadFindByProjectIdAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DatasetUploadFindByProjectIdApp',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DatasetUploadFindByProjectIdAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dataset_upload_find_by_project_id_app(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByProjectIdAppRequest,
    ) -> holowatcher_20200730_models.DatasetUploadFindByProjectIdAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.dataset_upload_find_by_project_id_app_with_options(request, runtime)

    async def dataset_upload_find_by_project_id_app_async(
        self,
        request: holowatcher_20200730_models.DatasetUploadFindByProjectIdAppRequest,
    ) -> holowatcher_20200730_models.DatasetUploadFindByProjectIdAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dataset_upload_find_by_project_id_app_with_options_async(request, runtime)

    def del_bim_drawing_with_options(
        self,
        request: holowatcher_20200730_models.DelBimDrawingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DelBimDrawingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelBimDrawing',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DelBimDrawingResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_bim_drawing_with_options_async(
        self,
        request: holowatcher_20200730_models.DelBimDrawingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DelBimDrawingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelBimDrawing',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DelBimDrawingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_bim_drawing(
        self,
        request: holowatcher_20200730_models.DelBimDrawingRequest,
    ) -> holowatcher_20200730_models.DelBimDrawingResponse:
        runtime = util_models.RuntimeOptions()
        return self.del_bim_drawing_with_options(request, runtime)

    async def del_bim_drawing_async(
        self,
        request: holowatcher_20200730_models.DelBimDrawingRequest,
    ) -> holowatcher_20200730_models.DelBimDrawingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.del_bim_drawing_with_options_async(request, runtime)

    def del_bim_project_with_options(
        self,
        request: holowatcher_20200730_models.DelBimProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DelBimProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelBimProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DelBimProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_bim_project_with_options_async(
        self,
        request: holowatcher_20200730_models.DelBimProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DelBimProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelBimProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DelBimProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_bim_project(
        self,
        request: holowatcher_20200730_models.DelBimProjectRequest,
    ) -> holowatcher_20200730_models.DelBimProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.del_bim_project_with_options(request, runtime)

    async def del_bim_project_async(
        self,
        request: holowatcher_20200730_models.DelBimProjectRequest,
    ) -> holowatcher_20200730_models.DelBimProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.del_bim_project_with_options_async(request, runtime)

    def delete_material_with_options(
        self,
        request: holowatcher_20200730_models.DeleteMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteMaterialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMaterial',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_material_with_options_async(
        self,
        request: holowatcher_20200730_models.DeleteMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteMaterialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMaterial',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_material(
        self,
        request: holowatcher_20200730_models.DeleteMaterialRequest,
    ) -> holowatcher_20200730_models.DeleteMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_material_with_options(request, runtime)

    async def delete_material_async(
        self,
        request: holowatcher_20200730_models.DeleteMaterialRequest,
    ) -> holowatcher_20200730_models.DeleteMaterialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_material_with_options_async(request, runtime)

    def delete_materials_with_options(
        self,
        request: holowatcher_20200730_models.DeleteMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMaterials',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_materials_with_options_async(
        self,
        request: holowatcher_20200730_models.DeleteMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMaterials',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_materials(
        self,
        request: holowatcher_20200730_models.DeleteMaterialsRequest,
    ) -> holowatcher_20200730_models.DeleteMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_materials_with_options(request, runtime)

    async def delete_materials_async(
        self,
        request: holowatcher_20200730_models.DeleteMaterialsRequest,
    ) -> holowatcher_20200730_models.DeleteMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_materials_with_options_async(request, runtime)

    def delete_one_with_options(
        self,
        request: holowatcher_20200730_models.DeleteOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_one_with_options_async(
        self,
        request: holowatcher_20200730_models.DeleteOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_one(
        self,
        request: holowatcher_20200730_models.DeleteOneRequest,
    ) -> holowatcher_20200730_models.DeleteOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_one_with_options(request, runtime)

    async def delete_one_async(
        self,
        request: holowatcher_20200730_models.DeleteOneRequest,
    ) -> holowatcher_20200730_models.DeleteOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_one_with_options_async(request, runtime)

    def delete_project_trans_model_with_options(
        self,
        request: holowatcher_20200730_models.DeleteProjectTransModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteProjectTransModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.trans_model_id):
            query['TransModelId'] = request.trans_model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProjectTransModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteProjectTransModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_trans_model_with_options_async(
        self,
        request: holowatcher_20200730_models.DeleteProjectTransModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteProjectTransModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.trans_model_id):
            query['TransModelId'] = request.trans_model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProjectTransModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteProjectTransModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project_trans_model(
        self,
        request: holowatcher_20200730_models.DeleteProjectTransModelRequest,
    ) -> holowatcher_20200730_models.DeleteProjectTransModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_trans_model_with_options(request, runtime)

    async def delete_project_trans_model_async(
        self,
        request: holowatcher_20200730_models.DeleteProjectTransModelRequest,
    ) -> holowatcher_20200730_models.DeleteProjectTransModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_trans_model_with_options_async(request, runtime)

    def delete_qrcode_with_options(
        self,
        request: holowatcher_20200730_models.DeleteQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteQRCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sid):
            query['SId'] = request.sid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQRCode',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteQRCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_qrcode_with_options_async(
        self,
        request: holowatcher_20200730_models.DeleteQRCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DeleteQRCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sid):
            query['SId'] = request.sid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQRCode',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DeleteQRCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_qrcode(
        self,
        request: holowatcher_20200730_models.DeleteQRCodeRequest,
    ) -> holowatcher_20200730_models.DeleteQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_qrcode_with_options(request, runtime)

    async def delete_qrcode_async(
        self,
        request: holowatcher_20200730_models.DeleteQRCodeRequest,
    ) -> holowatcher_20200730_models.DeleteQRCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_qrcode_with_options_async(request, runtime)

    def disabel_user_with_options(
        self,
        request: holowatcher_20200730_models.DisabelUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DisabelUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisabelUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DisabelUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def disabel_user_with_options_async(
        self,
        request: holowatcher_20200730_models.DisabelUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.DisabelUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisabelUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.DisabelUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disabel_user(
        self,
        request: holowatcher_20200730_models.DisabelUserRequest,
    ) -> holowatcher_20200730_models.DisabelUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.disabel_user_with_options(request, runtime)

    async def disabel_user_async(
        self,
        request: holowatcher_20200730_models.DisabelUserRequest,
    ) -> holowatcher_20200730_models.DisabelUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disabel_user_with_options_async(request, runtime)

    def find_region_with_options(
        self,
        request: holowatcher_20200730_models.FindRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.FindRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindRegion',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.FindRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_region_with_options_async(
        self,
        request: holowatcher_20200730_models.FindRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.FindRegionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindRegion',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.FindRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_region(
        self,
        request: holowatcher_20200730_models.FindRegionRequest,
    ) -> holowatcher_20200730_models.FindRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_region_with_options(request, runtime)

    async def find_region_async(
        self,
        request: holowatcher_20200730_models.FindRegionRequest,
    ) -> holowatcher_20200730_models.FindRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_region_with_options_async(request, runtime)

    def floor_plan_with_options(
        self,
        request: holowatcher_20200730_models.FloorPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.FloorPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FloorPlan',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.FloorPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def floor_plan_with_options_async(
        self,
        request: holowatcher_20200730_models.FloorPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.FloorPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FloorPlan',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.FloorPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def floor_plan(
        self,
        request: holowatcher_20200730_models.FloorPlanRequest,
    ) -> holowatcher_20200730_models.FloorPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.floor_plan_with_options(request, runtime)

    async def floor_plan_async(
        self,
        request: holowatcher_20200730_models.FloorPlanRequest,
    ) -> holowatcher_20200730_models.FloorPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.floor_plan_with_options_async(request, runtime)

    def get_bim_drawing_detail_with_options(
        self,
        request: holowatcher_20200730_models.GetBimDrawingDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimDrawingDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimDrawingDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimDrawingDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_drawing_detail_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimDrawingDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimDrawingDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimDrawingDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimDrawingDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_drawing_detail(
        self,
        request: holowatcher_20200730_models.GetBimDrawingDetailRequest,
    ) -> holowatcher_20200730_models.GetBimDrawingDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_drawing_detail_with_options(request, runtime)

    async def get_bim_drawing_detail_async(
        self,
        request: holowatcher_20200730_models.GetBimDrawingDetailRequest,
    ) -> holowatcher_20200730_models.GetBimDrawingDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_drawing_detail_with_options_async(request, runtime)

    def get_bim_drawing_list_with_options(
        self,
        request: holowatcher_20200730_models.GetBimDrawingListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimDrawingListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimDrawingList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimDrawingListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_drawing_list_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimDrawingListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimDrawingListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimDrawingList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimDrawingListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_drawing_list(
        self,
        request: holowatcher_20200730_models.GetBimDrawingListRequest,
    ) -> holowatcher_20200730_models.GetBimDrawingListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_drawing_list_with_options(request, runtime)

    async def get_bim_drawing_list_async(
        self,
        request: holowatcher_20200730_models.GetBimDrawingListRequest,
    ) -> holowatcher_20200730_models.GetBimDrawingListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_drawing_list_with_options_async(request, runtime)

    def get_bim_drawing_render_with_options(
        self,
        request: holowatcher_20200730_models.GetBimDrawingRenderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimDrawingRenderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimDrawingRender',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimDrawingRenderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_drawing_render_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimDrawingRenderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimDrawingRenderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimDrawingRender',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimDrawingRenderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_drawing_render(
        self,
        request: holowatcher_20200730_models.GetBimDrawingRenderRequest,
    ) -> holowatcher_20200730_models.GetBimDrawingRenderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_drawing_render_with_options(request, runtime)

    async def get_bim_drawing_render_async(
        self,
        request: holowatcher_20200730_models.GetBimDrawingRenderRequest,
    ) -> holowatcher_20200730_models.GetBimDrawingRenderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_drawing_render_with_options_async(request, runtime)

    def get_bim_drawing_status_with_options(
        self,
        tmp_req: holowatcher_20200730_models.GetBimDrawingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimDrawingStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.GetBimDrawingStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimDrawingStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimDrawingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_drawing_status_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.GetBimDrawingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimDrawingStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.GetBimDrawingStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimDrawingStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimDrawingStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_drawing_status(
        self,
        request: holowatcher_20200730_models.GetBimDrawingStatusRequest,
    ) -> holowatcher_20200730_models.GetBimDrawingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_drawing_status_with_options(request, runtime)

    async def get_bim_drawing_status_async(
        self,
        request: holowatcher_20200730_models.GetBimDrawingStatusRequest,
    ) -> holowatcher_20200730_models.GetBimDrawingStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_drawing_status_with_options_async(request, runtime)

    def get_bim_fragment_list_with_options(
        self,
        request: holowatcher_20200730_models.GetBimFragmentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimFragmentListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimFragmentList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimFragmentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_fragment_list_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimFragmentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimFragmentListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimFragmentList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimFragmentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_fragment_list(
        self,
        request: holowatcher_20200730_models.GetBimFragmentListRequest,
    ) -> holowatcher_20200730_models.GetBimFragmentListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_fragment_list_with_options(request, runtime)

    async def get_bim_fragment_list_async(
        self,
        request: holowatcher_20200730_models.GetBimFragmentListRequest,
    ) -> holowatcher_20200730_models.GetBimFragmentListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_fragment_list_with_options_async(request, runtime)

    def get_bim_glb_model_list_with_options(
        self,
        request: holowatcher_20200730_models.GetBimGlbModelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimGlbModelListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimGlbModelList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimGlbModelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_glb_model_list_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimGlbModelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimGlbModelListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimGlbModelList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimGlbModelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_glb_model_list(
        self,
        request: holowatcher_20200730_models.GetBimGlbModelListRequest,
    ) -> holowatcher_20200730_models.GetBimGlbModelListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_glb_model_list_with_options(request, runtime)

    async def get_bim_glb_model_list_async(
        self,
        request: holowatcher_20200730_models.GetBimGlbModelListRequest,
    ) -> holowatcher_20200730_models.GetBimGlbModelListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_glb_model_list_with_options_async(request, runtime)

    def get_bim_model_config_with_options(
        self,
        request: holowatcher_20200730_models.GetBimModelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimModelConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimModelConfig',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimModelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_model_config_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimModelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimModelConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimModelConfig',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimModelConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_model_config(
        self,
        request: holowatcher_20200730_models.GetBimModelConfigRequest,
    ) -> holowatcher_20200730_models.GetBimModelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_model_config_with_options(request, runtime)

    async def get_bim_model_config_async(
        self,
        request: holowatcher_20200730_models.GetBimModelConfigRequest,
    ) -> holowatcher_20200730_models.GetBimModelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_model_config_with_options_async(request, runtime)

    def get_bim_origin_model_with_options(
        self,
        request: holowatcher_20200730_models.GetBimOriginModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimOriginModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimOriginModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimOriginModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_origin_model_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimOriginModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimOriginModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimOriginModel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimOriginModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_origin_model(
        self,
        request: holowatcher_20200730_models.GetBimOriginModelRequest,
    ) -> holowatcher_20200730_models.GetBimOriginModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_origin_model_with_options(request, runtime)

    async def get_bim_origin_model_async(
        self,
        request: holowatcher_20200730_models.GetBimOriginModelRequest,
    ) -> holowatcher_20200730_models.GetBimOriginModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_origin_model_with_options_async(request, runtime)

    def get_bim_project_detail_with_options(
        self,
        request: holowatcher_20200730_models.GetBimProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_project_detail_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_project_detail(
        self,
        request: holowatcher_20200730_models.GetBimProjectDetailRequest,
    ) -> holowatcher_20200730_models.GetBimProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_project_detail_with_options(request, runtime)

    async def get_bim_project_detail_async(
        self,
        request: holowatcher_20200730_models.GetBimProjectDetailRequest,
    ) -> holowatcher_20200730_models.GetBimProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_project_detail_with_options_async(request, runtime)

    def get_bim_project_draw_files_with_options(
        self,
        request: holowatcher_20200730_models.GetBimProjectDrawFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectDrawFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectDrawFiles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectDrawFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_project_draw_files_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimProjectDrawFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectDrawFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectDrawFiles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectDrawFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_project_draw_files(
        self,
        request: holowatcher_20200730_models.GetBimProjectDrawFilesRequest,
    ) -> holowatcher_20200730_models.GetBimProjectDrawFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_project_draw_files_with_options(request, runtime)

    async def get_bim_project_draw_files_async(
        self,
        request: holowatcher_20200730_models.GetBimProjectDrawFilesRequest,
    ) -> holowatcher_20200730_models.GetBimProjectDrawFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_project_draw_files_with_options_async(request, runtime)

    def get_bim_project_list_with_options(
        self,
        request: holowatcher_20200730_models.GetBimProjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_project_list_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimProjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_project_list(
        self,
        request: holowatcher_20200730_models.GetBimProjectListRequest,
    ) -> holowatcher_20200730_models.GetBimProjectListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_project_list_with_options(request, runtime)

    async def get_bim_project_list_async(
        self,
        request: holowatcher_20200730_models.GetBimProjectListRequest,
    ) -> holowatcher_20200730_models.GetBimProjectListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_project_list_with_options_async(request, runtime)

    def get_bim_project_list_status_with_options(
        self,
        tmp_req: holowatcher_20200730_models.GetBimProjectListStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectListStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.GetBimProjectListStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectListStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectListStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_project_list_status_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.GetBimProjectListStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectListStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.GetBimProjectListStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectListStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectListStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_project_list_status(
        self,
        request: holowatcher_20200730_models.GetBimProjectListStatusRequest,
    ) -> holowatcher_20200730_models.GetBimProjectListStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_project_list_status_with_options(request, runtime)

    async def get_bim_project_list_status_async(
        self,
        request: holowatcher_20200730_models.GetBimProjectListStatusRequest,
    ) -> holowatcher_20200730_models.GetBimProjectListStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_project_list_status_with_options_async(request, runtime)

    def get_bim_project_share_model_list_with_options(
        self,
        request: holowatcher_20200730_models.GetBimProjectShareModelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectShareModelListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.share_id):
            query['ShareId'] = request.share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectShareModelList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectShareModelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_project_share_model_list_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimProjectShareModelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimProjectShareModelListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.share_id):
            query['ShareId'] = request.share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimProjectShareModelList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimProjectShareModelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_project_share_model_list(
        self,
        request: holowatcher_20200730_models.GetBimProjectShareModelListRequest,
    ) -> holowatcher_20200730_models.GetBimProjectShareModelListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_project_share_model_list_with_options(request, runtime)

    async def get_bim_project_share_model_list_async(
        self,
        request: holowatcher_20200730_models.GetBimProjectShareModelListRequest,
    ) -> holowatcher_20200730_models.GetBimProjectShareModelListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_project_share_model_list_with_options_async(request, runtime)

    def get_bim_standard_auto_mark_with_options(
        self,
        request: holowatcher_20200730_models.GetBimStandardAutoMarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardAutoMarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardAutoMark',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardAutoMarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_standard_auto_mark_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardAutoMarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardAutoMarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardAutoMark',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardAutoMarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_standard_auto_mark(
        self,
        request: holowatcher_20200730_models.GetBimStandardAutoMarkRequest,
    ) -> holowatcher_20200730_models.GetBimStandardAutoMarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_standard_auto_mark_with_options(request, runtime)

    async def get_bim_standard_auto_mark_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardAutoMarkRequest,
    ) -> holowatcher_20200730_models.GetBimStandardAutoMarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_standard_auto_mark_with_options_async(request, runtime)

    def get_bim_standard_list_with_options(
        self,
        request: holowatcher_20200730_models.GetBimStandardListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_standard_list_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_standard_list(
        self,
        request: holowatcher_20200730_models.GetBimStandardListRequest,
    ) -> holowatcher_20200730_models.GetBimStandardListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_standard_list_with_options(request, runtime)

    async def get_bim_standard_list_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardListRequest,
    ) -> holowatcher_20200730_models.GetBimStandardListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_standard_list_with_options_async(request, runtime)

    def get_bim_standard_plan_with_options(
        self,
        request: holowatcher_20200730_models.GetBimStandardPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard):
            query['Standard'] = request.standard
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardPlan',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_standard_plan_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard):
            query['Standard'] = request.standard
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardPlan',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_standard_plan(
        self,
        request: holowatcher_20200730_models.GetBimStandardPlanRequest,
    ) -> holowatcher_20200730_models.GetBimStandardPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_standard_plan_with_options(request, runtime)

    async def get_bim_standard_plan_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardPlanRequest,
    ) -> holowatcher_20200730_models.GetBimStandardPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_standard_plan_with_options_async(request, runtime)

    def get_bim_standard_render_with_options(
        self,
        request: holowatcher_20200730_models.GetBimStandardRenderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardRenderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardRender',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardRenderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_standard_render_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardRenderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardRenderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardRender',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardRenderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_standard_render(
        self,
        request: holowatcher_20200730_models.GetBimStandardRenderRequest,
    ) -> holowatcher_20200730_models.GetBimStandardRenderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_standard_render_with_options(request, runtime)

    async def get_bim_standard_render_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardRenderRequest,
    ) -> holowatcher_20200730_models.GetBimStandardRenderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_standard_render_with_options_async(request, runtime)

    def get_bim_standard_sample_with_options(
        self,
        request: holowatcher_20200730_models.GetBimStandardSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardSampleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardSample',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_standard_sample_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardSampleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardSample',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_standard_sample(
        self,
        request: holowatcher_20200730_models.GetBimStandardSampleRequest,
    ) -> holowatcher_20200730_models.GetBimStandardSampleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_standard_sample_with_options(request, runtime)

    async def get_bim_standard_sample_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardSampleRequest,
    ) -> holowatcher_20200730_models.GetBimStandardSampleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_standard_sample_with_options_async(request, runtime)

    def get_bim_standard_status_by_ids_with_options(
        self,
        tmp_req: holowatcher_20200730_models.GetBimStandardStatusByIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardStatusByIdsResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.GetBimStandardStatusByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardStatusByIds',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardStatusByIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_standard_status_by_ids_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.GetBimStandardStatusByIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimStandardStatusByIdsResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.GetBimStandardStatusByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimStandardStatusByIds',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimStandardStatusByIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_standard_status_by_ids(
        self,
        request: holowatcher_20200730_models.GetBimStandardStatusByIdsRequest,
    ) -> holowatcher_20200730_models.GetBimStandardStatusByIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_standard_status_by_ids_with_options(request, runtime)

    async def get_bim_standard_status_by_ids_async(
        self,
        request: holowatcher_20200730_models.GetBimStandardStatusByIdsRequest,
    ) -> holowatcher_20200730_models.GetBimStandardStatusByIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_standard_status_by_ids_with_options_async(request, runtime)

    def get_bim_task_detail_with_options(
        self,
        request: holowatcher_20200730_models.GetBimTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimTaskDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_task_detail_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimTaskDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_task_detail(
        self,
        request: holowatcher_20200730_models.GetBimTaskDetailRequest,
    ) -> holowatcher_20200730_models.GetBimTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_task_detail_with_options(request, runtime)

    async def get_bim_task_detail_async(
        self,
        request: holowatcher_20200730_models.GetBimTaskDetailRequest,
    ) -> holowatcher_20200730_models.GetBimTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_task_detail_with_options_async(request, runtime)

    def get_bim_tenant_flow_with_options(
        self,
        request: holowatcher_20200730_models.GetBimTenantFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimTenantFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimTenantFlow',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimTenantFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_tenant_flow_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimTenantFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimTenantFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimTenantFlow',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimTenantFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_tenant_flow(
        self,
        request: holowatcher_20200730_models.GetBimTenantFlowRequest,
    ) -> holowatcher_20200730_models.GetBimTenantFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_tenant_flow_with_options(request, runtime)

    async def get_bim_tenant_flow_async(
        self,
        request: holowatcher_20200730_models.GetBimTenantFlowRequest,
    ) -> holowatcher_20200730_models.GetBimTenantFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_tenant_flow_with_options_async(request, runtime)

    def get_bim_trans_model_list_with_options(
        self,
        request: holowatcher_20200730_models.GetBimTransModelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimTransModelListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimTransModelList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimTransModelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_trans_model_list_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimTransModelListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimTransModelListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimTransModelList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimTransModelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_trans_model_list(
        self,
        request: holowatcher_20200730_models.GetBimTransModelListRequest,
    ) -> holowatcher_20200730_models.GetBimTransModelListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_trans_model_list_with_options(request, runtime)

    async def get_bim_trans_model_list_async(
        self,
        request: holowatcher_20200730_models.GetBimTransModelListRequest,
    ) -> holowatcher_20200730_models.GetBimTransModelListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_trans_model_list_with_options_async(request, runtime)

    def get_bim_upload_sts_token_with_options(
        self,
        request: holowatcher_20200730_models.GetBimUploadStsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimUploadStsTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimUploadStsToken',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimUploadStsTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bim_upload_sts_token_with_options_async(
        self,
        request: holowatcher_20200730_models.GetBimUploadStsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetBimUploadStsTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBimUploadStsToken',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetBimUploadStsTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bim_upload_sts_token(
        self,
        request: holowatcher_20200730_models.GetBimUploadStsTokenRequest,
    ) -> holowatcher_20200730_models.GetBimUploadStsTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bim_upload_sts_token_with_options(request, runtime)

    async def get_bim_upload_sts_token_async(
        self,
        request: holowatcher_20200730_models.GetBimUploadStsTokenRequest,
    ) -> holowatcher_20200730_models.GetBimUploadStsTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bim_upload_sts_token_with_options_async(request, runtime)

    def get_current_user_with_options(
        self,
        request: holowatcher_20200730_models.GetCurrentUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetCurrentUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCurrentUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetCurrentUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_current_user_with_options_async(
        self,
        request: holowatcher_20200730_models.GetCurrentUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetCurrentUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCurrentUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetCurrentUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_current_user(
        self,
        request: holowatcher_20200730_models.GetCurrentUserRequest,
    ) -> holowatcher_20200730_models.GetCurrentUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_current_user_with_options(request, runtime)

    async def get_current_user_async(
        self,
        request: holowatcher_20200730_models.GetCurrentUserRequest,
    ) -> holowatcher_20200730_models.GetCurrentUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_current_user_with_options_async(request, runtime)

    def get_instances_with_options(
        self,
        request: holowatcher_20200730_models.GetInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_node_id):
            query['PipelineNodeId'] = request.pipeline_node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstances',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instances_with_options_async(
        self,
        request: holowatcher_20200730_models.GetInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_node_id):
            query['PipelineNodeId'] = request.pipeline_node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstances',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instances(
        self,
        request: holowatcher_20200730_models.GetInstancesRequest,
    ) -> holowatcher_20200730_models.GetInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instances_with_options(request, runtime)

    async def get_instances_async(
        self,
        request: holowatcher_20200730_models.GetInstancesRequest,
    ) -> holowatcher_20200730_models.GetInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instances_with_options_async(request, runtime)

    def get_latest_node_by_type_with_options(
        self,
        request: holowatcher_20200730_models.GetLatestNodeByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetLatestNodeByTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLatestNodeByType',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetLatestNodeByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_latest_node_by_type_with_options_async(
        self,
        request: holowatcher_20200730_models.GetLatestNodeByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetLatestNodeByTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLatestNodeByType',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetLatestNodeByTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_latest_node_by_type(
        self,
        request: holowatcher_20200730_models.GetLatestNodeByTypeRequest,
    ) -> holowatcher_20200730_models.GetLatestNodeByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_latest_node_by_type_with_options(request, runtime)

    async def get_latest_node_by_type_async(
        self,
        request: holowatcher_20200730_models.GetLatestNodeByTypeRequest,
    ) -> holowatcher_20200730_models.GetLatestNodeByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_latest_node_by_type_with_options_async(request, runtime)

    def get_material_list_with_options(
        self,
        request: holowatcher_20200730_models.GetMaterialListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetMaterialListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['Current'] = request.current
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMaterialList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetMaterialListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_material_list_with_options_async(
        self,
        request: holowatcher_20200730_models.GetMaterialListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetMaterialListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['Current'] = request.current
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMaterialList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetMaterialListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_material_list(
        self,
        request: holowatcher_20200730_models.GetMaterialListRequest,
    ) -> holowatcher_20200730_models.GetMaterialListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_material_list_with_options(request, runtime)

    async def get_material_list_async(
        self,
        request: holowatcher_20200730_models.GetMaterialListRequest,
    ) -> holowatcher_20200730_models.GetMaterialListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_material_list_with_options_async(request, runtime)

    def get_oss_credential_with_options(
        self,
        request: holowatcher_20200730_models.GetOssCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetOssCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssCredential',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetOssCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_credential_with_options_async(
        self,
        request: holowatcher_20200730_models.GetOssCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetOssCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssCredential',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetOssCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_credential(
        self,
        request: holowatcher_20200730_models.GetOssCredentialRequest,
    ) -> holowatcher_20200730_models.GetOssCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_credential_with_options(request, runtime)

    async def get_oss_credential_async(
        self,
        request: holowatcher_20200730_models.GetOssCredentialRequest,
    ) -> holowatcher_20200730_models.GetOssCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_credential_with_options_async(request, runtime)

    def get_project_phase_detail_with_options(
        self,
        request: holowatcher_20200730_models.GetProjectPhaseDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetProjectPhaseDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectPhaseDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetProjectPhaseDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_phase_detail_with_options_async(
        self,
        request: holowatcher_20200730_models.GetProjectPhaseDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetProjectPhaseDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectPhaseDetail',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetProjectPhaseDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_phase_detail(
        self,
        request: holowatcher_20200730_models.GetProjectPhaseDetailRequest,
    ) -> holowatcher_20200730_models.GetProjectPhaseDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_phase_detail_with_options(request, runtime)

    async def get_project_phase_detail_async(
        self,
        request: holowatcher_20200730_models.GetProjectPhaseDetailRequest,
    ) -> holowatcher_20200730_models.GetProjectPhaseDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_phase_detail_with_options_async(request, runtime)

    def get_status_and_oss_with_options(
        self,
        request: holowatcher_20200730_models.GetStatusAndOssRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetStatusAndOssResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.body):
            query['body'] = request.body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStatusAndOss',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetStatusAndOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_status_and_oss_with_options_async(
        self,
        request: holowatcher_20200730_models.GetStatusAndOssRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetStatusAndOssResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.body):
            query['body'] = request.body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStatusAndOss',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetStatusAndOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_status_and_oss(
        self,
        request: holowatcher_20200730_models.GetStatusAndOssRequest,
    ) -> holowatcher_20200730_models.GetStatusAndOssResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_status_and_oss_with_options(request, runtime)

    async def get_status_and_oss_async(
        self,
        request: holowatcher_20200730_models.GetStatusAndOssRequest,
    ) -> holowatcher_20200730_models.GetStatusAndOssResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_status_and_oss_with_options_async(request, runtime)

    def get_template_list_with_options(
        self,
        request: holowatcher_20200730_models.GetTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['Current'] = request.current
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.style):
            query['Style'] = request.style
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_list_with_options_async(
        self,
        request: holowatcher_20200730_models.GetTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current):
            query['Current'] = request.current
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.style):
            query['Style'] = request.style
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateList',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_list(
        self,
        request: holowatcher_20200730_models.GetTemplateListRequest,
    ) -> holowatcher_20200730_models.GetTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_list_with_options(request, runtime)

    async def get_template_list_async(
        self,
        request: holowatcher_20200730_models.GetTemplateListRequest,
    ) -> holowatcher_20200730_models.GetTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_list_with_options_async(request, runtime)

    def get_token_with_options(
        self,
        request: holowatcher_20200730_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.path_type):
            query['PathType'] = request.path_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: holowatcher_20200730_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.GetTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.path_type):
            query['PathType'] = request.path_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: holowatcher_20200730_models.GetTokenRequest,
    ) -> holowatcher_20200730_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    async def get_token_async(
        self,
        request: holowatcher_20200730_models.GetTokenRequest,
    ) -> holowatcher_20200730_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_token_with_options_async(request, runtime)

    def material_create_one_picture_with_options(
        self,
        request: holowatcher_20200730_models.MaterialCreateOnePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialCreateOnePictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialCreateOnePicture',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialCreateOnePictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_create_one_picture_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialCreateOnePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialCreateOnePictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialCreateOnePicture',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialCreateOnePictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_create_one_picture(
        self,
        request: holowatcher_20200730_models.MaterialCreateOnePictureRequest,
    ) -> holowatcher_20200730_models.MaterialCreateOnePictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_create_one_picture_with_options(request, runtime)

    async def material_create_one_picture_async(
        self,
        request: holowatcher_20200730_models.MaterialCreateOnePictureRequest,
    ) -> holowatcher_20200730_models.MaterialCreateOnePictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_create_one_picture_with_options_async(request, runtime)

    def material_create_one_video_with_options(
        self,
        request: holowatcher_20200730_models.MaterialCreateOneVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialCreateOneVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialCreateOneVideo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialCreateOneVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_create_one_video_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialCreateOneVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialCreateOneVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialCreateOneVideo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialCreateOneVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_create_one_video(
        self,
        request: holowatcher_20200730_models.MaterialCreateOneVideoRequest,
    ) -> holowatcher_20200730_models.MaterialCreateOneVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_create_one_video_with_options(request, runtime)

    async def material_create_one_video_async(
        self,
        request: holowatcher_20200730_models.MaterialCreateOneVideoRequest,
    ) -> holowatcher_20200730_models.MaterialCreateOneVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_create_one_video_with_options_async(request, runtime)

    def material_delete_one_with_options(
        self,
        request: holowatcher_20200730_models.MaterialDeleteOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialDeleteOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialDeleteOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialDeleteOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_delete_one_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialDeleteOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialDeleteOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialDeleteOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialDeleteOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_delete_one(
        self,
        request: holowatcher_20200730_models.MaterialDeleteOneRequest,
    ) -> holowatcher_20200730_models.MaterialDeleteOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_delete_one_with_options(request, runtime)

    async def material_delete_one_async(
        self,
        request: holowatcher_20200730_models.MaterialDeleteOneRequest,
    ) -> holowatcher_20200730_models.MaterialDeleteOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_delete_one_with_options_async(request, runtime)

    def material_find_all_with_options(
        self,
        request: holowatcher_20200730_models.MaterialFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.material_type):
            query['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFindAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_find_all_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.material_type):
            query['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFindAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_find_all(
        self,
        request: holowatcher_20200730_models.MaterialFindAllRequest,
    ) -> holowatcher_20200730_models.MaterialFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_find_all_with_options(request, runtime)

    async def material_find_all_async(
        self,
        request: holowatcher_20200730_models.MaterialFindAllRequest,
    ) -> holowatcher_20200730_models.MaterialFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_find_all_with_options_async(request, runtime)

    def material_find_all_picture_with_options(
        self,
        request: holowatcher_20200730_models.MaterialFindAllPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFindAllPictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFindAllPicture',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFindAllPictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_find_all_picture_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialFindAllPictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFindAllPictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFindAllPicture',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFindAllPictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_find_all_picture(
        self,
        request: holowatcher_20200730_models.MaterialFindAllPictureRequest,
    ) -> holowatcher_20200730_models.MaterialFindAllPictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_find_all_picture_with_options(request, runtime)

    async def material_find_all_picture_async(
        self,
        request: holowatcher_20200730_models.MaterialFindAllPictureRequest,
    ) -> holowatcher_20200730_models.MaterialFindAllPictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_find_all_picture_with_options_async(request, runtime)

    def material_find_all_video_with_options(
        self,
        request: holowatcher_20200730_models.MaterialFindAllVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFindAllVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFindAllVideo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFindAllVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_find_all_video_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialFindAllVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFindAllVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFindAllVideo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFindAllVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_find_all_video(
        self,
        request: holowatcher_20200730_models.MaterialFindAllVideoRequest,
    ) -> holowatcher_20200730_models.MaterialFindAllVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_find_all_video_with_options(request, runtime)

    async def material_find_all_video_async(
        self,
        request: holowatcher_20200730_models.MaterialFindAllVideoRequest,
    ) -> holowatcher_20200730_models.MaterialFindAllVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_find_all_video_with_options_async(request, runtime)

    def material_find_one_with_options(
        self,
        request: holowatcher_20200730_models.MaterialFindOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFindOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFindOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFindOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_find_one_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialFindOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFindOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFindOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFindOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_find_one(
        self,
        request: holowatcher_20200730_models.MaterialFindOneRequest,
    ) -> holowatcher_20200730_models.MaterialFindOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_find_one_with_options(request, runtime)

    async def material_find_one_async(
        self,
        request: holowatcher_20200730_models.MaterialFindOneRequest,
    ) -> holowatcher_20200730_models.MaterialFindOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_find_one_with_options_async(request, runtime)

    def material_flush_upload_with_options(
        self,
        request: holowatcher_20200730_models.MaterialFlushUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFlushUploadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFlushUpload',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFlushUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_flush_upload_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialFlushUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialFlushUploadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialFlushUpload',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialFlushUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_flush_upload(
        self,
        request: holowatcher_20200730_models.MaterialFlushUploadRequest,
    ) -> holowatcher_20200730_models.MaterialFlushUploadResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_flush_upload_with_options(request, runtime)

    async def material_flush_upload_async(
        self,
        request: holowatcher_20200730_models.MaterialFlushUploadRequest,
    ) -> holowatcher_20200730_models.MaterialFlushUploadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_flush_upload_with_options_async(request, runtime)

    def material_get_oss_creadentials_with_options(
        self,
        request: holowatcher_20200730_models.MaterialGetOssCreadentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialGetOssCreadentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialGetOssCreadentials',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialGetOssCreadentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_get_oss_creadentials_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialGetOssCreadentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialGetOssCreadentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialGetOssCreadentials',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialGetOssCreadentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_get_oss_creadentials(
        self,
        request: holowatcher_20200730_models.MaterialGetOssCreadentialsRequest,
    ) -> holowatcher_20200730_models.MaterialGetOssCreadentialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_get_oss_creadentials_with_options(request, runtime)

    async def material_get_oss_creadentials_async(
        self,
        request: holowatcher_20200730_models.MaterialGetOssCreadentialsRequest,
    ) -> holowatcher_20200730_models.MaterialGetOssCreadentialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_get_oss_creadentials_with_options_async(request, runtime)

    def material_update_one_with_options(
        self,
        request: holowatcher_20200730_models.MaterialUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialUpdateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def material_update_one_with_options_async(
        self,
        request: holowatcher_20200730_models.MaterialUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.MaterialUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MaterialUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.MaterialUpdateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def material_update_one(
        self,
        request: holowatcher_20200730_models.MaterialUpdateOneRequest,
    ) -> holowatcher_20200730_models.MaterialUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.material_update_one_with_options(request, runtime)

    async def material_update_one_async(
        self,
        request: holowatcher_20200730_models.MaterialUpdateOneRequest,
    ) -> holowatcher_20200730_models.MaterialUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.material_update_one_with_options_async(request, runtime)

    def order_assigned_scan_isvwith_options(
        self,
        request: holowatcher_20200730_models.OrderAssignedScanISVRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderAssignedScanISVResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderAssignedScanISV',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderAssignedScanISVResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_assigned_scan_isvwith_options_async(
        self,
        request: holowatcher_20200730_models.OrderAssignedScanISVRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderAssignedScanISVResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderAssignedScanISV',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderAssignedScanISVResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_assigned_scan_isv(
        self,
        request: holowatcher_20200730_models.OrderAssignedScanISVRequest,
    ) -> holowatcher_20200730_models.OrderAssignedScanISVResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_assigned_scan_isvwith_options(request, runtime)

    async def order_assigned_scan_isv_async(
        self,
        request: holowatcher_20200730_models.OrderAssignedScanISVRequest,
    ) -> holowatcher_20200730_models.OrderAssignedScanISVResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_assigned_scan_isvwith_options_async(request, runtime)

    def order_batch_create_with_options(
        self,
        request: holowatcher_20200730_models.OrderBatchCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderBatchCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderBatchCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderBatchCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_batch_create_with_options_async(
        self,
        request: holowatcher_20200730_models.OrderBatchCreateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderBatchCreateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderBatchCreate',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderBatchCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_batch_create(
        self,
        request: holowatcher_20200730_models.OrderBatchCreateRequest,
    ) -> holowatcher_20200730_models.OrderBatchCreateResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_batch_create_with_options(request, runtime)

    async def order_batch_create_async(
        self,
        request: holowatcher_20200730_models.OrderBatchCreateRequest,
    ) -> holowatcher_20200730_models.OrderBatchCreateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_batch_create_with_options_async(request, runtime)

    def order_batch_delete_with_options(
        self,
        request: holowatcher_20200730_models.OrderBatchDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderBatchDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderBatchDelete',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderBatchDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_batch_delete_with_options_async(
        self,
        request: holowatcher_20200730_models.OrderBatchDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderBatchDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderBatchDelete',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderBatchDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_batch_delete(
        self,
        request: holowatcher_20200730_models.OrderBatchDeleteRequest,
    ) -> holowatcher_20200730_models.OrderBatchDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_batch_delete_with_options(request, runtime)

    async def order_batch_delete_async(
        self,
        request: holowatcher_20200730_models.OrderBatchDeleteRequest,
    ) -> holowatcher_20200730_models.OrderBatchDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_batch_delete_with_options_async(request, runtime)

    def order_batch_update_order_state_with_options(
        self,
        request: holowatcher_20200730_models.OrderBatchUpdateOrderStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderBatchUpdateOrderStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderBatchUpdateOrderState',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderBatchUpdateOrderStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_batch_update_order_state_with_options_async(
        self,
        request: holowatcher_20200730_models.OrderBatchUpdateOrderStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderBatchUpdateOrderStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderBatchUpdateOrderState',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderBatchUpdateOrderStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_batch_update_order_state(
        self,
        request: holowatcher_20200730_models.OrderBatchUpdateOrderStateRequest,
    ) -> holowatcher_20200730_models.OrderBatchUpdateOrderStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_batch_update_order_state_with_options(request, runtime)

    async def order_batch_update_order_state_async(
        self,
        request: holowatcher_20200730_models.OrderBatchUpdateOrderStateRequest,
    ) -> holowatcher_20200730_models.OrderBatchUpdateOrderStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_batch_update_order_state_with_options_async(request, runtime)

    def order_find_all_with_options(
        self,
        request: holowatcher_20200730_models.OrderFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderFindAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_find_all_with_options_async(
        self,
        request: holowatcher_20200730_models.OrderFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderFindAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_find_all(
        self,
        request: holowatcher_20200730_models.OrderFindAllRequest,
    ) -> holowatcher_20200730_models.OrderFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_find_all_with_options(request, runtime)

    async def order_find_all_async(
        self,
        request: holowatcher_20200730_models.OrderFindAllRequest,
    ) -> holowatcher_20200730_models.OrderFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_find_all_with_options_async(request, runtime)

    def order_query_one_with_options(
        self,
        request: holowatcher_20200730_models.OrderQueryOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderQueryOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderQueryOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderQueryOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_query_one_with_options_async(
        self,
        request: holowatcher_20200730_models.OrderQueryOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderQueryOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderQueryOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderQueryOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_query_one(
        self,
        request: holowatcher_20200730_models.OrderQueryOneRequest,
    ) -> holowatcher_20200730_models.OrderQueryOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_query_one_with_options(request, runtime)

    async def order_query_one_async(
        self,
        request: holowatcher_20200730_models.OrderQueryOneRequest,
    ) -> holowatcher_20200730_models.OrderQueryOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_query_one_with_options_async(request, runtime)

    def order_query_one_app_with_options(
        self,
        request: holowatcher_20200730_models.OrderQueryOneAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderQueryOneAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderQueryOneApp',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderQueryOneAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_query_one_app_with_options_async(
        self,
        request: holowatcher_20200730_models.OrderQueryOneAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderQueryOneAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderQueryOneApp',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderQueryOneAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_query_one_app(
        self,
        request: holowatcher_20200730_models.OrderQueryOneAppRequest,
    ) -> holowatcher_20200730_models.OrderQueryOneAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_query_one_app_with_options(request, runtime)

    async def order_query_one_app_async(
        self,
        request: holowatcher_20200730_models.OrderQueryOneAppRequest,
    ) -> holowatcher_20200730_models.OrderQueryOneAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_query_one_app_with_options_async(request, runtime)

    def order_update_one_with_options(
        self,
        request: holowatcher_20200730_models.OrderUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderUpdateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def order_update_one_with_options_async(
        self,
        request: holowatcher_20200730_models.OrderUpdateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.OrderUpdateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OrderUpdateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.OrderUpdateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def order_update_one(
        self,
        request: holowatcher_20200730_models.OrderUpdateOneRequest,
    ) -> holowatcher_20200730_models.OrderUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.order_update_one_with_options(request, runtime)

    async def order_update_one_async(
        self,
        request: holowatcher_20200730_models.OrderUpdateOneRequest,
    ) -> holowatcher_20200730_models.OrderUpdateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.order_update_one_with_options_async(request, runtime)

    def p_cdataset_create_one_with_options(
        self,
        request: holowatcher_20200730_models.PCDatasetCreateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PCDatasetCreateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PCDatasetCreateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PCDatasetCreateOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def p_cdataset_create_one_with_options_async(
        self,
        request: holowatcher_20200730_models.PCDatasetCreateOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PCDatasetCreateOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PCDatasetCreateOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PCDatasetCreateOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def p_cdataset_create_one(
        self,
        request: holowatcher_20200730_models.PCDatasetCreateOneRequest,
    ) -> holowatcher_20200730_models.PCDatasetCreateOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.p_cdataset_create_one_with_options(request, runtime)

    async def p_cdataset_create_one_async(
        self,
        request: holowatcher_20200730_models.PCDatasetCreateOneRequest,
    ) -> holowatcher_20200730_models.PCDatasetCreateOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.p_cdataset_create_one_with_options_async(request, runtime)

    def p_cupload_build_with_options(
        self,
        request: holowatcher_20200730_models.PCUploadBuildRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PCUploadBuildResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PCUploadBuild',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PCUploadBuildResponse(),
            self.call_api(params, req, runtime)
        )

    async def p_cupload_build_with_options_async(
        self,
        request: holowatcher_20200730_models.PCUploadBuildRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PCUploadBuildResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PCUploadBuild',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PCUploadBuildResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def p_cupload_build(
        self,
        request: holowatcher_20200730_models.PCUploadBuildRequest,
    ) -> holowatcher_20200730_models.PCUploadBuildResponse:
        runtime = util_models.RuntimeOptions()
        return self.p_cupload_build_with_options(request, runtime)

    async def p_cupload_build_async(
        self,
        request: holowatcher_20200730_models.PCUploadBuildRequest,
    ) -> holowatcher_20200730_models.PCUploadBuildResponse:
        runtime = util_models.RuntimeOptions()
        return await self.p_cupload_build_with_options_async(request, runtime)

    def p_cupload_publish_with_options(
        self,
        request: holowatcher_20200730_models.PCUploadPublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PCUploadPublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PCUploadPublish',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PCUploadPublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def p_cupload_publish_with_options_async(
        self,
        request: holowatcher_20200730_models.PCUploadPublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PCUploadPublishResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PCUploadPublish',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PCUploadPublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def p_cupload_publish(
        self,
        request: holowatcher_20200730_models.PCUploadPublishRequest,
    ) -> holowatcher_20200730_models.PCUploadPublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.p_cupload_publish_with_options(request, runtime)

    async def p_cupload_publish_async(
        self,
        request: holowatcher_20200730_models.PCUploadPublishRequest,
    ) -> holowatcher_20200730_models.PCUploadPublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.p_cupload_publish_with_options_async(request, runtime)

    def pipeline_find_all_with_options(
        self,
        request: holowatcher_20200730_models.PipelineFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PipelineFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.exposed):
            query['Exposed'] = request.exposed
        if not UtilClient.is_unset(request.is_root):
            query['IsRoot'] = request.is_root
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PipelineFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PipelineFindAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def pipeline_find_all_with_options_async(
        self,
        request: holowatcher_20200730_models.PipelineFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PipelineFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.exposed):
            query['Exposed'] = request.exposed
        if not UtilClient.is_unset(request.is_root):
            query['IsRoot'] = request.is_root
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PipelineFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PipelineFindAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pipeline_find_all(
        self,
        request: holowatcher_20200730_models.PipelineFindAllRequest,
    ) -> holowatcher_20200730_models.PipelineFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.pipeline_find_all_with_options(request, runtime)

    async def pipeline_find_all_async(
        self,
        request: holowatcher_20200730_models.PipelineFindAllRequest,
    ) -> holowatcher_20200730_models.PipelineFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pipeline_find_all_with_options_async(request, runtime)

    def produce_expo_notice_with_options(
        self,
        request: holowatcher_20200730_models.ProduceExpoNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProduceExpoNoticeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProduceExpoNotice',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProduceExpoNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def produce_expo_notice_with_options_async(
        self,
        request: holowatcher_20200730_models.ProduceExpoNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProduceExpoNoticeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProduceExpoNotice',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProduceExpoNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def produce_expo_notice(
        self,
        request: holowatcher_20200730_models.ProduceExpoNoticeRequest,
    ) -> holowatcher_20200730_models.ProduceExpoNoticeResponse:
        runtime = util_models.RuntimeOptions()
        return self.produce_expo_notice_with_options(request, runtime)

    async def produce_expo_notice_async(
        self,
        request: holowatcher_20200730_models.ProduceExpoNoticeRequest,
    ) -> holowatcher_20200730_models.ProduceExpoNoticeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.produce_expo_notice_with_options_async(request, runtime)

    def produce_notice_with_options(
        self,
        request: holowatcher_20200730_models.ProduceNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProduceNoticeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProduceNotice',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProduceNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def produce_notice_with_options_async(
        self,
        request: holowatcher_20200730_models.ProduceNoticeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProduceNoticeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProduceNotice',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProduceNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def produce_notice(
        self,
        request: holowatcher_20200730_models.ProduceNoticeRequest,
    ) -> holowatcher_20200730_models.ProduceNoticeResponse:
        runtime = util_models.RuntimeOptions()
        return self.produce_notice_with_options(request, runtime)

    async def produce_notice_async(
        self,
        request: holowatcher_20200730_models.ProduceNoticeRequest,
    ) -> holowatcher_20200730_models.ProduceNoticeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.produce_notice_with_options_async(request, runtime)

    def project_create_one_appwith_options(
        self,
        request: holowatcher_20200730_models.ProjectCreateOneAPPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectCreateOneAPPResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectCreateOneAPP',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectCreateOneAPPResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_create_one_appwith_options_async(
        self,
        request: holowatcher_20200730_models.ProjectCreateOneAPPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectCreateOneAPPResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectCreateOneAPP',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectCreateOneAPPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_create_one_app(
        self,
        request: holowatcher_20200730_models.ProjectCreateOneAPPRequest,
    ) -> holowatcher_20200730_models.ProjectCreateOneAPPResponse:
        runtime = util_models.RuntimeOptions()
        return self.project_create_one_appwith_options(request, runtime)

    async def project_create_one_app_async(
        self,
        request: holowatcher_20200730_models.ProjectCreateOneAPPRequest,
    ) -> holowatcher_20200730_models.ProjectCreateOneAPPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.project_create_one_appwith_options_async(request, runtime)

    def project_create_or_update_ext_info_with_options(
        self,
        request: holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.ext_info_str):
            query['ExtInfoStr'] = request.ext_info_str
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectCreateOrUpdateExtInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_create_or_update_ext_info_with_options_async(
        self,
        request: holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.ext_info_str):
            query['ExtInfoStr'] = request.ext_info_str
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectCreateOrUpdateExtInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_create_or_update_ext_info(
        self,
        request: holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoRequest,
    ) -> holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.project_create_or_update_ext_info_with_options(request, runtime)

    async def project_create_or_update_ext_info_async(
        self,
        request: holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoRequest,
    ) -> holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.project_create_or_update_ext_info_with_options_async(request, runtime)

    def project_create_or_update_ext_info_app_with_options(
        self,
        request: holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.ext_info_str):
            query['ExtInfoStr'] = request.ext_info_str
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectCreateOrUpdateExtInfoApp',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_create_or_update_ext_info_app_with_options_async(
        self,
        request: holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.ext_info_str):
            query['ExtInfoStr'] = request.ext_info_str
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectCreateOrUpdateExtInfoApp',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_create_or_update_ext_info_app(
        self,
        request: holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppRequest,
    ) -> holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.project_create_or_update_ext_info_app_with_options(request, runtime)

    async def project_create_or_update_ext_info_app_async(
        self,
        request: holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppRequest,
    ) -> holowatcher_20200730_models.ProjectCreateOrUpdateExtInfoAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.project_create_or_update_ext_info_app_with_options_async(request, runtime)

    def project_find_all_with_options(
        self,
        request: holowatcher_20200730_models.ProjectFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.json_params):
            query['JsonParams'] = request.json_params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectFindAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_find_all_with_options_async(
        self,
        request: holowatcher_20200730_models.ProjectFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.json_params):
            query['JsonParams'] = request.json_params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectFindAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_find_all(
        self,
        request: holowatcher_20200730_models.ProjectFindAllRequest,
    ) -> holowatcher_20200730_models.ProjectFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.project_find_all_with_options(request, runtime)

    async def project_find_all_async(
        self,
        request: holowatcher_20200730_models.ProjectFindAllRequest,
    ) -> holowatcher_20200730_models.ProjectFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.project_find_all_with_options_async(request, runtime)

    def project_find_uploads_with_options(
        self,
        request: holowatcher_20200730_models.ProjectFindUploadsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectFindUploadsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.created_by_current_user):
            query['CreatedByCurrentUser'] = request.created_by_current_user
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.live):
            query['Live'] = request.live
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectFindUploads',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectFindUploadsResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_find_uploads_with_options_async(
        self,
        request: holowatcher_20200730_models.ProjectFindUploadsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectFindUploadsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.created_by_current_user):
            query['CreatedByCurrentUser'] = request.created_by_current_user
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.live):
            query['Live'] = request.live
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectFindUploads',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectFindUploadsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_find_uploads(
        self,
        request: holowatcher_20200730_models.ProjectFindUploadsRequest,
    ) -> holowatcher_20200730_models.ProjectFindUploadsResponse:
        runtime = util_models.RuntimeOptions()
        return self.project_find_uploads_with_options(request, runtime)

    async def project_find_uploads_async(
        self,
        request: holowatcher_20200730_models.ProjectFindUploadsRequest,
    ) -> holowatcher_20200730_models.ProjectFindUploadsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.project_find_uploads_with_options_async(request, runtime)

    def project_get_one_with_options(
        self,
        request: holowatcher_20200730_models.ProjectGetOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectGetOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectGetOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectGetOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_get_one_with_options_async(
        self,
        request: holowatcher_20200730_models.ProjectGetOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectGetOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectGetOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectGetOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_get_one(
        self,
        request: holowatcher_20200730_models.ProjectGetOneRequest,
    ) -> holowatcher_20200730_models.ProjectGetOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.project_get_one_with_options(request, runtime)

    async def project_get_one_async(
        self,
        request: holowatcher_20200730_models.ProjectGetOneRequest,
    ) -> holowatcher_20200730_models.ProjectGetOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.project_get_one_with_options_async(request, runtime)

    def project_get_one_app_with_options(
        self,
        request: holowatcher_20200730_models.ProjectGetOneAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectGetOneAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectGetOneApp',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectGetOneAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_get_one_app_with_options_async(
        self,
        request: holowatcher_20200730_models.ProjectGetOneAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectGetOneAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectGetOneApp',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectGetOneAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_get_one_app(
        self,
        request: holowatcher_20200730_models.ProjectGetOneAppRequest,
    ) -> holowatcher_20200730_models.ProjectGetOneAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.project_get_one_app_with_options(request, runtime)

    async def project_get_one_app_async(
        self,
        request: holowatcher_20200730_models.ProjectGetOneAppRequest,
    ) -> holowatcher_20200730_models.ProjectGetOneAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.project_get_one_app_with_options_async(request, runtime)

    def project_get_status_and_oss_with_options(
        self,
        request: holowatcher_20200730_models.ProjectGetStatusAndOssRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectGetStatusAndOssResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectGetStatusAndOss',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectGetStatusAndOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_get_status_and_oss_with_options_async(
        self,
        request: holowatcher_20200730_models.ProjectGetStatusAndOssRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectGetStatusAndOssResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectGetStatusAndOss',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectGetStatusAndOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_get_status_and_oss(
        self,
        request: holowatcher_20200730_models.ProjectGetStatusAndOssRequest,
    ) -> holowatcher_20200730_models.ProjectGetStatusAndOssResponse:
        runtime = util_models.RuntimeOptions()
        return self.project_get_status_and_oss_with_options(request, runtime)

    async def project_get_status_and_oss_async(
        self,
        request: holowatcher_20200730_models.ProjectGetStatusAndOssRequest,
    ) -> holowatcher_20200730_models.ProjectGetStatusAndOssResponse:
        runtime = util_models.RuntimeOptions()
        return await self.project_get_status_and_oss_with_options_async(request, runtime)

    def project_sync_project_status_with_options(
        self,
        request: holowatcher_20200730_models.ProjectSyncProjectStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectSyncProjectStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectSyncProjectStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectSyncProjectStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def project_sync_project_status_with_options_async(
        self,
        request: holowatcher_20200730_models.ProjectSyncProjectStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ProjectSyncProjectStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProjectSyncProjectStatus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ProjectSyncProjectStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def project_sync_project_status(
        self,
        request: holowatcher_20200730_models.ProjectSyncProjectStatusRequest,
    ) -> holowatcher_20200730_models.ProjectSyncProjectStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.project_sync_project_status_with_options(request, runtime)

    async def project_sync_project_status_async(
        self,
        request: holowatcher_20200730_models.ProjectSyncProjectStatusRequest,
    ) -> holowatcher_20200730_models.ProjectSyncProjectStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.project_sync_project_status_with_options_async(request, runtime)

    def publish_gallery_with_options(
        self,
        request: holowatcher_20200730_models.PublishGalleryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PublishGalleryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishGallery',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PublishGalleryResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_gallery_with_options_async(
        self,
        request: holowatcher_20200730_models.PublishGalleryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PublishGalleryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishGallery',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PublishGalleryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_gallery(
        self,
        request: holowatcher_20200730_models.PublishGalleryRequest,
    ) -> holowatcher_20200730_models.PublishGalleryResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_gallery_with_options(request, runtime)

    async def publish_gallery_async(
        self,
        request: holowatcher_20200730_models.PublishGalleryRequest,
    ) -> holowatcher_20200730_models.PublishGalleryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_gallery_with_options_async(request, runtime)

    def publish_real_with_options(
        self,
        request: holowatcher_20200730_models.PublishRealRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PublishRealResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishReal',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PublishRealResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_real_with_options_async(
        self,
        request: holowatcher_20200730_models.PublishRealRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.PublishRealResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishReal',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.PublishRealResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_real(
        self,
        request: holowatcher_20200730_models.PublishRealRequest,
    ) -> holowatcher_20200730_models.PublishRealResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_real_with_options(request, runtime)

    async def publish_real_async(
        self,
        request: holowatcher_20200730_models.PublishRealRequest,
    ) -> holowatcher_20200730_models.PublishRealResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_real_with_options_async(request, runtime)

    def query_account_label_with_options(
        self,
        request: holowatcher_20200730_models.QueryAccountLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.QueryAccountLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_series):
            query['LabelSeries'] = request.label_series
        if not UtilClient.is_unset(request.pk):
            query['PK'] = request.pk
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountLabel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.QueryAccountLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_label_with_options_async(
        self,
        request: holowatcher_20200730_models.QueryAccountLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.QueryAccountLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_series):
            query['LabelSeries'] = request.label_series
        if not UtilClient.is_unset(request.pk):
            query['PK'] = request.pk
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountLabel',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.QueryAccountLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_label(
        self,
        request: holowatcher_20200730_models.QueryAccountLabelRequest,
    ) -> holowatcher_20200730_models.QueryAccountLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_account_label_with_options(request, runtime)

    async def query_account_label_async(
        self,
        request: holowatcher_20200730_models.QueryAccountLabelRequest,
    ) -> holowatcher_20200730_models.QueryAccountLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_account_label_with_options_async(request, runtime)

    def query_biz_log_by_op_type_and_time_with_options(
        self,
        request: holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizLogByOpTypeAndTime',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_biz_log_by_op_type_and_time_with_options_async(
        self,
        request: holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizLogByOpTypeAndTime',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_biz_log_by_op_type_and_time(
        self,
        request: holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeRequest,
    ) -> holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_biz_log_by_op_type_and_time_with_options(request, runtime)

    async def query_biz_log_by_op_type_and_time_async(
        self,
        request: holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeRequest,
    ) -> holowatcher_20200730_models.QueryBizLogByOpTypeAndTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_biz_log_by_op_type_and_time_with_options_async(request, runtime)

    def query_qrcode_info_with_options(
        self,
        request: holowatcher_20200730_models.QueryQRCodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.QueryQRCodeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sid):
            query['SId'] = request.sid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQRCodeInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.QueryQRCodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_qrcode_info_with_options_async(
        self,
        request: holowatcher_20200730_models.QueryQRCodeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.QueryQRCodeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sid):
            query['SId'] = request.sid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQRCodeInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.QueryQRCodeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_qrcode_info(
        self,
        request: holowatcher_20200730_models.QueryQRCodeInfoRequest,
    ) -> holowatcher_20200730_models.QueryQRCodeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_qrcode_info_with_options(request, runtime)

    async def query_qrcode_info_async(
        self,
        request: holowatcher_20200730_models.QueryQRCodeInfoRequest,
    ) -> holowatcher_20200730_models.QueryQRCodeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_qrcode_info_with_options_async(request, runtime)

    def scan_data_create_project_with_options(
        self,
        tmp_req: holowatcher_20200730_models.ScanDataCreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataCreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.ScanDataCreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_scan_user_data_request):
            request.create_scan_user_data_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_scan_user_data_request), 'CreateScanUserDataRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.create_scan_user_data_request_shrink):
            query['CreateScanUserDataRequest'] = request.create_scan_user_data_request_shrink
        if not UtilClient.is_unset(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataCreateProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataCreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_data_create_project_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.ScanDataCreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataCreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.ScanDataCreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_scan_user_data_request):
            request.create_scan_user_data_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_scan_user_data_request), 'CreateScanUserDataRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.create_scan_user_data_request_shrink):
            query['CreateScanUserDataRequest'] = request.create_scan_user_data_request_shrink
        if not UtilClient.is_unset(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataCreateProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataCreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_data_create_project(
        self,
        request: holowatcher_20200730_models.ScanDataCreateProjectRequest,
    ) -> holowatcher_20200730_models.ScanDataCreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_data_create_project_with_options(request, runtime)

    async def scan_data_create_project_async(
        self,
        request: holowatcher_20200730_models.ScanDataCreateProjectRequest,
    ) -> holowatcher_20200730_models.ScanDataCreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_data_create_project_with_options_async(request, runtime)

    def scan_data_query_project_with_options(
        self,
        request: holowatcher_20200730_models.ScanDataQueryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataQueryProjectResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataQueryProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataQueryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_data_query_project_with_options_async(
        self,
        request: holowatcher_20200730_models.ScanDataQueryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataQueryProjectResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataQueryProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataQueryProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_data_query_project(
        self,
        request: holowatcher_20200730_models.ScanDataQueryProjectRequest,
    ) -> holowatcher_20200730_models.ScanDataQueryProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_data_query_project_with_options(request, runtime)

    async def scan_data_query_project_async(
        self,
        request: holowatcher_20200730_models.ScanDataQueryProjectRequest,
    ) -> holowatcher_20200730_models.ScanDataQueryProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_data_query_project_with_options_async(request, runtime)

    def scan_data_remove_role_with_options(
        self,
        tmp_req: holowatcher_20200730_models.ScanDataRemoveRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataRemoveRoleResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.ScanDataRemoveRoleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remove_user_data_request):
            request.remove_user_data_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.remove_user_data_request), 'RemoveUserDataRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.remove_user_data_request_shrink):
            query['RemoveUserDataRequest'] = request.remove_user_data_request_shrink
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataRemoveRole',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataRemoveRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_data_remove_role_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.ScanDataRemoveRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataRemoveRoleResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.ScanDataRemoveRoleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remove_user_data_request):
            request.remove_user_data_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.remove_user_data_request), 'RemoveUserDataRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.remove_user_data_request_shrink):
            query['RemoveUserDataRequest'] = request.remove_user_data_request_shrink
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataRemoveRole',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataRemoveRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_data_remove_role(
        self,
        request: holowatcher_20200730_models.ScanDataRemoveRoleRequest,
    ) -> holowatcher_20200730_models.ScanDataRemoveRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_data_remove_role_with_options(request, runtime)

    async def scan_data_remove_role_async(
        self,
        request: holowatcher_20200730_models.ScanDataRemoveRoleRequest,
    ) -> holowatcher_20200730_models.ScanDataRemoveRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_data_remove_role_with_options_async(request, runtime)

    def scan_data_share_project_with_options(
        self,
        tmp_req: holowatcher_20200730_models.ScanDataShareProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataShareProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.ScanDataShareProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.share_user_data_request):
            request.share_user_data_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.share_user_data_request), 'ShareUserDataRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.share_user_data_request_shrink):
            query['ShareUserDataRequest'] = request.share_user_data_request_shrink
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataShareProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataShareProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_data_share_project_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.ScanDataShareProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataShareProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.ScanDataShareProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.share_user_data_request):
            request.share_user_data_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.share_user_data_request), 'ShareUserDataRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.share_user_data_request_shrink):
            query['ShareUserDataRequest'] = request.share_user_data_request_shrink
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataShareProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataShareProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_data_share_project(
        self,
        request: holowatcher_20200730_models.ScanDataShareProjectRequest,
    ) -> holowatcher_20200730_models.ScanDataShareProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_data_share_project_with_options(request, runtime)

    async def scan_data_share_project_async(
        self,
        request: holowatcher_20200730_models.ScanDataShareProjectRequest,
    ) -> holowatcher_20200730_models.ScanDataShareProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_data_share_project_with_options_async(request, runtime)

    def scan_data_update_project_with_options(
        self,
        request: holowatcher_20200730_models.ScanDataUpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataUpdateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user_mob_num):
            query['UserMobNum'] = request.user_mob_num
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataUpdateProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataUpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_data_update_project_with_options_async(
        self,
        request: holowatcher_20200730_models.ScanDataUpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ScanDataUpdateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.project_desc):
            query['ProjectDesc'] = request.project_desc
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.user_mob_num):
            query['UserMobNum'] = request.user_mob_num
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScanDataUpdateProject',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ScanDataUpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_data_update_project(
        self,
        request: holowatcher_20200730_models.ScanDataUpdateProjectRequest,
    ) -> holowatcher_20200730_models.ScanDataUpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_data_update_project_with_options(request, runtime)

    async def scan_data_update_project_async(
        self,
        request: holowatcher_20200730_models.ScanDataUpdateProjectRequest,
    ) -> holowatcher_20200730_models.ScanDataUpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_data_update_project_with_options_async(request, runtime)

    def spilt_bim_drawing_with_options(
        self,
        request: holowatcher_20200730_models.SpiltBimDrawingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.SpiltBimDrawingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SpiltBimDrawing',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.SpiltBimDrawingResponse(),
            self.call_api(params, req, runtime)
        )

    async def spilt_bim_drawing_with_options_async(
        self,
        request: holowatcher_20200730_models.SpiltBimDrawingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.SpiltBimDrawingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SpiltBimDrawing',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.SpiltBimDrawingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def spilt_bim_drawing(
        self,
        request: holowatcher_20200730_models.SpiltBimDrawingRequest,
    ) -> holowatcher_20200730_models.SpiltBimDrawingResponse:
        runtime = util_models.RuntimeOptions()
        return self.spilt_bim_drawing_with_options(request, runtime)

    async def spilt_bim_drawing_async(
        self,
        request: holowatcher_20200730_models.SpiltBimDrawingRequest,
    ) -> holowatcher_20200730_models.SpiltBimDrawingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.spilt_bim_drawing_with_options_async(request, runtime)

    def test_pop_params_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.TestPopParamsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='TestPopParams',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.TestPopParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_pop_params_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.TestPopParamsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='TestPopParams',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.TestPopParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_pop_params(self) -> holowatcher_20200730_models.TestPopParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.test_pop_params_with_options(runtime)

    async def test_pop_params_async(self) -> holowatcher_20200730_models.TestPopParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.test_pop_params_with_options_async(runtime)

    def trans_text_to_audio_with_options(
        self,
        request: holowatcher_20200730_models.TransTextToAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.TransTextToAudioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransTextToAudio',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.TransTextToAudioResponse(),
            self.call_api(params, req, runtime)
        )

    async def trans_text_to_audio_with_options_async(
        self,
        request: holowatcher_20200730_models.TransTextToAudioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.TransTextToAudioResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransTextToAudio',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.TransTextToAudioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trans_text_to_audio(
        self,
        request: holowatcher_20200730_models.TransTextToAudioRequest,
    ) -> holowatcher_20200730_models.TransTextToAudioResponse:
        runtime = util_models.RuntimeOptions()
        return self.trans_text_to_audio_with_options(request, runtime)

    async def trans_text_to_audio_async(
        self,
        request: holowatcher_20200730_models.TransTextToAudioRequest,
    ) -> holowatcher_20200730_models.TransTextToAudioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.trans_text_to_audio_with_options_async(request, runtime)

    def update_bim_fragment_with_options(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimFragmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimFragmentResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimFragmentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.coordinates):
            request.coordinates_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.coordinates, 'Coordinates', 'json')
        if not UtilClient.is_unset(tmp_req.floor_info):
            request.floor_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.floor_info), 'FloorInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.building_no):
            query['BuildingNo'] = request.building_no
        if not UtilClient.is_unset(request.coordinates_shrink):
            query['Coordinates'] = request.coordinates_shrink
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.floor_info_shrink):
            query['FloorInfo'] = request.floor_info_shrink
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.selection_mode):
            query['SelectionMode'] = request.selection_mode
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.suffix):
            query['Suffix'] = request.suffix
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimFragment',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimFragmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_bim_fragment_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimFragmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimFragmentResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimFragmentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.coordinates):
            request.coordinates_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.coordinates, 'Coordinates', 'json')
        if not UtilClient.is_unset(tmp_req.floor_info):
            request.floor_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.floor_info), 'FloorInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.building_no):
            query['BuildingNo'] = request.building_no
        if not UtilClient.is_unset(request.coordinates_shrink):
            query['Coordinates'] = request.coordinates_shrink
        if not UtilClient.is_unset(request.drawing_id):
            query['DrawingId'] = request.drawing_id
        if not UtilClient.is_unset(request.floor_info_shrink):
            query['FloorInfo'] = request.floor_info_shrink
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.selection_mode):
            query['SelectionMode'] = request.selection_mode
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.suffix):
            query['Suffix'] = request.suffix
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimFragment',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimFragmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_bim_fragment(
        self,
        request: holowatcher_20200730_models.UpdateBimFragmentRequest,
    ) -> holowatcher_20200730_models.UpdateBimFragmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_bim_fragment_with_options(request, runtime)

    async def update_bim_fragment_async(
        self,
        request: holowatcher_20200730_models.UpdateBimFragmentRequest,
    ) -> holowatcher_20200730_models.UpdateBimFragmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_bim_fragment_with_options_async(request, runtime)

    def update_bim_model_config_with_options(
        self,
        request: holowatcher_20200730_models.UpdateBimModelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimModelConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.beam_height):
            query['BeamHeight'] = request.beam_height
        if not UtilClient.is_unset(request.beam_mode):
            query['BeamMode'] = request.beam_mode
        if not UtilClient.is_unset(request.beam_offset):
            query['BeamOffset'] = request.beam_offset
        if not UtilClient.is_unset(request.door_height):
            query['DoorHeight'] = request.door_height
        if not UtilClient.is_unset(request.door_offset):
            query['DoorOffset'] = request.door_offset
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.room_mode):
            query['RoomMode'] = request.room_mode
        if not UtilClient.is_unset(request.slab_mode):
            query['SlabMode'] = request.slab_mode
        if not UtilClient.is_unset(request.slab_thickness):
            query['SlabThickness'] = request.slab_thickness
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.window_height):
            query['WindowHeight'] = request.window_height
        if not UtilClient.is_unset(request.window_offset):
            query['WindowOffset'] = request.window_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimModelConfig',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimModelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_bim_model_config_with_options_async(
        self,
        request: holowatcher_20200730_models.UpdateBimModelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimModelConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.beam_height):
            query['BeamHeight'] = request.beam_height
        if not UtilClient.is_unset(request.beam_mode):
            query['BeamMode'] = request.beam_mode
        if not UtilClient.is_unset(request.beam_offset):
            query['BeamOffset'] = request.beam_offset
        if not UtilClient.is_unset(request.door_height):
            query['DoorHeight'] = request.door_height
        if not UtilClient.is_unset(request.door_offset):
            query['DoorOffset'] = request.door_offset
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.room_mode):
            query['RoomMode'] = request.room_mode
        if not UtilClient.is_unset(request.slab_mode):
            query['SlabMode'] = request.slab_mode
        if not UtilClient.is_unset(request.slab_thickness):
            query['SlabThickness'] = request.slab_thickness
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.window_height):
            query['WindowHeight'] = request.window_height
        if not UtilClient.is_unset(request.window_offset):
            query['WindowOffset'] = request.window_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimModelConfig',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimModelConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_bim_model_config(
        self,
        request: holowatcher_20200730_models.UpdateBimModelConfigRequest,
    ) -> holowatcher_20200730_models.UpdateBimModelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_bim_model_config_with_options(request, runtime)

    async def update_bim_model_config_async(
        self,
        request: holowatcher_20200730_models.UpdateBimModelConfigRequest,
    ) -> holowatcher_20200730_models.UpdateBimModelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_bim_model_config_with_options_async(request, runtime)

    def update_bim_project_draw_files_with_options(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimProjectDrawFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimProjectDrawFilesResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimProjectDrawFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.architecture_files):
            request.architecture_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.architecture_files, 'ArchitectureFiles', 'json')
        if not UtilClient.is_unset(tmp_req.structure_files):
            request.structure_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.structure_files, 'StructureFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.architecture_files_shrink):
            query['ArchitectureFiles'] = request.architecture_files_shrink
        if not UtilClient.is_unset(request.structure_files_shrink):
            query['StructureFiles'] = request.structure_files_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimProjectDrawFiles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimProjectDrawFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_bim_project_draw_files_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimProjectDrawFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimProjectDrawFilesResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimProjectDrawFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.architecture_files):
            request.architecture_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.architecture_files, 'ArchitectureFiles', 'json')
        if not UtilClient.is_unset(tmp_req.structure_files):
            request.structure_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.structure_files, 'StructureFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.architecture_files_shrink):
            query['ArchitectureFiles'] = request.architecture_files_shrink
        if not UtilClient.is_unset(request.structure_files_shrink):
            query['StructureFiles'] = request.structure_files_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimProjectDrawFiles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimProjectDrawFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_bim_project_draw_files(
        self,
        request: holowatcher_20200730_models.UpdateBimProjectDrawFilesRequest,
    ) -> holowatcher_20200730_models.UpdateBimProjectDrawFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_bim_project_draw_files_with_options(request, runtime)

    async def update_bim_project_draw_files_async(
        self,
        request: holowatcher_20200730_models.UpdateBimProjectDrawFilesRequest,
    ) -> holowatcher_20200730_models.UpdateBimProjectDrawFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_bim_project_draw_files_with_options_async(request, runtime)

    def update_bim_standard_dw_info_with_options(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimStandardDwInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimStandardDwInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimStandardDwInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data):
            request.data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_shrink):
            query['Data'] = request.data_shrink
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimStandardDwInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimStandardDwInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_bim_standard_dw_info_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimStandardDwInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimStandardDwInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimStandardDwInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data):
            request.data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_shrink):
            query['Data'] = request.data_shrink
        if not UtilClient.is_unset(request.keys_shrink):
            query['Keys'] = request.keys_shrink
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimStandardDwInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimStandardDwInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_bim_standard_dw_info(
        self,
        request: holowatcher_20200730_models.UpdateBimStandardDwInfoRequest,
    ) -> holowatcher_20200730_models.UpdateBimStandardDwInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_bim_standard_dw_info_with_options(request, runtime)

    async def update_bim_standard_dw_info_async(
        self,
        request: holowatcher_20200730_models.UpdateBimStandardDwInfoRequest,
    ) -> holowatcher_20200730_models.UpdateBimStandardDwInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_bim_standard_dw_info_with_options_async(request, runtime)

    def update_bim_standard_elevation_with_options(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimStandardElevationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimStandardElevationResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimStandardElevationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.floors):
            request.floors_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.floors, 'Floors', 'json')
        query = {}
        if not UtilClient.is_unset(request.floors_shrink):
            query['Floors'] = request.floors_shrink
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.terrace_height):
            query['TerraceHeight'] = request.terrace_height
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimStandardElevation',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimStandardElevationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_bim_standard_elevation_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimStandardElevationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimStandardElevationResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimStandardElevationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.floors):
            request.floors_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.floors, 'Floors', 'json')
        query = {}
        if not UtilClient.is_unset(request.floors_shrink):
            query['Floors'] = request.floors_shrink
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.terrace_height):
            query['TerraceHeight'] = request.terrace_height
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimStandardElevation',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimStandardElevationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_bim_standard_elevation(
        self,
        request: holowatcher_20200730_models.UpdateBimStandardElevationRequest,
    ) -> holowatcher_20200730_models.UpdateBimStandardElevationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_bim_standard_elevation_with_options(request, runtime)

    async def update_bim_standard_elevation_async(
        self,
        request: holowatcher_20200730_models.UpdateBimStandardElevationRequest,
    ) -> holowatcher_20200730_models.UpdateBimStandardElevationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_bim_standard_elevation_with_options_async(request, runtime)

    def update_bim_standard_slab_info_with_options(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimStandardSlabInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimStandardSlabInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimStandardSlabInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.legends):
            request.legends_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.legends, 'Legends', 'json')
        query = {}
        if not UtilClient.is_unset(request.legends_shrink):
            query['Legends'] = request.legends_shrink
        if not UtilClient.is_unset(request.root_dir):
            query['RootDir'] = request.root_dir
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.thickness):
            query['Thickness'] = request.thickness
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimStandardSlabInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimStandardSlabInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_bim_standard_slab_info_with_options_async(
        self,
        tmp_req: holowatcher_20200730_models.UpdateBimStandardSlabInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateBimStandardSlabInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = holowatcher_20200730_models.UpdateBimStandardSlabInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.legends):
            request.legends_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.legends, 'Legends', 'json')
        query = {}
        if not UtilClient.is_unset(request.legends_shrink):
            query['Legends'] = request.legends_shrink
        if not UtilClient.is_unset(request.root_dir):
            query['RootDir'] = request.root_dir
        if not UtilClient.is_unset(request.standard_id):
            query['StandardId'] = request.standard_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.thickness):
            query['Thickness'] = request.thickness
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBimStandardSlabInfo',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateBimStandardSlabInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_bim_standard_slab_info(
        self,
        request: holowatcher_20200730_models.UpdateBimStandardSlabInfoRequest,
    ) -> holowatcher_20200730_models.UpdateBimStandardSlabInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_bim_standard_slab_info_with_options(request, runtime)

    async def update_bim_standard_slab_info_async(
        self,
        request: holowatcher_20200730_models.UpdateBimStandardSlabInfoRequest,
    ) -> holowatcher_20200730_models.UpdateBimStandardSlabInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_bim_standard_slab_info_with_options_async(request, runtime)

    def update_note_with_options(
        self,
        request: holowatcher_20200730_models.UpdateNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateNoteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNote',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateNoteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_note_with_options_async(
        self,
        request: holowatcher_20200730_models.UpdateNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateNoteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNote',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateNoteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_note(
        self,
        request: holowatcher_20200730_models.UpdateNoteRequest,
    ) -> holowatcher_20200730_models.UpdateNoteResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_note_with_options(request, runtime)

    async def update_note_async(
        self,
        request: holowatcher_20200730_models.UpdateNoteRequest,
    ) -> holowatcher_20200730_models.UpdateNoteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_note_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: holowatcher_20200730_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: holowatcher_20200730_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: holowatcher_20200730_models.UpdateUserRequest,
    ) -> holowatcher_20200730_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: holowatcher_20200730_models.UpdateUserRequest,
    ) -> holowatcher_20200730_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def user_find_all_with_options(
        self,
        request: holowatcher_20200730_models.UserFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserFindAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_find_all_with_options_async(
        self,
        request: holowatcher_20200730_models.UserFindAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserFindAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserFindAll',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserFindAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_find_all(
        self,
        request: holowatcher_20200730_models.UserFindAllRequest,
    ) -> holowatcher_20200730_models.UserFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.user_find_all_with_options(request, runtime)

    async def user_find_all_async(
        self,
        request: holowatcher_20200730_models.UserFindAllRequest,
    ) -> holowatcher_20200730_models.UserFindAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.user_find_all_with_options_async(request, runtime)

    def user_find_by_roles_with_options(
        self,
        request: holowatcher_20200730_models.UserFindByRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserFindByRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.role_names):
            query['RoleNames'] = request.role_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserFindByRoles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserFindByRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_find_by_roles_with_options_async(
        self,
        request: holowatcher_20200730_models.UserFindByRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserFindByRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.role_names):
            query['RoleNames'] = request.role_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserFindByRoles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserFindByRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_find_by_roles(
        self,
        request: holowatcher_20200730_models.UserFindByRolesRequest,
    ) -> holowatcher_20200730_models.UserFindByRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.user_find_by_roles_with_options(request, runtime)

    async def user_find_by_roles_async(
        self,
        request: holowatcher_20200730_models.UserFindByRolesRequest,
    ) -> holowatcher_20200730_models.UserFindByRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.user_find_by_roles_with_options_async(request, runtime)

    def user_get_one_with_options(
        self,
        request: holowatcher_20200730_models.UserGetOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserGetOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserGetOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserGetOneResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_get_one_with_options_async(
        self,
        request: holowatcher_20200730_models.UserGetOneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserGetOneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserGetOne',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserGetOneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_get_one(
        self,
        request: holowatcher_20200730_models.UserGetOneRequest,
    ) -> holowatcher_20200730_models.UserGetOneResponse:
        runtime = util_models.RuntimeOptions()
        return self.user_get_one_with_options(request, runtime)

    async def user_get_one_async(
        self,
        request: holowatcher_20200730_models.UserGetOneRequest,
    ) -> holowatcher_20200730_models.UserGetOneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.user_get_one_with_options_async(request, runtime)

    def user_list_menus_with_options(
        self,
        request: holowatcher_20200730_models.UserListMenusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserListMenusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserListMenus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserListMenusResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_list_menus_with_options_async(
        self,
        request: holowatcher_20200730_models.UserListMenusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserListMenusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserListMenus',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserListMenusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_list_menus(
        self,
        request: holowatcher_20200730_models.UserListMenusRequest,
    ) -> holowatcher_20200730_models.UserListMenusResponse:
        runtime = util_models.RuntimeOptions()
        return self.user_list_menus_with_options(request, runtime)

    async def user_list_menus_async(
        self,
        request: holowatcher_20200730_models.UserListMenusRequest,
    ) -> holowatcher_20200730_models.UserListMenusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.user_list_menus_with_options_async(request, runtime)

    def user_list_permissions_with_options(
        self,
        request: holowatcher_20200730_models.UserListPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserListPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserListPermissions',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_list_permissions_with_options_async(
        self,
        request: holowatcher_20200730_models.UserListPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserListPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserListPermissions',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserListPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_list_permissions(
        self,
        request: holowatcher_20200730_models.UserListPermissionsRequest,
    ) -> holowatcher_20200730_models.UserListPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.user_list_permissions_with_options(request, runtime)

    async def user_list_permissions_async(
        self,
        request: holowatcher_20200730_models.UserListPermissionsRequest,
    ) -> holowatcher_20200730_models.UserListPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.user_list_permissions_with_options_async(request, runtime)

    def user_list_roles_with_options(
        self,
        request: holowatcher_20200730_models.UserListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserListRoles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_list_roles_with_options_async(
        self,
        request: holowatcher_20200730_models.UserListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserListRoles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_list_roles(
        self,
        request: holowatcher_20200730_models.UserListRolesRequest,
    ) -> holowatcher_20200730_models.UserListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.user_list_roles_with_options(request, runtime)

    async def user_list_roles_async(
        self,
        request: holowatcher_20200730_models.UserListRolesRequest,
    ) -> holowatcher_20200730_models.UserListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.user_list_roles_with_options_async(request, runtime)

    def user_list_sub_roles_with_options(
        self,
        request: holowatcher_20200730_models.UserListSubRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserListSubRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserListSubRoles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserListSubRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_list_sub_roles_with_options_async(
        self,
        request: holowatcher_20200730_models.UserListSubRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.UserListSubRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UserListSubRoles',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.UserListSubRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_list_sub_roles(
        self,
        request: holowatcher_20200730_models.UserListSubRolesRequest,
    ) -> holowatcher_20200730_models.UserListSubRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.user_list_sub_roles_with_options(request, runtime)

    async def user_list_sub_roles_async(
        self,
        request: holowatcher_20200730_models.UserListSubRolesRequest,
    ) -> holowatcher_20200730_models.UserListSubRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.user_list_sub_roles_with_options_async(request, runtime)

    def valid_aliyun_uid_with_options(
        self,
        request: holowatcher_20200730_models.ValidAliyunUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ValidAliyunUidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidAliyunUid',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ValidAliyunUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def valid_aliyun_uid_with_options_async(
        self,
        request: holowatcher_20200730_models.ValidAliyunUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ValidAliyunUidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.aliyun_uid):
            query['AliyunUid'] = request.aliyun_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidAliyunUid',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ValidAliyunUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def valid_aliyun_uid(
        self,
        request: holowatcher_20200730_models.ValidAliyunUidRequest,
    ) -> holowatcher_20200730_models.ValidAliyunUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.valid_aliyun_uid_with_options(request, runtime)

    async def valid_aliyun_uid_async(
        self,
        request: holowatcher_20200730_models.ValidAliyunUidRequest,
    ) -> holowatcher_20200730_models.ValidAliyunUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.valid_aliyun_uid_with_options_async(request, runtime)

    def valid_company_name_with_options(
        self,
        request: holowatcher_20200730_models.ValidCompanyNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ValidCompanyNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidCompanyName',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ValidCompanyNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def valid_company_name_with_options_async(
        self,
        request: holowatcher_20200730_models.ValidCompanyNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.ValidCompanyNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_jwt):
            query['AliyunJwt'] = request.aliyun_jwt
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidCompanyName',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.ValidCompanyNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def valid_company_name(
        self,
        request: holowatcher_20200730_models.ValidCompanyNameRequest,
    ) -> holowatcher_20200730_models.ValidCompanyNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.valid_company_name_with_options(request, runtime)

    async def valid_company_name_async(
        self,
        request: holowatcher_20200730_models.ValidCompanyNameRequest,
    ) -> holowatcher_20200730_models.ValidCompanyNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.valid_company_name_with_options_async(request, runtime)

    def vr_user_create_scan_user_with_options(
        self,
        request: holowatcher_20200730_models.VrUserCreateScanUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.VrUserCreateScanUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VrUserCreateScanUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.VrUserCreateScanUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def vr_user_create_scan_user_with_options_async(
        self,
        request: holowatcher_20200730_models.VrUserCreateScanUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> holowatcher_20200730_models.VrUserCreateScanUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_order_no):
            query['BizOrderNo'] = request.biz_order_no
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VrUserCreateScanUser',
            version='2020-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            holowatcher_20200730_models.VrUserCreateScanUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vr_user_create_scan_user(
        self,
        request: holowatcher_20200730_models.VrUserCreateScanUserRequest,
    ) -> holowatcher_20200730_models.VrUserCreateScanUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.vr_user_create_scan_user_with_options(request, runtime)

    async def vr_user_create_scan_user_async(
        self,
        request: holowatcher_20200730_models.VrUserCreateScanUserRequest,
    ) -> holowatcher_20200730_models.VrUserCreateScanUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vr_user_create_scan_user_with_options_async(request, runtime)
