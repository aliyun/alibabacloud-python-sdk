# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_live_interaction20201214 import models as live_interaction_20201214_models
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
        self._endpoint = self.get_endpoint('live-interaction', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_app_infos_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ListAppInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListAppInfosResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListAppInfosShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListAppInfosResponse(),
            self.do_rpcrequest('ListAppInfos', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_app_infos_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ListAppInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListAppInfosResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListAppInfosShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListAppInfosResponse(),
            await self.do_rpcrequest_async('ListAppInfos', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_infos(
        self,
        request: live_interaction_20201214_models.ListAppInfosRequest,
    ) -> live_interaction_20201214_models.ListAppInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_infos_with_options(request, runtime)

    async def list_app_infos_async(
        self,
        request: live_interaction_20201214_models.ListAppInfosRequest,
    ) -> live_interaction_20201214_models.ListAppInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_infos_with_options_async(request, runtime)

    def remove_single_chat_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveSingleChatExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveSingleChatExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_single_chat_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.RemoveSingleChatExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse(),
            await self.do_rpcrequest_async('RemoveSingleChatExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_single_chat_extension_by_keys(
        self,
        request: live_interaction_20201214_models.RemoveSingleChatExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_single_chat_extension_by_keys_with_options(request, runtime)

    async def remove_single_chat_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.RemoveSingleChatExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_single_chat_extension_by_keys_with_options_async(request, runtime)

    def import_message_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ImportMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportMessageResponse(),
            self.do_rpcrequest('ImportMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_message_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ImportMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportMessageResponse(),
            await self.do_rpcrequest_async('ImportMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_message(
        self,
        request: live_interaction_20201214_models.ImportMessageRequest,
    ) -> live_interaction_20201214_models.ImportMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_message_with_options(request, runtime)

    async def import_message_async(
        self,
        request: live_interaction_20201214_models.ImportMessageRequest,
    ) -> live_interaction_20201214_models.ImportMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_message_with_options_async(request, runtime)

    def silence_all_group_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SilenceAllGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SilenceAllGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SilenceAllGroupMembersResponse(),
            self.do_rpcrequest('SilenceAllGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def silence_all_group_members_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.SilenceAllGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SilenceAllGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SilenceAllGroupMembersResponse(),
            await self.do_rpcrequest_async('SilenceAllGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def silence_all_group_members(
        self,
        request: live_interaction_20201214_models.SilenceAllGroupMembersRequest,
    ) -> live_interaction_20201214_models.SilenceAllGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.silence_all_group_members_with_options(request, runtime)

    async def silence_all_group_members_async(
        self,
        request: live_interaction_20201214_models.SilenceAllGroupMembersRequest,
    ) -> live_interaction_20201214_models.SilenceAllGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.silence_all_group_members_with_options_async(request, runtime)

    def list_room_messages_with_options(
        self,
        request: live_interaction_20201214_models.ListRoomMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListRoomMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomMessagesResponse(),
            self.do_rpcrequest('ListRoomMessages', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_room_messages_with_options_async(
        self,
        request: live_interaction_20201214_models.ListRoomMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListRoomMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomMessagesResponse(),
            await self.do_rpcrequest_async('ListRoomMessages', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_room_messages(
        self,
        request: live_interaction_20201214_models.ListRoomMessagesRequest,
    ) -> live_interaction_20201214_models.ListRoomMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_room_messages_with_options(request, runtime)

    async def list_room_messages_async(
        self,
        request: live_interaction_20201214_models.ListRoomMessagesRequest,
    ) -> live_interaction_20201214_models.ListRoomMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_room_messages_with_options_async(request, runtime)

    def set_group_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetGroupExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetGroupExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupExtensionByKeysResponse(),
            self.do_rpcrequest('SetGroupExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_group_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.SetGroupExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetGroupExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupExtensionByKeysResponse(),
            await self.do_rpcrequest_async('SetGroupExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_group_extension_by_keys(
        self,
        request: live_interaction_20201214_models.SetGroupExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetGroupExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_group_extension_by_keys_with_options(request, runtime)

    async def set_group_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.SetGroupExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetGroupExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_group_extension_by_keys_with_options_async(request, runtime)

    def remove_group_member_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveGroupMemberExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_group_member_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse(),
            await self.do_rpcrequest_async('RemoveGroupMemberExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_member_extension_by_keys(
        self,
        request: live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_group_member_extension_by_keys_with_options(request, runtime)

    async def remove_group_member_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_group_member_extension_by_keys_with_options_async(request, runtime)

    def add_group_silence_blacklist_with_options(
        self,
        tmp_req: live_interaction_20201214_models.AddGroupSilenceBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.AddGroupSilenceBlacklistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceBlacklistResponse(),
            self.do_rpcrequest('AddGroupSilenceBlacklist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_group_silence_blacklist_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.AddGroupSilenceBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.AddGroupSilenceBlacklistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceBlacklistResponse(),
            await self.do_rpcrequest_async('AddGroupSilenceBlacklist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_group_silence_blacklist(
        self,
        request: live_interaction_20201214_models.AddGroupSilenceBlacklistRequest,
    ) -> live_interaction_20201214_models.AddGroupSilenceBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_group_silence_blacklist_with_options(request, runtime)

    async def add_group_silence_blacklist_async(
        self,
        request: live_interaction_20201214_models.AddGroupSilenceBlacklistRequest,
    ) -> live_interaction_20201214_models.AddGroupSilenceBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_group_silence_blacklist_with_options_async(request, runtime)

    def remove_group_silence_whitelist_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupSilenceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse(),
            self.do_rpcrequest('RemoveGroupSilenceWhitelist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_group_silence_whitelist_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupSilenceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse(),
            await self.do_rpcrequest_async('RemoveGroupSilenceWhitelist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_silence_whitelist(
        self,
        request: live_interaction_20201214_models.RemoveGroupSilenceWhitelistRequest,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_group_silence_whitelist_with_options(request, runtime)

    async def remove_group_silence_whitelist_async(
        self,
        request: live_interaction_20201214_models.RemoveGroupSilenceWhitelistRequest,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_group_silence_whitelist_with_options_async(request, runtime)

    def list_detail_report_statistics_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ListDetailReportStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListDetailReportStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListDetailReportStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListDetailReportStatisticsResponse(),
            self.do_rpcrequest('ListDetailReportStatistics', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_detail_report_statistics_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ListDetailReportStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListDetailReportStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListDetailReportStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListDetailReportStatisticsResponse(),
            await self.do_rpcrequest_async('ListDetailReportStatistics', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_detail_report_statistics(
        self,
        request: live_interaction_20201214_models.ListDetailReportStatisticsRequest,
    ) -> live_interaction_20201214_models.ListDetailReportStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_detail_report_statistics_with_options(request, runtime)

    async def list_detail_report_statistics_async(
        self,
        request: live_interaction_20201214_models.ListDetailReportStatisticsRequest,
    ) -> live_interaction_20201214_models.ListDetailReportStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_detail_report_statistics_with_options_async(request, runtime)

    def set_user_conversation_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetUserConversationExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse(),
            self.do_rpcrequest('SetUserConversationExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_user_conversation_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.SetUserConversationExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse(),
            await self.do_rpcrequest_async('SetUserConversationExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_user_conversation_extension_by_keys(
        self,
        request: live_interaction_20201214_models.SetUserConversationExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_user_conversation_extension_by_keys_with_options(request, runtime)

    async def set_user_conversation_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.SetUserConversationExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_user_conversation_extension_by_keys_with_options_async(request, runtime)

    def get_group_by_id_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetGroupByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetGroupByIdResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupByIdResponse(),
            self.do_rpcrequest('GetGroupById', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_group_by_id_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.GetGroupByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetGroupByIdResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupByIdResponse(),
            await self.do_rpcrequest_async('GetGroupById', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_group_by_id(
        self,
        request: live_interaction_20201214_models.GetGroupByIdRequest,
    ) -> live_interaction_20201214_models.GetGroupByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_by_id_with_options(request, runtime)

    async def get_group_by_id_async(
        self,
        request: live_interaction_20201214_models.GetGroupByIdRequest,
    ) -> live_interaction_20201214_models.GetGroupByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_by_id_with_options_async(request, runtime)

    def update_tenant_status_with_options(
        self,
        request: live_interaction_20201214_models.UpdateTenantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateTenantStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateTenantStatusResponse(),
            self.do_rpcrequest('UpdateTenantStatus', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_tenant_status_with_options_async(
        self,
        request: live_interaction_20201214_models.UpdateTenantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateTenantStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateTenantStatusResponse(),
            await self.do_rpcrequest_async('UpdateTenantStatus', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_tenant_status(
        self,
        request: live_interaction_20201214_models.UpdateTenantStatusRequest,
    ) -> live_interaction_20201214_models.UpdateTenantStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_tenant_status_with_options(request, runtime)

    async def update_tenant_status_async(
        self,
        request: live_interaction_20201214_models.UpdateTenantStatusRequest,
    ) -> live_interaction_20201214_models.UpdateTenantStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_tenant_status_with_options_async(request, runtime)

    def get_common_config_with_options(
        self,
        request: live_interaction_20201214_models.GetCommonConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetCommonConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetCommonConfigResponse(),
            self.do_rpcrequest('GetCommonConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_common_config_with_options_async(
        self,
        request: live_interaction_20201214_models.GetCommonConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetCommonConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetCommonConfigResponse(),
            await self.do_rpcrequest_async('GetCommonConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_common_config(
        self,
        request: live_interaction_20201214_models.GetCommonConfigRequest,
    ) -> live_interaction_20201214_models.GetCommonConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_common_config_with_options(request, runtime)

    async def get_common_config_async(
        self,
        request: live_interaction_20201214_models.GetCommonConfigRequest,
    ) -> live_interaction_20201214_models.GetCommonConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_common_config_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendMessageResponse(),
            self.do_rpcrequest('SendMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_message_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendMessageResponse(),
            await self.do_rpcrequest_async('SendMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_message(
        self,
        request: live_interaction_20201214_models.SendMessageRequest,
    ) -> live_interaction_20201214_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: live_interaction_20201214_models.SendMessageRequest,
    ) -> live_interaction_20201214_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)

    def update_group_members_role_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateGroupMembersRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateGroupMembersRoleResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupMembersRoleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupMembersRoleResponse(),
            self.do_rpcrequest('UpdateGroupMembersRole', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_group_members_role_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.UpdateGroupMembersRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateGroupMembersRoleResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupMembersRoleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupMembersRoleResponse(),
            await self.do_rpcrequest_async('UpdateGroupMembersRole', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group_members_role(
        self,
        request: live_interaction_20201214_models.UpdateGroupMembersRoleRequest,
    ) -> live_interaction_20201214_models.UpdateGroupMembersRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_members_role_with_options(request, runtime)

    async def update_group_members_role_async(
        self,
        request: live_interaction_20201214_models.UpdateGroupMembersRoleRequest,
    ) -> live_interaction_20201214_models.UpdateGroupMembersRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_members_role_with_options_async(request, runtime)

    def cancel_silence_all_group_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.CancelSilenceAllGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CancelSilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse(),
            self.do_rpcrequest('CancelSilenceAllGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_silence_all_group_members_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.CancelSilenceAllGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CancelSilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse(),
            await self.do_rpcrequest_async('CancelSilenceAllGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_silence_all_group_members(
        self,
        request: live_interaction_20201214_models.CancelSilenceAllGroupMembersRequest,
    ) -> live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_silence_all_group_members_with_options(request, runtime)

    async def cancel_silence_all_group_members_async(
        self,
        request: live_interaction_20201214_models.CancelSilenceAllGroupMembersRequest,
    ) -> live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_silence_all_group_members_with_options_async(request, runtime)

    def update_group_icon_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateGroupIconRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateGroupIconResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupIconShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupIconResponse(),
            self.do_rpcrequest('UpdateGroupIcon', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_group_icon_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.UpdateGroupIconRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateGroupIconResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupIconShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupIconResponse(),
            await self.do_rpcrequest_async('UpdateGroupIcon', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group_icon(
        self,
        request: live_interaction_20201214_models.UpdateGroupIconRequest,
    ) -> live_interaction_20201214_models.UpdateGroupIconResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_icon_with_options(request, runtime)

    async def update_group_icon_async(
        self,
        request: live_interaction_20201214_models.UpdateGroupIconRequest,
    ) -> live_interaction_20201214_models.UpdateGroupIconResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_icon_with_options_async(request, runtime)

    def remove_group_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMembersResponse(),
            self.do_rpcrequest('RemoveGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_group_members_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMembersResponse(),
            await self.do_rpcrequest_async('RemoveGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_members(
        self,
        request: live_interaction_20201214_models.RemoveGroupMembersRequest,
    ) -> live_interaction_20201214_models.RemoveGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_group_members_with_options(request, runtime)

    async def remove_group_members_async(
        self,
        request: live_interaction_20201214_models.RemoveGroupMembersRequest,
    ) -> live_interaction_20201214_models.RemoveGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_group_members_with_options_async(request, runtime)

    def list_group_all_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ListGroupAllMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListGroupAllMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupAllMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupAllMembersResponse(),
            self.do_rpcrequest('ListGroupAllMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_group_all_members_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ListGroupAllMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListGroupAllMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupAllMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupAllMembersResponse(),
            await self.do_rpcrequest_async('ListGroupAllMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_group_all_members(
        self,
        request: live_interaction_20201214_models.ListGroupAllMembersRequest,
    ) -> live_interaction_20201214_models.ListGroupAllMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_group_all_members_with_options(request, runtime)

    async def list_group_all_members_async(
        self,
        request: live_interaction_20201214_models.ListGroupAllMembersRequest,
    ) -> live_interaction_20201214_models.ListGroupAllMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_group_all_members_with_options_async(request, runtime)

    def get_user_mute_setting_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetUserMuteSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetUserMuteSettingResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetUserMuteSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetUserMuteSettingResponse(),
            self.do_rpcrequest('GetUserMuteSetting', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_mute_setting_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.GetUserMuteSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetUserMuteSettingResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetUserMuteSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetUserMuteSettingResponse(),
            await self.do_rpcrequest_async('GetUserMuteSetting', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_mute_setting(
        self,
        request: live_interaction_20201214_models.GetUserMuteSettingRequest,
    ) -> live_interaction_20201214_models.GetUserMuteSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_mute_setting_with_options(request, runtime)

    async def get_user_mute_setting_async(
        self,
        request: live_interaction_20201214_models.GetUserMuteSettingRequest,
    ) -> live_interaction_20201214_models.GetUserMuteSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_mute_setting_with_options_async(request, runtime)

    def get_room_statistics_with_options(
        self,
        request: live_interaction_20201214_models.GetRoomStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetRoomStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetRoomStatisticsResponse(),
            self.do_rpcrequest('GetRoomStatistics', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_room_statistics_with_options_async(
        self,
        request: live_interaction_20201214_models.GetRoomStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetRoomStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetRoomStatisticsResponse(),
            await self.do_rpcrequest_async('GetRoomStatistics', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_room_statistics(
        self,
        request: live_interaction_20201214_models.GetRoomStatisticsRequest,
    ) -> live_interaction_20201214_models.GetRoomStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_room_statistics_with_options(request, runtime)

    async def get_room_statistics_async(
        self,
        request: live_interaction_20201214_models.GetRoomStatisticsRequest,
    ) -> live_interaction_20201214_models.GetRoomStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_room_statistics_with_options_async(request, runtime)

    def add_group_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.AddGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.AddGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupMembersResponse(),
            self.do_rpcrequest('AddGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_group_members_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.AddGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.AddGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupMembersResponse(),
            await self.do_rpcrequest_async('AddGroupMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_group_members(
        self,
        request: live_interaction_20201214_models.AddGroupMembersRequest,
    ) -> live_interaction_20201214_models.AddGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_group_members_with_options(request, runtime)

    async def add_group_members_async(
        self,
        request: live_interaction_20201214_models.AddGroupMembersRequest,
    ) -> live_interaction_20201214_models.AddGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_group_members_with_options_async(request, runtime)

    def get_group_member_by_ids_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetGroupMemberByIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetGroupMemberByIdsResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupMemberByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupMemberByIdsResponse(),
            self.do_rpcrequest('GetGroupMemberByIds', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_group_member_by_ids_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.GetGroupMemberByIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetGroupMemberByIdsResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupMemberByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupMemberByIdsResponse(),
            await self.do_rpcrequest_async('GetGroupMemberByIds', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_group_member_by_ids(
        self,
        request: live_interaction_20201214_models.GetGroupMemberByIdsRequest,
    ) -> live_interaction_20201214_models.GetGroupMemberByIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_member_by_ids_with_options(request, runtime)

    async def get_group_member_by_ids_async(
        self,
        request: live_interaction_20201214_models.GetGroupMemberByIdsRequest,
    ) -> live_interaction_20201214_models.GetGroupMemberByIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_member_by_ids_with_options_async(request, runtime)

    def send_custom_message_with_options(
        self,
        request: live_interaction_20201214_models.SendCustomMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendCustomMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageResponse(),
            self.do_rpcrequest('SendCustomMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_custom_message_with_options_async(
        self,
        request: live_interaction_20201214_models.SendCustomMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendCustomMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageResponse(),
            await self.do_rpcrequest_async('SendCustomMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_custom_message(
        self,
        request: live_interaction_20201214_models.SendCustomMessageRequest,
    ) -> live_interaction_20201214_models.SendCustomMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_with_options(request, runtime)

    async def send_custom_message_async(
        self,
        request: live_interaction_20201214_models.SendCustomMessageRequest,
    ) -> live_interaction_20201214_models.SendCustomMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_custom_message_with_options_async(request, runtime)

    def update_app_name_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateAppNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateAppNameResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppNameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppNameResponse(),
            self.do_rpcrequest('UpdateAppName', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_name_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.UpdateAppNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateAppNameResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppNameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppNameResponse(),
            await self.do_rpcrequest_async('UpdateAppName', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_name(
        self,
        request: live_interaction_20201214_models.UpdateAppNameRequest,
    ) -> live_interaction_20201214_models.UpdateAppNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_name_with_options(request, runtime)

    async def update_app_name_async(
        self,
        request: live_interaction_20201214_models.UpdateAppNameRequest,
    ) -> live_interaction_20201214_models.UpdateAppNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_name_with_options_async(request, runtime)

    def get_imconfig_with_options(
        self,
        request: live_interaction_20201214_models.GetIMConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetIMConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetIMConfigResponse(),
            self.do_rpcrequest('GetIMConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_imconfig_with_options_async(
        self,
        request: live_interaction_20201214_models.GetIMConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetIMConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetIMConfigResponse(),
            await self.do_rpcrequest_async('GetIMConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_imconfig(
        self,
        request: live_interaction_20201214_models.GetIMConfigRequest,
    ) -> live_interaction_20201214_models.GetIMConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_imconfig_with_options(request, runtime)

    async def get_imconfig_async(
        self,
        request: live_interaction_20201214_models.GetIMConfigRequest,
    ) -> live_interaction_20201214_models.GetIMConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_imconfig_with_options_async(request, runtime)

    def set_single_chat_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetSingleChatExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse(),
            self.do_rpcrequest('SetSingleChatExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_single_chat_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.SetSingleChatExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse(),
            await self.do_rpcrequest_async('SetSingleChatExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_single_chat_extension_by_keys(
        self,
        request: live_interaction_20201214_models.SetSingleChatExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_single_chat_extension_by_keys_with_options(request, runtime)

    async def set_single_chat_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.SetSingleChatExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_single_chat_extension_by_keys_with_options_async(request, runtime)

    def update_app_status_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateAppStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppStatusResponse(),
            self.do_rpcrequest('UpdateAppStatus', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_status_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.UpdateAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateAppStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppStatusResponse(),
            await self.do_rpcrequest_async('UpdateAppStatus', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_status(
        self,
        request: live_interaction_20201214_models.UpdateAppStatusRequest,
    ) -> live_interaction_20201214_models.UpdateAppStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_status_with_options(request, runtime)

    async def update_app_status_async(
        self,
        request: live_interaction_20201214_models.UpdateAppStatusRequest,
    ) -> live_interaction_20201214_models.UpdateAppStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_status_with_options_async(request, runtime)

    def mute_users_with_options(
        self,
        tmp_req: live_interaction_20201214_models.MuteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.MuteUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.MuteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.MuteUsersResponse(),
            self.do_rpcrequest('MuteUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mute_users_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.MuteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.MuteUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.MuteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.MuteUsersResponse(),
            await self.do_rpcrequest_async('MuteUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mute_users(
        self,
        request: live_interaction_20201214_models.MuteUsersRequest,
    ) -> live_interaction_20201214_models.MuteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.mute_users_with_options(request, runtime)

    async def mute_users_async(
        self,
        request: live_interaction_20201214_models.MuteUsersRequest,
    ) -> live_interaction_20201214_models.MuteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mute_users_with_options_async(request, runtime)

    def recall_message_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RecallMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RecallMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RecallMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RecallMessageResponse(),
            self.do_rpcrequest('RecallMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recall_message_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.RecallMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RecallMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RecallMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RecallMessageResponse(),
            await self.do_rpcrequest_async('RecallMessage', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recall_message(
        self,
        request: live_interaction_20201214_models.RecallMessageRequest,
    ) -> live_interaction_20201214_models.RecallMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.recall_message_with_options(request, runtime)

    async def recall_message_async(
        self,
        request: live_interaction_20201214_models.RecallMessageRequest,
    ) -> live_interaction_20201214_models.RecallMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recall_message_with_options_async(request, runtime)

    def add_group_silence_whitelist_with_options(
        self,
        tmp_req: live_interaction_20201214_models.AddGroupSilenceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.AddGroupSilenceWhitelistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceWhitelistResponse(),
            self.do_rpcrequest('AddGroupSilenceWhitelist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_group_silence_whitelist_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.AddGroupSilenceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.AddGroupSilenceWhitelistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceWhitelistResponse(),
            await self.do_rpcrequest_async('AddGroupSilenceWhitelist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_group_silence_whitelist(
        self,
        request: live_interaction_20201214_models.AddGroupSilenceWhitelistRequest,
    ) -> live_interaction_20201214_models.AddGroupSilenceWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_group_silence_whitelist_with_options(request, runtime)

    async def add_group_silence_whitelist_async(
        self,
        request: live_interaction_20201214_models.AddGroupSilenceWhitelistRequest,
    ) -> live_interaction_20201214_models.AddGroupSilenceWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_group_silence_whitelist_with_options_async(request, runtime)

    def set_group_owner_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetGroupOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetGroupOwnerResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupOwnerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupOwnerResponse(),
            self.do_rpcrequest('SetGroupOwner', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_group_owner_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.SetGroupOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetGroupOwnerResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupOwnerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupOwnerResponse(),
            await self.do_rpcrequest_async('SetGroupOwner', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_group_owner(
        self,
        request: live_interaction_20201214_models.SetGroupOwnerRequest,
    ) -> live_interaction_20201214_models.SetGroupOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_group_owner_with_options(request, runtime)

    async def set_group_owner_async(
        self,
        request: live_interaction_20201214_models.SetGroupOwnerRequest,
    ) -> live_interaction_20201214_models.SetGroupOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_group_owner_with_options_async(request, runtime)

    def list_room_users_with_options(
        self,
        request: live_interaction_20201214_models.ListRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListRoomUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomUsersResponse(),
            self.do_rpcrequest('ListRoomUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_room_users_with_options_async(
        self,
        request: live_interaction_20201214_models.ListRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListRoomUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomUsersResponse(),
            await self.do_rpcrequest_async('ListRoomUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_room_users(
        self,
        request: live_interaction_20201214_models.ListRoomUsersRequest,
    ) -> live_interaction_20201214_models.ListRoomUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_room_users_with_options(request, runtime)

    async def list_room_users_async(
        self,
        request: live_interaction_20201214_models.ListRoomUsersRequest,
    ) -> live_interaction_20201214_models.ListRoomUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_room_users_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: live_interaction_20201214_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DeleteAppResponse(),
            self.do_rpcrequest('DeleteApp', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: live_interaction_20201214_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DeleteAppResponse(),
            await self.do_rpcrequest_async('DeleteApp', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app(
        self,
        request: live_interaction_20201214_models.DeleteAppRequest,
    ) -> live_interaction_20201214_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: live_interaction_20201214_models.DeleteAppRequest,
    ) -> live_interaction_20201214_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def remove_group_silence_blacklist_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupSilenceBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse(),
            self.do_rpcrequest('RemoveGroupSilenceBlacklist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_group_silence_blacklist_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupSilenceBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse(),
            await self.do_rpcrequest_async('RemoveGroupSilenceBlacklist', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_silence_blacklist(
        self,
        request: live_interaction_20201214_models.RemoveGroupSilenceBlacklistRequest,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_group_silence_blacklist_with_options(request, runtime)

    async def remove_group_silence_blacklist_async(
        self,
        request: live_interaction_20201214_models.RemoveGroupSilenceBlacklistRequest,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_group_silence_blacklist_with_options_async(request, runtime)

    def remove_message_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveMessageExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveMessageExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_message_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.RemoveMessageExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse(),
            await self.do_rpcrequest_async('RemoveMessageExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_message_extension_by_keys(
        self,
        request: live_interaction_20201214_models.RemoveMessageExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_message_extension_by_keys_with_options(request, runtime)

    async def remove_message_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.RemoveMessageExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_message_extension_by_keys_with_options_async(request, runtime)

    def get_media_upload_url_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetMediaUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetMediaUploadUrlResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMediaUploadUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUploadUrlResponse(),
            self.do_rpcrequest('GetMediaUploadUrl', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_upload_url_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.GetMediaUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetMediaUploadUrlResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMediaUploadUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUploadUrlResponse(),
            await self.do_rpcrequest_async('GetMediaUploadUrl', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_upload_url(
        self,
        request: live_interaction_20201214_models.GetMediaUploadUrlRequest,
    ) -> live_interaction_20201214_models.GetMediaUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_upload_url_with_options(request, runtime)

    async def get_media_upload_url_async(
        self,
        request: live_interaction_20201214_models.GetMediaUploadUrlRequest,
    ) -> live_interaction_20201214_models.GetMediaUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_upload_url_with_options_async(request, runtime)

    def get_media_url_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetMediaUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetMediaUrlResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMediaUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUrlResponse(),
            self.do_rpcrequest('GetMediaUrl', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_url_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.GetMediaUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetMediaUrlResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMediaUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUrlResponse(),
            await self.do_rpcrequest_async('GetMediaUrl', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_url(
        self,
        request: live_interaction_20201214_models.GetMediaUrlRequest,
    ) -> live_interaction_20201214_models.GetMediaUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_url_with_options(request, runtime)

    async def get_media_url_async(
        self,
        request: live_interaction_20201214_models.GetMediaUrlRequest,
    ) -> live_interaction_20201214_models.GetMediaUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_url_with_options_async(request, runtime)

    def import_single_conversation_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ImportSingleConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportSingleConversationResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportSingleConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportSingleConversationResponse(),
            self.do_rpcrequest('ImportSingleConversation', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_single_conversation_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ImportSingleConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportSingleConversationResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportSingleConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportSingleConversationResponse(),
            await self.do_rpcrequest_async('ImportSingleConversation', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_single_conversation(
        self,
        request: live_interaction_20201214_models.ImportSingleConversationRequest,
    ) -> live_interaction_20201214_models.ImportSingleConversationResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_single_conversation_with_options(request, runtime)

    async def import_single_conversation_async(
        self,
        request: live_interaction_20201214_models.ImportSingleConversationRequest,
    ) -> live_interaction_20201214_models.ImportSingleConversationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_single_conversation_with_options_async(request, runtime)

    def update_callback_config_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateCallbackConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateCallbackConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateCallbackConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateCallbackConfigResponse(),
            self.do_rpcrequest('UpdateCallbackConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_callback_config_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.UpdateCallbackConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateCallbackConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateCallbackConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateCallbackConfigResponse(),
            await self.do_rpcrequest_async('UpdateCallbackConfig', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_callback_config(
        self,
        request: live_interaction_20201214_models.UpdateCallbackConfigRequest,
    ) -> live_interaction_20201214_models.UpdateCallbackConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_callback_config_with_options(request, runtime)

    async def update_callback_config_async(
        self,
        request: live_interaction_20201214_models.UpdateCallbackConfigRequest,
    ) -> live_interaction_20201214_models.UpdateCallbackConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_callback_config_with_options_async(request, runtime)

    def init_tenant_with_options(
        self,
        request: live_interaction_20201214_models.InitTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.InitTenantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.InitTenantResponse(),
            self.do_rpcrequest('InitTenant', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def init_tenant_with_options_async(
        self,
        request: live_interaction_20201214_models.InitTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.InitTenantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.InitTenantResponse(),
            await self.do_rpcrequest_async('InitTenant', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_tenant(
        self,
        request: live_interaction_20201214_models.InitTenantRequest,
    ) -> live_interaction_20201214_models.InitTenantResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_tenant_with_options(request, runtime)

    async def init_tenant_async(
        self,
        request: live_interaction_20201214_models.InitTenantRequest,
    ) -> live_interaction_20201214_models.InitTenantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_tenant_with_options_async(request, runtime)

    def import_group_chat_member_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ImportGroupChatMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportGroupChatMemberResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatMemberResponse(),
            self.do_rpcrequest('ImportGroupChatMember', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_group_chat_member_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ImportGroupChatMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportGroupChatMemberResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatMemberResponse(),
            await self.do_rpcrequest_async('ImportGroupChatMember', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_group_chat_member(
        self,
        request: live_interaction_20201214_models.ImportGroupChatMemberRequest,
    ) -> live_interaction_20201214_models.ImportGroupChatMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_group_chat_member_with_options(request, runtime)

    async def import_group_chat_member_async(
        self,
        request: live_interaction_20201214_models.ImportGroupChatMemberRequest,
    ) -> live_interaction_20201214_models.ImportGroupChatMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_group_chat_member_with_options_async(request, runtime)

    def list_group_silence_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ListGroupSilenceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListGroupSilenceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupSilenceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupSilenceMembersResponse(),
            self.do_rpcrequest('ListGroupSilenceMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_group_silence_members_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ListGroupSilenceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListGroupSilenceMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupSilenceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupSilenceMembersResponse(),
            await self.do_rpcrequest_async('ListGroupSilenceMembers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_group_silence_members(
        self,
        request: live_interaction_20201214_models.ListGroupSilenceMembersRequest,
    ) -> live_interaction_20201214_models.ListGroupSilenceMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_group_silence_members_with_options(request, runtime)

    async def list_group_silence_members_async(
        self,
        request: live_interaction_20201214_models.ListGroupSilenceMembersRequest,
    ) -> live_interaction_20201214_models.ListGroupSilenceMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_group_silence_members_with_options_async(request, runtime)

    def remove_group_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveGroupExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_group_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse(),
            await self.do_rpcrequest_async('RemoveGroupExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_group_extension_by_keys(
        self,
        request: live_interaction_20201214_models.RemoveGroupExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_group_extension_by_keys_with_options(request, runtime)

    async def remove_group_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.RemoveGroupExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_group_extension_by_keys_with_options_async(request, runtime)

    def set_group_member_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetGroupMemberExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse(),
            self.do_rpcrequest('SetGroupMemberExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_group_member_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.SetGroupMemberExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse(),
            await self.do_rpcrequest_async('SetGroupMemberExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_group_member_extension_by_keys(
        self,
        request: live_interaction_20201214_models.SetGroupMemberExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_group_member_extension_by_keys_with_options(request, runtime)

    async def set_group_member_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.SetGroupMemberExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_group_member_extension_by_keys_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        tmp_req: live_interaction_20201214_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CreateGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CreateGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateGroupResponse(),
            self.do_rpcrequest('CreateGroup', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_group_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CreateGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CreateGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateGroupResponse(),
            await self.do_rpcrequest_async('CreateGroup', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group(
        self,
        request: live_interaction_20201214_models.CreateGroupRequest,
    ) -> live_interaction_20201214_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: live_interaction_20201214_models.CreateGroupRequest,
    ) -> live_interaction_20201214_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def get_message_by_id_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetMessageByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetMessageByIdResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMessageByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMessageByIdResponse(),
            self.do_rpcrequest('GetMessageById', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_message_by_id_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.GetMessageByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetMessageByIdResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMessageByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMessageByIdResponse(),
            await self.do_rpcrequest_async('GetMessageById', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_message_by_id(
        self,
        request: live_interaction_20201214_models.GetMessageByIdRequest,
    ) -> live_interaction_20201214_models.GetMessageByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_message_by_id_with_options(request, runtime)

    async def get_message_by_id_async(
        self,
        request: live_interaction_20201214_models.GetMessageByIdRequest,
    ) -> live_interaction_20201214_models.GetMessageByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_message_by_id_with_options_async(request, runtime)

    def destroy_room_with_options(
        self,
        request: live_interaction_20201214_models.DestroyRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DestroyRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DestroyRoomResponse(),
            self.do_rpcrequest('DestroyRoom', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def destroy_room_with_options_async(
        self,
        request: live_interaction_20201214_models.DestroyRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DestroyRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DestroyRoomResponse(),
            await self.do_rpcrequest_async('DestroyRoom', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def destroy_room(
        self,
        request: live_interaction_20201214_models.DestroyRoomRequest,
    ) -> live_interaction_20201214_models.DestroyRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_room_with_options(request, runtime)

    async def destroy_room_async(
        self,
        request: live_interaction_20201214_models.DestroyRoomRequest,
    ) -> live_interaction_20201214_models.DestroyRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_room_with_options_async(request, runtime)

    def kick_off_with_options(
        self,
        tmp_req: live_interaction_20201214_models.KickOffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.KickOffResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.KickOffShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.KickOffResponse(),
            self.do_rpcrequest('KickOff', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def kick_off_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.KickOffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.KickOffResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.KickOffShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.KickOffResponse(),
            await self.do_rpcrequest_async('KickOff', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kick_off(
        self,
        request: live_interaction_20201214_models.KickOffRequest,
    ) -> live_interaction_20201214_models.KickOffResponse:
        runtime = util_models.RuntimeOptions()
        return self.kick_off_with_options(request, runtime)

    async def kick_off_async(
        self,
        request: live_interaction_20201214_models.KickOffRequest,
    ) -> live_interaction_20201214_models.KickOffResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kick_off_with_options_async(request, runtime)

    def list_callback_api_ids_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListCallbackApiIdsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            live_interaction_20201214_models.ListCallbackApiIdsResponse(),
            self.do_rpcrequest('ListCallbackApiIds', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_callback_api_ids_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListCallbackApiIdsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            live_interaction_20201214_models.ListCallbackApiIdsResponse(),
            await self.do_rpcrequest_async('ListCallbackApiIds', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_callback_api_ids(self) -> live_interaction_20201214_models.ListCallbackApiIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_callback_api_ids_with_options(runtime)

    async def list_callback_api_ids_async(self) -> live_interaction_20201214_models.ListCallbackApiIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_callback_api_ids_with_options_async(runtime)

    def set_message_read_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetMessageReadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetMessageReadResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageReadShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageReadResponse(),
            self.do_rpcrequest('SetMessageRead', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_message_read_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.SetMessageReadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetMessageReadResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageReadShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageReadResponse(),
            await self.do_rpcrequest_async('SetMessageRead', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_message_read(
        self,
        request: live_interaction_20201214_models.SetMessageReadRequest,
    ) -> live_interaction_20201214_models.SetMessageReadResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_message_read_with_options(request, runtime)

    async def set_message_read_async(
        self,
        request: live_interaction_20201214_models.SetMessageReadRequest,
    ) -> live_interaction_20201214_models.SetMessageReadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_message_read_with_options_async(request, runtime)

    def update_msg_recall_interval_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateMsgRecallIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateMsgRecallIntervalResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateMsgRecallIntervalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateMsgRecallIntervalResponse(),
            self.do_rpcrequest('UpdateMsgRecallInterval', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_msg_recall_interval_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.UpdateMsgRecallIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateMsgRecallIntervalResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateMsgRecallIntervalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateMsgRecallIntervalResponse(),
            await self.do_rpcrequest_async('UpdateMsgRecallInterval', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_msg_recall_interval(
        self,
        request: live_interaction_20201214_models.UpdateMsgRecallIntervalRequest,
    ) -> live_interaction_20201214_models.UpdateMsgRecallIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_msg_recall_interval_with_options(request, runtime)

    async def update_msg_recall_interval_async(
        self,
        request: live_interaction_20201214_models.UpdateMsgRecallIntervalRequest,
    ) -> live_interaction_20201214_models.UpdateMsgRecallIntervalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_msg_recall_interval_with_options_async(request, runtime)

    def send_custom_message_to_room_users_with_options(
        self,
        request: live_interaction_20201214_models.SendCustomMessageToRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse(),
            self.do_rpcrequest('SendCustomMessageToRoomUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_custom_message_to_room_users_with_options_async(
        self,
        request: live_interaction_20201214_models.SendCustomMessageToRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse(),
            await self.do_rpcrequest_async('SendCustomMessageToRoomUsers', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_custom_message_to_room_users(
        self,
        request: live_interaction_20201214_models.SendCustomMessageToRoomUsersRequest,
    ) -> live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_custom_message_to_room_users_with_options(request, runtime)

    async def send_custom_message_to_room_users_async(
        self,
        request: live_interaction_20201214_models.SendCustomMessageToRoomUsersRequest,
    ) -> live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_custom_message_to_room_users_with_options_async(request, runtime)

    def update_group_title_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateGroupTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateGroupTitleResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupTitleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupTitleResponse(),
            self.do_rpcrequest('UpdateGroupTitle', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_group_title_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.UpdateGroupTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateGroupTitleResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupTitleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupTitleResponse(),
            await self.do_rpcrequest_async('UpdateGroupTitle', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_group_title(
        self,
        request: live_interaction_20201214_models.UpdateGroupTitleRequest,
    ) -> live_interaction_20201214_models.UpdateGroupTitleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_title_with_options(request, runtime)

    async def update_group_title_async(
        self,
        request: live_interaction_20201214_models.UpdateGroupTitleRequest,
    ) -> live_interaction_20201214_models.UpdateGroupTitleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_title_with_options_async(request, runtime)

    def get_login_token_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetLoginTokenResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetLoginTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetLoginTokenResponse(),
            self.do_rpcrequest('GetLoginToken', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_login_token_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.GetLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetLoginTokenResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetLoginTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetLoginTokenResponse(),
            await self.do_rpcrequest_async('GetLoginToken', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_login_token(
        self,
        request: live_interaction_20201214_models.GetLoginTokenRequest,
    ) -> live_interaction_20201214_models.GetLoginTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_login_token_with_options(request, runtime)

    async def get_login_token_async(
        self,
        request: live_interaction_20201214_models.GetLoginTokenRequest,
    ) -> live_interaction_20201214_models.GetLoginTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_login_token_with_options_async(request, runtime)

    def dismiss_group_with_options(
        self,
        tmp_req: live_interaction_20201214_models.DismissGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DismissGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.DismissGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DismissGroupResponse(),
            self.do_rpcrequest('DismissGroup', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dismiss_group_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.DismissGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DismissGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.DismissGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DismissGroupResponse(),
            await self.do_rpcrequest_async('DismissGroup', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dismiss_group(
        self,
        request: live_interaction_20201214_models.DismissGroupRequest,
    ) -> live_interaction_20201214_models.DismissGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.dismiss_group_with_options(request, runtime)

    async def dismiss_group_async(
        self,
        request: live_interaction_20201214_models.DismissGroupRequest,
    ) -> live_interaction_20201214_models.DismissGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dismiss_group_with_options_async(request, runtime)

    def import_group_chat_conversation_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ImportGroupChatConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportGroupChatConversationResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatConversationResponse(),
            self.do_rpcrequest('ImportGroupChatConversation', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_group_chat_conversation_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ImportGroupChatConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportGroupChatConversationResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatConversationResponse(),
            await self.do_rpcrequest_async('ImportGroupChatConversation', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_group_chat_conversation(
        self,
        request: live_interaction_20201214_models.ImportGroupChatConversationRequest,
    ) -> live_interaction_20201214_models.ImportGroupChatConversationResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_group_chat_conversation_with_options(request, runtime)

    async def import_group_chat_conversation_async(
        self,
        request: live_interaction_20201214_models.ImportGroupChatConversationRequest,
    ) -> live_interaction_20201214_models.ImportGroupChatConversationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_group_chat_conversation_with_options_async(request, runtime)

    def create_room_with_options(
        self,
        request: live_interaction_20201214_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CreateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateRoomResponse(),
            self.do_rpcrequest('CreateRoom', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_room_with_options_async(
        self,
        request: live_interaction_20201214_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CreateRoomResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateRoomResponse(),
            await self.do_rpcrequest_async('CreateRoom', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_room(
        self,
        request: live_interaction_20201214_models.CreateRoomRequest,
    ) -> live_interaction_20201214_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    async def create_room_async(
        self,
        request: live_interaction_20201214_models.CreateRoomRequest,
    ) -> live_interaction_20201214_models.CreateRoomResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_room_with_options_async(request, runtime)

    def remove_user_conversation_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveUserConversationExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse(),
            self.do_rpcrequest('RemoveUserConversationExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_user_conversation_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.RemoveUserConversationExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse(),
            await self.do_rpcrequest_async('RemoveUserConversationExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_user_conversation_extension_by_keys(
        self,
        request: live_interaction_20201214_models.RemoveUserConversationExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_user_conversation_extension_by_keys_with_options(request, runtime)

    async def remove_user_conversation_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.RemoveUserConversationExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_conversation_extension_by_keys_with_options_async(request, runtime)

    def set_message_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetMessageExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetMessageExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageExtensionByKeysResponse(),
            self.do_rpcrequest('SetMessageExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_message_extension_by_keys_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.SetMessageExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetMessageExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.request_params), 'RequestParams', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageExtensionByKeysResponse(),
            await self.do_rpcrequest_async('SetMessageExtensionByKeys', '2020-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_message_extension_by_keys(
        self,
        request: live_interaction_20201214_models.SetMessageExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetMessageExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_message_extension_by_keys_with_options(request, runtime)

    async def set_message_extension_by_keys_async(
        self,
        request: live_interaction_20201214_models.SetMessageExtensionByKeysRequest,
    ) -> live_interaction_20201214_models.SetMessageExtensionByKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_message_extension_by_keys_with_options_async(request, runtime)
