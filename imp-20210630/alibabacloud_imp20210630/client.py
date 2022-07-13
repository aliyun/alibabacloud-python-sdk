# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imp20210630 import models as imp_20210630_models
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
        self._endpoint = self.get_endpoint('imp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def ban_all_comment_with_options(
        self,
        request: imp_20210630_models.BanAllCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.BanAllCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BanAllComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.BanAllCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def ban_all_comment_with_options_async(
        self,
        request: imp_20210630_models.BanAllCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.BanAllCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BanAllComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.BanAllCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ban_all_comment(
        self,
        request: imp_20210630_models.BanAllCommentRequest,
    ) -> imp_20210630_models.BanAllCommentResponse:
        runtime = util_models.RuntimeOptions()
        return self.ban_all_comment_with_options(request, runtime)

    async def ban_all_comment_async(
        self,
        request: imp_20210630_models.BanAllCommentRequest,
    ) -> imp_20210630_models.BanAllCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ban_all_comment_with_options_async(request, runtime)

    def ban_comment_with_options(
        self,
        request: imp_20210630_models.BanCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.BanCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ban_comment_time):
            body['BanCommentTime'] = request.ban_comment_time
        if not UtilClient.is_unset(request.ban_comment_user):
            body['BanCommentUser'] = request.ban_comment_user
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BanComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.BanCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def ban_comment_with_options_async(
        self,
        request: imp_20210630_models.BanCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.BanCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ban_comment_time):
            body['BanCommentTime'] = request.ban_comment_time
        if not UtilClient.is_unset(request.ban_comment_user):
            body['BanCommentUser'] = request.ban_comment_user
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BanComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.BanCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ban_comment(
        self,
        request: imp_20210630_models.BanCommentRequest,
    ) -> imp_20210630_models.BanCommentResponse:
        runtime = util_models.RuntimeOptions()
        return self.ban_comment_with_options(request, runtime)

    async def ban_comment_async(
        self,
        request: imp_20210630_models.BanCommentRequest,
    ) -> imp_20210630_models.BanCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ban_comment_with_options_async(request, runtime)

    def cancel_ban_all_comment_with_options(
        self,
        request: imp_20210630_models.CancelBanAllCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CancelBanAllCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelBanAllComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelBanAllCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_ban_all_comment_with_options_async(
        self,
        request: imp_20210630_models.CancelBanAllCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CancelBanAllCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelBanAllComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelBanAllCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_ban_all_comment(
        self,
        request: imp_20210630_models.CancelBanAllCommentRequest,
    ) -> imp_20210630_models.CancelBanAllCommentResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_ban_all_comment_with_options(request, runtime)

    async def cancel_ban_all_comment_async(
        self,
        request: imp_20210630_models.CancelBanAllCommentRequest,
    ) -> imp_20210630_models.CancelBanAllCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_ban_all_comment_with_options_async(request, runtime)

    def cancel_ban_comment_with_options(
        self,
        request: imp_20210630_models.CancelBanCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CancelBanCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ban_comment_user):
            body['BanCommentUser'] = request.ban_comment_user
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelBanComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelBanCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_ban_comment_with_options_async(
        self,
        request: imp_20210630_models.CancelBanCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CancelBanCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ban_comment_user):
            body['BanCommentUser'] = request.ban_comment_user
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelBanComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelBanCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_ban_comment(
        self,
        request: imp_20210630_models.CancelBanCommentRequest,
    ) -> imp_20210630_models.CancelBanCommentResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_ban_comment_with_options(request, runtime)

    async def cancel_ban_comment_async(
        self,
        request: imp_20210630_models.CancelBanCommentRequest,
    ) -> imp_20210630_models.CancelBanCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_ban_comment_with_options_async(request, runtime)

    def cancel_user_admin_with_options(
        self,
        request: imp_20210630_models.CancelUserAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CancelUserAdminResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelUserAdmin',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelUserAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_user_admin_with_options_async(
        self,
        request: imp_20210630_models.CancelUserAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CancelUserAdminResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelUserAdmin',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CancelUserAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_user_admin(
        self,
        request: imp_20210630_models.CancelUserAdminRequest,
    ) -> imp_20210630_models.CancelUserAdminResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_user_admin_with_options(request, runtime)

    async def cancel_user_admin_async(
        self,
        request: imp_20210630_models.CancelUserAdminRequest,
    ) -> imp_20210630_models.CancelUserAdminResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_user_admin_with_options_async(request, runtime)

    def create_class_with_options(
        self,
        request: imp_20210630_models.CreateClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.create_nickname):
            body['CreateNickname'] = request.create_nickname
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_class_with_options_async(
        self,
        request: imp_20210630_models.CreateClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.create_nickname):
            body['CreateNickname'] = request.create_nickname
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_class(
        self,
        request: imp_20210630_models.CreateClassRequest,
    ) -> imp_20210630_models.CreateClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_class_with_options(request, runtime)

    async def create_class_async(
        self,
        request: imp_20210630_models.CreateClassRequest,
    ) -> imp_20210630_models.CreateClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_class_with_options_async(request, runtime)

    def create_live_with_options(
        self,
        request: imp_20210630_models.CreateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.anchor_id):
            body['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.code_level):
            body['CodeLevel'] = request.code_level
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_with_options_async(
        self,
        request: imp_20210630_models.CreateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.anchor_id):
            body['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.code_level):
            body['CodeLevel'] = request.code_level
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live(
        self,
        request: imp_20210630_models.CreateLiveRequest,
    ) -> imp_20210630_models.CreateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_with_options(request, runtime)

    async def create_live_async(
        self,
        request: imp_20210630_models.CreateLiveRequest,
    ) -> imp_20210630_models.CreateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_with_options_async(request, runtime)

    def create_live_record_slice_file_with_options(
        self,
        request: imp_20210630_models.CreateLiveRecordSliceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateLiveRecordSliceFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveRecordSliceFile',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveRecordSliceFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_record_slice_file_with_options_async(
        self,
        request: imp_20210630_models.CreateLiveRecordSliceFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateLiveRecordSliceFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveRecordSliceFile',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveRecordSliceFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live_record_slice_file(
        self,
        request: imp_20210630_models.CreateLiveRecordSliceFileRequest,
    ) -> imp_20210630_models.CreateLiveRecordSliceFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_record_slice_file_with_options(request, runtime)

    async def create_live_record_slice_file_async(
        self,
        request: imp_20210630_models.CreateLiveRecordSliceFileRequest,
    ) -> imp_20210630_models.CreateLiveRecordSliceFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_record_slice_file_with_options_async(request, runtime)

    def create_live_room_with_options(
        self,
        tmp_req: imp_20210630_models.CreateLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateLiveRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateLiveRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.anchor_id):
            body['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.anchor_nick):
            body['AnchorNick'] = request.anchor_nick
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.enable_link_mic):
            body['EnableLinkMic'] = request.enable_link_mic
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_room_with_options_async(
        self,
        tmp_req: imp_20210630_models.CreateLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateLiveRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateLiveRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.anchor_id):
            body['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.anchor_nick):
            body['AnchorNick'] = request.anchor_nick
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.enable_link_mic):
            body['EnableLinkMic'] = request.enable_link_mic
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateLiveRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live_room(
        self,
        request: imp_20210630_models.CreateLiveRoomRequest,
    ) -> imp_20210630_models.CreateLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_room_with_options(request, runtime)

    async def create_live_room_async(
        self,
        request: imp_20210630_models.CreateLiveRoomRequest,
    ) -> imp_20210630_models.CreateLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_room_with_options_async(request, runtime)

    def create_room_with_options(
        self,
        tmp_req: imp_20210630_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_owner_id):
            body['RoomOwnerId'] = request.room_owner_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_room_with_options_async(
        self,
        tmp_req: imp_20210630_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_owner_id):
            body['RoomOwnerId'] = request.room_owner_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_room(
        self,
        request: imp_20210630_models.CreateRoomRequest,
    ) -> imp_20210630_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    async def create_room_async(
        self,
        request: imp_20210630_models.CreateRoomRequest,
    ) -> imp_20210630_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_room_with_options_async(request, runtime)

    def create_sensitive_word_with_options(
        self,
        tmp_req: imp_20210630_models.CreateSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateSensitiveWordResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateSensitiveWordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.word_list):
            request.word_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.word_list, 'WordList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.word_list_shrink):
            body['WordList'] = request.word_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSensitiveWord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sensitive_word_with_options_async(
        self,
        tmp_req: imp_20210630_models.CreateSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateSensitiveWordResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateSensitiveWordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.word_list):
            request.word_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.word_list, 'WordList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.word_list_shrink):
            body['WordList'] = request.word_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSensitiveWord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.CreateSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sensitive_word(
        self,
        request: imp_20210630_models.CreateSensitiveWordRequest,
    ) -> imp_20210630_models.CreateSensitiveWordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sensitive_word_with_options(request, runtime)

    async def create_sensitive_word_async(
        self,
        request: imp_20210630_models.CreateSensitiveWordRequest,
    ) -> imp_20210630_models.CreateSensitiveWordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sensitive_word_with_options_async(request, runtime)

    def delete_class_with_options(
        self,
        request: imp_20210630_models.DeleteClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_class_with_options_async(
        self,
        request: imp_20210630_models.DeleteClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_class(
        self,
        request: imp_20210630_models.DeleteClassRequest,
    ) -> imp_20210630_models.DeleteClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_class_with_options(request, runtime)

    async def delete_class_async(
        self,
        request: imp_20210630_models.DeleteClassRequest,
    ) -> imp_20210630_models.DeleteClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_class_with_options_async(request, runtime)

    def delete_comment_with_options(
        self,
        request: imp_20210630_models.DeleteCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        body_flat = {}
        if not UtilClient.is_unset(request.comment_id_list):
            body_flat['CommentIdList'] = request.comment_id_list
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_comment_with_options_async(
        self,
        request: imp_20210630_models.DeleteCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteCommentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        body_flat = {}
        if not UtilClient.is_unset(request.comment_id_list):
            body_flat['CommentIdList'] = request.comment_id_list
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_comment(
        self,
        request: imp_20210630_models.DeleteCommentRequest,
    ) -> imp_20210630_models.DeleteCommentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_comment_with_options(request, runtime)

    async def delete_comment_async(
        self,
        request: imp_20210630_models.DeleteCommentRequest,
    ) -> imp_20210630_models.DeleteCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_comment_with_options_async(request, runtime)

    def delete_comment_by_creator_id_with_options(
        self,
        request: imp_20210630_models.DeleteCommentByCreatorIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteCommentByCreatorIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        body_flat = {}
        if not UtilClient.is_unset(request.comment_id_list):
            body_flat['CommentIdList'] = request.comment_id_list
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCommentByCreatorId',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteCommentByCreatorIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_comment_by_creator_id_with_options_async(
        self,
        request: imp_20210630_models.DeleteCommentByCreatorIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteCommentByCreatorIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        body_flat = {}
        if not UtilClient.is_unset(request.comment_id_list):
            body_flat['CommentIdList'] = request.comment_id_list
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCommentByCreatorId',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteCommentByCreatorIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_comment_by_creator_id(
        self,
        request: imp_20210630_models.DeleteCommentByCreatorIdRequest,
    ) -> imp_20210630_models.DeleteCommentByCreatorIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_comment_by_creator_id_with_options(request, runtime)

    async def delete_comment_by_creator_id_async(
        self,
        request: imp_20210630_models.DeleteCommentByCreatorIdRequest,
    ) -> imp_20210630_models.DeleteCommentByCreatorIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_comment_by_creator_id_with_options_async(request, runtime)

    def delete_conference_with_options(
        self,
        request: imp_20210630_models.DeleteConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConference',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_conference_with_options_async(
        self,
        request: imp_20210630_models.DeleteConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConference',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_conference(
        self,
        request: imp_20210630_models.DeleteConferenceRequest,
    ) -> imp_20210630_models.DeleteConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_conference_with_options(request, runtime)

    async def delete_conference_async(
        self,
        request: imp_20210630_models.DeleteConferenceRequest,
    ) -> imp_20210630_models.DeleteConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_conference_with_options_async(request, runtime)

    def delete_live_with_options(
        self,
        request: imp_20210630_models.DeleteLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_with_options_async(
        self,
        request: imp_20210630_models.DeleteLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live(
        self,
        request: imp_20210630_models.DeleteLiveRequest,
    ) -> imp_20210630_models.DeleteLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_with_options(request, runtime)

    async def delete_live_async(
        self,
        request: imp_20210630_models.DeleteLiveRequest,
    ) -> imp_20210630_models.DeleteLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_with_options_async(request, runtime)

    def delete_live_room_with_options(
        self,
        request: imp_20210630_models.DeleteLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteLiveRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_room_with_options_async(
        self,
        request: imp_20210630_models.DeleteLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteLiveRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteLiveRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_room(
        self,
        request: imp_20210630_models.DeleteLiveRoomRequest,
    ) -> imp_20210630_models.DeleteLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_room_with_options(request, runtime)

    async def delete_live_room_async(
        self,
        request: imp_20210630_models.DeleteLiveRoomRequest,
    ) -> imp_20210630_models.DeleteLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_room_with_options_async(request, runtime)

    def delete_record_file_info_with_options(
        self,
        request: imp_20210630_models.DeleteRecordFileInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteRecordFileInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordFileInfo',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteRecordFileInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_file_info_with_options_async(
        self,
        request: imp_20210630_models.DeleteRecordFileInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteRecordFileInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordFileInfo',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteRecordFileInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_record_file_info(
        self,
        request: imp_20210630_models.DeleteRecordFileInfoRequest,
    ) -> imp_20210630_models.DeleteRecordFileInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_record_file_info_with_options(request, runtime)

    async def delete_record_file_info_async(
        self,
        request: imp_20210630_models.DeleteRecordFileInfoRequest,
    ) -> imp_20210630_models.DeleteRecordFileInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_record_file_info_with_options_async(request, runtime)

    def delete_room_with_options(
        self,
        request: imp_20210630_models.DeleteRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_room_with_options_async(
        self,
        request: imp_20210630_models.DeleteRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_room(
        self,
        request: imp_20210630_models.DeleteRoomRequest,
    ) -> imp_20210630_models.DeleteRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_room_with_options(request, runtime)

    async def delete_room_async(
        self,
        request: imp_20210630_models.DeleteRoomRequest,
    ) -> imp_20210630_models.DeleteRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_room_with_options_async(request, runtime)

    def delete_sensitive_word_with_options(
        self,
        tmp_req: imp_20210630_models.DeleteSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteSensitiveWordResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.DeleteSensitiveWordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.word_list):
            request.word_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.word_list, 'WordList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.word_list_shrink):
            body['WordList'] = request.word_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSensitiveWord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sensitive_word_with_options_async(
        self,
        tmp_req: imp_20210630_models.DeleteSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteSensitiveWordResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.DeleteSensitiveWordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.word_list):
            request.word_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.word_list, 'WordList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.word_list_shrink):
            body['WordList'] = request.word_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSensitiveWord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DeleteSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sensitive_word(
        self,
        request: imp_20210630_models.DeleteSensitiveWordRequest,
    ) -> imp_20210630_models.DeleteSensitiveWordResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sensitive_word_with_options(request, runtime)

    async def delete_sensitive_word_async(
        self,
        request: imp_20210630_models.DeleteSensitiveWordRequest,
    ) -> imp_20210630_models.DeleteSensitiveWordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sensitive_word_with_options_async(request, runtime)

    def describe_meter_imp_play_back_time_by_live_id_with_options(
        self,
        request: imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.live_id):
            query['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImpPlayBackTimeByLiveId',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_imp_play_back_time_by_live_id_with_options_async(
        self,
        request: imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.live_id):
            query['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImpPlayBackTimeByLiveId',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_imp_play_back_time_by_live_id(
        self,
        request: imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdRequest,
    ) -> imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_imp_play_back_time_by_live_id_with_options(request, runtime)

    async def describe_meter_imp_play_back_time_by_live_id_async(
        self,
        request: imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdRequest,
    ) -> imp_20210630_models.DescribeMeterImpPlayBackTimeByLiveIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_imp_play_back_time_by_live_id_with_options_async(request, runtime)

    def describe_meter_imp_watch_live_time_by_live_id_with_options(
        self,
        request: imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            query['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImpWatchLiveTimeByLiveId',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_imp_watch_live_time_by_live_id_with_options_async(
        self,
        request: imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            query['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImpWatchLiveTimeByLiveId',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_imp_watch_live_time_by_live_id(
        self,
        request: imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdRequest,
    ) -> imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_imp_watch_live_time_by_live_id_with_options(request, runtime)

    async def describe_meter_imp_watch_live_time_by_live_id_async(
        self,
        request: imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdRequest,
    ) -> imp_20210630_models.DescribeMeterImpWatchLiveTimeByLiveIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_imp_watch_live_time_by_live_id_with_options_async(request, runtime)

    def get_auth_token_with_options(
        self,
        request: imp_20210630_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAuthTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAuthToken',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auth_token_with_options_async(
        self,
        request: imp_20210630_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAuthTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAuthToken',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetAuthTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auth_token(
        self,
        request: imp_20210630_models.GetAuthTokenRequest,
    ) -> imp_20210630_models.GetAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    async def get_auth_token_async(
        self,
        request: imp_20210630_models.GetAuthTokenRequest,
    ) -> imp_20210630_models.GetAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auth_token_with_options_async(request, runtime)

    def get_class_detail_with_options(
        self,
        request: imp_20210630_models.GetClassDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetClassDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClassDetail',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetClassDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_class_detail_with_options_async(
        self,
        request: imp_20210630_models.GetClassDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetClassDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClassDetail',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetClassDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_class_detail(
        self,
        request: imp_20210630_models.GetClassDetailRequest,
    ) -> imp_20210630_models.GetClassDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_class_detail_with_options(request, runtime)

    async def get_class_detail_async(
        self,
        request: imp_20210630_models.GetClassDetailRequest,
    ) -> imp_20210630_models.GetClassDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_class_detail_with_options_async(request, runtime)

    def get_class_record_with_options(
        self,
        request: imp_20210630_models.GetClassRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetClassRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClassRecord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetClassRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_class_record_with_options_async(
        self,
        request: imp_20210630_models.GetClassRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetClassRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClassRecord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetClassRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_class_record(
        self,
        request: imp_20210630_models.GetClassRecordRequest,
    ) -> imp_20210630_models.GetClassRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_class_record_with_options(request, runtime)

    async def get_class_record_async(
        self,
        request: imp_20210630_models.GetClassRecordRequest,
    ) -> imp_20210630_models.GetClassRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_class_record_with_options_async(request, runtime)

    def get_conference_with_options(
        self,
        request: imp_20210630_models.GetConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConference',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conference_with_options_async(
        self,
        request: imp_20210630_models.GetConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConference',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conference(
        self,
        request: imp_20210630_models.GetConferenceRequest,
    ) -> imp_20210630_models.GetConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_conference_with_options(request, runtime)

    async def get_conference_async(
        self,
        request: imp_20210630_models.GetConferenceRequest,
    ) -> imp_20210630_models.GetConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_conference_with_options_async(request, runtime)

    def get_live_with_options(
        self,
        request: imp_20210630_models.GetLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_with_options_async(
        self,
        request: imp_20210630_models.GetLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live(
        self,
        request: imp_20210630_models.GetLiveRequest,
    ) -> imp_20210630_models.GetLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_with_options(request, runtime)

    async def get_live_async(
        self,
        request: imp_20210630_models.GetLiveRequest,
    ) -> imp_20210630_models.GetLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_with_options_async(request, runtime)

    def get_live_record_with_options(
        self,
        request: imp_20210630_models.GetLiveRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRecord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_record_with_options_async(
        self,
        request: imp_20210630_models.GetLiveRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveRecordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRecord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_record(
        self,
        request: imp_20210630_models.GetLiveRecordRequest,
    ) -> imp_20210630_models.GetLiveRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_record_with_options(request, runtime)

    async def get_live_record_async(
        self,
        request: imp_20210630_models.GetLiveRecordRequest,
    ) -> imp_20210630_models.GetLiveRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_record_with_options_async(request, runtime)

    def get_live_room_with_options(
        self,
        request: imp_20210630_models.GetLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_room_with_options_async(
        self,
        request: imp_20210630_models.GetLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_room(
        self,
        request: imp_20210630_models.GetLiveRoomRequest,
    ) -> imp_20210630_models.GetLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_room_with_options(request, runtime)

    async def get_live_room_async(
        self,
        request: imp_20210630_models.GetLiveRoomRequest,
    ) -> imp_20210630_models.GetLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_room_with_options_async(request, runtime)

    def get_live_room_statistics_with_options(
        self,
        request: imp_20210630_models.GetLiveRoomStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveRoomStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRoomStatistics',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRoomStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_room_statistics_with_options_async(
        self,
        request: imp_20210630_models.GetLiveRoomStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveRoomStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRoomStatistics',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRoomStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_room_statistics(
        self,
        request: imp_20210630_models.GetLiveRoomStatisticsRequest,
    ) -> imp_20210630_models.GetLiveRoomStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_room_statistics_with_options(request, runtime)

    async def get_live_room_statistics_async(
        self,
        request: imp_20210630_models.GetLiveRoomStatisticsRequest,
    ) -> imp_20210630_models.GetLiveRoomStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_room_statistics_with_options_async(request, runtime)

    def get_live_room_user_statistics_with_options(
        self,
        request: imp_20210630_models.GetLiveRoomUserStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveRoomUserStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRoomUserStatistics',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRoomUserStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_room_user_statistics_with_options_async(
        self,
        request: imp_20210630_models.GetLiveRoomUserStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveRoomUserStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveRoomUserStatistics',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetLiveRoomUserStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_room_user_statistics(
        self,
        request: imp_20210630_models.GetLiveRoomUserStatisticsRequest,
    ) -> imp_20210630_models.GetLiveRoomUserStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_room_user_statistics_with_options(request, runtime)

    async def get_live_room_user_statistics_async(
        self,
        request: imp_20210630_models.GetLiveRoomUserStatisticsRequest,
    ) -> imp_20210630_models.GetLiveRoomUserStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_room_user_statistics_with_options_async(request, runtime)

    def get_record_file_info_with_options(
        self,
        request: imp_20210630_models.GetRecordFileInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetRecordFileInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordFileInfo',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetRecordFileInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_record_file_info_with_options_async(
        self,
        request: imp_20210630_models.GetRecordFileInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetRecordFileInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordFileInfo',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetRecordFileInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_record_file_info(
        self,
        request: imp_20210630_models.GetRecordFileInfoRequest,
    ) -> imp_20210630_models.GetRecordFileInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_record_file_info_with_options(request, runtime)

    async def get_record_file_info_async(
        self,
        request: imp_20210630_models.GetRecordFileInfoRequest,
    ) -> imp_20210630_models.GetRecordFileInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_record_file_info_with_options_async(request, runtime)

    def get_room_with_options(
        self,
        request: imp_20210630_models.GetRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_room_with_options_async(
        self,
        request: imp_20210630_models.GetRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_room(
        self,
        request: imp_20210630_models.GetRoomRequest,
    ) -> imp_20210630_models.GetRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_room_with_options(request, runtime)

    async def get_room_async(
        self,
        request: imp_20210630_models.GetRoomRequest,
    ) -> imp_20210630_models.GetRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_room_with_options_async(request, runtime)

    def get_standard_room_jump_url_with_options(
        self,
        request: imp_20210630_models.GetStandardRoomJumpUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetStandardRoomJumpUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_nick):
            body['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStandardRoomJumpUrl',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetStandardRoomJumpUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_standard_room_jump_url_with_options_async(
        self,
        request: imp_20210630_models.GetStandardRoomJumpUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetStandardRoomJumpUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_key):
            body['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_nick):
            body['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStandardRoomJumpUrl',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetStandardRoomJumpUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_standard_room_jump_url(
        self,
        request: imp_20210630_models.GetStandardRoomJumpUrlRequest,
    ) -> imp_20210630_models.GetStandardRoomJumpUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_standard_room_jump_url_with_options(request, runtime)

    async def get_standard_room_jump_url_async(
        self,
        request: imp_20210630_models.GetStandardRoomJumpUrlRequest,
    ) -> imp_20210630_models.GetStandardRoomJumpUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_standard_room_jump_url_with_options_async(request, runtime)

    def kick_room_user_with_options(
        self,
        request: imp_20210630_models.KickRoomUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.KickRoomUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.block_time):
            body['BlockTime'] = request.block_time
        if not UtilClient.is_unset(request.kick_user):
            body['KickUser'] = request.kick_user
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KickRoomUser',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.KickRoomUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def kick_room_user_with_options_async(
        self,
        request: imp_20210630_models.KickRoomUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.KickRoomUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.block_time):
            body['BlockTime'] = request.block_time
        if not UtilClient.is_unset(request.kick_user):
            body['KickUser'] = request.kick_user
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KickRoomUser',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.KickRoomUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kick_room_user(
        self,
        request: imp_20210630_models.KickRoomUserRequest,
    ) -> imp_20210630_models.KickRoomUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.kick_room_user_with_options(request, runtime)

    async def kick_room_user_async(
        self,
        request: imp_20210630_models.KickRoomUserRequest,
    ) -> imp_20210630_models.KickRoomUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kick_room_user_with_options_async(request, runtime)

    def list_classes_with_options(
        self,
        request: imp_20210630_models.ListClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListClassesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClasses',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_classes_with_options_async(
        self,
        request: imp_20210630_models.ListClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListClassesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClasses',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_classes(
        self,
        request: imp_20210630_models.ListClassesRequest,
    ) -> imp_20210630_models.ListClassesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_classes_with_options(request, runtime)

    async def list_classes_async(
        self,
        request: imp_20210630_models.ListClassesRequest,
    ) -> imp_20210630_models.ListClassesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_classes_with_options_async(request, runtime)

    def list_comments_with_options(
        self,
        request: imp_20210630_models.ListCommentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListCommentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComments',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListCommentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_comments_with_options_async(
        self,
        request: imp_20210630_models.ListCommentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListCommentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComments',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListCommentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_comments(
        self,
        request: imp_20210630_models.ListCommentsRequest,
    ) -> imp_20210630_models.ListCommentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_comments_with_options(request, runtime)

    async def list_comments_async(
        self,
        request: imp_20210630_models.ListCommentsRequest,
    ) -> imp_20210630_models.ListCommentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_comments_with_options_async(request, runtime)

    def list_conference_users_with_options(
        self,
        request: imp_20210630_models.ListConferenceUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListConferenceUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConferenceUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListConferenceUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conference_users_with_options_async(
        self,
        request: imp_20210630_models.ListConferenceUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListConferenceUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConferenceUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListConferenceUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conference_users(
        self,
        request: imp_20210630_models.ListConferenceUsersRequest,
    ) -> imp_20210630_models.ListConferenceUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_conference_users_with_options(request, runtime)

    async def list_conference_users_async(
        self,
        request: imp_20210630_models.ListConferenceUsersRequest,
    ) -> imp_20210630_models.ListConferenceUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_conference_users_with_options_async(request, runtime)

    def list_live_files_with_options(
        self,
        request: imp_20210630_models.ListLiveFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListLiveFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            query['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveFiles',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListLiveFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_files_with_options_async(
        self,
        request: imp_20210630_models.ListLiveFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListLiveFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            query['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveFiles',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListLiveFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_files(
        self,
        request: imp_20210630_models.ListLiveFilesRequest,
    ) -> imp_20210630_models.ListLiveFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_files_with_options(request, runtime)

    async def list_live_files_async(
        self,
        request: imp_20210630_models.ListLiveFilesRequest,
    ) -> imp_20210630_models.ListLiveFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_files_with_options_async(request, runtime)

    def list_live_rooms_with_options(
        self,
        request: imp_20210630_models.ListLiveRoomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListLiveRoomsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLiveRooms',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListLiveRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_rooms_with_options_async(
        self,
        request: imp_20210630_models.ListLiveRoomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListLiveRoomsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLiveRooms',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListLiveRoomsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_rooms(
        self,
        request: imp_20210630_models.ListLiveRoomsRequest,
    ) -> imp_20210630_models.ListLiveRoomsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_rooms_with_options(request, runtime)

    async def list_live_rooms_async(
        self,
        request: imp_20210630_models.ListLiveRoomsRequest,
    ) -> imp_20210630_models.ListLiveRoomsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_rooms_with_options_async(request, runtime)

    def list_live_rooms_by_id_with_options(
        self,
        tmp_req: imp_20210630_models.ListLiveRoomsByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListLiveRoomsByIdResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.ListLiveRoomsByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.live_id_list):
            request.live_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.live_id_list, 'LiveIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id_list_shrink):
            body['LiveIdList'] = request.live_id_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLiveRoomsById',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListLiveRoomsByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_rooms_by_id_with_options_async(
        self,
        tmp_req: imp_20210630_models.ListLiveRoomsByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListLiveRoomsByIdResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.ListLiveRoomsByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.live_id_list):
            request.live_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.live_id_list, 'LiveIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id_list_shrink):
            body['LiveIdList'] = request.live_id_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLiveRoomsById',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListLiveRoomsByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_rooms_by_id(
        self,
        request: imp_20210630_models.ListLiveRoomsByIdRequest,
    ) -> imp_20210630_models.ListLiveRoomsByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_rooms_by_id_with_options(request, runtime)

    async def list_live_rooms_by_id_async(
        self,
        request: imp_20210630_models.ListLiveRoomsByIdRequest,
    ) -> imp_20210630_models.ListLiveRoomsByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_rooms_by_id_with_options_async(request, runtime)

    def list_room_users_with_options(
        self,
        request: imp_20210630_models.ListRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListRoomUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_room_users_with_options_async(
        self,
        request: imp_20210630_models.ListRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListRoomUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_room_users(
        self,
        request: imp_20210630_models.ListRoomUsersRequest,
    ) -> imp_20210630_models.ListRoomUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_room_users_with_options(request, runtime)

    async def list_room_users_async(
        self,
        request: imp_20210630_models.ListRoomUsersRequest,
    ) -> imp_20210630_models.ListRoomUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_room_users_with_options_async(request, runtime)

    def list_rooms_with_options(
        self,
        request: imp_20210630_models.ListRoomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListRoomsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRooms',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rooms_with_options_async(
        self,
        request: imp_20210630_models.ListRoomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListRoomsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRooms',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListRoomsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rooms(
        self,
        request: imp_20210630_models.ListRoomsRequest,
    ) -> imp_20210630_models.ListRoomsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rooms_with_options(request, runtime)

    async def list_rooms_async(
        self,
        request: imp_20210630_models.ListRoomsRequest,
    ) -> imp_20210630_models.ListRoomsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rooms_with_options_async(request, runtime)

    def list_sensitive_word_with_options(
        self,
        request: imp_20210630_models.ListSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListSensitiveWordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSensitiveWord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sensitive_word_with_options_async(
        self,
        request: imp_20210630_models.ListSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListSensitiveWordResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSensitiveWord',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.ListSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sensitive_word(
        self,
        request: imp_20210630_models.ListSensitiveWordRequest,
    ) -> imp_20210630_models.ListSensitiveWordResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sensitive_word_with_options(request, runtime)

    async def list_sensitive_word_async(
        self,
        request: imp_20210630_models.ListSensitiveWordRequest,
    ) -> imp_20210630_models.ListSensitiveWordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sensitive_word_with_options_async(request, runtime)

    def publish_live_with_options(
        self,
        request: imp_20210630_models.PublishLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.PublishLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.PublishLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_live_with_options_async(
        self,
        request: imp_20210630_models.PublishLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.PublishLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.PublishLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_live(
        self,
        request: imp_20210630_models.PublishLiveRequest,
    ) -> imp_20210630_models.PublishLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_live_with_options(request, runtime)

    async def publish_live_async(
        self,
        request: imp_20210630_models.PublishLiveRequest,
    ) -> imp_20210630_models.PublishLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_live_with_options_async(request, runtime)

    def publish_live_room_with_options(
        self,
        request: imp_20210630_models.PublishLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.PublishLiveRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.PublishLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_live_room_with_options_async(
        self,
        request: imp_20210630_models.PublishLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.PublishLiveRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.PublishLiveRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_live_room(
        self,
        request: imp_20210630_models.PublishLiveRoomRequest,
    ) -> imp_20210630_models.PublishLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_live_room_with_options(request, runtime)

    async def publish_live_room_async(
        self,
        request: imp_20210630_models.PublishLiveRoomRequest,
    ) -> imp_20210630_models.PublishLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_live_room_with_options_async(request, runtime)

    def remove_member_with_options(
        self,
        request: imp_20210630_models.RemoveMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.RemoveMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.from_user_id):
            body['FromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.to_user_id):
            body['ToUserId'] = request.to_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveMember',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.RemoveMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_member_with_options_async(
        self,
        request: imp_20210630_models.RemoveMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.RemoveMemberResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.from_user_id):
            body['FromUserId'] = request.from_user_id
        if not UtilClient.is_unset(request.to_user_id):
            body['ToUserId'] = request.to_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveMember',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.RemoveMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_member(
        self,
        request: imp_20210630_models.RemoveMemberRequest,
    ) -> imp_20210630_models.RemoveMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_member_with_options(request, runtime)

    async def remove_member_async(
        self,
        request: imp_20210630_models.RemoveMemberRequest,
    ) -> imp_20210630_models.RemoveMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_member_with_options_async(request, runtime)

    def send_comment_with_options(
        self,
        tmp_req: imp_20210630_models.SendCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.SendCommentResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.SendCommentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.sender_id):
            body['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            body['SenderNick'] = request.sender_nick
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCommentResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_comment_with_options_async(
        self,
        tmp_req: imp_20210630_models.SendCommentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.SendCommentResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.SendCommentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.sender_id):
            body['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            body['SenderNick'] = request.sender_nick
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendComment',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCommentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_comment(
        self,
        request: imp_20210630_models.SendCommentRequest,
    ) -> imp_20210630_models.SendCommentResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_comment_with_options(request, runtime)

    async def send_comment_async(
        self,
        request: imp_20210630_models.SendCommentRequest,
    ) -> imp_20210630_models.SendCommentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_comment_with_options_async(request, runtime)

    def send_custom_message_to_all_with_options(
        self,
        request: imp_20210630_models.SendCustomMessageToAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.SendCustomMessageToAllResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessageToAll',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCustomMessageToAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_custom_message_to_all_with_options_async(
        self,
        request: imp_20210630_models.SendCustomMessageToAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.SendCustomMessageToAllResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessageToAll',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCustomMessageToAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_custom_message_to_all(
        self,
        request: imp_20210630_models.SendCustomMessageToAllRequest,
    ) -> imp_20210630_models.SendCustomMessageToAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_to_all_with_options(request, runtime)

    async def send_custom_message_to_all_async(
        self,
        request: imp_20210630_models.SendCustomMessageToAllRequest,
    ) -> imp_20210630_models.SendCustomMessageToAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_custom_message_to_all_with_options_async(request, runtime)

    def send_custom_message_to_users_with_options(
        self,
        request: imp_20210630_models.SendCustomMessageToUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.SendCustomMessageToUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        body_flat = {}
        if not UtilClient.is_unset(request.receiver_list):
            body_flat['ReceiverList'] = request.receiver_list
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessageToUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCustomMessageToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_custom_message_to_users_with_options_async(
        self,
        request: imp_20210630_models.SendCustomMessageToUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.SendCustomMessageToUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        body_flat = {}
        if not UtilClient.is_unset(request.receiver_list):
            body_flat['ReceiverList'] = request.receiver_list
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessageToUsers',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SendCustomMessageToUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_custom_message_to_users(
        self,
        request: imp_20210630_models.SendCustomMessageToUsersRequest,
    ) -> imp_20210630_models.SendCustomMessageToUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_to_users_with_options(request, runtime)

    async def send_custom_message_to_users_async(
        self,
        request: imp_20210630_models.SendCustomMessageToUsersRequest,
    ) -> imp_20210630_models.SendCustomMessageToUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_custom_message_to_users_with_options_async(request, runtime)

    def set_user_admin_with_options(
        self,
        request: imp_20210630_models.SetUserAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.SetUserAdminResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserAdmin',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SetUserAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_admin_with_options_async(
        self,
        request: imp_20210630_models.SetUserAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.SetUserAdminResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserAdmin',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.SetUserAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_admin(
        self,
        request: imp_20210630_models.SetUserAdminRequest,
    ) -> imp_20210630_models.SetUserAdminResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_user_admin_with_options(request, runtime)

    async def set_user_admin_async(
        self,
        request: imp_20210630_models.SetUserAdminRequest,
    ) -> imp_20210630_models.SetUserAdminResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_user_admin_with_options_async(request, runtime)

    def stop_class_with_options(
        self,
        request: imp_20210630_models.StopClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.StopClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.StopClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_class_with_options_async(
        self,
        request: imp_20210630_models.StopClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.StopClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.StopClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_class(
        self,
        request: imp_20210630_models.StopClassRequest,
    ) -> imp_20210630_models.StopClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_class_with_options(request, runtime)

    async def stop_class_async(
        self,
        request: imp_20210630_models.StopClassRequest,
    ) -> imp_20210630_models.StopClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_class_with_options_async(request, runtime)

    def stop_live_with_options(
        self,
        request: imp_20210630_models.StopLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.StopLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.StopLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_live_with_options_async(
        self,
        request: imp_20210630_models.StopLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.StopLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.StopLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_live(
        self,
        request: imp_20210630_models.StopLiveRequest,
    ) -> imp_20210630_models.StopLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_live_with_options(request, runtime)

    async def stop_live_async(
        self,
        request: imp_20210630_models.StopLiveRequest,
    ) -> imp_20210630_models.StopLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_live_with_options_async(request, runtime)

    def stop_live_room_with_options(
        self,
        request: imp_20210630_models.StopLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.StopLiveRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.StopLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_live_room_with_options_async(
        self,
        request: imp_20210630_models.StopLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.StopLiveRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.StopLiveRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_live_room(
        self,
        request: imp_20210630_models.StopLiveRoomRequest,
    ) -> imp_20210630_models.StopLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_live_room_with_options(request, runtime)

    async def stop_live_room_async(
        self,
        request: imp_20210630_models.StopLiveRoomRequest,
    ) -> imp_20210630_models.StopLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_live_room_with_options_async(request, runtime)

    def update_class_with_options(
        self,
        request: imp_20210630_models.UpdateClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.create_nickname):
            body['CreateNickname'] = request.create_nickname
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_class_with_options_async(
        self,
        request: imp_20210630_models.UpdateClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateClassResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.create_nickname):
            body['CreateNickname'] = request.create_nickname
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClass',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_class(
        self,
        request: imp_20210630_models.UpdateClassRequest,
    ) -> imp_20210630_models.UpdateClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_class_with_options(request, runtime)

    async def update_class_async(
        self,
        request: imp_20210630_models.UpdateClassRequest,
    ) -> imp_20210630_models.UpdateClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_class_with_options_async(request, runtime)

    def update_live_with_options(
        self,
        request: imp_20210630_models.UpdateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_with_options_async(
        self,
        request: imp_20210630_models.UpdateLiveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateLiveResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.introduction):
            body['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLive',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live(
        self,
        request: imp_20210630_models.UpdateLiveRequest,
    ) -> imp_20210630_models.UpdateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_with_options(request, runtime)

    async def update_live_async(
        self,
        request: imp_20210630_models.UpdateLiveRequest,
    ) -> imp_20210630_models.UpdateLiveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_with_options_async(request, runtime)

    def update_live_room_with_options(
        self,
        tmp_req: imp_20210630_models.UpdateLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateLiveRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateLiveRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.anchor_id):
            body['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.anchor_nick):
            body['AnchorNick'] = request.anchor_nick
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateLiveRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_room_with_options_async(
        self,
        tmp_req: imp_20210630_models.UpdateLiveRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateLiveRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateLiveRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.anchor_id):
            body['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.anchor_nick):
            body['AnchorNick'] = request.anchor_nick
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cover_url):
            body['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.live_id):
            body['LiveId'] = request.live_id
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLiveRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateLiveRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_room(
        self,
        request: imp_20210630_models.UpdateLiveRoomRequest,
    ) -> imp_20210630_models.UpdateLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_room_with_options(request, runtime)

    async def update_live_room_async(
        self,
        request: imp_20210630_models.UpdateLiveRoomRequest,
    ) -> imp_20210630_models.UpdateLiveRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_room_with_options_async(request, runtime)

    def update_room_with_options(
        self,
        tmp_req: imp_20210630_models.UpdateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_owner_id):
            body['RoomOwnerId'] = request.room_owner_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_room_with_options_async(
        self,
        tmp_req: imp_20210630_models.UpdateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateRoomResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_owner_id):
            body['RoomOwnerId'] = request.room_owner_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRoom',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_room(
        self,
        request: imp_20210630_models.UpdateRoomRequest,
    ) -> imp_20210630_models.UpdateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_room_with_options(request, runtime)

    async def update_room_async(
        self,
        request: imp_20210630_models.UpdateRoomRequest,
    ) -> imp_20210630_models.UpdateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_room_with_options_async(request, runtime)

    def update_share_screen_layout_with_options(
        self,
        request: imp_20210630_models.UpdateShareScreenLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateShareScreenLayoutResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.enable_overlay):
            body['EnableOverlay'] = request.enable_overlay
        if not UtilClient.is_unset(request.overlay_height):
            body['OverlayHeight'] = request.overlay_height
        if not UtilClient.is_unset(request.overlay_width):
            body['OverlayWidth'] = request.overlay_width
        if not UtilClient.is_unset(request.overlay_x):
            body['OverlayX'] = request.overlay_x
        if not UtilClient.is_unset(request.overlay_y):
            body['OverlayY'] = request.overlay_y
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShareScreenLayout',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateShareScreenLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_share_screen_layout_with_options_async(
        self,
        request: imp_20210630_models.UpdateShareScreenLayoutRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateShareScreenLayoutResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.class_id):
            body['ClassId'] = request.class_id
        if not UtilClient.is_unset(request.enable_overlay):
            body['EnableOverlay'] = request.enable_overlay
        if not UtilClient.is_unset(request.overlay_height):
            body['OverlayHeight'] = request.overlay_height
        if not UtilClient.is_unset(request.overlay_width):
            body['OverlayWidth'] = request.overlay_width
        if not UtilClient.is_unset(request.overlay_x):
            body['OverlayX'] = request.overlay_x
        if not UtilClient.is_unset(request.overlay_y):
            body['OverlayY'] = request.overlay_y
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShareScreenLayout',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.UpdateShareScreenLayoutResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_share_screen_layout(
        self,
        request: imp_20210630_models.UpdateShareScreenLayoutRequest,
    ) -> imp_20210630_models.UpdateShareScreenLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_share_screen_layout_with_options(request, runtime)

    async def update_share_screen_layout_async(
        self,
        request: imp_20210630_models.UpdateShareScreenLayoutRequest,
    ) -> imp_20210630_models.UpdateShareScreenLayoutResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_share_screen_layout_with_options_async(request, runtime)
