# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_yundun_bastionhost20191209 import models as main_models
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
        self._endpoint = self.get_endpoint('yundun-bastionhost', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accept_approve_command_with_options(
        self,
        request: main_models.AcceptApproveCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptApproveCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptApproveCommand',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptApproveCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_approve_command_with_options_async(
        self,
        request: main_models.AcceptApproveCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptApproveCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptApproveCommand',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptApproveCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_approve_command(
        self,
        request: main_models.AcceptApproveCommandRequest,
    ) -> main_models.AcceptApproveCommandResponse:
        runtime = RuntimeOptions()
        return self.accept_approve_command_with_options(request, runtime)

    async def accept_approve_command_async(
        self,
        request: main_models.AcceptApproveCommandRequest,
    ) -> main_models.AcceptApproveCommandResponse:
        runtime = RuntimeOptions()
        return await self.accept_approve_command_with_options_async(request, runtime)

    def accept_operation_ticket_with_options(
        self,
        request: main_models.AcceptOperationTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptOperationTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.effect_count):
            query['EffectCount'] = request.effect_count
        if not DaraCore.is_null(request.effect_end_time):
            query['EffectEndTime'] = request.effect_end_time
        if not DaraCore.is_null(request.effect_start_time):
            query['EffectStartTime'] = request.effect_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_ticket_id):
            query['OperationTicketId'] = request.operation_ticket_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptOperationTicket',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptOperationTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_operation_ticket_with_options_async(
        self,
        request: main_models.AcceptOperationTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AcceptOperationTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.effect_count):
            query['EffectCount'] = request.effect_count
        if not DaraCore.is_null(request.effect_end_time):
            query['EffectEndTime'] = request.effect_end_time
        if not DaraCore.is_null(request.effect_start_time):
            query['EffectStartTime'] = request.effect_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_ticket_id):
            query['OperationTicketId'] = request.operation_ticket_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AcceptOperationTicket',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AcceptOperationTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_operation_ticket(
        self,
        request: main_models.AcceptOperationTicketRequest,
    ) -> main_models.AcceptOperationTicketResponse:
        runtime = RuntimeOptions()
        return self.accept_operation_ticket_with_options(request, runtime)

    async def accept_operation_ticket_async(
        self,
        request: main_models.AcceptOperationTicketRequest,
    ) -> main_models.AcceptOperationTicketResponse:
        runtime = RuntimeOptions()
        return await self.accept_operation_ticket_with_options_async(request, runtime)

    def add_databases_to_group_with_options(
        self,
        request: main_models.AddDatabasesToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDatabasesToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDatabasesToGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDatabasesToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_databases_to_group_with_options_async(
        self,
        request: main_models.AddDatabasesToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDatabasesToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDatabasesToGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDatabasesToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_databases_to_group(
        self,
        request: main_models.AddDatabasesToGroupRequest,
    ) -> main_models.AddDatabasesToGroupResponse:
        runtime = RuntimeOptions()
        return self.add_databases_to_group_with_options(request, runtime)

    async def add_databases_to_group_async(
        self,
        request: main_models.AddDatabasesToGroupRequest,
    ) -> main_models.AddDatabasesToGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_databases_to_group_with_options_async(request, runtime)

    def add_hosts_to_group_with_options(
        self,
        request: main_models.AddHostsToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddHostsToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddHostsToGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddHostsToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_hosts_to_group_with_options_async(
        self,
        request: main_models.AddHostsToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddHostsToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddHostsToGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddHostsToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_hosts_to_group(
        self,
        request: main_models.AddHostsToGroupRequest,
    ) -> main_models.AddHostsToGroupResponse:
        runtime = RuntimeOptions()
        return self.add_hosts_to_group_with_options(request, runtime)

    async def add_hosts_to_group_async(
        self,
        request: main_models.AddHostsToGroupRequest,
    ) -> main_models.AddHostsToGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_hosts_to_group_with_options_async(request, runtime)

    def add_instance_rd_member_with_options(
        self,
        request: main_models.AddInstanceRdMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddInstanceRdMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddInstanceRdMember',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddInstanceRdMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_instance_rd_member_with_options_async(
        self,
        request: main_models.AddInstanceRdMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddInstanceRdMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddInstanceRdMember',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddInstanceRdMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_instance_rd_member(
        self,
        request: main_models.AddInstanceRdMemberRequest,
    ) -> main_models.AddInstanceRdMemberResponse:
        runtime = RuntimeOptions()
        return self.add_instance_rd_member_with_options(request, runtime)

    async def add_instance_rd_member_async(
        self,
        request: main_models.AddInstanceRdMemberRequest,
    ) -> main_models.AddInstanceRdMemberResponse:
        runtime = RuntimeOptions()
        return await self.add_instance_rd_member_with_options_async(request, runtime)

    def add_users_to_group_with_options(
        self,
        request: main_models.AddUsersToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUsersToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUsersToGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUsersToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_users_to_group_with_options_async(
        self,
        request: main_models.AddUsersToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUsersToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUsersToGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUsersToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_users_to_group(
        self,
        request: main_models.AddUsersToGroupRequest,
    ) -> main_models.AddUsersToGroupResponse:
        runtime = RuntimeOptions()
        return self.add_users_to_group_with_options(request, runtime)

    async def add_users_to_group_async(
        self,
        request: main_models.AddUsersToGroupRequest,
    ) -> main_models.AddUsersToGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_users_to_group_with_options_async(request, runtime)

    def attach_database_accounts_to_user_with_options(
        self,
        request: main_models.AttachDatabaseAccountsToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDatabaseAccountsToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachDatabaseAccountsToUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDatabaseAccountsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_database_accounts_to_user_with_options_async(
        self,
        request: main_models.AttachDatabaseAccountsToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDatabaseAccountsToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachDatabaseAccountsToUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDatabaseAccountsToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_database_accounts_to_user(
        self,
        request: main_models.AttachDatabaseAccountsToUserRequest,
    ) -> main_models.AttachDatabaseAccountsToUserResponse:
        runtime = RuntimeOptions()
        return self.attach_database_accounts_to_user_with_options(request, runtime)

    async def attach_database_accounts_to_user_async(
        self,
        request: main_models.AttachDatabaseAccountsToUserRequest,
    ) -> main_models.AttachDatabaseAccountsToUserResponse:
        runtime = RuntimeOptions()
        return await self.attach_database_accounts_to_user_with_options_async(request, runtime)

    def attach_database_accounts_to_user_group_with_options(
        self,
        request: main_models.AttachDatabaseAccountsToUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDatabaseAccountsToUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachDatabaseAccountsToUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDatabaseAccountsToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_database_accounts_to_user_group_with_options_async(
        self,
        request: main_models.AttachDatabaseAccountsToUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDatabaseAccountsToUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachDatabaseAccountsToUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDatabaseAccountsToUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_database_accounts_to_user_group(
        self,
        request: main_models.AttachDatabaseAccountsToUserGroupRequest,
    ) -> main_models.AttachDatabaseAccountsToUserGroupResponse:
        runtime = RuntimeOptions()
        return self.attach_database_accounts_to_user_group_with_options(request, runtime)

    async def attach_database_accounts_to_user_group_async(
        self,
        request: main_models.AttachDatabaseAccountsToUserGroupRequest,
    ) -> main_models.AttachDatabaseAccountsToUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.attach_database_accounts_to_user_group_with_options_async(request, runtime)

    def attach_host_accounts_to_host_share_key_with_options(
        self,
        request: main_models.AttachHostAccountsToHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostAccountsToHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostAccountsToHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostAccountsToHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_accounts_to_host_share_key_with_options_async(
        self,
        request: main_models.AttachHostAccountsToHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostAccountsToHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostAccountsToHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostAccountsToHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_host_accounts_to_host_share_key(
        self,
        request: main_models.AttachHostAccountsToHostShareKeyRequest,
    ) -> main_models.AttachHostAccountsToHostShareKeyResponse:
        runtime = RuntimeOptions()
        return self.attach_host_accounts_to_host_share_key_with_options(request, runtime)

    async def attach_host_accounts_to_host_share_key_async(
        self,
        request: main_models.AttachHostAccountsToHostShareKeyRequest,
    ) -> main_models.AttachHostAccountsToHostShareKeyResponse:
        runtime = RuntimeOptions()
        return await self.attach_host_accounts_to_host_share_key_with_options_async(request, runtime)

    def attach_host_accounts_to_user_with_options(
        self,
        request: main_models.AttachHostAccountsToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostAccountsToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostAccountsToUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostAccountsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_accounts_to_user_with_options_async(
        self,
        request: main_models.AttachHostAccountsToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostAccountsToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostAccountsToUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostAccountsToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_host_accounts_to_user(
        self,
        request: main_models.AttachHostAccountsToUserRequest,
    ) -> main_models.AttachHostAccountsToUserResponse:
        runtime = RuntimeOptions()
        return self.attach_host_accounts_to_user_with_options(request, runtime)

    async def attach_host_accounts_to_user_async(
        self,
        request: main_models.AttachHostAccountsToUserRequest,
    ) -> main_models.AttachHostAccountsToUserResponse:
        runtime = RuntimeOptions()
        return await self.attach_host_accounts_to_user_with_options_async(request, runtime)

    def attach_host_accounts_to_user_group_with_options(
        self,
        request: main_models.AttachHostAccountsToUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostAccountsToUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostAccountsToUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostAccountsToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_accounts_to_user_group_with_options_async(
        self,
        request: main_models.AttachHostAccountsToUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostAccountsToUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostAccountsToUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostAccountsToUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_host_accounts_to_user_group(
        self,
        request: main_models.AttachHostAccountsToUserGroupRequest,
    ) -> main_models.AttachHostAccountsToUserGroupResponse:
        runtime = RuntimeOptions()
        return self.attach_host_accounts_to_user_group_with_options(request, runtime)

    async def attach_host_accounts_to_user_group_async(
        self,
        request: main_models.AttachHostAccountsToUserGroupRequest,
    ) -> main_models.AttachHostAccountsToUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.attach_host_accounts_to_user_group_with_options_async(request, runtime)

    def attach_host_group_accounts_to_user_with_options(
        self,
        request: main_models.AttachHostGroupAccountsToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostGroupAccountsToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostGroupAccountsToUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostGroupAccountsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_group_accounts_to_user_with_options_async(
        self,
        request: main_models.AttachHostGroupAccountsToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostGroupAccountsToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostGroupAccountsToUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostGroupAccountsToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_host_group_accounts_to_user(
        self,
        request: main_models.AttachHostGroupAccountsToUserRequest,
    ) -> main_models.AttachHostGroupAccountsToUserResponse:
        runtime = RuntimeOptions()
        return self.attach_host_group_accounts_to_user_with_options(request, runtime)

    async def attach_host_group_accounts_to_user_async(
        self,
        request: main_models.AttachHostGroupAccountsToUserRequest,
    ) -> main_models.AttachHostGroupAccountsToUserResponse:
        runtime = RuntimeOptions()
        return await self.attach_host_group_accounts_to_user_with_options_async(request, runtime)

    def attach_host_group_accounts_to_user_group_with_options(
        self,
        request: main_models.AttachHostGroupAccountsToUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostGroupAccountsToUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostGroupAccountsToUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostGroupAccountsToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_group_accounts_to_user_group_with_options_async(
        self,
        request: main_models.AttachHostGroupAccountsToUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachHostGroupAccountsToUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachHostGroupAccountsToUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachHostGroupAccountsToUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_host_group_accounts_to_user_group(
        self,
        request: main_models.AttachHostGroupAccountsToUserGroupRequest,
    ) -> main_models.AttachHostGroupAccountsToUserGroupResponse:
        runtime = RuntimeOptions()
        return self.attach_host_group_accounts_to_user_group_with_options(request, runtime)

    async def attach_host_group_accounts_to_user_group_async(
        self,
        request: main_models.AttachHostGroupAccountsToUserGroupRequest,
    ) -> main_models.AttachHostGroupAccountsToUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.attach_host_group_accounts_to_user_group_with_options_async(request, runtime)

    def config_instance_security_groups_with_options(
        self,
        request: main_models.ConfigInstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigInstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorized_security_groups):
            query['AuthorizedSecurityGroups'] = request.authorized_security_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigInstanceSecurityGroups',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigInstanceSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_instance_security_groups_with_options_async(
        self,
        request: main_models.ConfigInstanceSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigInstanceSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorized_security_groups):
            query['AuthorizedSecurityGroups'] = request.authorized_security_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigInstanceSecurityGroups',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigInstanceSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_instance_security_groups(
        self,
        request: main_models.ConfigInstanceSecurityGroupsRequest,
    ) -> main_models.ConfigInstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return self.config_instance_security_groups_with_options(request, runtime)

    async def config_instance_security_groups_async(
        self,
        request: main_models.ConfigInstanceSecurityGroupsRequest,
    ) -> main_models.ConfigInstanceSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return await self.config_instance_security_groups_with_options_async(request, runtime)

    def config_instance_white_list_with_options(
        self,
        request: main_models.ConfigInstanceWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigInstanceWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.white_list):
            query['WhiteList'] = request.white_list
        if not DaraCore.is_null(request.white_list_policies):
            query['WhiteListPolicies'] = request.white_list_policies
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigInstanceWhiteList',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigInstanceWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_instance_white_list_with_options_async(
        self,
        request: main_models.ConfigInstanceWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigInstanceWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.white_list):
            query['WhiteList'] = request.white_list
        if not DaraCore.is_null(request.white_list_policies):
            query['WhiteListPolicies'] = request.white_list_policies
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigInstanceWhiteList',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigInstanceWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_instance_white_list(
        self,
        request: main_models.ConfigInstanceWhiteListRequest,
    ) -> main_models.ConfigInstanceWhiteListResponse:
        runtime = RuntimeOptions()
        return self.config_instance_white_list_with_options(request, runtime)

    async def config_instance_white_list_async(
        self,
        request: main_models.ConfigInstanceWhiteListRequest,
    ) -> main_models.ConfigInstanceWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.config_instance_white_list_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        request: main_models.CreateDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_port):
            query['DatabasePort'] = request.database_port
        if not DaraCore.is_null(request.database_private_address):
            query['DatabasePrivateAddress'] = request.database_private_address
        if not DaraCore.is_null(request.database_public_address):
            query['DatabasePublicAddress'] = request.database_public_address
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_member_id):
            query['InstanceMemberId'] = request.instance_member_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.polar_dbendpoint_type):
            query['PolarDBEndpointType'] = request.polar_dbendpoint_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.source_instance_region_id):
            query['SourceInstanceRegionId'] = request.source_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatabase',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_with_options_async(
        self,
        request: main_models.CreateDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_port):
            query['DatabasePort'] = request.database_port
        if not DaraCore.is_null(request.database_private_address):
            query['DatabasePrivateAddress'] = request.database_private_address
        if not DaraCore.is_null(request.database_public_address):
            query['DatabasePublicAddress'] = request.database_public_address
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_member_id):
            query['InstanceMemberId'] = request.instance_member_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.polar_dbendpoint_type):
            query['PolarDBEndpointType'] = request.polar_dbendpoint_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.source_instance_region_id):
            query['SourceInstanceRegionId'] = request.source_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatabase',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database(
        self,
        request: main_models.CreateDatabaseRequest,
    ) -> main_models.CreateDatabaseResponse:
        runtime = RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: main_models.CreateDatabaseRequest,
    ) -> main_models.CreateDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_database_account_with_options(
        self,
        request: main_models.CreateDatabaseAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatabaseAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_attribute):
            query['LoginAttribute'] = request.login_attribute
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatabaseAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatabaseAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_account_with_options_async(
        self,
        request: main_models.CreateDatabaseAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatabaseAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_attribute):
            query['LoginAttribute'] = request.login_attribute
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatabaseAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatabaseAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database_account(
        self,
        request: main_models.CreateDatabaseAccountRequest,
    ) -> main_models.CreateDatabaseAccountResponse:
        runtime = RuntimeOptions()
        return self.create_database_account_with_options(request, runtime)

    async def create_database_account_async(
        self,
        request: main_models.CreateDatabaseAccountRequest,
    ) -> main_models.CreateDatabaseAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_database_account_with_options_async(request, runtime)

    def create_export_config_job_with_options(
        self,
        request: main_models.CreateExportConfigJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExportConfigJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExportConfigJob',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExportConfigJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_export_config_job_with_options_async(
        self,
        request: main_models.CreateExportConfigJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExportConfigJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExportConfigJob',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExportConfigJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_export_config_job(
        self,
        request: main_models.CreateExportConfigJobRequest,
    ) -> main_models.CreateExportConfigJobResponse:
        runtime = RuntimeOptions()
        return self.create_export_config_job_with_options(request, runtime)

    async def create_export_config_job_async(
        self,
        request: main_models.CreateExportConfigJobRequest,
    ) -> main_models.CreateExportConfigJobResponse:
        runtime = RuntimeOptions()
        return await self.create_export_config_job_with_options_async(request, runtime)

    def create_host_with_options(
        self,
        request: main_models.CreateHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not DaraCore.is_null(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_member_id):
            query['InstanceMemberId'] = request.instance_member_id
        if not DaraCore.is_null(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHost',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_with_options_async(
        self,
        request: main_models.CreateHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not DaraCore.is_null(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_member_id):
            query['InstanceMemberId'] = request.instance_member_id
        if not DaraCore.is_null(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHost',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host(
        self,
        request: main_models.CreateHostRequest,
    ) -> main_models.CreateHostResponse:
        runtime = RuntimeOptions()
        return self.create_host_with_options(request, runtime)

    async def create_host_async(
        self,
        request: main_models.CreateHostRequest,
    ) -> main_models.CreateHostResponse:
        runtime = RuntimeOptions()
        return await self.create_host_with_options_async(request, runtime)

    def create_host_account_with_options(
        self,
        request: main_models.CreateHostAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rotation_mode):
            query['RotationMode'] = request.rotation_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHostAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_account_with_options_async(
        self,
        request: main_models.CreateHostAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rotation_mode):
            query['RotationMode'] = request.rotation_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHostAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host_account(
        self,
        request: main_models.CreateHostAccountRequest,
    ) -> main_models.CreateHostAccountResponse:
        runtime = RuntimeOptions()
        return self.create_host_account_with_options(request, runtime)

    async def create_host_account_async(
        self,
        request: main_models.CreateHostAccountRequest,
    ) -> main_models.CreateHostAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_host_account_with_options_async(request, runtime)

    def create_host_group_with_options(
        self,
        request: main_models.CreateHostGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHostGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_group_with_options_async(
        self,
        request: main_models.CreateHostGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHostGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host_group(
        self,
        request: main_models.CreateHostGroupRequest,
    ) -> main_models.CreateHostGroupResponse:
        runtime = RuntimeOptions()
        return self.create_host_group_with_options(request, runtime)

    async def create_host_group_async(
        self,
        request: main_models.CreateHostGroupRequest,
    ) -> main_models.CreateHostGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_host_group_with_options_async(request, runtime)

    def create_host_share_key_with_options(
        self,
        request: main_models.CreateHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_share_key_with_options_async(
        self,
        request: main_models.CreateHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host_share_key(
        self,
        request: main_models.CreateHostShareKeyRequest,
    ) -> main_models.CreateHostShareKeyResponse:
        runtime = RuntimeOptions()
        return self.create_host_share_key_with_options(request, runtime)

    async def create_host_share_key_async(
        self,
        request: main_models.CreateHostShareKeyRequest,
    ) -> main_models.CreateHostShareKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_host_share_key_with_options_async(request, runtime)

    def create_network_domain_with_options(
        self,
        request: main_models.CreateNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not DaraCore.is_null(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not DaraCore.is_null(request.proxies):
            query['Proxies'] = request.proxies
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_domain_with_options_async(
        self,
        request: main_models.CreateNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not DaraCore.is_null(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not DaraCore.is_null(request.proxies):
            query['Proxies'] = request.proxies
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_domain(
        self,
        request: main_models.CreateNetworkDomainRequest,
    ) -> main_models.CreateNetworkDomainResponse:
        runtime = RuntimeOptions()
        return self.create_network_domain_with_options(request, runtime)

    async def create_network_domain_async(
        self,
        request: main_models.CreateNetworkDomainRequest,
    ) -> main_models.CreateNetworkDomainResponse:
        runtime = RuntimeOptions()
        return await self.create_network_domain_with_options_async(request, runtime)

    def create_operation_ticket_with_options(
        self,
        request: main_models.CreateOperationTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOperationTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.approve_comment):
            query['ApproveComment'] = request.approve_comment
        if not DaraCore.is_null(request.asset_account_name):
            query['AssetAccountName'] = request.asset_account_name
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.effect_end_time):
            query['EffectEndTime'] = request.effect_end_time
        if not DaraCore.is_null(request.effect_start_time):
            query['EffectStartTime'] = request.effect_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_one_time_effect):
            query['IsOneTimeEffect'] = request.is_one_time_effect
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOperationTicket',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOperationTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_operation_ticket_with_options_async(
        self,
        request: main_models.CreateOperationTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOperationTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.approve_comment):
            query['ApproveComment'] = request.approve_comment
        if not DaraCore.is_null(request.asset_account_name):
            query['AssetAccountName'] = request.asset_account_name
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.effect_end_time):
            query['EffectEndTime'] = request.effect_end_time
        if not DaraCore.is_null(request.effect_start_time):
            query['EffectStartTime'] = request.effect_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_one_time_effect):
            query['IsOneTimeEffect'] = request.is_one_time_effect
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOperationTicket',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOperationTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_operation_ticket(
        self,
        request: main_models.CreateOperationTicketRequest,
    ) -> main_models.CreateOperationTicketResponse:
        runtime = RuntimeOptions()
        return self.create_operation_ticket_with_options(request, runtime)

    async def create_operation_ticket_async(
        self,
        request: main_models.CreateOperationTicketRequest,
    ) -> main_models.CreateOperationTicketResponse:
        runtime = RuntimeOptions()
        return await self.create_operation_ticket_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: main_models.CreatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: main_models.CreateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: main_models.CreateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        request: main_models.CreateRuleRequest,
    ) -> main_models.CreateRuleResponse:
        runtime = RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: main_models.CreateRuleRequest,
    ) -> main_models.CreateRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.language_status):
            query['LanguageStatus'] = request.language_status
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not DaraCore.is_null(request.need_reset_password):
            query['NeedResetPassword'] = request.need_reset_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not DaraCore.is_null(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        if not DaraCore.is_null(request.two_factor_status):
            query['TwoFactorStatus'] = request.two_factor_status
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.language_status):
            query['LanguageStatus'] = request.language_status
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not DaraCore.is_null(request.need_reset_password):
            query['NeedResetPassword'] = request.need_reset_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not DaraCore.is_null(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        if not DaraCore.is_null(request.two_factor_status):
            query['TwoFactorStatus'] = request.two_factor_status
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: main_models.CreateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_group_with_options_async(
        self,
        request: main_models.CreateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_group(
        self,
        request: main_models.CreateUserGroupRequest,
    ) -> main_models.CreateUserGroupResponse:
        runtime = RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: main_models.CreateUserGroupRequest,
    ) -> main_models.CreateUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def create_user_public_key_with_options(
        self,
        request: main_models.CreateUserPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        if not DaraCore.is_null(request.public_key_name):
            query['PublicKeyName'] = request.public_key_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserPublicKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_public_key_with_options_async(
        self,
        request: main_models.CreateUserPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        if not DaraCore.is_null(request.public_key_name):
            query['PublicKeyName'] = request.public_key_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserPublicKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_public_key(
        self,
        request: main_models.CreateUserPublicKeyRequest,
    ) -> main_models.CreateUserPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.create_user_public_key_with_options(request, runtime)

    async def create_user_public_key_async(
        self,
        request: main_models.CreateUserPublicKeyRequest,
    ) -> main_models.CreateUserPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_user_public_key_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: main_models.DeleteDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatabase',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: main_models.DeleteDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatabase',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database(
        self,
        request: main_models.DeleteDatabaseRequest,
    ) -> main_models.DeleteDatabaseResponse:
        runtime = RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: main_models.DeleteDatabaseRequest,
    ) -> main_models.DeleteDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_database_account_with_options(
        self,
        request: main_models.DeleteDatabaseAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatabaseAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatabaseAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatabaseAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_account_with_options_async(
        self,
        request: main_models.DeleteDatabaseAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatabaseAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDatabaseAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatabaseAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database_account(
        self,
        request: main_models.DeleteDatabaseAccountRequest,
    ) -> main_models.DeleteDatabaseAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_database_account_with_options(request, runtime)

    async def delete_database_account_async(
        self,
        request: main_models.DeleteDatabaseAccountRequest,
    ) -> main_models.DeleteDatabaseAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_database_account_with_options_async(request, runtime)

    def delete_host_with_options(
        self,
        request: main_models.DeleteHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHost',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_with_options_async(
        self,
        request: main_models.DeleteHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHost',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host(
        self,
        request: main_models.DeleteHostRequest,
    ) -> main_models.DeleteHostResponse:
        runtime = RuntimeOptions()
        return self.delete_host_with_options(request, runtime)

    async def delete_host_async(
        self,
        request: main_models.DeleteHostRequest,
    ) -> main_models.DeleteHostResponse:
        runtime = RuntimeOptions()
        return await self.delete_host_with_options_async(request, runtime)

    def delete_host_account_with_options(
        self,
        request: main_models.DeleteHostAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHostAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_account_with_options_async(
        self,
        request: main_models.DeleteHostAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHostAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_account(
        self,
        request: main_models.DeleteHostAccountRequest,
    ) -> main_models.DeleteHostAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_host_account_with_options(request, runtime)

    async def delete_host_account_async(
        self,
        request: main_models.DeleteHostAccountRequest,
    ) -> main_models.DeleteHostAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_host_account_with_options_async(request, runtime)

    def delete_host_group_with_options(
        self,
        request: main_models.DeleteHostGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHostGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_group_with_options_async(
        self,
        request: main_models.DeleteHostGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHostGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_group(
        self,
        request: main_models.DeleteHostGroupRequest,
    ) -> main_models.DeleteHostGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_host_group_with_options(request, runtime)

    async def delete_host_group_async(
        self,
        request: main_models.DeleteHostGroupRequest,
    ) -> main_models.DeleteHostGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_host_group_with_options_async(request, runtime)

    def delete_host_share_key_with_options(
        self,
        request: main_models.DeleteHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_share_key_with_options_async(
        self,
        request: main_models.DeleteHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_share_key(
        self,
        request: main_models.DeleteHostShareKeyRequest,
    ) -> main_models.DeleteHostShareKeyResponse:
        runtime = RuntimeOptions()
        return self.delete_host_share_key_with_options(request, runtime)

    async def delete_host_share_key_async(
        self,
        request: main_models.DeleteHostShareKeyRequest,
    ) -> main_models.DeleteHostShareKeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_host_share_key_with_options_async(request, runtime)

    def delete_network_domain_with_options(
        self,
        request: main_models.DeleteNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_domain_with_options_async(
        self,
        request: main_models.DeleteNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_domain(
        self,
        request: main_models.DeleteNetworkDomainRequest,
    ) -> main_models.DeleteNetworkDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_network_domain_with_options(request, runtime)

    async def delete_network_domain_async(
        self,
        request: main_models.DeleteNetworkDomainRequest,
    ) -> main_models.DeleteNetworkDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_network_domain_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: main_models.DeletePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: main_models.DeletePolicyRequest,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: main_models.DeleteUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: main_models.DeleteUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group(
        self,
        request: main_models.DeleteUserGroupRequest,
    ) -> main_models.DeleteUserGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: main_models.DeleteUserGroupRequest,
    ) -> main_models.DeleteUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def delete_user_public_key_with_options(
        self,
        request: main_models.DeleteUserPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_key_id):
            query['PublicKeyId'] = request.public_key_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserPublicKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_public_key_with_options_async(
        self,
        request: main_models.DeleteUserPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_key_id):
            query['PublicKeyId'] = request.public_key_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserPublicKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_public_key(
        self,
        request: main_models.DeleteUserPublicKeyRequest,
    ) -> main_models.DeleteUserPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.delete_user_public_key_with_options(request, runtime)

    async def delete_user_public_key_async(
        self,
        request: main_models.DeleteUserPublicKeyRequest,
    ) -> main_models.DeleteUserPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_public_key_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: main_models.DescribeInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAttribute',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: main_models.DescribeInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAttribute',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: main_models.DescribeInstanceAttributeRequest,
    ) -> main_models.DescribeInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: main_models.DescribeInstanceAttributeRequest,
    ) -> main_models.DescribeInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def detach_database_accounts_from_user_with_options(
        self,
        request: main_models.DetachDatabaseAccountsFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDatabaseAccountsFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachDatabaseAccountsFromUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDatabaseAccountsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_database_accounts_from_user_with_options_async(
        self,
        request: main_models.DetachDatabaseAccountsFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDatabaseAccountsFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachDatabaseAccountsFromUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDatabaseAccountsFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_database_accounts_from_user(
        self,
        request: main_models.DetachDatabaseAccountsFromUserRequest,
    ) -> main_models.DetachDatabaseAccountsFromUserResponse:
        runtime = RuntimeOptions()
        return self.detach_database_accounts_from_user_with_options(request, runtime)

    async def detach_database_accounts_from_user_async(
        self,
        request: main_models.DetachDatabaseAccountsFromUserRequest,
    ) -> main_models.DetachDatabaseAccountsFromUserResponse:
        runtime = RuntimeOptions()
        return await self.detach_database_accounts_from_user_with_options_async(request, runtime)

    def detach_database_accounts_from_user_group_with_options(
        self,
        request: main_models.DetachDatabaseAccountsFromUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDatabaseAccountsFromUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachDatabaseAccountsFromUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDatabaseAccountsFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_database_accounts_from_user_group_with_options_async(
        self,
        request: main_models.DetachDatabaseAccountsFromUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDatabaseAccountsFromUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachDatabaseAccountsFromUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDatabaseAccountsFromUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_database_accounts_from_user_group(
        self,
        request: main_models.DetachDatabaseAccountsFromUserGroupRequest,
    ) -> main_models.DetachDatabaseAccountsFromUserGroupResponse:
        runtime = RuntimeOptions()
        return self.detach_database_accounts_from_user_group_with_options(request, runtime)

    async def detach_database_accounts_from_user_group_async(
        self,
        request: main_models.DetachDatabaseAccountsFromUserGroupRequest,
    ) -> main_models.DetachDatabaseAccountsFromUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.detach_database_accounts_from_user_group_with_options_async(request, runtime)

    def detach_host_accounts_from_host_share_key_with_options(
        self,
        request: main_models.DetachHostAccountsFromHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostAccountsFromHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostAccountsFromHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostAccountsFromHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_accounts_from_host_share_key_with_options_async(
        self,
        request: main_models.DetachHostAccountsFromHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostAccountsFromHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostAccountsFromHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostAccountsFromHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_host_accounts_from_host_share_key(
        self,
        request: main_models.DetachHostAccountsFromHostShareKeyRequest,
    ) -> main_models.DetachHostAccountsFromHostShareKeyResponse:
        runtime = RuntimeOptions()
        return self.detach_host_accounts_from_host_share_key_with_options(request, runtime)

    async def detach_host_accounts_from_host_share_key_async(
        self,
        request: main_models.DetachHostAccountsFromHostShareKeyRequest,
    ) -> main_models.DetachHostAccountsFromHostShareKeyResponse:
        runtime = RuntimeOptions()
        return await self.detach_host_accounts_from_host_share_key_with_options_async(request, runtime)

    def detach_host_accounts_from_user_with_options(
        self,
        request: main_models.DetachHostAccountsFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostAccountsFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostAccountsFromUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostAccountsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_accounts_from_user_with_options_async(
        self,
        request: main_models.DetachHostAccountsFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostAccountsFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostAccountsFromUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostAccountsFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_host_accounts_from_user(
        self,
        request: main_models.DetachHostAccountsFromUserRequest,
    ) -> main_models.DetachHostAccountsFromUserResponse:
        runtime = RuntimeOptions()
        return self.detach_host_accounts_from_user_with_options(request, runtime)

    async def detach_host_accounts_from_user_async(
        self,
        request: main_models.DetachHostAccountsFromUserRequest,
    ) -> main_models.DetachHostAccountsFromUserResponse:
        runtime = RuntimeOptions()
        return await self.detach_host_accounts_from_user_with_options_async(request, runtime)

    def detach_host_accounts_from_user_group_with_options(
        self,
        request: main_models.DetachHostAccountsFromUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostAccountsFromUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostAccountsFromUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostAccountsFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_accounts_from_user_group_with_options_async(
        self,
        request: main_models.DetachHostAccountsFromUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostAccountsFromUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostAccountsFromUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostAccountsFromUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_host_accounts_from_user_group(
        self,
        request: main_models.DetachHostAccountsFromUserGroupRequest,
    ) -> main_models.DetachHostAccountsFromUserGroupResponse:
        runtime = RuntimeOptions()
        return self.detach_host_accounts_from_user_group_with_options(request, runtime)

    async def detach_host_accounts_from_user_group_async(
        self,
        request: main_models.DetachHostAccountsFromUserGroupRequest,
    ) -> main_models.DetachHostAccountsFromUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.detach_host_accounts_from_user_group_with_options_async(request, runtime)

    def detach_host_group_accounts_from_user_with_options(
        self,
        request: main_models.DetachHostGroupAccountsFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostGroupAccountsFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostGroupAccountsFromUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostGroupAccountsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_group_accounts_from_user_with_options_async(
        self,
        request: main_models.DetachHostGroupAccountsFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostGroupAccountsFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostGroupAccountsFromUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostGroupAccountsFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_host_group_accounts_from_user(
        self,
        request: main_models.DetachHostGroupAccountsFromUserRequest,
    ) -> main_models.DetachHostGroupAccountsFromUserResponse:
        runtime = RuntimeOptions()
        return self.detach_host_group_accounts_from_user_with_options(request, runtime)

    async def detach_host_group_accounts_from_user_async(
        self,
        request: main_models.DetachHostGroupAccountsFromUserRequest,
    ) -> main_models.DetachHostGroupAccountsFromUserResponse:
        runtime = RuntimeOptions()
        return await self.detach_host_group_accounts_from_user_with_options_async(request, runtime)

    def detach_host_group_accounts_from_user_group_with_options(
        self,
        request: main_models.DetachHostGroupAccountsFromUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostGroupAccountsFromUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostGroupAccountsFromUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostGroupAccountsFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_group_accounts_from_user_group_with_options_async(
        self,
        request: main_models.DetachHostGroupAccountsFromUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachHostGroupAccountsFromUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachHostGroupAccountsFromUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachHostGroupAccountsFromUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_host_group_accounts_from_user_group(
        self,
        request: main_models.DetachHostGroupAccountsFromUserGroupRequest,
    ) -> main_models.DetachHostGroupAccountsFromUserGroupResponse:
        runtime = RuntimeOptions()
        return self.detach_host_group_accounts_from_user_group_with_options(request, runtime)

    async def detach_host_group_accounts_from_user_group_async(
        self,
        request: main_models.DetachHostGroupAccountsFromUserGroupRequest,
    ) -> main_models.DetachHostGroupAccountsFromUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.detach_host_group_accounts_from_user_group_with_options_async(request, runtime)

    def disable_instance_public_access_with_options(
        self,
        request: main_models.DisableInstancePublicAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInstancePublicAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInstancePublicAccess',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInstancePublicAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_instance_public_access_with_options_async(
        self,
        request: main_models.DisableInstancePublicAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInstancePublicAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInstancePublicAccess',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInstancePublicAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_instance_public_access(
        self,
        request: main_models.DisableInstancePublicAccessRequest,
    ) -> main_models.DisableInstancePublicAccessResponse:
        runtime = RuntimeOptions()
        return self.disable_instance_public_access_with_options(request, runtime)

    async def disable_instance_public_access_async(
        self,
        request: main_models.DisableInstancePublicAccessRequest,
    ) -> main_models.DisableInstancePublicAccessResponse:
        runtime = RuntimeOptions()
        return await self.disable_instance_public_access_with_options_async(request, runtime)

    def disable_rule_with_options(
        self,
        request: main_models.DisableRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_rule_with_options_async(
        self,
        request: main_models.DisableRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_rule(
        self,
        request: main_models.DisableRuleRequest,
    ) -> main_models.DisableRuleResponse:
        runtime = RuntimeOptions()
        return self.disable_rule_with_options(request, runtime)

    async def disable_rule_async(
        self,
        request: main_models.DisableRuleRequest,
    ) -> main_models.DisableRuleResponse:
        runtime = RuntimeOptions()
        return await self.disable_rule_with_options_async(request, runtime)

    def enable_instance_public_access_with_options(
        self,
        request: main_models.EnableInstancePublicAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInstancePublicAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInstancePublicAccess',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInstancePublicAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_instance_public_access_with_options_async(
        self,
        request: main_models.EnableInstancePublicAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInstancePublicAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInstancePublicAccess',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInstancePublicAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_instance_public_access(
        self,
        request: main_models.EnableInstancePublicAccessRequest,
    ) -> main_models.EnableInstancePublicAccessResponse:
        runtime = RuntimeOptions()
        return self.enable_instance_public_access_with_options(request, runtime)

    async def enable_instance_public_access_async(
        self,
        request: main_models.EnableInstancePublicAccessRequest,
    ) -> main_models.EnableInstancePublicAccessResponse:
        runtime = RuntimeOptions()
        return await self.enable_instance_public_access_with_options_async(request, runtime)

    def enable_rule_with_options(
        self,
        request: main_models.EnableRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_rule_with_options_async(
        self,
        request: main_models.EnableRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_rule(
        self,
        request: main_models.EnableRuleRequest,
    ) -> main_models.EnableRuleResponse:
        runtime = RuntimeOptions()
        return self.enable_rule_with_options(request, runtime)

    async def enable_rule_async(
        self,
        request: main_models.EnableRuleRequest,
    ) -> main_models.EnableRuleResponse:
        runtime = RuntimeOptions()
        return await self.enable_rule_with_options_async(request, runtime)

    def generate_asset_operation_token_with_options(
        self,
        request: main_models.GenerateAssetOperationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAssetOperationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_account_id):
            query['AssetAccountId'] = request.asset_account_id
        if not DaraCore.is_null(request.asset_account_name):
            query['AssetAccountName'] = request.asset_account_name
        if not DaraCore.is_null(request.asset_account_password):
            query['AssetAccountPassword'] = request.asset_account_password
        if not DaraCore.is_null(request.asset_account_protocol_name):
            query['AssetAccountProtocolName'] = request.asset_account_protocol_name
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.asset_type):
            query['AssetType'] = request.asset_type
        if not DaraCore.is_null(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_attribute):
            query['LoginAttribute'] = request.login_attribute
        if not DaraCore.is_null(request.operation_mode):
            query['OperationMode'] = request.operation_mode
        if not DaraCore.is_null(request.operation_note):
            query['OperationNote'] = request.operation_note
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sso_client):
            query['SsoClient'] = request.sso_client
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAssetOperationToken',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAssetOperationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_asset_operation_token_with_options_async(
        self,
        request: main_models.GenerateAssetOperationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateAssetOperationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_account_id):
            query['AssetAccountId'] = request.asset_account_id
        if not DaraCore.is_null(request.asset_account_name):
            query['AssetAccountName'] = request.asset_account_name
        if not DaraCore.is_null(request.asset_account_password):
            query['AssetAccountPassword'] = request.asset_account_password
        if not DaraCore.is_null(request.asset_account_protocol_name):
            query['AssetAccountProtocolName'] = request.asset_account_protocol_name
        if not DaraCore.is_null(request.asset_id):
            query['AssetId'] = request.asset_id
        if not DaraCore.is_null(request.asset_type):
            query['AssetType'] = request.asset_type
        if not DaraCore.is_null(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.login_attribute):
            query['LoginAttribute'] = request.login_attribute
        if not DaraCore.is_null(request.operation_mode):
            query['OperationMode'] = request.operation_mode
        if not DaraCore.is_null(request.operation_note):
            query['OperationNote'] = request.operation_note
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sso_client):
            query['SsoClient'] = request.sso_client
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateAssetOperationToken',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateAssetOperationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_asset_operation_token(
        self,
        request: main_models.GenerateAssetOperationTokenRequest,
    ) -> main_models.GenerateAssetOperationTokenResponse:
        runtime = RuntimeOptions()
        return self.generate_asset_operation_token_with_options(request, runtime)

    async def generate_asset_operation_token_async(
        self,
        request: main_models.GenerateAssetOperationTokenRequest,
    ) -> main_models.GenerateAssetOperationTokenResponse:
        runtime = RuntimeOptions()
        return await self.generate_asset_operation_token_with_options_async(request, runtime)

    def get_database_with_options(
        self,
        request: main_models.GetDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabase',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_with_options_async(
        self,
        request: main_models.GetDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabase',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database(
        self,
        request: main_models.GetDatabaseRequest,
    ) -> main_models.GetDatabaseResponse:
        runtime = RuntimeOptions()
        return self.get_database_with_options(request, runtime)

    async def get_database_async(
        self,
        request: main_models.GetDatabaseRequest,
    ) -> main_models.GetDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.get_database_with_options_async(request, runtime)

    def get_database_account_with_options(
        self,
        request: main_models.GetDatabaseAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabaseAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_account_with_options_async(
        self,
        request: main_models.GetDatabaseAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabaseAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database_account(
        self,
        request: main_models.GetDatabaseAccountRequest,
    ) -> main_models.GetDatabaseAccountResponse:
        runtime = RuntimeOptions()
        return self.get_database_account_with_options(request, runtime)

    async def get_database_account_async(
        self,
        request: main_models.GetDatabaseAccountRequest,
    ) -> main_models.GetDatabaseAccountResponse:
        runtime = RuntimeOptions()
        return await self.get_database_account_with_options_async(request, runtime)

    def get_export_config_job_with_options(
        self,
        request: main_models.GetExportConfigJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExportConfigJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExportConfigJob',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExportConfigJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_export_config_job_with_options_async(
        self,
        request: main_models.GetExportConfigJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExportConfigJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExportConfigJob',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExportConfigJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_export_config_job(
        self,
        request: main_models.GetExportConfigJobRequest,
    ) -> main_models.GetExportConfigJobResponse:
        runtime = RuntimeOptions()
        return self.get_export_config_job_with_options(request, runtime)

    async def get_export_config_job_async(
        self,
        request: main_models.GetExportConfigJobRequest,
    ) -> main_models.GetExportConfigJobResponse:
        runtime = RuntimeOptions()
        return await self.get_export_config_job_with_options_async(request, runtime)

    def get_host_with_options(
        self,
        request: main_models.GetHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHost',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_with_options_async(
        self,
        request: main_models.GetHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHost',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host(
        self,
        request: main_models.GetHostRequest,
    ) -> main_models.GetHostResponse:
        runtime = RuntimeOptions()
        return self.get_host_with_options(request, runtime)

    async def get_host_async(
        self,
        request: main_models.GetHostRequest,
    ) -> main_models.GetHostResponse:
        runtime = RuntimeOptions()
        return await self.get_host_with_options_async(request, runtime)

    def get_host_account_with_options(
        self,
        request: main_models.GetHostAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHostAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHostAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_account_with_options_async(
        self,
        request: main_models.GetHostAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHostAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHostAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host_account(
        self,
        request: main_models.GetHostAccountRequest,
    ) -> main_models.GetHostAccountResponse:
        runtime = RuntimeOptions()
        return self.get_host_account_with_options(request, runtime)

    async def get_host_account_async(
        self,
        request: main_models.GetHostAccountRequest,
    ) -> main_models.GetHostAccountResponse:
        runtime = RuntimeOptions()
        return await self.get_host_account_with_options_async(request, runtime)

    def get_host_group_with_options(
        self,
        request: main_models.GetHostGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHostGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHostGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_group_with_options_async(
        self,
        request: main_models.GetHostGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHostGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHostGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host_group(
        self,
        request: main_models.GetHostGroupRequest,
    ) -> main_models.GetHostGroupResponse:
        runtime = RuntimeOptions()
        return self.get_host_group_with_options(request, runtime)

    async def get_host_group_async(
        self,
        request: main_models.GetHostGroupRequest,
    ) -> main_models.GetHostGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_host_group_with_options_async(request, runtime)

    def get_host_share_key_with_options(
        self,
        request: main_models.GetHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_share_key_with_options_async(
        self,
        request: main_models.GetHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host_share_key(
        self,
        request: main_models.GetHostShareKeyRequest,
    ) -> main_models.GetHostShareKeyResponse:
        runtime = RuntimeOptions()
        return self.get_host_share_key_with_options(request, runtime)

    async def get_host_share_key_async(
        self,
        request: main_models.GetHostShareKeyRequest,
    ) -> main_models.GetHostShareKeyResponse:
        runtime = RuntimeOptions()
        return await self.get_host_share_key_with_options_async(request, runtime)

    def get_instance_adauth_server_with_options(
        self,
        request: main_models.GetInstanceADAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceADAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceADAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceADAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_adauth_server_with_options_async(
        self,
        request: main_models.GetInstanceADAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceADAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceADAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceADAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_adauth_server(
        self,
        request: main_models.GetInstanceADAuthServerRequest,
    ) -> main_models.GetInstanceADAuthServerResponse:
        runtime = RuntimeOptions()
        return self.get_instance_adauth_server_with_options(request, runtime)

    async def get_instance_adauth_server_async(
        self,
        request: main_models.GetInstanceADAuthServerRequest,
    ) -> main_models.GetInstanceADAuthServerResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_adauth_server_with_options_async(request, runtime)

    def get_instance_ldapauth_server_with_options(
        self,
        request: main_models.GetInstanceLDAPAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceLDAPAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceLDAPAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceLDAPAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_ldapauth_server_with_options_async(
        self,
        request: main_models.GetInstanceLDAPAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceLDAPAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceLDAPAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceLDAPAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_ldapauth_server(
        self,
        request: main_models.GetInstanceLDAPAuthServerRequest,
    ) -> main_models.GetInstanceLDAPAuthServerResponse:
        runtime = RuntimeOptions()
        return self.get_instance_ldapauth_server_with_options(request, runtime)

    async def get_instance_ldapauth_server_async(
        self,
        request: main_models.GetInstanceLDAPAuthServerRequest,
    ) -> main_models.GetInstanceLDAPAuthServerResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_ldapauth_server_with_options_async(request, runtime)

    def get_instance_store_info_with_options(
        self,
        request: main_models.GetInstanceStoreInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceStoreInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceStoreInfo',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceStoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_store_info_with_options_async(
        self,
        request: main_models.GetInstanceStoreInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceStoreInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceStoreInfo',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceStoreInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_store_info(
        self,
        request: main_models.GetInstanceStoreInfoRequest,
    ) -> main_models.GetInstanceStoreInfoResponse:
        runtime = RuntimeOptions()
        return self.get_instance_store_info_with_options(request, runtime)

    async def get_instance_store_info_async(
        self,
        request: main_models.GetInstanceStoreInfoRequest,
    ) -> main_models.GetInstanceStoreInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_store_info_with_options_async(request, runtime)

    def get_instance_two_factor_with_options(
        self,
        request: main_models.GetInstanceTwoFactorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceTwoFactorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceTwoFactor',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceTwoFactorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_two_factor_with_options_async(
        self,
        request: main_models.GetInstanceTwoFactorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceTwoFactorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceTwoFactor',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceTwoFactorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_two_factor(
        self,
        request: main_models.GetInstanceTwoFactorRequest,
    ) -> main_models.GetInstanceTwoFactorResponse:
        runtime = RuntimeOptions()
        return self.get_instance_two_factor_with_options(request, runtime)

    async def get_instance_two_factor_async(
        self,
        request: main_models.GetInstanceTwoFactorRequest,
    ) -> main_models.GetInstanceTwoFactorResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_two_factor_with_options_async(request, runtime)

    def get_network_domain_with_options(
        self,
        request: main_models.GetNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_proxy_state):
            query['CheckProxyState'] = request.check_proxy_state
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_domain_with_options_async(
        self,
        request: main_models.GetNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_proxy_state):
            query['CheckProxyState'] = request.check_proxy_state
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_domain(
        self,
        request: main_models.GetNetworkDomainRequest,
    ) -> main_models.GetNetworkDomainResponse:
        runtime = RuntimeOptions()
        return self.get_network_domain_with_options(request, runtime)

    async def get_network_domain_async(
        self,
        request: main_models.GetNetworkDomainRequest,
    ) -> main_models.GetNetworkDomainResponse:
        runtime = RuntimeOptions()
        return await self.get_network_domain_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: main_models.GetPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: main_models.GetPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        request: main_models.GetPolicyRequest,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: main_models.GetPolicyRequest,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_asset_scope_with_options(
        self,
        request: main_models.GetPolicyAssetScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyAssetScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyAssetScope',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyAssetScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_asset_scope_with_options_async(
        self,
        request: main_models.GetPolicyAssetScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyAssetScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyAssetScope',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyAssetScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_asset_scope(
        self,
        request: main_models.GetPolicyAssetScopeRequest,
    ) -> main_models.GetPolicyAssetScopeResponse:
        runtime = RuntimeOptions()
        return self.get_policy_asset_scope_with_options(request, runtime)

    async def get_policy_asset_scope_async(
        self,
        request: main_models.GetPolicyAssetScopeRequest,
    ) -> main_models.GetPolicyAssetScopeResponse:
        runtime = RuntimeOptions()
        return await self.get_policy_asset_scope_with_options_async(request, runtime)

    def get_policy_user_scope_with_options(
        self,
        request: main_models.GetPolicyUserScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyUserScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyUserScope',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyUserScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_user_scope_with_options_async(
        self,
        request: main_models.GetPolicyUserScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyUserScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyUserScope',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyUserScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_user_scope(
        self,
        request: main_models.GetPolicyUserScopeRequest,
    ) -> main_models.GetPolicyUserScopeResponse:
        runtime = RuntimeOptions()
        return self.get_policy_user_scope_with_options(request, runtime)

    async def get_policy_user_scope_async(
        self,
        request: main_models.GetPolicyUserScopeRequest,
    ) -> main_models.GetPolicyUserScopeResponse:
        runtime = RuntimeOptions()
        return await self.get_policy_user_scope_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: main_models.GetRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: main_models.GetRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule(
        self,
        request: main_models.GetRuleRequest,
    ) -> main_models.GetRuleResponse:
        runtime = RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: main_models.GetRuleRequest,
    ) -> main_models.GetRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_group_with_options(
        self,
        request: main_models.GetUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_group_with_options_async(
        self,
        request: main_models.GetUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_group(
        self,
        request: main_models.GetUserGroupRequest,
    ) -> main_models.GetUserGroupResponse:
        runtime = RuntimeOptions()
        return self.get_user_group_with_options(request, runtime)

    async def get_user_group_async(
        self,
        request: main_models.GetUserGroupRequest,
    ) -> main_models.GetUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_user_group_with_options_async(request, runtime)

    def list_approve_commands_with_options(
        self,
        request: main_models.ListApproveCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApproveCommandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApproveCommands',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApproveCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_approve_commands_with_options_async(
        self,
        request: main_models.ListApproveCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApproveCommandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApproveCommands',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApproveCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_approve_commands(
        self,
        request: main_models.ListApproveCommandsRequest,
    ) -> main_models.ListApproveCommandsResponse:
        runtime = RuntimeOptions()
        return self.list_approve_commands_with_options(request, runtime)

    async def list_approve_commands_async(
        self,
        request: main_models.ListApproveCommandsRequest,
    ) -> main_models.ListApproveCommandsResponse:
        runtime = RuntimeOptions()
        return await self.list_approve_commands_with_options_async(request, runtime)

    def list_database_accounts_with_options(
        self,
        request: main_models.ListDatabaseAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseAccounts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_accounts_with_options_async(
        self,
        request: main_models.ListDatabaseAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseAccounts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_accounts(
        self,
        request: main_models.ListDatabaseAccountsRequest,
    ) -> main_models.ListDatabaseAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_database_accounts_with_options(request, runtime)

    async def list_database_accounts_async(
        self,
        request: main_models.ListDatabaseAccountsRequest,
    ) -> main_models.ListDatabaseAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_database_accounts_with_options_async(request, runtime)

    def list_database_accounts_for_user_with_options(
        self,
        request: main_models.ListDatabaseAccountsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseAccountsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseAccountsForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseAccountsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_accounts_for_user_with_options_async(
        self,
        request: main_models.ListDatabaseAccountsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseAccountsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseAccountsForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseAccountsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_accounts_for_user(
        self,
        request: main_models.ListDatabaseAccountsForUserRequest,
    ) -> main_models.ListDatabaseAccountsForUserResponse:
        runtime = RuntimeOptions()
        return self.list_database_accounts_for_user_with_options(request, runtime)

    async def list_database_accounts_for_user_async(
        self,
        request: main_models.ListDatabaseAccountsForUserRequest,
    ) -> main_models.ListDatabaseAccountsForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_database_accounts_for_user_with_options_async(request, runtime)

    def list_database_accounts_for_user_group_with_options(
        self,
        request: main_models.ListDatabaseAccountsForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseAccountsForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseAccountsForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseAccountsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_accounts_for_user_group_with_options_async(
        self,
        request: main_models.ListDatabaseAccountsForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseAccountsForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseAccountsForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseAccountsForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_accounts_for_user_group(
        self,
        request: main_models.ListDatabaseAccountsForUserGroupRequest,
    ) -> main_models.ListDatabaseAccountsForUserGroupResponse:
        runtime = RuntimeOptions()
        return self.list_database_accounts_for_user_group_with_options(request, runtime)

    async def list_database_accounts_for_user_group_async(
        self,
        request: main_models.ListDatabaseAccountsForUserGroupRequest,
    ) -> main_models.ListDatabaseAccountsForUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_database_accounts_for_user_group_with_options_async(request, runtime)

    def list_databases_with_options(
        self,
        request: main_models.ListDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_with_options_async(
        self,
        request: main_models.ListDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases(
        self,
        request: main_models.ListDatabasesRequest,
    ) -> main_models.ListDatabasesResponse:
        runtime = RuntimeOptions()
        return self.list_databases_with_options(request, runtime)

    async def list_databases_async(
        self,
        request: main_models.ListDatabasesRequest,
    ) -> main_models.ListDatabasesResponse:
        runtime = RuntimeOptions()
        return await self.list_databases_with_options_async(request, runtime)

    def list_databases_for_user_with_options(
        self,
        request: main_models.ListDatabasesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabasesForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_for_user_with_options_async(
        self,
        request: main_models.ListDatabasesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabasesForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases_for_user(
        self,
        request: main_models.ListDatabasesForUserRequest,
    ) -> main_models.ListDatabasesForUserResponse:
        runtime = RuntimeOptions()
        return self.list_databases_for_user_with_options(request, runtime)

    async def list_databases_for_user_async(
        self,
        request: main_models.ListDatabasesForUserRequest,
    ) -> main_models.ListDatabasesForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_databases_for_user_with_options_async(request, runtime)

    def list_databases_for_user_group_with_options(
        self,
        request: main_models.ListDatabasesForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabasesForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_for_user_group_with_options_async(
        self,
        request: main_models.ListDatabasesForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabasesForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases_for_user_group(
        self,
        request: main_models.ListDatabasesForUserGroupRequest,
    ) -> main_models.ListDatabasesForUserGroupResponse:
        runtime = RuntimeOptions()
        return self.list_databases_for_user_group_with_options(request, runtime)

    async def list_databases_for_user_group_async(
        self,
        request: main_models.ListDatabasesForUserGroupRequest,
    ) -> main_models.ListDatabasesForUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_databases_for_user_group_with_options_async(request, runtime)

    def list_host_accounts_with_options(
        self,
        request: main_models.ListHostAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostAccounts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_accounts_with_options_async(
        self,
        request: main_models.ListHostAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostAccounts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_accounts(
        self,
        request: main_models.ListHostAccountsRequest,
    ) -> main_models.ListHostAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_host_accounts_with_options(request, runtime)

    async def list_host_accounts_async(
        self,
        request: main_models.ListHostAccountsRequest,
    ) -> main_models.ListHostAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_host_accounts_with_options_async(request, runtime)

    def list_host_accounts_for_host_share_key_with_options(
        self,
        request: main_models.ListHostAccountsForHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostAccountsForHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostAccountsForHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostAccountsForHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_accounts_for_host_share_key_with_options_async(
        self,
        request: main_models.ListHostAccountsForHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostAccountsForHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostAccountsForHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostAccountsForHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_accounts_for_host_share_key(
        self,
        request: main_models.ListHostAccountsForHostShareKeyRequest,
    ) -> main_models.ListHostAccountsForHostShareKeyResponse:
        runtime = RuntimeOptions()
        return self.list_host_accounts_for_host_share_key_with_options(request, runtime)

    async def list_host_accounts_for_host_share_key_async(
        self,
        request: main_models.ListHostAccountsForHostShareKeyRequest,
    ) -> main_models.ListHostAccountsForHostShareKeyResponse:
        runtime = RuntimeOptions()
        return await self.list_host_accounts_for_host_share_key_with_options_async(request, runtime)

    def list_host_accounts_for_user_with_options(
        self,
        request: main_models.ListHostAccountsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostAccountsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostAccountsForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostAccountsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_accounts_for_user_with_options_async(
        self,
        request: main_models.ListHostAccountsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostAccountsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostAccountsForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostAccountsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_accounts_for_user(
        self,
        request: main_models.ListHostAccountsForUserRequest,
    ) -> main_models.ListHostAccountsForUserResponse:
        runtime = RuntimeOptions()
        return self.list_host_accounts_for_user_with_options(request, runtime)

    async def list_host_accounts_for_user_async(
        self,
        request: main_models.ListHostAccountsForUserRequest,
    ) -> main_models.ListHostAccountsForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_host_accounts_for_user_with_options_async(request, runtime)

    def list_host_accounts_for_user_group_with_options(
        self,
        request: main_models.ListHostAccountsForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostAccountsForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostAccountsForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostAccountsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_accounts_for_user_group_with_options_async(
        self,
        request: main_models.ListHostAccountsForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostAccountsForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostAccountsForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostAccountsForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_accounts_for_user_group(
        self,
        request: main_models.ListHostAccountsForUserGroupRequest,
    ) -> main_models.ListHostAccountsForUserGroupResponse:
        runtime = RuntimeOptions()
        return self.list_host_accounts_for_user_group_with_options(request, runtime)

    async def list_host_accounts_for_user_group_async(
        self,
        request: main_models.ListHostAccountsForUserGroupRequest,
    ) -> main_models.ListHostAccountsForUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_host_accounts_for_user_group_with_options_async(request, runtime)

    def list_host_group_account_names_for_user_with_options(
        self,
        request: main_models.ListHostGroupAccountNamesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupAccountNamesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroupAccountNamesForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupAccountNamesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_group_account_names_for_user_with_options_async(
        self,
        request: main_models.ListHostGroupAccountNamesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupAccountNamesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroupAccountNamesForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupAccountNamesForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_group_account_names_for_user(
        self,
        request: main_models.ListHostGroupAccountNamesForUserRequest,
    ) -> main_models.ListHostGroupAccountNamesForUserResponse:
        runtime = RuntimeOptions()
        return self.list_host_group_account_names_for_user_with_options(request, runtime)

    async def list_host_group_account_names_for_user_async(
        self,
        request: main_models.ListHostGroupAccountNamesForUserRequest,
    ) -> main_models.ListHostGroupAccountNamesForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_host_group_account_names_for_user_with_options_async(request, runtime)

    def list_host_group_account_names_for_user_group_with_options(
        self,
        request: main_models.ListHostGroupAccountNamesForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupAccountNamesForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroupAccountNamesForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupAccountNamesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_group_account_names_for_user_group_with_options_async(
        self,
        request: main_models.ListHostGroupAccountNamesForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupAccountNamesForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroupAccountNamesForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupAccountNamesForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_group_account_names_for_user_group(
        self,
        request: main_models.ListHostGroupAccountNamesForUserGroupRequest,
    ) -> main_models.ListHostGroupAccountNamesForUserGroupResponse:
        runtime = RuntimeOptions()
        return self.list_host_group_account_names_for_user_group_with_options(request, runtime)

    async def list_host_group_account_names_for_user_group_async(
        self,
        request: main_models.ListHostGroupAccountNamesForUserGroupRequest,
    ) -> main_models.ListHostGroupAccountNamesForUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_host_group_account_names_for_user_group_with_options_async(request, runtime)

    def list_host_groups_with_options(
        self,
        request: main_models.ListHostGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroups',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_groups_with_options_async(
        self,
        request: main_models.ListHostGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroups',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_groups(
        self,
        request: main_models.ListHostGroupsRequest,
    ) -> main_models.ListHostGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_host_groups_with_options(request, runtime)

    async def list_host_groups_async(
        self,
        request: main_models.ListHostGroupsRequest,
    ) -> main_models.ListHostGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_host_groups_with_options_async(request, runtime)

    def list_host_groups_for_user_with_options(
        self,
        request: main_models.ListHostGroupsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroupsForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_groups_for_user_with_options_async(
        self,
        request: main_models.ListHostGroupsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroupsForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_groups_for_user(
        self,
        request: main_models.ListHostGroupsForUserRequest,
    ) -> main_models.ListHostGroupsForUserResponse:
        runtime = RuntimeOptions()
        return self.list_host_groups_for_user_with_options(request, runtime)

    async def list_host_groups_for_user_async(
        self,
        request: main_models.ListHostGroupsForUserRequest,
    ) -> main_models.ListHostGroupsForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_host_groups_for_user_with_options_async(request, runtime)

    def list_host_groups_for_user_group_with_options(
        self,
        request: main_models.ListHostGroupsForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupsForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroupsForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_groups_for_user_group_with_options_async(
        self,
        request: main_models.ListHostGroupsForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostGroupsForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostGroupsForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostGroupsForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_groups_for_user_group(
        self,
        request: main_models.ListHostGroupsForUserGroupRequest,
    ) -> main_models.ListHostGroupsForUserGroupResponse:
        runtime = RuntimeOptions()
        return self.list_host_groups_for_user_group_with_options(request, runtime)

    async def list_host_groups_for_user_group_async(
        self,
        request: main_models.ListHostGroupsForUserGroupRequest,
    ) -> main_models.ListHostGroupsForUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_host_groups_for_user_group_with_options_async(request, runtime)

    def list_host_share_keys_with_options(
        self,
        request: main_models.ListHostShareKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostShareKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostShareKeys',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostShareKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_share_keys_with_options_async(
        self,
        request: main_models.ListHostShareKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostShareKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostShareKeys',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostShareKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_share_keys(
        self,
        request: main_models.ListHostShareKeysRequest,
    ) -> main_models.ListHostShareKeysResponse:
        runtime = RuntimeOptions()
        return self.list_host_share_keys_with_options(request, runtime)

    async def list_host_share_keys_async(
        self,
        request: main_models.ListHostShareKeysRequest,
    ) -> main_models.ListHostShareKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_host_share_keys_with_options_async(request, runtime)

    def list_hosts_with_options(
        self,
        request: main_models.ListHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHosts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hosts_with_options_async(
        self,
        request: main_models.ListHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHosts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hosts(
        self,
        request: main_models.ListHostsRequest,
    ) -> main_models.ListHostsResponse:
        runtime = RuntimeOptions()
        return self.list_hosts_with_options(request, runtime)

    async def list_hosts_async(
        self,
        request: main_models.ListHostsRequest,
    ) -> main_models.ListHostsResponse:
        runtime = RuntimeOptions()
        return await self.list_hosts_with_options_async(request, runtime)

    def list_hosts_for_user_with_options(
        self,
        request: main_models.ListHostsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostsForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hosts_for_user_with_options_async(
        self,
        request: main_models.ListHostsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostsForUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hosts_for_user(
        self,
        request: main_models.ListHostsForUserRequest,
    ) -> main_models.ListHostsForUserResponse:
        runtime = RuntimeOptions()
        return self.list_hosts_for_user_with_options(request, runtime)

    async def list_hosts_for_user_async(
        self,
        request: main_models.ListHostsForUserRequest,
    ) -> main_models.ListHostsForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_hosts_for_user_with_options_async(request, runtime)

    def list_hosts_for_user_group_with_options(
        self,
        request: main_models.ListHostsForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostsForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostsForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hosts_for_user_group_with_options_async(
        self,
        request: main_models.ListHostsForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHostsForUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHostsForUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHostsForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hosts_for_user_group(
        self,
        request: main_models.ListHostsForUserGroupRequest,
    ) -> main_models.ListHostsForUserGroupResponse:
        runtime = RuntimeOptions()
        return self.list_hosts_for_user_group_with_options(request, runtime)

    async def list_hosts_for_user_group_async(
        self,
        request: main_models.ListHostsForUserGroupRequest,
    ) -> main_models.ListHostsForUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_hosts_for_user_group_with_options_async(request, runtime)

    def list_instance_rd_members_with_options(
        self,
        request: main_models.ListInstanceRdMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceRdMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceRdMembers',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceRdMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_rd_members_with_options_async(
        self,
        request: main_models.ListInstanceRdMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceRdMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceRdMembers',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceRdMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_rd_members(
        self,
        request: main_models.ListInstanceRdMembersRequest,
    ) -> main_models.ListInstanceRdMembersResponse:
        runtime = RuntimeOptions()
        return self.list_instance_rd_members_with_options(request, runtime)

    async def list_instance_rd_members_async(
        self,
        request: main_models.ListInstanceRdMembersRequest,
    ) -> main_models.ListInstanceRdMembersResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_rd_members_with_options_async(request, runtime)

    def list_network_domains_with_options(
        self,
        request: main_models.ListNetworkDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not DaraCore.is_null(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkDomains',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_domains_with_options_async(
        self,
        request: main_models.ListNetworkDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not DaraCore.is_null(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkDomains',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_domains(
        self,
        request: main_models.ListNetworkDomainsRequest,
    ) -> main_models.ListNetworkDomainsResponse:
        runtime = RuntimeOptions()
        return self.list_network_domains_with_options(request, runtime)

    async def list_network_domains_async(
        self,
        request: main_models.ListNetworkDomainsRequest,
    ) -> main_models.ListNetworkDomainsResponse:
        runtime = RuntimeOptions()
        return await self.list_network_domains_with_options_async(request, runtime)

    def list_operation_database_accounts_with_options(
        self,
        request: main_models.ListOperationDatabaseAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationDatabaseAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationDatabaseAccounts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationDatabaseAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_database_accounts_with_options_async(
        self,
        request: main_models.ListOperationDatabaseAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationDatabaseAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationDatabaseAccounts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationDatabaseAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_database_accounts(
        self,
        request: main_models.ListOperationDatabaseAccountsRequest,
    ) -> main_models.ListOperationDatabaseAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_operation_database_accounts_with_options(request, runtime)

    async def list_operation_database_accounts_async(
        self,
        request: main_models.ListOperationDatabaseAccountsRequest,
    ) -> main_models.ListOperationDatabaseAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_operation_database_accounts_with_options_async(request, runtime)

    def list_operation_databases_with_options(
        self,
        request: main_models.ListOperationDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationDatabases',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_databases_with_options_async(
        self,
        request: main_models.ListOperationDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationDatabases',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_databases(
        self,
        request: main_models.ListOperationDatabasesRequest,
    ) -> main_models.ListOperationDatabasesResponse:
        runtime = RuntimeOptions()
        return self.list_operation_databases_with_options(request, runtime)

    async def list_operation_databases_async(
        self,
        request: main_models.ListOperationDatabasesRequest,
    ) -> main_models.ListOperationDatabasesResponse:
        runtime = RuntimeOptions()
        return await self.list_operation_databases_with_options_async(request, runtime)

    def list_operation_host_accounts_with_options(
        self,
        request: main_models.ListOperationHostAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationHostAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationHostAccounts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationHostAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_host_accounts_with_options_async(
        self,
        request: main_models.ListOperationHostAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationHostAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationHostAccounts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationHostAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_host_accounts(
        self,
        request: main_models.ListOperationHostAccountsRequest,
    ) -> main_models.ListOperationHostAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_operation_host_accounts_with_options(request, runtime)

    async def list_operation_host_accounts_async(
        self,
        request: main_models.ListOperationHostAccountsRequest,
    ) -> main_models.ListOperationHostAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_operation_host_accounts_with_options_async(request, runtime)

    def list_operation_hosts_with_options(
        self,
        request: main_models.ListOperationHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationHostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationHosts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_hosts_with_options_async(
        self,
        request: main_models.ListOperationHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationHostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_address):
            query['HostAddress'] = request.host_address
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not DaraCore.is_null(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationHosts',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_hosts(
        self,
        request: main_models.ListOperationHostsRequest,
    ) -> main_models.ListOperationHostsResponse:
        runtime = RuntimeOptions()
        return self.list_operation_hosts_with_options(request, runtime)

    async def list_operation_hosts_async(
        self,
        request: main_models.ListOperationHostsRequest,
    ) -> main_models.ListOperationHostsResponse:
        runtime = RuntimeOptions()
        return await self.list_operation_hosts_with_options_async(request, runtime)

    def list_operation_tickets_with_options(
        self,
        request: main_models.ListOperationTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationTicketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_address):
            query['AssetAddress'] = request.asset_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationTickets',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_tickets_with_options_async(
        self,
        request: main_models.ListOperationTicketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationTicketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_address):
            query['AssetAddress'] = request.asset_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationTickets',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationTicketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_tickets(
        self,
        request: main_models.ListOperationTicketsRequest,
    ) -> main_models.ListOperationTicketsResponse:
        runtime = RuntimeOptions()
        return self.list_operation_tickets_with_options(request, runtime)

    async def list_operation_tickets_async(
        self,
        request: main_models.ListOperationTicketsRequest,
    ) -> main_models.ListOperationTicketsResponse:
        runtime = RuntimeOptions()
        return await self.list_operation_tickets_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: main_models.ListRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_state):
            query['RuleState'] = request.rule_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRules',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: main_models.ListRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_state):
            query['RuleState'] = request.rule_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRules',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: main_models.ListRulesRequest,
    ) -> main_models.ListRulesResponse:
        runtime = RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: main_models.ListRulesRequest,
    ) -> main_models.ListRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_groups_with_options(
        self,
        request: main_models.ListUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroups',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_with_options_async(
        self,
        request: main_models.ListUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroups',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups(
        self,
        request: main_models.ListUserGroupsRequest,
    ) -> main_models.ListUserGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    async def list_user_groups_async(
        self,
        request: main_models.ListUserGroupsRequest,
    ) -> main_models.ListUserGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_groups_with_options_async(request, runtime)

    def list_user_public_keys_with_options(
        self,
        request: main_models.ListUserPublicKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPublicKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserPublicKeys',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserPublicKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_public_keys_with_options_async(
        self,
        request: main_models.ListUserPublicKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPublicKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserPublicKeys',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserPublicKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_public_keys(
        self,
        request: main_models.ListUserPublicKeysRequest,
    ) -> main_models.ListUserPublicKeysResponse:
        runtime = RuntimeOptions()
        return self.list_user_public_keys_with_options(request, runtime)

    async def list_user_public_keys_async(
        self,
        request: main_models.ListUserPublicKeysRequest,
    ) -> main_models.ListUserPublicKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_user_public_keys_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_state):
            query['UserState'] = request.user_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_state):
            query['UserState'] = request.user_state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def lock_users_with_options(
        self,
        request: main_models.LockUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LockUsers',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_users_with_options_async(
        self,
        request: main_models.LockUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LockUsers',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LockUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_users(
        self,
        request: main_models.LockUsersRequest,
    ) -> main_models.LockUsersResponse:
        runtime = RuntimeOptions()
        return self.lock_users_with_options(request, runtime)

    async def lock_users_async(
        self,
        request: main_models.LockUsersRequest,
    ) -> main_models.LockUsersResponse:
        runtime = RuntimeOptions()
        return await self.lock_users_with_options_async(request, runtime)

    def modify_database_with_options(
        self,
        request: main_models.ModifyDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_port):
            query['DatabasePort'] = request.database_port
        if not DaraCore.is_null(request.database_private_address):
            query['DatabasePrivateAddress'] = request.database_private_address
        if not DaraCore.is_null(request.database_public_address):
            query['DatabasePublicAddress'] = request.database_public_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabase',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_with_options_async(
        self,
        request: main_models.ModifyDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.database_id):
            query['DatabaseId'] = request.database_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.database_port):
            query['DatabasePort'] = request.database_port
        if not DaraCore.is_null(request.database_private_address):
            query['DatabasePrivateAddress'] = request.database_private_address
        if not DaraCore.is_null(request.database_public_address):
            query['DatabasePublicAddress'] = request.database_public_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabase',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database(
        self,
        request: main_models.ModifyDatabaseRequest,
    ) -> main_models.ModifyDatabaseResponse:
        runtime = RuntimeOptions()
        return self.modify_database_with_options(request, runtime)

    async def modify_database_async(
        self,
        request: main_models.ModifyDatabaseRequest,
    ) -> main_models.ModifyDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.modify_database_with_options_async(request, runtime)

    def modify_database_account_with_options(
        self,
        request: main_models.ModifyDatabaseAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabaseAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_account_with_options_async(
        self,
        request: main_models.ModifyDatabaseAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not DaraCore.is_null(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not DaraCore.is_null(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabaseAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_account(
        self,
        request: main_models.ModifyDatabaseAccountRequest,
    ) -> main_models.ModifyDatabaseAccountResponse:
        runtime = RuntimeOptions()
        return self.modify_database_account_with_options(request, runtime)

    async def modify_database_account_async(
        self,
        request: main_models.ModifyDatabaseAccountRequest,
    ) -> main_models.ModifyDatabaseAccountResponse:
        runtime = RuntimeOptions()
        return await self.modify_database_account_with_options_async(request, runtime)

    def modify_host_with_options(
        self,
        request: main_models.ModifyHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not DaraCore.is_null(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.pref_kex):
            query['PrefKex'] = request.pref_kex
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHost',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_with_options_async(
        self,
        request: main_models.ModifyHostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.host_id):
            query['HostId'] = request.host_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not DaraCore.is_null(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.ostype):
            query['OSType'] = request.ostype
        if not DaraCore.is_null(request.pref_kex):
            query['PrefKex'] = request.pref_kex
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHost',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host(
        self,
        request: main_models.ModifyHostRequest,
    ) -> main_models.ModifyHostResponse:
        runtime = RuntimeOptions()
        return self.modify_host_with_options(request, runtime)

    async def modify_host_async(
        self,
        request: main_models.ModifyHostRequest,
    ) -> main_models.ModifyHostResponse:
        runtime = RuntimeOptions()
        return await self.modify_host_with_options_async(request, runtime)

    def modify_host_account_with_options(
        self,
        request: main_models.ModifyHostAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rotation_mode):
            query['RotationMode'] = request.rotation_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_account_with_options_async(
        self,
        request: main_models.ModifyHostAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not DaraCore.is_null(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rotation_mode):
            query['RotationMode'] = request.rotation_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostAccount',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host_account(
        self,
        request: main_models.ModifyHostAccountRequest,
    ) -> main_models.ModifyHostAccountResponse:
        runtime = RuntimeOptions()
        return self.modify_host_account_with_options(request, runtime)

    async def modify_host_account_async(
        self,
        request: main_models.ModifyHostAccountRequest,
    ) -> main_models.ModifyHostAccountResponse:
        runtime = RuntimeOptions()
        return await self.modify_host_account_with_options_async(request, runtime)

    def modify_host_group_with_options(
        self,
        request: main_models.ModifyHostGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_group_with_options_async(
        self,
        request: main_models.ModifyHostGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host_group(
        self,
        request: main_models.ModifyHostGroupRequest,
    ) -> main_models.ModifyHostGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_host_group_with_options(request, runtime)

    async def modify_host_group_async(
        self,
        request: main_models.ModifyHostGroupRequest,
    ) -> main_models.ModifyHostGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_host_group_with_options_async(request, runtime)

    def modify_host_share_key_with_options(
        self,
        request: main_models.ModifyHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_share_key_with_options_async(
        self,
        request: main_models.ModifyHostShareKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostShareKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not DaraCore.is_null(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostShareKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host_share_key(
        self,
        request: main_models.ModifyHostShareKeyRequest,
    ) -> main_models.ModifyHostShareKeyResponse:
        runtime = RuntimeOptions()
        return self.modify_host_share_key_with_options(request, runtime)

    async def modify_host_share_key_async(
        self,
        request: main_models.ModifyHostShareKeyRequest,
    ) -> main_models.ModifyHostShareKeyResponse:
        runtime = RuntimeOptions()
        return await self.modify_host_share_key_with_options_async(request, runtime)

    def modify_hosts_active_address_type_with_options(
        self,
        request: main_models.ModifyHostsActiveAddressTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostsActiveAddressTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostsActiveAddressType',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostsActiveAddressTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hosts_active_address_type_with_options_async(
        self,
        request: main_models.ModifyHostsActiveAddressTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostsActiveAddressTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostsActiveAddressType',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostsActiveAddressTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hosts_active_address_type(
        self,
        request: main_models.ModifyHostsActiveAddressTypeRequest,
    ) -> main_models.ModifyHostsActiveAddressTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_hosts_active_address_type_with_options(request, runtime)

    async def modify_hosts_active_address_type_async(
        self,
        request: main_models.ModifyHostsActiveAddressTypeRequest,
    ) -> main_models.ModifyHostsActiveAddressTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_hosts_active_address_type_with_options_async(request, runtime)

    def modify_hosts_port_with_options(
        self,
        request: main_models.ModifyHostsPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostsPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostsPort',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostsPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hosts_port_with_options_async(
        self,
        request: main_models.ModifyHostsPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostsPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostsPort',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostsPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hosts_port(
        self,
        request: main_models.ModifyHostsPortRequest,
    ) -> main_models.ModifyHostsPortResponse:
        runtime = RuntimeOptions()
        return self.modify_hosts_port_with_options(request, runtime)

    async def modify_hosts_port_async(
        self,
        request: main_models.ModifyHostsPortRequest,
    ) -> main_models.ModifyHostsPortResponse:
        runtime = RuntimeOptions()
        return await self.modify_hosts_port_with_options_async(request, runtime)

    def modify_instance_adauth_server_with_options(
        self,
        request: main_models.ModifyInstanceADAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceADAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not DaraCore.is_null(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not DaraCore.is_null(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server):
            query['Server'] = request.server
        if not DaraCore.is_null(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceADAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceADAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_adauth_server_with_options_async(
        self,
        request: main_models.ModifyInstanceADAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceADAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not DaraCore.is_null(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not DaraCore.is_null(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server):
            query['Server'] = request.server
        if not DaraCore.is_null(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceADAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceADAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_adauth_server(
        self,
        request: main_models.ModifyInstanceADAuthServerRequest,
    ) -> main_models.ModifyInstanceADAuthServerResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_adauth_server_with_options(request, runtime)

    async def modify_instance_adauth_server_async(
        self,
        request: main_models.ModifyInstanceADAuthServerRequest,
    ) -> main_models.ModifyInstanceADAuthServerResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_adauth_server_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAttribute',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAttribute',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
    ) -> main_models.ModifyInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
    ) -> main_models.ModifyInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_ldapauth_server_with_options(
        self,
        request: main_models.ModifyInstanceLDAPAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceLDAPAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not DaraCore.is_null(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not DaraCore.is_null(request.login_name_mapping):
            query['LoginNameMapping'] = request.login_name_mapping
        if not DaraCore.is_null(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not DaraCore.is_null(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server):
            query['Server'] = request.server
        if not DaraCore.is_null(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceLDAPAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceLDAPAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_ldapauth_server_with_options_async(
        self,
        request: main_models.ModifyInstanceLDAPAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceLDAPAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not DaraCore.is_null(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not DaraCore.is_null(request.login_name_mapping):
            query['LoginNameMapping'] = request.login_name_mapping
        if not DaraCore.is_null(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not DaraCore.is_null(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server):
            query['Server'] = request.server
        if not DaraCore.is_null(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceLDAPAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceLDAPAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ldapauth_server(
        self,
        request: main_models.ModifyInstanceLDAPAuthServerRequest,
    ) -> main_models.ModifyInstanceLDAPAuthServerResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_ldapauth_server_with_options(request, runtime)

    async def modify_instance_ldapauth_server_async(
        self,
        request: main_models.ModifyInstanceLDAPAuthServerRequest,
    ) -> main_models.ModifyInstanceLDAPAuthServerResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_ldapauth_server_with_options_async(request, runtime)

    def modify_instance_two_factor_with_options(
        self,
        request: main_models.ModifyInstanceTwoFactorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceTwoFactorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_two_factor):
            query['EnableTwoFactor'] = request.enable_two_factor
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.skip_two_factor_time):
            query['SkipTwoFactorTime'] = request.skip_two_factor_time
        if not DaraCore.is_null(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceTwoFactor',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceTwoFactorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_two_factor_with_options_async(
        self,
        request: main_models.ModifyInstanceTwoFactorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceTwoFactorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_two_factor):
            query['EnableTwoFactor'] = request.enable_two_factor
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.skip_two_factor_time):
            query['SkipTwoFactorTime'] = request.skip_two_factor_time
        if not DaraCore.is_null(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceTwoFactor',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceTwoFactorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_two_factor(
        self,
        request: main_models.ModifyInstanceTwoFactorRequest,
    ) -> main_models.ModifyInstanceTwoFactorResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_two_factor_with_options(request, runtime)

    async def modify_instance_two_factor_async(
        self,
        request: main_models.ModifyInstanceTwoFactorRequest,
    ) -> main_models.ModifyInstanceTwoFactorResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_two_factor_with_options_async(request, runtime)

    def modify_network_domain_with_options(
        self,
        request: main_models.ModifyNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not DaraCore.is_null(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not DaraCore.is_null(request.proxies):
            query['Proxies'] = request.proxies
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_network_domain_with_options_async(
        self,
        request: main_models.ModifyNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not DaraCore.is_null(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not DaraCore.is_null(request.proxies):
            query['Proxies'] = request.proxies
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_network_domain(
        self,
        request: main_models.ModifyNetworkDomainRequest,
    ) -> main_models.ModifyNetworkDomainResponse:
        runtime = RuntimeOptions()
        return self.modify_network_domain_with_options(request, runtime)

    async def modify_network_domain_async(
        self,
        request: main_models.ModifyNetworkDomainRequest,
    ) -> main_models.ModifyNetworkDomainResponse:
        runtime = RuntimeOptions()
        return await self.modify_network_domain_with_options_async(request, runtime)

    def modify_policy_with_options(
        self,
        request: main_models.ModifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicy',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_with_options_async(
        self,
        request: main_models.ModifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicy',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy(
        self,
        request: main_models.ModifyPolicyRequest,
    ) -> main_models.ModifyPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_policy_with_options(request, runtime)

    async def modify_policy_async(
        self,
        request: main_models.ModifyPolicyRequest,
    ) -> main_models.ModifyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_policy_with_options_async(request, runtime)

    def modify_rule_with_options(
        self,
        request: main_models.ModifyRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rule_with_options_async(
        self,
        request: main_models.ModifyRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRule',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rule(
        self,
        request: main_models.ModifyRuleRequest,
    ) -> main_models.ModifyRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_rule_with_options(request, runtime)

    async def modify_rule_async(
        self,
        request: main_models.ModifyRuleRequest,
    ) -> main_models.ModifyRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_rule_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: main_models.ModifyUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.language_status):
            query['LanguageStatus'] = request.language_status
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not DaraCore.is_null(request.need_reset_password):
            query['NeedResetPassword'] = request.need_reset_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        if not DaraCore.is_null(request.two_factor_status):
            query['TwoFactorStatus'] = request.two_factor_status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: main_models.ModifyUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.language_status):
            query['LanguageStatus'] = request.language_status
        if not DaraCore.is_null(request.mobile):
            query['Mobile'] = request.mobile
        if not DaraCore.is_null(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not DaraCore.is_null(request.need_reset_password):
            query['NeedResetPassword'] = request.need_reset_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        if not DaraCore.is_null(request.two_factor_status):
            query['TwoFactorStatus'] = request.two_factor_status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUser',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user(
        self,
        request: main_models.ModifyUserRequest,
    ) -> main_models.ModifyUserResponse:
        runtime = RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: main_models.ModifyUserRequest,
    ) -> main_models.ModifyUserResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def modify_user_group_with_options(
        self,
        request: main_models.ModifyUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_group_with_options_async(
        self,
        request: main_models.ModifyUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_group(
        self,
        request: main_models.ModifyUserGroupRequest,
    ) -> main_models.ModifyUserGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_user_group_with_options(request, runtime)

    async def modify_user_group_async(
        self,
        request: main_models.ModifyUserGroupRequest,
    ) -> main_models.ModifyUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_group_with_options_async(request, runtime)

    def modify_user_public_key_with_options(
        self,
        request: main_models.ModifyUserPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        if not DaraCore.is_null(request.public_key_id):
            query['PublicKeyId'] = request.public_key_id
        if not DaraCore.is_null(request.public_key_name):
            query['PublicKeyName'] = request.public_key_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserPublicKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_public_key_with_options_async(
        self,
        request: main_models.ModifyUserPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        if not DaraCore.is_null(request.public_key_id):
            query['PublicKeyId'] = request.public_key_id
        if not DaraCore.is_null(request.public_key_name):
            query['PublicKeyName'] = request.public_key_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserPublicKey',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_public_key(
        self,
        request: main_models.ModifyUserPublicKeyRequest,
    ) -> main_models.ModifyUserPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.modify_user_public_key_with_options(request, runtime)

    async def modify_user_public_key_async(
        self,
        request: main_models.ModifyUserPublicKeyRequest,
    ) -> main_models.ModifyUserPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_public_key_with_options_async(request, runtime)

    def move_databases_to_network_domain_with_options(
        self,
        request: main_models.MoveDatabasesToNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveDatabasesToNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveDatabasesToNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveDatabasesToNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_databases_to_network_domain_with_options_async(
        self,
        request: main_models.MoveDatabasesToNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveDatabasesToNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveDatabasesToNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveDatabasesToNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_databases_to_network_domain(
        self,
        request: main_models.MoveDatabasesToNetworkDomainRequest,
    ) -> main_models.MoveDatabasesToNetworkDomainResponse:
        runtime = RuntimeOptions()
        return self.move_databases_to_network_domain_with_options(request, runtime)

    async def move_databases_to_network_domain_async(
        self,
        request: main_models.MoveDatabasesToNetworkDomainRequest,
    ) -> main_models.MoveDatabasesToNetworkDomainResponse:
        runtime = RuntimeOptions()
        return await self.move_databases_to_network_domain_with_options_async(request, runtime)

    def move_hosts_to_network_domain_with_options(
        self,
        request: main_models.MoveHostsToNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveHostsToNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveHostsToNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveHostsToNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_hosts_to_network_domain_with_options_async(
        self,
        request: main_models.MoveHostsToNetworkDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveHostsToNetworkDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveHostsToNetworkDomain',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveHostsToNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_hosts_to_network_domain(
        self,
        request: main_models.MoveHostsToNetworkDomainRequest,
    ) -> main_models.MoveHostsToNetworkDomainResponse:
        runtime = RuntimeOptions()
        return self.move_hosts_to_network_domain_with_options(request, runtime)

    async def move_hosts_to_network_domain_async(
        self,
        request: main_models.MoveHostsToNetworkDomainRequest,
    ) -> main_models.MoveHostsToNetworkDomainResponse:
        runtime = RuntimeOptions()
        return await self.move_hosts_to_network_domain_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def reject_approve_command_with_options(
        self,
        request: main_models.RejectApproveCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectApproveCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectApproveCommand',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectApproveCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_approve_command_with_options_async(
        self,
        request: main_models.RejectApproveCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectApproveCommandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.command_id):
            query['CommandId'] = request.command_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectApproveCommand',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectApproveCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_approve_command(
        self,
        request: main_models.RejectApproveCommandRequest,
    ) -> main_models.RejectApproveCommandResponse:
        runtime = RuntimeOptions()
        return self.reject_approve_command_with_options(request, runtime)

    async def reject_approve_command_async(
        self,
        request: main_models.RejectApproveCommandRequest,
    ) -> main_models.RejectApproveCommandResponse:
        runtime = RuntimeOptions()
        return await self.reject_approve_command_with_options_async(request, runtime)

    def reject_operation_ticket_with_options(
        self,
        request: main_models.RejectOperationTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectOperationTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_ticket_id):
            query['OperationTicketId'] = request.operation_ticket_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectOperationTicket',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectOperationTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_operation_ticket_with_options_async(
        self,
        request: main_models.RejectOperationTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectOperationTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_ticket_id):
            query['OperationTicketId'] = request.operation_ticket_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectOperationTicket',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectOperationTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_operation_ticket(
        self,
        request: main_models.RejectOperationTicketRequest,
    ) -> main_models.RejectOperationTicketResponse:
        runtime = RuntimeOptions()
        return self.reject_operation_ticket_with_options(request, runtime)

    async def reject_operation_ticket_async(
        self,
        request: main_models.RejectOperationTicketRequest,
    ) -> main_models.RejectOperationTicketResponse:
        runtime = RuntimeOptions()
        return await self.reject_operation_ticket_with_options_async(request, runtime)

    def remove_databases_from_group_with_options(
        self,
        request: main_models.RemoveDatabasesFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDatabasesFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDatabasesFromGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDatabasesFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_databases_from_group_with_options_async(
        self,
        request: main_models.RemoveDatabasesFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDatabasesFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDatabasesFromGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDatabasesFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_databases_from_group(
        self,
        request: main_models.RemoveDatabasesFromGroupRequest,
    ) -> main_models.RemoveDatabasesFromGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_databases_from_group_with_options(request, runtime)

    async def remove_databases_from_group_async(
        self,
        request: main_models.RemoveDatabasesFromGroupRequest,
    ) -> main_models.RemoveDatabasesFromGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_databases_from_group_with_options_async(request, runtime)

    def remove_hosts_from_group_with_options(
        self,
        request: main_models.RemoveHostsFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveHostsFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveHostsFromGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveHostsFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_hosts_from_group_with_options_async(
        self,
        request: main_models.RemoveHostsFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveHostsFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not DaraCore.is_null(request.host_ids):
            query['HostIds'] = request.host_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveHostsFromGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveHostsFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_hosts_from_group(
        self,
        request: main_models.RemoveHostsFromGroupRequest,
    ) -> main_models.RemoveHostsFromGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_hosts_from_group_with_options(request, runtime)

    async def remove_hosts_from_group_async(
        self,
        request: main_models.RemoveHostsFromGroupRequest,
    ) -> main_models.RemoveHostsFromGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_hosts_from_group_with_options_async(request, runtime)

    def remove_instance_rd_member_with_options(
        self,
        request: main_models.RemoveInstanceRdMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveInstanceRdMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveInstanceRdMember',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveInstanceRdMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_instance_rd_member_with_options_async(
        self,
        request: main_models.RemoveInstanceRdMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveInstanceRdMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveInstanceRdMember',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveInstanceRdMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_instance_rd_member(
        self,
        request: main_models.RemoveInstanceRdMemberRequest,
    ) -> main_models.RemoveInstanceRdMemberResponse:
        runtime = RuntimeOptions()
        return self.remove_instance_rd_member_with_options(request, runtime)

    async def remove_instance_rd_member_async(
        self,
        request: main_models.RemoveInstanceRdMemberRequest,
    ) -> main_models.RemoveInstanceRdMemberResponse:
        runtime = RuntimeOptions()
        return await self.remove_instance_rd_member_with_options_async(request, runtime)

    def remove_users_from_group_with_options(
        self,
        request: main_models.RemoveUsersFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsersFromGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_from_group_with_options_async(
        self,
        request: main_models.RemoveUsersFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsersFromGroup',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users_from_group(
        self,
        request: main_models.RemoveUsersFromGroupRequest,
    ) -> main_models.RemoveUsersFromGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_users_from_group_with_options(request, runtime)

    async def remove_users_from_group_async(
        self,
        request: main_models.RemoveUsersFromGroupRequest,
    ) -> main_models.RemoveUsersFromGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_users_from_group_with_options_async(request, runtime)

    def renew_asset_operation_token_with_options(
        self,
        request: main_models.RenewAssetOperationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAssetOperationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.token_id):
            query['TokenId'] = request.token_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAssetOperationToken',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAssetOperationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_asset_operation_token_with_options_async(
        self,
        request: main_models.RenewAssetOperationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAssetOperationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.token_id):
            query['TokenId'] = request.token_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAssetOperationToken',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAssetOperationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_asset_operation_token(
        self,
        request: main_models.RenewAssetOperationTokenRequest,
    ) -> main_models.RenewAssetOperationTokenResponse:
        runtime = RuntimeOptions()
        return self.renew_asset_operation_token_with_options(request, runtime)

    async def renew_asset_operation_token_async(
        self,
        request: main_models.RenewAssetOperationTokenRequest,
    ) -> main_models.RenewAssetOperationTokenResponse:
        runtime = RuntimeOptions()
        return await self.renew_asset_operation_token_with_options_async(request, runtime)

    def reset_host_account_credential_with_options(
        self,
        request: main_models.ResetHostAccountCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetHostAccountCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not DaraCore.is_null(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetHostAccountCredential',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetHostAccountCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_host_account_credential_with_options_async(
        self,
        request: main_models.ResetHostAccountCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetHostAccountCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not DaraCore.is_null(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetHostAccountCredential',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetHostAccountCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_host_account_credential(
        self,
        request: main_models.ResetHostAccountCredentialRequest,
    ) -> main_models.ResetHostAccountCredentialResponse:
        runtime = RuntimeOptions()
        return self.reset_host_account_credential_with_options(request, runtime)

    async def reset_host_account_credential_async(
        self,
        request: main_models.ResetHostAccountCredentialRequest,
    ) -> main_models.ResetHostAccountCredentialResponse:
        runtime = RuntimeOptions()
        return await self.reset_host_account_credential_with_options_async(request, runtime)

    def set_policy_access_time_range_config_with_options(
        self,
        tmp_req: main_models.SetPolicyAccessTimeRangeConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyAccessTimeRangeConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyAccessTimeRangeConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.access_time_range_config):
            request.access_time_range_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.access_time_range_config, 'AccessTimeRangeConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.access_time_range_config_shrink):
            query['AccessTimeRangeConfig'] = request.access_time_range_config_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyAccessTimeRangeConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyAccessTimeRangeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_access_time_range_config_with_options_async(
        self,
        tmp_req: main_models.SetPolicyAccessTimeRangeConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyAccessTimeRangeConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyAccessTimeRangeConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.access_time_range_config):
            request.access_time_range_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.access_time_range_config, 'AccessTimeRangeConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.access_time_range_config_shrink):
            query['AccessTimeRangeConfig'] = request.access_time_range_config_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyAccessTimeRangeConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyAccessTimeRangeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_access_time_range_config(
        self,
        request: main_models.SetPolicyAccessTimeRangeConfigRequest,
    ) -> main_models.SetPolicyAccessTimeRangeConfigResponse:
        runtime = RuntimeOptions()
        return self.set_policy_access_time_range_config_with_options(request, runtime)

    async def set_policy_access_time_range_config_async(
        self,
        request: main_models.SetPolicyAccessTimeRangeConfigRequest,
    ) -> main_models.SetPolicyAccessTimeRangeConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_policy_access_time_range_config_with_options_async(request, runtime)

    def set_policy_approval_config_with_options(
        self,
        tmp_req: main_models.SetPolicyApprovalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyApprovalConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyApprovalConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.approval_config):
            request.approval_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.approval_config, 'ApprovalConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.approval_config_shrink):
            query['ApprovalConfig'] = request.approval_config_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyApprovalConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyApprovalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_approval_config_with_options_async(
        self,
        tmp_req: main_models.SetPolicyApprovalConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyApprovalConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyApprovalConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.approval_config):
            request.approval_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.approval_config, 'ApprovalConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.approval_config_shrink):
            query['ApprovalConfig'] = request.approval_config_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyApprovalConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyApprovalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_approval_config(
        self,
        request: main_models.SetPolicyApprovalConfigRequest,
    ) -> main_models.SetPolicyApprovalConfigResponse:
        runtime = RuntimeOptions()
        return self.set_policy_approval_config_with_options(request, runtime)

    async def set_policy_approval_config_async(
        self,
        request: main_models.SetPolicyApprovalConfigRequest,
    ) -> main_models.SetPolicyApprovalConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_policy_approval_config_with_options_async(request, runtime)

    def set_policy_asset_scope_with_options(
        self,
        request: main_models.SetPolicyAssetScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyAssetScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyAssetScope',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyAssetScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_asset_scope_with_options_async(
        self,
        request: main_models.SetPolicyAssetScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyAssetScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.databases):
            query['Databases'] = request.databases
        if not DaraCore.is_null(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not DaraCore.is_null(request.hosts):
            query['Hosts'] = request.hosts
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyAssetScope',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyAssetScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_asset_scope(
        self,
        request: main_models.SetPolicyAssetScopeRequest,
    ) -> main_models.SetPolicyAssetScopeResponse:
        runtime = RuntimeOptions()
        return self.set_policy_asset_scope_with_options(request, runtime)

    async def set_policy_asset_scope_async(
        self,
        request: main_models.SetPolicyAssetScopeRequest,
    ) -> main_models.SetPolicyAssetScopeResponse:
        runtime = RuntimeOptions()
        return await self.set_policy_asset_scope_with_options_async(request, runtime)

    def set_policy_command_config_with_options(
        self,
        tmp_req: main_models.SetPolicyCommandConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyCommandConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyCommandConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.command_config):
            request.command_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.command_config, 'CommandConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.command_config_shrink):
            query['CommandConfig'] = request.command_config_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyCommandConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyCommandConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_command_config_with_options_async(
        self,
        tmp_req: main_models.SetPolicyCommandConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyCommandConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyCommandConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.command_config):
            request.command_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.command_config, 'CommandConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.command_config_shrink):
            query['CommandConfig'] = request.command_config_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyCommandConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyCommandConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_command_config(
        self,
        request: main_models.SetPolicyCommandConfigRequest,
    ) -> main_models.SetPolicyCommandConfigResponse:
        runtime = RuntimeOptions()
        return self.set_policy_command_config_with_options(request, runtime)

    async def set_policy_command_config_async(
        self,
        request: main_models.SetPolicyCommandConfigRequest,
    ) -> main_models.SetPolicyCommandConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_policy_command_config_with_options_async(request, runtime)

    def set_policy_ipacl_config_with_options(
        self,
        tmp_req: main_models.SetPolicyIPAclConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyIPAclConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyIPAclConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ipacl_config):
            request.ipacl_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ipacl_config, 'IPAclConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.ipacl_config_shrink):
            query['IPAclConfig'] = request.ipacl_config_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyIPAclConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyIPAclConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_ipacl_config_with_options_async(
        self,
        tmp_req: main_models.SetPolicyIPAclConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyIPAclConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyIPAclConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ipacl_config):
            request.ipacl_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.ipacl_config, 'IPAclConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.ipacl_config_shrink):
            query['IPAclConfig'] = request.ipacl_config_shrink
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyIPAclConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyIPAclConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_ipacl_config(
        self,
        request: main_models.SetPolicyIPAclConfigRequest,
    ) -> main_models.SetPolicyIPAclConfigResponse:
        runtime = RuntimeOptions()
        return self.set_policy_ipacl_config_with_options(request, runtime)

    async def set_policy_ipacl_config_async(
        self,
        request: main_models.SetPolicyIPAclConfigRequest,
    ) -> main_models.SetPolicyIPAclConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_policy_ipacl_config_with_options_async(request, runtime)

    def set_policy_protocol_config_with_options(
        self,
        tmp_req: main_models.SetPolicyProtocolConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyProtocolConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyProtocolConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.protocol_config):
            request.protocol_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocol_config, 'ProtocolConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.protocol_config_shrink):
            query['ProtocolConfig'] = request.protocol_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyProtocolConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyProtocolConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_protocol_config_with_options_async(
        self,
        tmp_req: main_models.SetPolicyProtocolConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyProtocolConfigResponse:
        tmp_req.validate()
        request = main_models.SetPolicyProtocolConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.protocol_config):
            request.protocol_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocol_config, 'ProtocolConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.protocol_config_shrink):
            query['ProtocolConfig'] = request.protocol_config_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyProtocolConfig',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyProtocolConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_protocol_config(
        self,
        request: main_models.SetPolicyProtocolConfigRequest,
    ) -> main_models.SetPolicyProtocolConfigResponse:
        runtime = RuntimeOptions()
        return self.set_policy_protocol_config_with_options(request, runtime)

    async def set_policy_protocol_config_async(
        self,
        request: main_models.SetPolicyProtocolConfigRequest,
    ) -> main_models.SetPolicyProtocolConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_policy_protocol_config_with_options_async(request, runtime)

    def set_policy_user_scope_with_options(
        self,
        request: main_models.SetPolicyUserScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyUserScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyUserScope',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyUserScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_user_scope_with_options_async(
        self,
        request: main_models.SetPolicyUserScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPolicyUserScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPolicyUserScope',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPolicyUserScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_user_scope(
        self,
        request: main_models.SetPolicyUserScopeRequest,
    ) -> main_models.SetPolicyUserScopeResponse:
        runtime = RuntimeOptions()
        return self.set_policy_user_scope_with_options(request, runtime)

    async def set_policy_user_scope_async(
        self,
        request: main_models.SetPolicyUserScopeRequest,
    ) -> main_models.SetPolicyUserScopeResponse:
        runtime = RuntimeOptions()
        return await self.set_policy_user_scope_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: main_models.StartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_security_group_ids):
            query['ClientSecurityGroupIds'] = request.client_security_group_ids
        if not DaraCore.is_null(request.enable_portal_private_access):
            query['EnablePortalPrivateAccess'] = request.enable_portal_private_access
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not DaraCore.is_null(request.slave_vswitch_id):
            query['SlaveVswitchId'] = request.slave_vswitch_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: main_models.StartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_security_group_ids):
            query['ClientSecurityGroupIds'] = request.client_security_group_ids
        if not DaraCore.is_null(request.enable_portal_private_access):
            query['EnablePortalPrivateAccess'] = request.enable_portal_private_access
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not DaraCore.is_null(request.slave_vswitch_id):
            query['SlaveVswitchId'] = request.slave_vswitch_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: main_models.StartInstanceRequest,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: main_models.StartInstanceRequest,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unlock_users_with_options(
        self,
        request: main_models.UnlockUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockUsers',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_users_with_options_async(
        self,
        request: main_models.UnlockUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockUsers',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_users(
        self,
        request: main_models.UnlockUsersRequest,
    ) -> main_models.UnlockUsersResponse:
        runtime = RuntimeOptions()
        return self.unlock_users_with_options(request, runtime)

    async def unlock_users_async(
        self,
        request: main_models.UnlockUsersRequest,
    ) -> main_models.UnlockUsersResponse:
        runtime = RuntimeOptions()
        return await self.unlock_users_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def verify_instance_adauth_server_with_options(
        self,
        request: main_models.VerifyInstanceADAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyInstanceADAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server):
            query['Server'] = request.server
        if not DaraCore.is_null(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyInstanceADAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyInstanceADAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_instance_adauth_server_with_options_async(
        self,
        request: main_models.VerifyInstanceADAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyInstanceADAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server):
            query['Server'] = request.server
        if not DaraCore.is_null(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyInstanceADAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyInstanceADAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_instance_adauth_server(
        self,
        request: main_models.VerifyInstanceADAuthServerRequest,
    ) -> main_models.VerifyInstanceADAuthServerResponse:
        runtime = RuntimeOptions()
        return self.verify_instance_adauth_server_with_options(request, runtime)

    async def verify_instance_adauth_server_async(
        self,
        request: main_models.VerifyInstanceADAuthServerRequest,
    ) -> main_models.VerifyInstanceADAuthServerResponse:
        runtime = RuntimeOptions()
        return await self.verify_instance_adauth_server_with_options_async(request, runtime)

    def verify_instance_ldapauth_server_with_options(
        self,
        request: main_models.VerifyInstanceLDAPAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyInstanceLDAPAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server):
            query['Server'] = request.server
        if not DaraCore.is_null(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyInstanceLDAPAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyInstanceLDAPAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_instance_ldapauth_server_with_options_async(
        self,
        request: main_models.VerifyInstanceLDAPAuthServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyInstanceLDAPAuthServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.server):
            query['Server'] = request.server
        if not DaraCore.is_null(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyInstanceLDAPAuthServer',
            version = '2019-12-09',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyInstanceLDAPAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_instance_ldapauth_server(
        self,
        request: main_models.VerifyInstanceLDAPAuthServerRequest,
    ) -> main_models.VerifyInstanceLDAPAuthServerResponse:
        runtime = RuntimeOptions()
        return self.verify_instance_ldapauth_server_with_options(request, runtime)

    async def verify_instance_ldapauth_server_async(
        self,
        request: main_models.VerifyInstanceLDAPAuthServerRequest,
    ) -> main_models.VerifyInstanceLDAPAuthServerResponse:
        runtime = RuntimeOptions()
        return await self.verify_instance_ldapauth_server_with_options_async(request, runtime)
