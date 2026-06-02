# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_wyota20210420 import models as main_models
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
        self._endpoint = self.get_endpoint('wyota', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_terminal_with_options(
        self,
        request: main_models.AddTerminalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTerminalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['Alias'] = request.alias
        if not DaraCore.is_null(request.client_type):
            body['ClientType'] = request.client_type
        if not DaraCore.is_null(request.main_biz_type):
            body['MainBizType'] = request.main_biz_type
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTerminal',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_terminal_with_options_async(
        self,
        request: main_models.AddTerminalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTerminalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['Alias'] = request.alias
        if not DaraCore.is_null(request.client_type):
            body['ClientType'] = request.client_type
        if not DaraCore.is_null(request.main_biz_type):
            body['MainBizType'] = request.main_biz_type
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTerminal',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_terminal(
        self,
        request: main_models.AddTerminalRequest,
    ) -> main_models.AddTerminalResponse:
        runtime = RuntimeOptions()
        return self.add_terminal_with_options(request, runtime)

    async def add_terminal_async(
        self,
        request: main_models.AddTerminalRequest,
    ) -> main_models.AddTerminalResponse:
        runtime = RuntimeOptions()
        return await self.add_terminal_with_options_async(request, runtime)

    def add_terminals_with_options(
        self,
        request: main_models.AddTerminalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTerminalsResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.add_terminal_params):
            body_flat['AddTerminalParams'] = request.add_terminal_params
        if not DaraCore.is_null(request.main_biz_type):
            body['MainBizType'] = request.main_biz_type
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTerminals',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTerminalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_terminals_with_options_async(
        self,
        request: main_models.AddTerminalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTerminalsResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.add_terminal_params):
            body_flat['AddTerminalParams'] = request.add_terminal_params
        if not DaraCore.is_null(request.main_biz_type):
            body['MainBizType'] = request.main_biz_type
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTerminals',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTerminalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_terminals(
        self,
        request: main_models.AddTerminalsRequest,
    ) -> main_models.AddTerminalsResponse:
        runtime = RuntimeOptions()
        return self.add_terminals_with_options(request, runtime)

    async def add_terminals_async(
        self,
        request: main_models.AddTerminalsRequest,
    ) -> main_models.AddTerminalsResponse:
        runtime = RuntimeOptions()
        return await self.add_terminals_with_options_async(request, runtime)

    def bind_account_less_login_user_with_options(
        self,
        request: main_models.BindAccountLessLoginUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAccountLessLoginUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindAccountLessLoginUser',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAccountLessLoginUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_account_less_login_user_with_options_async(
        self,
        request: main_models.BindAccountLessLoginUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAccountLessLoginUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindAccountLessLoginUser',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAccountLessLoginUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_account_less_login_user(
        self,
        request: main_models.BindAccountLessLoginUserRequest,
    ) -> main_models.BindAccountLessLoginUserResponse:
        runtime = RuntimeOptions()
        return self.bind_account_less_login_user_with_options(request, runtime)

    async def bind_account_less_login_user_async(
        self,
        request: main_models.BindAccountLessLoginUserRequest,
    ) -> main_models.BindAccountLessLoginUserResponse:
        runtime = RuntimeOptions()
        return await self.bind_account_less_login_user_with_options_async(request, runtime)

    def bind_password_free_login_user_with_options(
        self,
        request: main_models.BindPasswordFreeLoginUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPasswordFreeLoginUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.main_biz_type):
            body['MainBizType'] = request.main_biz_type
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindPasswordFreeLoginUser',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPasswordFreeLoginUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_password_free_login_user_with_options_async(
        self,
        request: main_models.BindPasswordFreeLoginUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPasswordFreeLoginUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.main_biz_type):
            body['MainBizType'] = request.main_biz_type
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BindPasswordFreeLoginUser',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPasswordFreeLoginUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_password_free_login_user(
        self,
        request: main_models.BindPasswordFreeLoginUserRequest,
    ) -> main_models.BindPasswordFreeLoginUserResponse:
        runtime = RuntimeOptions()
        return self.bind_password_free_login_user_with_options(request, runtime)

    async def bind_password_free_login_user_async(
        self,
        request: main_models.BindPasswordFreeLoginUserRequest,
    ) -> main_models.BindPasswordFreeLoginUserResponse:
        runtime = RuntimeOptions()
        return await self.bind_password_free_login_user_with_options_async(request, runtime)

    def delete_clients_with_options(
        self,
        request: main_models.DeleteClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_ali_uid):
            query['CallerAliUid'] = request.caller_ali_uid
        body = {}
        if not DaraCore.is_null(request.in_manage):
            body['InManage'] = request.in_manage
        body_flat = {}
        if not DaraCore.is_null(request.uuids):
            body_flat['Uuids'] = request.uuids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClients',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_clients_with_options_async(
        self,
        request: main_models.DeleteClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_ali_uid):
            query['CallerAliUid'] = request.caller_ali_uid
        body = {}
        if not DaraCore.is_null(request.in_manage):
            body['InManage'] = request.in_manage
        body_flat = {}
        if not DaraCore.is_null(request.uuids):
            body_flat['Uuids'] = request.uuids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClients',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_clients(
        self,
        request: main_models.DeleteClientsRequest,
    ) -> main_models.DeleteClientsResponse:
        runtime = RuntimeOptions()
        return self.delete_clients_with_options(request, runtime)

    async def delete_clients_async(
        self,
        request: main_models.DeleteClientsRequest,
    ) -> main_models.DeleteClientsResponse:
        runtime = RuntimeOptions()
        return await self.delete_clients_with_options_async(request, runtime)

    def describe_clients_with_options(
        self,
        request: main_models.DescribeClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_ali_uid):
            query['CallerAliUid'] = request.caller_ali_uid
        body = {}
        if not DaraCore.is_null(request.client_type):
            body['ClientType'] = request.client_type
        if not DaraCore.is_null(request.custom_resource_id):
            body['CustomResourceId'] = request.custom_resource_id
        if not DaraCore.is_null(request.custom_resource_status):
            body['CustomResourceStatus'] = request.custom_resource_status
        if not DaraCore.is_null(request.in_manage):
            body['InManage'] = request.in_manage
        if not DaraCore.is_null(request.include_sub_groups):
            body['IncludeSubGroups'] = request.include_sub_groups
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.online_status):
            body['OnlineStatus'] = request.online_status
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not DaraCore.is_null(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        body_flat = {}
        if not DaraCore.is_null(request.uuids):
            body_flat['Uuids'] = request.uuids
        if not DaraCore.is_null(request.with_bind_user):
            body['WithBindUser'] = request.with_bind_user
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClients',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clients_with_options_async(
        self,
        request: main_models.DescribeClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_ali_uid):
            query['CallerAliUid'] = request.caller_ali_uid
        body = {}
        if not DaraCore.is_null(request.client_type):
            body['ClientType'] = request.client_type
        if not DaraCore.is_null(request.custom_resource_id):
            body['CustomResourceId'] = request.custom_resource_id
        if not DaraCore.is_null(request.custom_resource_status):
            body['CustomResourceStatus'] = request.custom_resource_status
        if not DaraCore.is_null(request.in_manage):
            body['InManage'] = request.in_manage
        if not DaraCore.is_null(request.include_sub_groups):
            body['IncludeSubGroups'] = request.include_sub_groups
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.online_status):
            body['OnlineStatus'] = request.online_status
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        if not DaraCore.is_null(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not DaraCore.is_null(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        body_flat = {}
        if not DaraCore.is_null(request.uuids):
            body_flat['Uuids'] = request.uuids
        if not DaraCore.is_null(request.with_bind_user):
            body['WithBindUser'] = request.with_bind_user
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClients',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clients(
        self,
        request: main_models.DescribeClientsRequest,
    ) -> main_models.DescribeClientsResponse:
        runtime = RuntimeOptions()
        return self.describe_clients_with_options(request, runtime)

    async def describe_clients_async(
        self,
        request: main_models.DescribeClientsRequest,
    ) -> main_models.DescribeClientsResponse:
        runtime = RuntimeOptions()
        return await self.describe_clients_with_options_async(request, runtime)

    def get_or_create_invitation_code_with_options(
        self,
        request: main_models.GetOrCreateInvitationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrCreateInvitationCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_days):
            body['ExpireDays'] = request.expire_days
        if not DaraCore.is_null(request.expire_minutes):
            body['ExpireMinutes'] = request.expire_minutes
        if not DaraCore.is_null(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOrCreateInvitationCode',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrCreateInvitationCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_or_create_invitation_code_with_options_async(
        self,
        request: main_models.GetOrCreateInvitationCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrCreateInvitationCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_days):
            body['ExpireDays'] = request.expire_days
        if not DaraCore.is_null(request.expire_minutes):
            body['ExpireMinutes'] = request.expire_minutes
        if not DaraCore.is_null(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOrCreateInvitationCode',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrCreateInvitationCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_or_create_invitation_code(
        self,
        request: main_models.GetOrCreateInvitationCodeRequest,
    ) -> main_models.GetOrCreateInvitationCodeResponse:
        runtime = RuntimeOptions()
        return self.get_or_create_invitation_code_with_options(request, runtime)

    async def get_or_create_invitation_code_async(
        self,
        request: main_models.GetOrCreateInvitationCodeRequest,
    ) -> main_models.GetOrCreateInvitationCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_or_create_invitation_code_with_options_async(request, runtime)

    def list_terminal_with_options(
        self,
        request: main_models.ListTerminalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTerminalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['Alias'] = request.alias
        if not DaraCore.is_null(request.build_id):
            body['BuildId'] = request.build_id
        if not DaraCore.is_null(request.client_type):
            body['ClientType'] = request.client_type
        if not DaraCore.is_null(request.in_manage):
            body['InManage'] = request.in_manage
        if not DaraCore.is_null(request.ipv_4):
            body['Ipv4'] = request.ipv_4
        if not DaraCore.is_null(request.location_info):
            body['LocationInfo'] = request.location_info
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTerminal',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_terminal_with_options_async(
        self,
        request: main_models.ListTerminalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTerminalResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['Alias'] = request.alias
        if not DaraCore.is_null(request.build_id):
            body['BuildId'] = request.build_id
        if not DaraCore.is_null(request.client_type):
            body['ClientType'] = request.client_type
        if not DaraCore.is_null(request.in_manage):
            body['InManage'] = request.in_manage
        if not DaraCore.is_null(request.ipv_4):
            body['Ipv4'] = request.ipv_4
        if not DaraCore.is_null(request.location_info):
            body['LocationInfo'] = request.location_info
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.model):
            body['Model'] = request.model
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.search_keyword):
            body['SearchKeyword'] = request.search_keyword
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.terminal_group_id):
            body['TerminalGroupId'] = request.terminal_group_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTerminal',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_terminal(
        self,
        request: main_models.ListTerminalRequest,
    ) -> main_models.ListTerminalResponse:
        runtime = RuntimeOptions()
        return self.list_terminal_with_options(request, runtime)

    async def list_terminal_async(
        self,
        request: main_models.ListTerminalRequest,
    ) -> main_models.ListTerminalResponse:
        runtime = RuntimeOptions()
        return await self.list_terminal_with_options_async(request, runtime)

    def send_ops_message_to_terminals_with_options(
        self,
        request: main_models.SendOpsMessageToTerminalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendOpsMessageToTerminalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delay):
            query['Delay'] = request.delay
        body = {}
        if not DaraCore.is_null(request.msg):
            body['Msg'] = request.msg
        if not DaraCore.is_null(request.ops_action):
            body['OpsAction'] = request.ops_action
        body_flat = {}
        if not DaraCore.is_null(request.uuids):
            body_flat['Uuids'] = request.uuids
        if not DaraCore.is_null(request.wait_for_ack):
            body['WaitForAck'] = request.wait_for_ack
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendOpsMessageToTerminals',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendOpsMessageToTerminalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_ops_message_to_terminals_with_options_async(
        self,
        request: main_models.SendOpsMessageToTerminalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendOpsMessageToTerminalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delay):
            query['Delay'] = request.delay
        body = {}
        if not DaraCore.is_null(request.msg):
            body['Msg'] = request.msg
        if not DaraCore.is_null(request.ops_action):
            body['OpsAction'] = request.ops_action
        body_flat = {}
        if not DaraCore.is_null(request.uuids):
            body_flat['Uuids'] = request.uuids
        if not DaraCore.is_null(request.wait_for_ack):
            body['WaitForAck'] = request.wait_for_ack
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendOpsMessageToTerminals',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendOpsMessageToTerminalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_ops_message_to_terminals(
        self,
        request: main_models.SendOpsMessageToTerminalsRequest,
    ) -> main_models.SendOpsMessageToTerminalsResponse:
        runtime = RuntimeOptions()
        return self.send_ops_message_to_terminals_with_options(request, runtime)

    async def send_ops_message_to_terminals_async(
        self,
        request: main_models.SendOpsMessageToTerminalsRequest,
    ) -> main_models.SendOpsMessageToTerminalsResponse:
        runtime = RuntimeOptions()
        return await self.send_ops_message_to_terminals_with_options_async(request, runtime)

    def unbind_account_less_login_user_with_options(
        self,
        request: main_models.UnbindAccountLessLoginUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAccountLessLoginUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAccountLessLoginUser',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAccountLessLoginUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_account_less_login_user_with_options_async(
        self,
        request: main_models.UnbindAccountLessLoginUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAccountLessLoginUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAccountLessLoginUser',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAccountLessLoginUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_account_less_login_user(
        self,
        request: main_models.UnbindAccountLessLoginUserRequest,
    ) -> main_models.UnbindAccountLessLoginUserResponse:
        runtime = RuntimeOptions()
        return self.unbind_account_less_login_user_with_options(request, runtime)

    async def unbind_account_less_login_user_async(
        self,
        request: main_models.UnbindAccountLessLoginUserRequest,
    ) -> main_models.UnbindAccountLessLoginUserResponse:
        runtime = RuntimeOptions()
        return await self.unbind_account_less_login_user_with_options_async(request, runtime)

    def unbind_password_free_login_user_with_options(
        self,
        request: main_models.UnbindPasswordFreeLoginUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindPasswordFreeLoginUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.main_biz_type):
            body['MainBizType'] = request.main_biz_type
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindPasswordFreeLoginUser',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindPasswordFreeLoginUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_password_free_login_user_with_options_async(
        self,
        request: main_models.UnbindPasswordFreeLoginUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindPasswordFreeLoginUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.main_biz_type):
            body['MainBizType'] = request.main_biz_type
        if not DaraCore.is_null(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnbindPasswordFreeLoginUser',
            version = '2021-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindPasswordFreeLoginUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_password_free_login_user(
        self,
        request: main_models.UnbindPasswordFreeLoginUserRequest,
    ) -> main_models.UnbindPasswordFreeLoginUserResponse:
        runtime = RuntimeOptions()
        return self.unbind_password_free_login_user_with_options(request, runtime)

    async def unbind_password_free_login_user_async(
        self,
        request: main_models.UnbindPasswordFreeLoginUserRequest,
    ) -> main_models.UnbindPasswordFreeLoginUserResponse:
        runtime = RuntimeOptions()
        return await self.unbind_password_free_login_user_with_options_async(request, runtime)
