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

    def add_group_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.AddGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.AddGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupMembersResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def add_group_silence_blacklist_with_options(
        self,
        tmp_req: live_interaction_20201214_models.AddGroupSilenceBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.AddGroupSilenceBlacklistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupSilenceBlacklist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceBlacklistResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupSilenceBlacklist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
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

    def add_group_silence_whitelist_with_options(
        self,
        tmp_req: live_interaction_20201214_models.AddGroupSilenceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.AddGroupSilenceWhitelistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.AddGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupSilenceWhitelist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceWhitelistResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupSilenceWhitelist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.AddGroupSilenceWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
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

    def bind_interconnection_cid_with_options(
        self,
        tmp_req: live_interaction_20201214_models.BindInterconnectionCidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.BindInterconnectionCidResponse:
        """
        @deprecated
        
        @param tmp_req: BindInterconnectionCidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindInterconnectionCidResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.BindInterconnectionCidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindInterconnectionCid',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.BindInterconnectionCidResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_interconnection_cid_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.BindInterconnectionCidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.BindInterconnectionCidResponse:
        """
        @deprecated
        
        @param tmp_req: BindInterconnectionCidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindInterconnectionCidResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.BindInterconnectionCidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindInterconnectionCid',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.BindInterconnectionCidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_interconnection_cid(
        self,
        request: live_interaction_20201214_models.BindInterconnectionCidRequest,
    ) -> live_interaction_20201214_models.BindInterconnectionCidResponse:
        """
        @deprecated
        
        @param request: BindInterconnectionCidRequest
        @return: BindInterconnectionCidResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_interconnection_cid_with_options(request, runtime)

    async def bind_interconnection_cid_async(
        self,
        request: live_interaction_20201214_models.BindInterconnectionCidRequest,
    ) -> live_interaction_20201214_models.BindInterconnectionCidResponse:
        """
        @deprecated
        
        @param request: BindInterconnectionCidRequest
        @return: BindInterconnectionCidResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_interconnection_cid_with_options_async(request, runtime)

    def bind_interconnection_uid_with_options(
        self,
        tmp_req: live_interaction_20201214_models.BindInterconnectionUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.BindInterconnectionUidResponse:
        """
        @deprecated
        
        @param tmp_req: BindInterconnectionUidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindInterconnectionUidResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.BindInterconnectionUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindInterconnectionUid',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.BindInterconnectionUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_interconnection_uid_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.BindInterconnectionUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.BindInterconnectionUidResponse:
        """
        @deprecated
        
        @param tmp_req: BindInterconnectionUidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindInterconnectionUidResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.BindInterconnectionUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindInterconnectionUid',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.BindInterconnectionUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_interconnection_uid(
        self,
        request: live_interaction_20201214_models.BindInterconnectionUidRequest,
    ) -> live_interaction_20201214_models.BindInterconnectionUidResponse:
        """
        @deprecated
        
        @param request: BindInterconnectionUidRequest
        @return: BindInterconnectionUidResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_interconnection_uid_with_options(request, runtime)

    async def bind_interconnection_uid_async(
        self,
        request: live_interaction_20201214_models.BindInterconnectionUidRequest,
    ) -> live_interaction_20201214_models.BindInterconnectionUidResponse:
        """
        @deprecated
        
        @param request: BindInterconnectionUidRequest
        @return: BindInterconnectionUidResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_interconnection_uid_with_options_async(request, runtime)

    def cancel_silence_all_group_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.CancelSilenceAllGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CancelSilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelSilenceAllGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelSilenceAllGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CancelSilenceAllGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_group_with_options(
        self,
        tmp_req: live_interaction_20201214_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CreateGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.CreateGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_room_with_options(
        self,
        request: live_interaction_20201214_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CreateRoomResponse:
        """
        @deprecated
        
        @param request: CreateRoomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoomResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoom',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_room_with_options_async(
        self,
        request: live_interaction_20201214_models.CreateRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.CreateRoomResponse:
        """
        @deprecated
        
        @param request: CreateRoomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoomResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoom',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.CreateRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_room(
        self,
        request: live_interaction_20201214_models.CreateRoomRequest,
    ) -> live_interaction_20201214_models.CreateRoomResponse:
        """
        @deprecated
        
        @param request: CreateRoomRequest
        @return: CreateRoomResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_room_with_options(request, runtime)

    async def create_room_async(
        self,
        request: live_interaction_20201214_models.CreateRoomRequest,
    ) -> live_interaction_20201214_models.CreateRoomResponse:
        """
        @deprecated
        
        @param request: CreateRoomRequest
        @return: CreateRoomResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_room_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: live_interaction_20201214_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: live_interaction_20201214_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
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

    def destroy_room_with_options(
        self,
        request: live_interaction_20201214_models.DestroyRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DestroyRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DestroyRoom',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DestroyRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_room_with_options_async(
        self,
        request: live_interaction_20201214_models.DestroyRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DestroyRoomResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DestroyRoom',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DestroyRoomResponse(),
            await self.call_api_async(params, req, runtime)
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

    def dismiss_group_with_options(
        self,
        tmp_req: live_interaction_20201214_models.DismissGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DismissGroupResponse:
        """
        @deprecated
        
        @param tmp_req: DismissGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DismissGroupResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.DismissGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DismissGroup',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DismissGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def dismiss_group_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.DismissGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.DismissGroupResponse:
        """
        @deprecated
        
        @param tmp_req: DismissGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DismissGroupResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.DismissGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DismissGroup',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.DismissGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dismiss_group(
        self,
        request: live_interaction_20201214_models.DismissGroupRequest,
    ) -> live_interaction_20201214_models.DismissGroupResponse:
        """
        @deprecated
        
        @param request: DismissGroupRequest
        @return: DismissGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.dismiss_group_with_options(request, runtime)

    async def dismiss_group_async(
        self,
        request: live_interaction_20201214_models.DismissGroupRequest,
    ) -> live_interaction_20201214_models.DismissGroupResponse:
        """
        @deprecated
        
        @param request: DismissGroupRequest
        @return: DismissGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.dismiss_group_with_options_async(request, runtime)

    def get_common_config_with_options(
        self,
        request: live_interaction_20201214_models.GetCommonConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetCommonConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCommonConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetCommonConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_common_config_with_options_async(
        self,
        request: live_interaction_20201214_models.GetCommonConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetCommonConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCommonConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetCommonConfigResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_group_by_id_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetGroupByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetGroupByIdResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroupById',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupByIdResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroupById',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupByIdResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_group_member_by_ids_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetGroupMemberByIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetGroupMemberByIdsResponse:
        """
        @deprecated
        
        @param tmp_req: GetGroupMemberByIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupMemberByIdsResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupMemberByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroupMemberByIds',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupMemberByIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_member_by_ids_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.GetGroupMemberByIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetGroupMemberByIdsResponse:
        """
        @deprecated
        
        @param tmp_req: GetGroupMemberByIdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupMemberByIdsResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetGroupMemberByIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroupMemberByIds',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetGroupMemberByIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group_member_by_ids(
        self,
        request: live_interaction_20201214_models.GetGroupMemberByIdsRequest,
    ) -> live_interaction_20201214_models.GetGroupMemberByIdsResponse:
        """
        @deprecated
        
        @param request: GetGroupMemberByIdsRequest
        @return: GetGroupMemberByIdsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_group_member_by_ids_with_options(request, runtime)

    async def get_group_member_by_ids_async(
        self,
        request: live_interaction_20201214_models.GetGroupMemberByIdsRequest,
    ) -> live_interaction_20201214_models.GetGroupMemberByIdsResponse:
        """
        @deprecated
        
        @param request: GetGroupMemberByIdsRequest
        @return: GetGroupMemberByIdsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_group_member_by_ids_with_options_async(request, runtime)

    def get_imconfig_with_options(
        self,
        request: live_interaction_20201214_models.GetIMConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetIMConfigResponse:
        """
        @deprecated
        
        @param request: GetIMConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIMConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIMConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetIMConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_imconfig_with_options_async(
        self,
        request: live_interaction_20201214_models.GetIMConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetIMConfigResponse:
        """
        @deprecated
        
        @param request: GetIMConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIMConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIMConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetIMConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_imconfig(
        self,
        request: live_interaction_20201214_models.GetIMConfigRequest,
    ) -> live_interaction_20201214_models.GetIMConfigResponse:
        """
        @deprecated
        
        @param request: GetIMConfigRequest
        @return: GetIMConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_imconfig_with_options(request, runtime)

    async def get_imconfig_async(
        self,
        request: live_interaction_20201214_models.GetIMConfigRequest,
    ) -> live_interaction_20201214_models.GetIMConfigResponse:
        """
        @deprecated
        
        @param request: GetIMConfigRequest
        @return: GetIMConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_imconfig_with_options_async(request, runtime)

    def get_login_token_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetLoginTokenResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetLoginTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLoginToken',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetLoginTokenResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLoginToken',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_media_upload_url_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetMediaUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetMediaUploadUrlResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMediaUploadUrlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMediaUploadUrl',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUploadUrlResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMediaUploadUrl',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMediaUrl',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUrlResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMediaUrl',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMediaUrlResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_message_by_id_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetMessageByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetMessageByIdResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetMessageByIdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageById',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMessageByIdResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageById',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetMessageByIdResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_room_statistics_with_options(
        self,
        request: live_interaction_20201214_models.GetRoomStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetRoomStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoomStatistics',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetRoomStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_room_statistics_with_options_async(
        self,
        request: live_interaction_20201214_models.GetRoomStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetRoomStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoomStatistics',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetRoomStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_user_mute_setting_with_options(
        self,
        tmp_req: live_interaction_20201214_models.GetUserMuteSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetUserMuteSettingResponse:
        """
        @deprecated
        
        @param tmp_req: GetUserMuteSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserMuteSettingResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetUserMuteSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserMuteSetting',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetUserMuteSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_mute_setting_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.GetUserMuteSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.GetUserMuteSettingResponse:
        """
        @deprecated
        
        @param tmp_req: GetUserMuteSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserMuteSettingResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.GetUserMuteSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserMuteSetting',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.GetUserMuteSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_mute_setting(
        self,
        request: live_interaction_20201214_models.GetUserMuteSettingRequest,
    ) -> live_interaction_20201214_models.GetUserMuteSettingResponse:
        """
        @deprecated
        
        @param request: GetUserMuteSettingRequest
        @return: GetUserMuteSettingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_mute_setting_with_options(request, runtime)

    async def get_user_mute_setting_async(
        self,
        request: live_interaction_20201214_models.GetUserMuteSettingRequest,
    ) -> live_interaction_20201214_models.GetUserMuteSettingResponse:
        """
        @deprecated
        
        @param request: GetUserMuteSettingRequest
        @return: GetUserMuteSettingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_mute_setting_with_options_async(request, runtime)

    def import_group_chat_conversation_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ImportGroupChatConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportGroupChatConversationResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportGroupChatConversation',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatConversationResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportGroupChatConversation',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatConversationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def import_group_chat_member_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ImportGroupChatMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportGroupChatMemberResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportGroupChatMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportGroupChatMember',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatMemberResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportGroupChatMember',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportGroupChatMemberResponse(),
            await self.call_api_async(params, req, runtime)
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

    def import_message_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ImportMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportMessageResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportMessageResponse(),
            await self.call_api_async(params, req, runtime)
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

    def import_single_conversation_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ImportSingleConversationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ImportSingleConversationResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ImportSingleConversationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportSingleConversation',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportSingleConversationResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportSingleConversation',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ImportSingleConversationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def init_tenant_with_options(
        self,
        request: live_interaction_20201214_models.InitTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.InitTenantResponse:
        """
        @deprecated
        
        @param request: InitTenantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitTenantResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitTenant',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.InitTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_tenant_with_options_async(
        self,
        request: live_interaction_20201214_models.InitTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.InitTenantResponse:
        """
        @deprecated
        
        @param request: InitTenantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitTenantResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitTenant',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.InitTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_tenant(
        self,
        request: live_interaction_20201214_models.InitTenantRequest,
    ) -> live_interaction_20201214_models.InitTenantResponse:
        """
        @deprecated
        
        @param request: InitTenantRequest
        @return: InitTenantResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.init_tenant_with_options(request, runtime)

    async def init_tenant_async(
        self,
        request: live_interaction_20201214_models.InitTenantRequest,
    ) -> live_interaction_20201214_models.InitTenantResponse:
        """
        @deprecated
        
        @param request: InitTenantRequest
        @return: InitTenantResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.init_tenant_with_options_async(request, runtime)

    def kick_off_with_options(
        self,
        tmp_req: live_interaction_20201214_models.KickOffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.KickOffResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.KickOffShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KickOff',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.KickOffResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KickOff',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.KickOffResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_app_infos_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ListAppInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListAppInfosResponse:
        """
        @deprecated
        
        @param tmp_req: ListAppInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppInfosResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListAppInfosShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppInfos',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListAppInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_infos_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ListAppInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListAppInfosResponse:
        """
        @deprecated
        
        @param tmp_req: ListAppInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppInfosResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListAppInfosShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppInfos',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListAppInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_infos(
        self,
        request: live_interaction_20201214_models.ListAppInfosRequest,
    ) -> live_interaction_20201214_models.ListAppInfosResponse:
        """
        @deprecated
        
        @param request: ListAppInfosRequest
        @return: ListAppInfosResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_infos_with_options(request, runtime)

    async def list_app_infos_async(
        self,
        request: live_interaction_20201214_models.ListAppInfosRequest,
    ) -> live_interaction_20201214_models.ListAppInfosResponse:
        """
        @deprecated
        
        @param request: ListAppInfosRequest
        @return: ListAppInfosResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_infos_with_options_async(request, runtime)

    def list_callback_api_ids_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListCallbackApiIdsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCallbackApiIds',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListCallbackApiIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_callback_api_ids_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListCallbackApiIdsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCallbackApiIds',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListCallbackApiIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_callback_api_ids(self) -> live_interaction_20201214_models.ListCallbackApiIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_callback_api_ids_with_options(runtime)

    async def list_callback_api_ids_async(self) -> live_interaction_20201214_models.ListCallbackApiIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_callback_api_ids_with_options_async(runtime)

    def list_detail_report_statistics_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ListDetailReportStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListDetailReportStatisticsResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListDetailReportStatisticsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDetailReportStatistics',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListDetailReportStatisticsResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDetailReportStatistics',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListDetailReportStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_group_all_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ListGroupAllMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListGroupAllMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupAllMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroupAllMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupAllMembersResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroupAllMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupAllMembersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_group_silence_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.ListGroupSilenceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListGroupSilenceMembersResponse:
        """
        @deprecated
        
        @param tmp_req: ListGroupSilenceMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupSilenceMembersResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupSilenceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroupSilenceMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupSilenceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_silence_members_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.ListGroupSilenceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListGroupSilenceMembersResponse:
        """
        @deprecated
        
        @param tmp_req: ListGroupSilenceMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupSilenceMembersResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.ListGroupSilenceMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroupSilenceMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListGroupSilenceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group_silence_members(
        self,
        request: live_interaction_20201214_models.ListGroupSilenceMembersRequest,
    ) -> live_interaction_20201214_models.ListGroupSilenceMembersResponse:
        """
        @deprecated
        
        @param request: ListGroupSilenceMembersRequest
        @return: ListGroupSilenceMembersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_group_silence_members_with_options(request, runtime)

    async def list_group_silence_members_async(
        self,
        request: live_interaction_20201214_models.ListGroupSilenceMembersRequest,
    ) -> live_interaction_20201214_models.ListGroupSilenceMembersResponse:
        """
        @deprecated
        
        @param request: ListGroupSilenceMembersRequest
        @return: ListGroupSilenceMembersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_group_silence_members_with_options_async(request, runtime)

    def list_room_messages_with_options(
        self,
        request: live_interaction_20201214_models.ListRoomMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListRoomMessagesResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomMessages',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_room_messages_with_options_async(
        self,
        request: live_interaction_20201214_models.ListRoomMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListRoomMessagesResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomMessages',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomMessagesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_room_users_with_options(
        self,
        request: live_interaction_20201214_models.ListRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListRoomUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_room_users_with_options_async(
        self,
        request: live_interaction_20201214_models.ListRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.ListRoomUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRoomUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.ListRoomUsersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def mute_users_with_options(
        self,
        tmp_req: live_interaction_20201214_models.MuteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.MuteUsersResponse:
        """
        @deprecated
        
        @param tmp_req: MuteUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MuteUsersResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.MuteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MuteUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.MuteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def mute_users_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.MuteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.MuteUsersResponse:
        """
        @deprecated
        
        @param tmp_req: MuteUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MuteUsersResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.MuteUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MuteUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.MuteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mute_users(
        self,
        request: live_interaction_20201214_models.MuteUsersRequest,
    ) -> live_interaction_20201214_models.MuteUsersResponse:
        """
        @deprecated
        
        @param request: MuteUsersRequest
        @return: MuteUsersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.mute_users_with_options(request, runtime)

    async def mute_users_async(
        self,
        request: live_interaction_20201214_models.MuteUsersRequest,
    ) -> live_interaction_20201214_models.MuteUsersResponse:
        """
        @deprecated
        
        @param request: MuteUsersRequest
        @return: MuteUsersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.mute_users_with_options_async(request, runtime)

    def query_interconnection_cid_mapping_with_options(
        self,
        tmp_req: live_interaction_20201214_models.QueryInterconnectionCidMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.QueryInterconnectionCidMappingResponse:
        """
        @deprecated
        
        @param tmp_req: QueryInterconnectionCidMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInterconnectionCidMappingResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.QueryInterconnectionCidMappingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInterconnectionCidMapping',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.QueryInterconnectionCidMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_interconnection_cid_mapping_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.QueryInterconnectionCidMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.QueryInterconnectionCidMappingResponse:
        """
        @deprecated
        
        @param tmp_req: QueryInterconnectionCidMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInterconnectionCidMappingResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.QueryInterconnectionCidMappingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInterconnectionCidMapping',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.QueryInterconnectionCidMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_interconnection_cid_mapping(
        self,
        request: live_interaction_20201214_models.QueryInterconnectionCidMappingRequest,
    ) -> live_interaction_20201214_models.QueryInterconnectionCidMappingResponse:
        """
        @deprecated
        
        @param request: QueryInterconnectionCidMappingRequest
        @return: QueryInterconnectionCidMappingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.query_interconnection_cid_mapping_with_options(request, runtime)

    async def query_interconnection_cid_mapping_async(
        self,
        request: live_interaction_20201214_models.QueryInterconnectionCidMappingRequest,
    ) -> live_interaction_20201214_models.QueryInterconnectionCidMappingResponse:
        """
        @deprecated
        
        @param request: QueryInterconnectionCidMappingRequest
        @return: QueryInterconnectionCidMappingResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_interconnection_cid_mapping_with_options_async(request, runtime)

    def recall_message_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RecallMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RecallMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RecallMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecallMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RecallMessageResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecallMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RecallMessageResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_group_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_group_member_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupMemberExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupMemberExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMemberExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_group_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMembersResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_group_silence_blacklist_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupSilenceBlacklistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceBlacklistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupSilenceBlacklist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupSilenceBlacklist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceBlacklistResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_group_silence_whitelist_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveGroupSilenceWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveGroupSilenceWhitelistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupSilenceWhitelist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupSilenceWhitelist',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveGroupSilenceWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_message_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveMessageExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveMessageExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveMessageExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveMessageExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_single_chat_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveSingleChatExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveSingleChatExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveSingleChatExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveSingleChatExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def remove_user_conversation_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.RemoveUserConversationExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.RemoveUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUserConversationExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUserConversationExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.RemoveUserConversationExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def send_custom_message_with_options(
        self,
        request: live_interaction_20201214_models.SendCustomMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendCustomMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_custom_message_with_options_async(
        self,
        request: live_interaction_20201214_models.SendCustomMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendCustomMessageResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageResponse(),
            await self.call_api_async(params, req, runtime)
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

    def send_custom_message_to_room_users_with_options(
        self,
        request: live_interaction_20201214_models.SendCustomMessageToRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.receivers):
            body_flat['Receivers'] = request.receivers
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessageToRoomUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_custom_message_to_room_users_with_options_async(
        self,
        request: live_interaction_20201214_models.SendCustomMessageToRoomUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.receivers):
            body_flat['Receivers'] = request.receivers
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCustomMessageToRoomUsers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendCustomMessageToRoomUsersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def send_message_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SendMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_group_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetGroupExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetGroupExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetGroupExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetGroupExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_group_member_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetGroupMemberExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupMemberExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetGroupMemberExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetGroupMemberExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupMemberExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_group_owner_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetGroupOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetGroupOwnerResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetGroupOwnerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetGroupOwner',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupOwnerResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetGroupOwner',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetGroupOwnerResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_message_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetMessageExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetMessageExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetMessageExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetMessageExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_message_read_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetMessageReadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetMessageReadResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetMessageReadShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetMessageRead',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageReadResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetMessageRead',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetMessageReadResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_single_chat_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetSingleChatExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetSingleChatExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSingleChatExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSingleChatExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetSingleChatExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_user_conversation_extension_by_keys_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SetUserConversationExtensionByKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SetUserConversationExtensionByKeysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserConversationExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserConversationExtensionByKeys',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SetUserConversationExtensionByKeysResponse(),
            await self.call_api_async(params, req, runtime)
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

    def silence_all_group_members_with_options(
        self,
        tmp_req: live_interaction_20201214_models.SilenceAllGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.SilenceAllGroupMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.SilenceAllGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SilenceAllGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SilenceAllGroupMembersResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SilenceAllGroupMembers',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.SilenceAllGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def unbind_interconnection_uid_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UnbindInterconnectionUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UnbindInterconnectionUidResponse:
        """
        @deprecated
        
        @param tmp_req: UnbindInterconnectionUidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindInterconnectionUidResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UnbindInterconnectionUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindInterconnectionUid',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UnbindInterconnectionUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_interconnection_uid_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.UnbindInterconnectionUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UnbindInterconnectionUidResponse:
        """
        @deprecated
        
        @param tmp_req: UnbindInterconnectionUidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindInterconnectionUidResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UnbindInterconnectionUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindInterconnectionUid',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UnbindInterconnectionUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_interconnection_uid(
        self,
        request: live_interaction_20201214_models.UnbindInterconnectionUidRequest,
    ) -> live_interaction_20201214_models.UnbindInterconnectionUidResponse:
        """
        @deprecated
        
        @param request: UnbindInterconnectionUidRequest
        @return: UnbindInterconnectionUidResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_interconnection_uid_with_options(request, runtime)

    async def unbind_interconnection_uid_async(
        self,
        request: live_interaction_20201214_models.UnbindInterconnectionUidRequest,
    ) -> live_interaction_20201214_models.UnbindInterconnectionUidResponse:
        """
        @deprecated
        
        @param request: UnbindInterconnectionUidRequest
        @return: UnbindInterconnectionUidResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_interconnection_uid_with_options_async(request, runtime)

    def update_app_name_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateAppNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateAppNameResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppNameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppName',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppNameResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppName',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppNameResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_app_status_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateAppStatusResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateAppStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppStatus',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppStatusResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppStatus',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateAppStatusResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_callback_config_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateCallbackConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateCallbackConfigResponse:
        """
        @deprecated
        
        @param tmp_req: UpdateCallbackConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCallbackConfigResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateCallbackConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCallbackConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateCallbackConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_callback_config_with_options_async(
        self,
        tmp_req: live_interaction_20201214_models.UpdateCallbackConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateCallbackConfigResponse:
        """
        @deprecated
        
        @param tmp_req: UpdateCallbackConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCallbackConfigResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateCallbackConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCallbackConfig',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateCallbackConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_callback_config(
        self,
        request: live_interaction_20201214_models.UpdateCallbackConfigRequest,
    ) -> live_interaction_20201214_models.UpdateCallbackConfigResponse:
        """
        @deprecated
        
        @param request: UpdateCallbackConfigRequest
        @return: UpdateCallbackConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_callback_config_with_options(request, runtime)

    async def update_callback_config_async(
        self,
        request: live_interaction_20201214_models.UpdateCallbackConfigRequest,
    ) -> live_interaction_20201214_models.UpdateCallbackConfigResponse:
        """
        @deprecated
        
        @param request: UpdateCallbackConfigRequest
        @return: UpdateCallbackConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_callback_config_with_options_async(request, runtime)

    def update_group_icon_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateGroupIconRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateGroupIconResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupIconShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupIcon',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupIconResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupIcon',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupIconResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_group_members_role_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateGroupMembersRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateGroupMembersRoleResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupMembersRoleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupMembersRole',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupMembersRoleResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupMembersRole',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupMembersRoleResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_group_title_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateGroupTitleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateGroupTitleResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateGroupTitleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupTitle',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupTitleResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroupTitle',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateGroupTitleResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_msg_recall_interval_with_options(
        self,
        tmp_req: live_interaction_20201214_models.UpdateMsgRecallIntervalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateMsgRecallIntervalResponse:
        UtilClient.validate_model(tmp_req)
        request = live_interaction_20201214_models.UpdateMsgRecallIntervalShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.request_params):
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMsgRecallInterval',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateMsgRecallIntervalResponse(),
            self.call_api(params, req, runtime)
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
            request.request_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_params, 'RequestParams', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.request_params_shrink):
            body['RequestParams'] = request.request_params_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMsgRecallInterval',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateMsgRecallIntervalResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_tenant_status_with_options(
        self,
        request: live_interaction_20201214_models.UpdateTenantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateTenantStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTenantStatus',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateTenantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tenant_status_with_options_async(
        self,
        request: live_interaction_20201214_models.UpdateTenantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> live_interaction_20201214_models.UpdateTenantStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.request):
            body_flat['Request'] = request.request
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTenantStatus',
            version='2020-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_interaction_20201214_models.UpdateTenantStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
