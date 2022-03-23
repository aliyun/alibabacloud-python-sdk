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

    def add_member_with_options(
        self,
        request: imp_20210630_models.AddMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.AddMemberResponse:
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
            action='AddMember',
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
            imp_20210630_models.AddMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_member_with_options_async(
        self,
        request: imp_20210630_models.AddMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.AddMemberResponse:
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
            action='AddMember',
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
            imp_20210630_models.AddMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_member(
        self,
        request: imp_20210630_models.AddMemberRequest,
    ) -> imp_20210630_models.AddMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_member_with_options(request, runtime)

    async def add_member_async(
        self,
        request: imp_20210630_models.AddMemberRequest,
    ) -> imp_20210630_models.AddMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_member_with_options_async(request, runtime)

    def agree_link_mic_with_options(
        self,
        request: imp_20210630_models.AgreeLinkMicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.AgreeLinkMicResponse:
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
            action='AgreeLinkMic',
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
            imp_20210630_models.AgreeLinkMicResponse(),
            self.call_api(params, req, runtime)
        )

    async def agree_link_mic_with_options_async(
        self,
        request: imp_20210630_models.AgreeLinkMicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.AgreeLinkMicResponse:
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
            action='AgreeLinkMic',
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
            imp_20210630_models.AgreeLinkMicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agree_link_mic(
        self,
        request: imp_20210630_models.AgreeLinkMicRequest,
    ) -> imp_20210630_models.AgreeLinkMicResponse:
        runtime = util_models.RuntimeOptions()
        return self.agree_link_mic_with_options(request, runtime)

    async def agree_link_mic_async(
        self,
        request: imp_20210630_models.AgreeLinkMicRequest,
    ) -> imp_20210630_models.AgreeLinkMicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.agree_link_mic_with_options_async(request, runtime)

    def apply_link_mic_with_options(
        self,
        request: imp_20210630_models.ApplyLinkMicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ApplyLinkMicResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyLinkMic',
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
            imp_20210630_models.ApplyLinkMicResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_link_mic_with_options_async(
        self,
        request: imp_20210630_models.ApplyLinkMicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ApplyLinkMicResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyLinkMic',
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
            imp_20210630_models.ApplyLinkMicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_link_mic(
        self,
        request: imp_20210630_models.ApplyLinkMicRequest,
    ) -> imp_20210630_models.ApplyLinkMicResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_link_mic_with_options(request, runtime)

    async def apply_link_mic_async(
        self,
        request: imp_20210630_models.ApplyLinkMicRequest,
    ) -> imp_20210630_models.ApplyLinkMicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_link_mic_with_options_async(request, runtime)

    def attach_standard_room_https_certificate_with_options(
        self,
        request: imp_20210630_models.AttachStandardRoomHttpsCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.AttachStandardRoomHttpsCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.certificate_private_key):
            body['CertificatePrivateKey'] = request.certificate_private_key
        if not UtilClient.is_unset(request.certificate_public_key):
            body['CertificatePublicKey'] = request.certificate_public_key
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachStandardRoomHttpsCertificate',
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
            imp_20210630_models.AttachStandardRoomHttpsCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_standard_room_https_certificate_with_options_async(
        self,
        request: imp_20210630_models.AttachStandardRoomHttpsCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.AttachStandardRoomHttpsCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.certificate_private_key):
            body['CertificatePrivateKey'] = request.certificate_private_key
        if not UtilClient.is_unset(request.certificate_public_key):
            body['CertificatePublicKey'] = request.certificate_public_key
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachStandardRoomHttpsCertificate',
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
            imp_20210630_models.AttachStandardRoomHttpsCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_standard_room_https_certificate(
        self,
        request: imp_20210630_models.AttachStandardRoomHttpsCertificateRequest,
    ) -> imp_20210630_models.AttachStandardRoomHttpsCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_standard_room_https_certificate_with_options(request, runtime)

    async def attach_standard_room_https_certificate_async(
        self,
        request: imp_20210630_models.AttachStandardRoomHttpsCertificateRequest,
    ) -> imp_20210630_models.AttachStandardRoomHttpsCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_standard_room_https_certificate_with_options_async(request, runtime)

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

    def cancel_apply_link_mic_with_options(
        self,
        request: imp_20210630_models.CancelApplyLinkMicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CancelApplyLinkMicResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelApplyLinkMic',
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
            imp_20210630_models.CancelApplyLinkMicResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_apply_link_mic_with_options_async(
        self,
        request: imp_20210630_models.CancelApplyLinkMicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CancelApplyLinkMicResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelApplyLinkMic',
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
            imp_20210630_models.CancelApplyLinkMicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_apply_link_mic(
        self,
        request: imp_20210630_models.CancelApplyLinkMicRequest,
    ) -> imp_20210630_models.CancelApplyLinkMicResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_apply_link_mic_with_options(request, runtime)

    async def cancel_apply_link_mic_async(
        self,
        request: imp_20210630_models.CancelApplyLinkMicRequest,
    ) -> imp_20210630_models.CancelApplyLinkMicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_apply_link_mic_with_options_async(request, runtime)

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

    def create_app_with_options(
        self,
        request: imp_20210630_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
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
            imp_20210630_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: imp_20210630_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
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
            imp_20210630_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: imp_20210630_models.CreateAppRequest,
    ) -> imp_20210630_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: imp_20210630_models.CreateAppRequest,
    ) -> imp_20210630_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_app_template_with_options(
        self,
        tmp_req: imp_20210630_models.CreateAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateAppTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateAppTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_list):
            request.component_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_list, 'ComponentList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_template_name):
            body['AppTemplateName'] = request.app_template_name
        if not UtilClient.is_unset(request.component_list_shrink):
            body['ComponentList'] = request.component_list_shrink
        if not UtilClient.is_unset(request.integration_mode):
            body['IntegrationMode'] = request.integration_mode
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppTemplate',
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
            imp_20210630_models.CreateAppTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_template_with_options_async(
        self,
        tmp_req: imp_20210630_models.CreateAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateAppTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.CreateAppTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_list):
            request.component_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_list, 'ComponentList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_template_name):
            body['AppTemplateName'] = request.app_template_name
        if not UtilClient.is_unset(request.component_list_shrink):
            body['ComponentList'] = request.component_list_shrink
        if not UtilClient.is_unset(request.integration_mode):
            body['IntegrationMode'] = request.integration_mode
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppTemplate',
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
            imp_20210630_models.CreateAppTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_template(
        self,
        request: imp_20210630_models.CreateAppTemplateRequest,
    ) -> imp_20210630_models.CreateAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_template_with_options(request, runtime)

    async def create_app_template_async(
        self,
        request: imp_20210630_models.CreateAppTemplateRequest,
    ) -> imp_20210630_models.CreateAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_template_with_options_async(request, runtime)

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

    def create_conference_with_options(
        self,
        request: imp_20210630_models.CreateConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
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
            action='CreateConference',
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
            imp_20210630_models.CreateConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_conference_with_options_async(
        self,
        request: imp_20210630_models.CreateConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.CreateConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
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
            action='CreateConference',
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
            imp_20210630_models.CreateConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_conference(
        self,
        request: imp_20210630_models.CreateConferenceRequest,
    ) -> imp_20210630_models.CreateConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_conference_with_options(request, runtime)

    async def create_conference_async(
        self,
        request: imp_20210630_models.CreateConferenceRequest,
    ) -> imp_20210630_models.CreateConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_conference_with_options_async(request, runtime)

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

    def delete_app_with_options(
        self,
        request: imp_20210630_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
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
            imp_20210630_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: imp_20210630_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
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
            imp_20210630_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: imp_20210630_models.DeleteAppRequest,
    ) -> imp_20210630_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: imp_20210630_models.DeleteAppRequest,
    ) -> imp_20210630_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_app_template_with_options(
        self,
        request: imp_20210630_models.DeleteAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteAppTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppTemplate',
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
            imp_20210630_models.DeleteAppTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_template_with_options_async(
        self,
        request: imp_20210630_models.DeleteAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DeleteAppTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppTemplate',
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
            imp_20210630_models.DeleteAppTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_template(
        self,
        request: imp_20210630_models.DeleteAppTemplateRequest,
    ) -> imp_20210630_models.DeleteAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_template_with_options(request, runtime)

    async def delete_app_template_async(
        self,
        request: imp_20210630_models.DeleteAppTemplateRequest,
    ) -> imp_20210630_models.DeleteAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_template_with_options_async(request, runtime)

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

    def describe_meter_imp_watch_time_with_options(
        self,
        request: imp_20210630_models.DescribeMeterImpWatchTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DescribeMeterImpWatchTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImpWatchTime',
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
            imp_20210630_models.DescribeMeterImpWatchTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_imp_watch_time_with_options_async(
        self,
        request: imp_20210630_models.DescribeMeterImpWatchTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.DescribeMeterImpWatchTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImpWatchTime',
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
            imp_20210630_models.DescribeMeterImpWatchTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_imp_watch_time(
        self,
        request: imp_20210630_models.DescribeMeterImpWatchTimeRequest,
    ) -> imp_20210630_models.DescribeMeterImpWatchTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_imp_watch_time_with_options(request, runtime)

    async def describe_meter_imp_watch_time_async(
        self,
        request: imp_20210630_models.DescribeMeterImpWatchTimeRequest,
    ) -> imp_20210630_models.DescribeMeterImpWatchTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_imp_watch_time_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: imp_20210630_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApp',
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
            imp_20210630_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: imp_20210630_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApp',
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
            imp_20210630_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        request: imp_20210630_models.GetAppRequest,
    ) -> imp_20210630_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: imp_20210630_models.GetAppRequest,
    ) -> imp_20210630_models.GetAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_app_template_with_options(
        self,
        request: imp_20210630_models.GetAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAppTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAppTemplate',
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
            imp_20210630_models.GetAppTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_template_with_options_async(
        self,
        request: imp_20210630_models.GetAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetAppTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAppTemplate',
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
            imp_20210630_models.GetAppTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_template(
        self,
        request: imp_20210630_models.GetAppTemplateRequest,
    ) -> imp_20210630_models.GetAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_template_with_options(request, runtime)

    async def get_app_template_async(
        self,
        request: imp_20210630_models.GetAppTemplateRequest,
    ) -> imp_20210630_models.GetAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_template_with_options_async(request, runtime)

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

    def get_cname_detail_with_options(
        self,
        request: imp_20210630_models.GetCnameDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetCnameDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCnameDetail',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetCnameDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cname_detail_with_options_async(
        self,
        request: imp_20210630_models.GetCnameDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetCnameDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCnameDetail',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetCnameDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cname_detail(
        self,
        request: imp_20210630_models.GetCnameDetailRequest,
    ) -> imp_20210630_models.GetCnameDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cname_detail_with_options(request, runtime)

    async def get_cname_detail_async(
        self,
        request: imp_20210630_models.GetCnameDetailRequest,
    ) -> imp_20210630_models.GetCnameDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cname_detail_with_options_async(request, runtime)

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

    def get_domain_owner_verify_content_with_options(
        self,
        request: imp_20210630_models.GetDomainOwnerVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetDomainOwnerVerifyContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_domain_name):
            body['LiveDomainName'] = request.live_domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDomainOwnerVerifyContent',
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
            imp_20210630_models.GetDomainOwnerVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_owner_verify_content_with_options_async(
        self,
        request: imp_20210630_models.GetDomainOwnerVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetDomainOwnerVerifyContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_domain_name):
            body['LiveDomainName'] = request.live_domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDomainOwnerVerifyContent',
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
            imp_20210630_models.GetDomainOwnerVerifyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_owner_verify_content(
        self,
        request: imp_20210630_models.GetDomainOwnerVerifyContentRequest,
    ) -> imp_20210630_models.GetDomainOwnerVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domain_owner_verify_content_with_options(request, runtime)

    async def get_domain_owner_verify_content_async(
        self,
        request: imp_20210630_models.GetDomainOwnerVerifyContentRequest,
    ) -> imp_20210630_models.GetDomainOwnerVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_owner_verify_content_with_options_async(request, runtime)

    def get_imp_product_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetImpProductStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetImpProductStatus',
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
            imp_20210630_models.GetImpProductStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_imp_product_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetImpProductStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetImpProductStatus',
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
            imp_20210630_models.GetImpProductStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_imp_product_status(self) -> imp_20210630_models.GetImpProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_imp_product_status_with_options(runtime)

    async def get_imp_product_status_async(self) -> imp_20210630_models.GetImpProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_imp_product_status_with_options_async(runtime)

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

    def get_live_domain_status_with_options(
        self,
        tmp_req: imp_20210630_models.GetLiveDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveDomainStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.GetLiveDomainStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.live_domain_list):
            request.live_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.live_domain_list, 'LiveDomainList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_domain_list_shrink):
            body['LiveDomainList'] = request.live_domain_list_shrink
        if not UtilClient.is_unset(request.live_domain_type):
            body['LiveDomainType'] = request.live_domain_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveDomainStatus',
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
            imp_20210630_models.GetLiveDomainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_domain_status_with_options_async(
        self,
        tmp_req: imp_20210630_models.GetLiveDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetLiveDomainStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.GetLiveDomainStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.live_domain_list):
            request.live_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.live_domain_list, 'LiveDomainList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.live_domain_list_shrink):
            body['LiveDomainList'] = request.live_domain_list_shrink
        if not UtilClient.is_unset(request.live_domain_type):
            body['LiveDomainType'] = request.live_domain_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLiveDomainStatus',
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
            imp_20210630_models.GetLiveDomainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_domain_status(
        self,
        request: imp_20210630_models.GetLiveDomainStatusRequest,
    ) -> imp_20210630_models.GetLiveDomainStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_domain_status_with_options(request, runtime)

    async def get_live_domain_status_async(
        self,
        request: imp_20210630_models.GetLiveDomainStatusRequest,
    ) -> imp_20210630_models.GetLiveDomainStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_domain_status_with_options_async(request, runtime)

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

    def get_page_config_with_options(
        self,
        request: imp_20210630_models.GetPageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetPageConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPageConfig',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetPageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_page_config_with_options_async(
        self,
        request: imp_20210630_models.GetPageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetPageConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPageConfig',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetPageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_page_config(
        self,
        request: imp_20210630_models.GetPageConfigRequest,
    ) -> imp_20210630_models.GetPageConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_page_config_with_options(request, runtime)

    async def get_page_config_async(
        self,
        request: imp_20210630_models.GetPageConfigRequest,
    ) -> imp_20210630_models.GetPageConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_page_config_with_options_async(request, runtime)

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

    def get_standard_room_https_certificate_with_options(
        self,
        request: imp_20210630_models.GetStandardRoomHttpsCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetStandardRoomHttpsCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_id):
            body['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStandardRoomHttpsCertificate',
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
            imp_20210630_models.GetStandardRoomHttpsCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_standard_room_https_certificate_with_options_async(
        self,
        request: imp_20210630_models.GetStandardRoomHttpsCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetStandardRoomHttpsCertificateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_id):
            body['CertificateId'] = request.certificate_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStandardRoomHttpsCertificate',
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
            imp_20210630_models.GetStandardRoomHttpsCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_standard_room_https_certificate(
        self,
        request: imp_20210630_models.GetStandardRoomHttpsCertificateRequest,
    ) -> imp_20210630_models.GetStandardRoomHttpsCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_standard_room_https_certificate_with_options(request, runtime)

    async def get_standard_room_https_certificate_async(
        self,
        request: imp_20210630_models.GetStandardRoomHttpsCertificateRequest,
    ) -> imp_20210630_models.GetStandardRoomHttpsCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_standard_room_https_certificate_with_options_async(request, runtime)

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

    def get_user_info_with_options(
        self,
        request: imp_20210630_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        request: imp_20210630_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2021-06-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imp_20210630_models.GetUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_info(
        self,
        request: imp_20210630_models.GetUserInfoRequest,
    ) -> imp_20210630_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_info_with_options(request, runtime)

    async def get_user_info_async(
        self,
        request: imp_20210630_models.GetUserInfoRequest,
    ) -> imp_20210630_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_info_with_options_async(request, runtime)

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

    def list_app_templates_with_options(
        self,
        request: imp_20210630_models.ListAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListAppTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppTemplates',
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
            imp_20210630_models.ListAppTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_templates_with_options_async(
        self,
        request: imp_20210630_models.ListAppTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListAppTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppTemplates',
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
            imp_20210630_models.ListAppTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_templates(
        self,
        request: imp_20210630_models.ListAppTemplatesRequest,
    ) -> imp_20210630_models.ListAppTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_templates_with_options(request, runtime)

    async def list_app_templates_async(
        self,
        request: imp_20210630_models.ListAppTemplatesRequest,
    ) -> imp_20210630_models.ListAppTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_templates_with_options_async(request, runtime)

    def list_apply_link_mic_users_with_options(
        self,
        request: imp_20210630_models.ListApplyLinkMicUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListApplyLinkMicUsersResponse:
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
            action='ListApplyLinkMicUsers',
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
            imp_20210630_models.ListApplyLinkMicUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apply_link_mic_users_with_options_async(
        self,
        request: imp_20210630_models.ListApplyLinkMicUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListApplyLinkMicUsersResponse:
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
            action='ListApplyLinkMicUsers',
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
            imp_20210630_models.ListApplyLinkMicUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apply_link_mic_users(
        self,
        request: imp_20210630_models.ListApplyLinkMicUsersRequest,
    ) -> imp_20210630_models.ListApplyLinkMicUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apply_link_mic_users_with_options(request, runtime)

    async def list_apply_link_mic_users_async(
        self,
        request: imp_20210630_models.ListApplyLinkMicUsersRequest,
    ) -> imp_20210630_models.ListApplyLinkMicUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apply_link_mic_users_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: imp_20210630_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListAppsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.integration_mode):
            body['IntegrationMode'] = request.integration_mode
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
            action='ListApps',
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
            imp_20210630_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: imp_20210630_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListAppsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.integration_mode):
            body['IntegrationMode'] = request.integration_mode
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
            action='ListApps',
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
            imp_20210630_models.ListAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apps(
        self,
        request: imp_20210630_models.ListAppsRequest,
    ) -> imp_20210630_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: imp_20210630_models.ListAppsRequest,
    ) -> imp_20210630_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

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

    def list_components_with_options(
        self,
        request: imp_20210630_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponents',
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
            imp_20210630_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: imp_20210630_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListComponentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponents',
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
            imp_20210630_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: imp_20210630_models.ListComponentsRequest,
    ) -> imp_20210630_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    async def list_components_async(
        self,
        request: imp_20210630_models.ListComponentsRequest,
    ) -> imp_20210630_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_components_with_options_async(request, runtime)

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

    def list_room_lives_with_options(
        self,
        tmp_req: imp_20210630_models.ListRoomLivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListRoomLivesResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.ListRoomLivesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_id_list):
            request.room_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_id_list, 'RoomIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.query_timestamp):
            body['QueryTimestamp'] = request.query_timestamp
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_id_list_shrink):
            body['RoomIdList'] = request.room_id_list_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomLives',
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
            imp_20210630_models.ListRoomLivesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_room_lives_with_options_async(
        self,
        tmp_req: imp_20210630_models.ListRoomLivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.ListRoomLivesResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.ListRoomLivesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.room_id_list):
            request.room_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.room_id_list, 'RoomIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.query_timestamp):
            body['QueryTimestamp'] = request.query_timestamp
        if not UtilClient.is_unset(request.room_id):
            body['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_id_list_shrink):
            body['RoomIdList'] = request.room_id_list_shrink
        if not UtilClient.is_unset(request.size):
            body['Size'] = request.size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomLives',
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
            imp_20210630_models.ListRoomLivesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_room_lives(
        self,
        request: imp_20210630_models.ListRoomLivesRequest,
    ) -> imp_20210630_models.ListRoomLivesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_room_lives_with_options(request, runtime)

    async def list_room_lives_async(
        self,
        request: imp_20210630_models.ListRoomLivesRequest,
    ) -> imp_20210630_models.ListRoomLivesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_room_lives_with_options_async(request, runtime)

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

    def reject_link_mic_with_options(
        self,
        request: imp_20210630_models.RejectLinkMicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.RejectLinkMicResponse:
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
            action='RejectLinkMic',
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
            imp_20210630_models.RejectLinkMicResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_link_mic_with_options_async(
        self,
        request: imp_20210630_models.RejectLinkMicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.RejectLinkMicResponse:
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
            action='RejectLinkMic',
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
            imp_20210630_models.RejectLinkMicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_link_mic(
        self,
        request: imp_20210630_models.RejectLinkMicRequest,
    ) -> imp_20210630_models.RejectLinkMicResponse:
        runtime = util_models.RuntimeOptions()
        return self.reject_link_mic_with_options(request, runtime)

    async def reject_link_mic_async(
        self,
        request: imp_20210630_models.RejectLinkMicRequest,
    ) -> imp_20210630_models.RejectLinkMicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reject_link_mic_with_options_async(request, runtime)

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

    def update_app_with_options(
        self,
        request: imp_20210630_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_status):
            body['AppStatus'] = request.app_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
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
            imp_20210630_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_with_options_async(
        self,
        request: imp_20210630_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_status):
            body['AppStatus'] = request.app_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
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
            imp_20210630_models.UpdateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app(
        self,
        request: imp_20210630_models.UpdateAppRequest,
    ) -> imp_20210630_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    async def update_app_async(
        self,
        request: imp_20210630_models.UpdateAppRequest,
    ) -> imp_20210630_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_with_options_async(request, runtime)

    def update_app_template_with_options(
        self,
        tmp_req: imp_20210630_models.UpdateAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateAppTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_list):
            request.component_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_list, 'ComponentList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        if not UtilClient.is_unset(request.app_template_name):
            body['AppTemplateName'] = request.app_template_name
        if not UtilClient.is_unset(request.component_list_shrink):
            body['ComponentList'] = request.component_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppTemplate',
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
            imp_20210630_models.UpdateAppTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_template_with_options_async(
        self,
        tmp_req: imp_20210630_models.UpdateAppTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateAppTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_list):
            request.component_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_list, 'ComponentList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        if not UtilClient.is_unset(request.app_template_name):
            body['AppTemplateName'] = request.app_template_name
        if not UtilClient.is_unset(request.component_list_shrink):
            body['ComponentList'] = request.component_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppTemplate',
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
            imp_20210630_models.UpdateAppTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_template(
        self,
        request: imp_20210630_models.UpdateAppTemplateRequest,
    ) -> imp_20210630_models.UpdateAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_template_with_options(request, runtime)

    async def update_app_template_async(
        self,
        request: imp_20210630_models.UpdateAppTemplateRequest,
    ) -> imp_20210630_models.UpdateAppTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_template_with_options_async(request, runtime)

    def update_app_template_config_with_options(
        self,
        tmp_req: imp_20210630_models.UpdateAppTemplateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppTemplateConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateAppTemplateConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        if not UtilClient.is_unset(request.config_list_shrink):
            body['ConfigList'] = request.config_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppTemplateConfig',
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
            imp_20210630_models.UpdateAppTemplateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_template_config_with_options_async(
        self,
        tmp_req: imp_20210630_models.UpdateAppTemplateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateAppTemplateConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = imp_20210630_models.UpdateAppTemplateConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_template_id):
            body['AppTemplateId'] = request.app_template_id
        if not UtilClient.is_unset(request.config_list_shrink):
            body['ConfigList'] = request.config_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppTemplateConfig',
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
            imp_20210630_models.UpdateAppTemplateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_template_config(
        self,
        request: imp_20210630_models.UpdateAppTemplateConfigRequest,
    ) -> imp_20210630_models.UpdateAppTemplateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_template_config_with_options(request, runtime)

    async def update_app_template_config_async(
        self,
        request: imp_20210630_models.UpdateAppTemplateConfigRequest,
    ) -> imp_20210630_models.UpdateAppTemplateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_template_config_with_options_async(request, runtime)

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

    def update_conference_with_options(
        self,
        request: imp_20210630_models.UpdateConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConference',
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
            imp_20210630_models.UpdateConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conference_with_options_async(
        self,
        request: imp_20210630_models.UpdateConferenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.UpdateConferenceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.conference_id):
            body['ConferenceId'] = request.conference_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConference',
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
            imp_20210630_models.UpdateConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conference(
        self,
        request: imp_20210630_models.UpdateConferenceRequest,
    ) -> imp_20210630_models.UpdateConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_conference_with_options(request, runtime)

    async def update_conference_async(
        self,
        request: imp_20210630_models.UpdateConferenceRequest,
    ) -> imp_20210630_models.UpdateConferenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_conference_with_options_async(request, runtime)

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

    def verify_domain_owner_with_options(
        self,
        request: imp_20210630_models.VerifyDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.VerifyDomainOwnerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_domain_name):
            body['LiveDomainName'] = request.live_domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyDomainOwner',
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
            imp_20210630_models.VerifyDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_domain_owner_with_options_async(
        self,
        request: imp_20210630_models.VerifyDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imp_20210630_models.VerifyDomainOwnerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.live_domain_name):
            body['LiveDomainName'] = request.live_domain_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyDomainOwner',
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
            imp_20210630_models.VerifyDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_domain_owner(
        self,
        request: imp_20210630_models.VerifyDomainOwnerRequest,
    ) -> imp_20210630_models.VerifyDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_domain_owner_with_options(request, runtime)

    async def verify_domain_owner_async(
        self,
        request: imp_20210630_models.VerifyDomainOwnerRequest,
    ) -> imp_20210630_models.VerifyDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_domain_owner_with_options_async(request, runtime)
