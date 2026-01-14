# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_quickbi_public20220101 import models as main_models
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
        self._endpoint = self.get_endpoint('quickbi-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_data_level_permission_rule_users_with_options(
        self,
        request: main_models.AddDataLevelPermissionRuleUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataLevelPermissionRuleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_user_model):
            query['AddUserModel'] = request.add_user_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDataLevelPermissionRuleUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataLevelPermissionRuleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_level_permission_rule_users_with_options_async(
        self,
        request: main_models.AddDataLevelPermissionRuleUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataLevelPermissionRuleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_user_model):
            query['AddUserModel'] = request.add_user_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDataLevelPermissionRuleUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataLevelPermissionRuleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_level_permission_rule_users(
        self,
        request: main_models.AddDataLevelPermissionRuleUsersRequest,
    ) -> main_models.AddDataLevelPermissionRuleUsersResponse:
        runtime = RuntimeOptions()
        return self.add_data_level_permission_rule_users_with_options(request, runtime)

    async def add_data_level_permission_rule_users_async(
        self,
        request: main_models.AddDataLevelPermissionRuleUsersRequest,
    ) -> main_models.AddDataLevelPermissionRuleUsersResponse:
        runtime = RuntimeOptions()
        return await self.add_data_level_permission_rule_users_with_options_async(request, runtime)

    def add_data_level_permission_white_list_with_options(
        self,
        request: main_models.AddDataLevelPermissionWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataLevelPermissionWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.target_ids):
            query['TargetIds'] = request.target_ids
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDataLevelPermissionWhiteList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataLevelPermissionWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_level_permission_white_list_with_options_async(
        self,
        request: main_models.AddDataLevelPermissionWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataLevelPermissionWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.target_ids):
            query['TargetIds'] = request.target_ids
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDataLevelPermissionWhiteList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataLevelPermissionWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_level_permission_white_list(
        self,
        request: main_models.AddDataLevelPermissionWhiteListRequest,
    ) -> main_models.AddDataLevelPermissionWhiteListResponse:
        runtime = RuntimeOptions()
        return self.add_data_level_permission_white_list_with_options(request, runtime)

    async def add_data_level_permission_white_list_async(
        self,
        request: main_models.AddDataLevelPermissionWhiteListRequest,
    ) -> main_models.AddDataLevelPermissionWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.add_data_level_permission_white_list_with_options_async(request, runtime)

    def add_data_source_with_options(
        self,
        request: main_models.AddDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_model):
            query['AddModel'] = request.add_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDataSource',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_source_with_options_async(
        self,
        request: main_models.AddDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_model):
            query['AddModel'] = request.add_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDataSource',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_source(
        self,
        request: main_models.AddDataSourceRequest,
    ) -> main_models.AddDataSourceResponse:
        runtime = RuntimeOptions()
        return self.add_data_source_with_options(request, runtime)

    async def add_data_source_async(
        self,
        request: main_models.AddDataSourceRequest,
    ) -> main_models.AddDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.add_data_source_with_options_async(request, runtime)

    def add_share_report_with_options(
        self,
        request: main_models.AddShareReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddShareReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_point):
            query['AuthPoint'] = request.auth_point
        if not DaraCore.is_null(request.expire_date):
            query['ExpireDate'] = request.expire_date
        if not DaraCore.is_null(request.share_to_id):
            query['ShareToId'] = request.share_to_id
        if not DaraCore.is_null(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddShareReport',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddShareReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_share_report_with_options_async(
        self,
        request: main_models.AddShareReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddShareReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_point):
            query['AuthPoint'] = request.auth_point
        if not DaraCore.is_null(request.expire_date):
            query['ExpireDate'] = request.expire_date
        if not DaraCore.is_null(request.share_to_id):
            query['ShareToId'] = request.share_to_id
        if not DaraCore.is_null(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddShareReport',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddShareReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_share_report(
        self,
        request: main_models.AddShareReportRequest,
    ) -> main_models.AddShareReportResponse:
        runtime = RuntimeOptions()
        return self.add_share_report_with_options(request, runtime)

    async def add_share_report_async(
        self,
        request: main_models.AddShareReportRequest,
    ) -> main_models.AddShareReportResponse:
        runtime = RuntimeOptions()
        return await self.add_share_report_with_options_async(request, runtime)

    def add_user_with_options(
        self,
        request: main_models.AddUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not DaraCore.is_null(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        body = {}
        if not DaraCore.is_null(request.role_ids):
            body['RoleIds'] = request.role_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUser',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_with_options_async(
        self,
        request: main_models.AddUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not DaraCore.is_null(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        body = {}
        if not DaraCore.is_null(request.role_ids):
            body['RoleIds'] = request.role_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUser',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user(
        self,
        request: main_models.AddUserRequest,
    ) -> main_models.AddUserResponse:
        runtime = RuntimeOptions()
        return self.add_user_with_options(request, runtime)

    async def add_user_async(
        self,
        request: main_models.AddUserRequest,
    ) -> main_models.AddUserResponse:
        runtime = RuntimeOptions()
        return await self.add_user_with_options_async(request, runtime)

    def add_user_group_member_with_options(
        self,
        request: main_models.AddUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserGroupMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserGroupMember',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_group_member_with_options_async(
        self,
        request: main_models.AddUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserGroupMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserGroupMember',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_group_member(
        self,
        request: main_models.AddUserGroupMemberRequest,
    ) -> main_models.AddUserGroupMemberResponse:
        runtime = RuntimeOptions()
        return self.add_user_group_member_with_options(request, runtime)

    async def add_user_group_member_async(
        self,
        request: main_models.AddUserGroupMemberRequest,
    ) -> main_models.AddUserGroupMemberResponse:
        runtime = RuntimeOptions()
        return await self.add_user_group_member_with_options_async(request, runtime)

    def add_user_group_members_with_options(
        self,
        request: main_models.AddUserGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserGroupMembers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_group_members_with_options_async(
        self,
        request: main_models.AddUserGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserGroupMembers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_group_members(
        self,
        request: main_models.AddUserGroupMembersRequest,
    ) -> main_models.AddUserGroupMembersResponse:
        runtime = RuntimeOptions()
        return self.add_user_group_members_with_options(request, runtime)

    async def add_user_group_members_async(
        self,
        request: main_models.AddUserGroupMembersRequest,
    ) -> main_models.AddUserGroupMembersResponse:
        runtime = RuntimeOptions()
        return await self.add_user_group_members_with_options_async(request, runtime)

    def add_user_tag_meta_with_options(
        self,
        request: main_models.AddUserTagMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserTagMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserTagMeta',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserTagMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_tag_meta_with_options_async(
        self,
        request: main_models.AddUserTagMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserTagMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserTagMeta',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserTagMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_tag_meta(
        self,
        request: main_models.AddUserTagMetaRequest,
    ) -> main_models.AddUserTagMetaResponse:
        runtime = RuntimeOptions()
        return self.add_user_tag_meta_with_options(request, runtime)

    async def add_user_tag_meta_async(
        self,
        request: main_models.AddUserTagMetaRequest,
    ) -> main_models.AddUserTagMetaResponse:
        runtime = RuntimeOptions()
        return await self.add_user_tag_meta_with_options_async(request, runtime)

    def add_user_to_workspace_with_options(
        self,
        request: main_models.AddUserToWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_workspace_with_options_async(
        self,
        request: main_models.AddUserToWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_workspace(
        self,
        request: main_models.AddUserToWorkspaceRequest,
    ) -> main_models.AddUserToWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.add_user_to_workspace_with_options(request, runtime)

    async def add_user_to_workspace_async(
        self,
        request: main_models.AddUserToWorkspaceRequest,
    ) -> main_models.AddUserToWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.add_user_to_workspace_with_options_async(request, runtime)

    def add_workspace_users_with_options(
        self,
        request: main_models.AddWorkspaceUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddWorkspaceUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddWorkspaceUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddWorkspaceUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_workspace_users_with_options_async(
        self,
        request: main_models.AddWorkspaceUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddWorkspaceUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddWorkspaceUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddWorkspaceUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_workspace_users(
        self,
        request: main_models.AddWorkspaceUsersRequest,
    ) -> main_models.AddWorkspaceUsersResponse:
        runtime = RuntimeOptions()
        return self.add_workspace_users_with_options(request, runtime)

    async def add_workspace_users_async(
        self,
        request: main_models.AddWorkspaceUsersRequest,
    ) -> main_models.AddWorkspaceUsersResponse:
        runtime = RuntimeOptions()
        return await self.add_workspace_users_with_options_async(request, runtime)

    def allot_dataset_acceleration_task_with_options(
        self,
        request: main_models.AllotDatasetAccelerationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllotDatasetAccelerationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllotDatasetAccelerationTask',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllotDatasetAccelerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def allot_dataset_acceleration_task_with_options_async(
        self,
        request: main_models.AllotDatasetAccelerationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllotDatasetAccelerationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllotDatasetAccelerationTask',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllotDatasetAccelerationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allot_dataset_acceleration_task(
        self,
        request: main_models.AllotDatasetAccelerationTaskRequest,
    ) -> main_models.AllotDatasetAccelerationTaskResponse:
        runtime = RuntimeOptions()
        return self.allot_dataset_acceleration_task_with_options(request, runtime)

    async def allot_dataset_acceleration_task_async(
        self,
        request: main_models.AllotDatasetAccelerationTaskRequest,
    ) -> main_models.AllotDatasetAccelerationTaskResponse:
        runtime = RuntimeOptions()
        return await self.allot_dataset_acceleration_task_with_options_async(request, runtime)

    def authorize_menu_with_options(
        self,
        request: main_models.AuthorizeMenuRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeMenuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_points_value):
            query['AuthPointsValue'] = request.auth_points_value
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not DaraCore.is_null(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeMenu',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeMenuResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_menu_with_options_async(
        self,
        request: main_models.AuthorizeMenuRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeMenuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_points_value):
            query['AuthPointsValue'] = request.auth_points_value
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not DaraCore.is_null(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeMenu',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeMenuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_menu(
        self,
        request: main_models.AuthorizeMenuRequest,
    ) -> main_models.AuthorizeMenuResponse:
        runtime = RuntimeOptions()
        return self.authorize_menu_with_options(request, runtime)

    async def authorize_menu_async(
        self,
        request: main_models.AuthorizeMenuRequest,
    ) -> main_models.AuthorizeMenuResponse:
        runtime = RuntimeOptions()
        return await self.authorize_menu_with_options_async(request, runtime)

    def batch_add_feishu_users_with_options(
        self,
        request: main_models.BatchAddFeishuUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddFeishuUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feishu_users):
            query['FeishuUsers'] = request.feishu_users
        if not DaraCore.is_null(request.is_admin):
            query['IsAdmin'] = request.is_admin
        if not DaraCore.is_null(request.is_auth_admin):
            query['IsAuthAdmin'] = request.is_auth_admin
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddFeishuUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddFeishuUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_feishu_users_with_options_async(
        self,
        request: main_models.BatchAddFeishuUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddFeishuUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feishu_users):
            query['FeishuUsers'] = request.feishu_users
        if not DaraCore.is_null(request.is_admin):
            query['IsAdmin'] = request.is_admin
        if not DaraCore.is_null(request.is_auth_admin):
            query['IsAuthAdmin'] = request.is_auth_admin
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddFeishuUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddFeishuUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_feishu_users(
        self,
        request: main_models.BatchAddFeishuUsersRequest,
    ) -> main_models.BatchAddFeishuUsersResponse:
        runtime = RuntimeOptions()
        return self.batch_add_feishu_users_with_options(request, runtime)

    async def batch_add_feishu_users_async(
        self,
        request: main_models.BatchAddFeishuUsersRequest,
    ) -> main_models.BatchAddFeishuUsersResponse:
        runtime = RuntimeOptions()
        return await self.batch_add_feishu_users_with_options_async(request, runtime)

    def cancel_authorization_menu_with_options(
        self,
        request: main_models.CancelAuthorizationMenuRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAuthorizationMenuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not DaraCore.is_null(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAuthorizationMenu',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAuthorizationMenuResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_authorization_menu_with_options_async(
        self,
        request: main_models.CancelAuthorizationMenuRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAuthorizationMenuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not DaraCore.is_null(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAuthorizationMenu',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAuthorizationMenuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_authorization_menu(
        self,
        request: main_models.CancelAuthorizationMenuRequest,
    ) -> main_models.CancelAuthorizationMenuResponse:
        runtime = RuntimeOptions()
        return self.cancel_authorization_menu_with_options(request, runtime)

    async def cancel_authorization_menu_async(
        self,
        request: main_models.CancelAuthorizationMenuRequest,
    ) -> main_models.CancelAuthorizationMenuResponse:
        runtime = RuntimeOptions()
        return await self.cancel_authorization_menu_with_options_async(request, runtime)

    def cancel_collection_with_options(
        self,
        request: main_models.CancelCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCollection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_collection_with_options_async(
        self,
        request: main_models.CancelCollectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCollectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCollection',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_collection(
        self,
        request: main_models.CancelCollectionRequest,
    ) -> main_models.CancelCollectionResponse:
        runtime = RuntimeOptions()
        return self.cancel_collection_with_options(request, runtime)

    async def cancel_collection_async(
        self,
        request: main_models.CancelCollectionRequest,
    ) -> main_models.CancelCollectionResponse:
        runtime = RuntimeOptions()
        return await self.cancel_collection_with_options_async(request, runtime)

    def cancel_report_share_with_options(
        self,
        request: main_models.CancelReportShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelReportShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        if not DaraCore.is_null(request.share_to_ids):
            query['ShareToIds'] = request.share_to_ids
        if not DaraCore.is_null(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelReportShare',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelReportShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_report_share_with_options_async(
        self,
        request: main_models.CancelReportShareRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelReportShareResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        if not DaraCore.is_null(request.share_to_ids):
            query['ShareToIds'] = request.share_to_ids
        if not DaraCore.is_null(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelReportShare',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelReportShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_report_share(
        self,
        request: main_models.CancelReportShareRequest,
    ) -> main_models.CancelReportShareResponse:
        runtime = RuntimeOptions()
        return self.cancel_report_share_with_options(request, runtime)

    async def cancel_report_share_async(
        self,
        request: main_models.CancelReportShareRequest,
    ) -> main_models.CancelReportShareResponse:
        runtime = RuntimeOptions()
        return await self.cancel_report_share_with_options_async(request, runtime)

    def change_visibility_model_with_options(
        self,
        request: main_models.ChangeVisibilityModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeVisibilityModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not DaraCore.is_null(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not DaraCore.is_null(request.show_only_with_access):
            query['ShowOnlyWithAccess'] = request.show_only_with_access
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeVisibilityModel',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeVisibilityModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_visibility_model_with_options_async(
        self,
        request: main_models.ChangeVisibilityModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeVisibilityModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not DaraCore.is_null(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not DaraCore.is_null(request.show_only_with_access):
            query['ShowOnlyWithAccess'] = request.show_only_with_access
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeVisibilityModel',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeVisibilityModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_visibility_model(
        self,
        request: main_models.ChangeVisibilityModelRequest,
    ) -> main_models.ChangeVisibilityModelResponse:
        runtime = RuntimeOptions()
        return self.change_visibility_model_with_options(request, runtime)

    async def change_visibility_model_async(
        self,
        request: main_models.ChangeVisibilityModelRequest,
    ) -> main_models.ChangeVisibilityModelResponse:
        runtime = RuntimeOptions()
        return await self.change_visibility_model_with_options_async(request, runtime)

    def check_dataset_existed_with_options(
        self,
        request: main_models.CheckDatasetExistedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDatasetExistedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDatasetExisted',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDatasetExistedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_dataset_existed_with_options_async(
        self,
        request: main_models.CheckDatasetExistedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDatasetExistedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDatasetExisted',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDatasetExistedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_dataset_existed(
        self,
        request: main_models.CheckDatasetExistedRequest,
    ) -> main_models.CheckDatasetExistedResponse:
        runtime = RuntimeOptions()
        return self.check_dataset_existed_with_options(request, runtime)

    async def check_dataset_existed_async(
        self,
        request: main_models.CheckDatasetExistedRequest,
    ) -> main_models.CheckDatasetExistedResponse:
        runtime = RuntimeOptions()
        return await self.check_dataset_existed_with_options_async(request, runtime)

    def check_organization_member_with_options(
        self,
        request: main_models.CheckOrganizationMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckOrganizationMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckOrganizationMember',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckOrganizationMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_organization_member_with_options_async(
        self,
        request: main_models.CheckOrganizationMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckOrganizationMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckOrganizationMember',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckOrganizationMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_organization_member(
        self,
        request: main_models.CheckOrganizationMemberRequest,
    ) -> main_models.CheckOrganizationMemberResponse:
        runtime = RuntimeOptions()
        return self.check_organization_member_with_options(request, runtime)

    async def check_organization_member_async(
        self,
        request: main_models.CheckOrganizationMemberRequest,
    ) -> main_models.CheckOrganizationMemberResponse:
        runtime = RuntimeOptions()
        return await self.check_organization_member_with_options_async(request, runtime)

    def check_readable_with_options(
        self,
        request: main_models.CheckReadableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckReadableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckReadable',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckReadableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_readable_with_options_async(
        self,
        request: main_models.CheckReadableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckReadableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckReadable',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckReadableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_readable(
        self,
        request: main_models.CheckReadableRequest,
    ) -> main_models.CheckReadableResponse:
        runtime = RuntimeOptions()
        return self.check_readable_with_options(request, runtime)

    async def check_readable_async(
        self,
        request: main_models.CheckReadableRequest,
    ) -> main_models.CheckReadableResponse:
        runtime = RuntimeOptions()
        return await self.check_readable_with_options_async(request, runtime)

    def create_cube_by_sql_with_options(
        self,
        request: main_models.CreateCubeBySqlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCubeBySqlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caption):
            query['Caption'] = request.caption
        if not DaraCore.is_null(request.custom_sql):
            query['CustomSql'] = request.custom_sql
        if not DaraCore.is_null(request.ds_id):
            query['DsId'] = request.ds_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCubeBySql',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCubeBySqlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cube_by_sql_with_options_async(
        self,
        request: main_models.CreateCubeBySqlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCubeBySqlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caption):
            query['Caption'] = request.caption
        if not DaraCore.is_null(request.custom_sql):
            query['CustomSql'] = request.custom_sql
        if not DaraCore.is_null(request.ds_id):
            query['DsId'] = request.ds_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCubeBySql',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCubeBySqlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cube_by_sql(
        self,
        request: main_models.CreateCubeBySqlRequest,
    ) -> main_models.CreateCubeBySqlResponse:
        runtime = RuntimeOptions()
        return self.create_cube_by_sql_with_options(request, runtime)

    async def create_cube_by_sql_async(
        self,
        request: main_models.CreateCubeBySqlRequest,
    ) -> main_models.CreateCubeBySqlResponse:
        runtime = RuntimeOptions()
        return await self.create_cube_by_sql_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        request: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ds_id):
            query['DsId'] = request.ds_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.target_directory_id):
            query['TargetDirectoryId'] = request.target_directory_id
        if not DaraCore.is_null(request.user_define_cube_name):
            query['UserDefineCubeName'] = request.user_define_cube_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        request: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ds_id):
            query['DsId'] = request.ds_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.target_directory_id):
            query['TargetDirectoryId'] = request.target_directory_id
        if not DaraCore.is_null(request.user_define_cube_name):
            query['UserDefineCubeName'] = request.user_define_cube_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_ticket_with_options(
        self,
        request: main_models.CreateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.cmpt_id):
            query['CmptId'] = request.cmpt_id
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.global_param):
            query['GlobalParam'] = request.global_param
        if not DaraCore.is_null(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.watermark_param):
            query['WatermarkParam'] = request.watermark_param
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: main_models.CreateTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.cmpt_id):
            query['CmptId'] = request.cmpt_id
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.global_param):
            query['GlobalParam'] = request.global_param
        if not DaraCore.is_null(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.watermark_param):
            query['WatermarkParam'] = request.watermark_param
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ticket(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        return self.create_ticket_with_options(request, runtime)

    async def create_ticket_async(
        self,
        request: main_models.CreateTicketRequest,
    ) -> main_models.CreateTicketResponse:
        runtime = RuntimeOptions()
        return await self.create_ticket_with_options_async(request, runtime)

    def create_ticket_4copilot_with_options(
        self,
        request: main_models.CreateTicket4CopilotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicket4CopilotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.copilot_id):
            query['CopilotId'] = request.copilot_id
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket4Copilot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicket4CopilotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ticket_4copilot_with_options_async(
        self,
        request: main_models.CreateTicket4CopilotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTicket4CopilotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.copilot_id):
            query['CopilotId'] = request.copilot_id
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTicket4Copilot',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTicket4CopilotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ticket_4copilot(
        self,
        request: main_models.CreateTicket4CopilotRequest,
    ) -> main_models.CreateTicket4CopilotResponse:
        runtime = RuntimeOptions()
        return self.create_ticket_4copilot_with_options(request, runtime)

    async def create_ticket_4copilot_async(
        self,
        request: main_models.CreateTicket4CopilotRequest,
    ) -> main_models.CreateTicket4CopilotResponse:
        runtime = RuntimeOptions()
        return await self.create_ticket_4copilot_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: main_models.CreateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        if not DaraCore.is_null(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroup',
            version = '2022-01-01',
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
        if not DaraCore.is_null(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        if not DaraCore.is_null(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroup',
            version = '2022-01-01',
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

    def create_workspace_with_options(
        self,
        request: main_models.CreateWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_publish):
            query['AllowPublish'] = request.allow_publish
        if not DaraCore.is_null(request.allow_share):
            query['AllowShare'] = request.allow_share
        if not DaraCore.is_null(request.allow_view_all):
            query['AllowViewAll'] = request.allow_view_all
        if not DaraCore.is_null(request.default_share_to_all):
            query['DefaultShareToAll'] = request.default_share_to_all
        if not DaraCore.is_null(request.only_admin_create_datasource):
            query['OnlyAdminCreateDatasource'] = request.only_admin_create_datasource
        if not DaraCore.is_null(request.use_comment):
            query['UseComment'] = request.use_comment
        if not DaraCore.is_null(request.workspace_description):
            query['WorkspaceDescription'] = request.workspace_description
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: main_models.CreateWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_publish):
            query['AllowPublish'] = request.allow_publish
        if not DaraCore.is_null(request.allow_share):
            query['AllowShare'] = request.allow_share
        if not DaraCore.is_null(request.allow_view_all):
            query['AllowViewAll'] = request.allow_view_all
        if not DaraCore.is_null(request.default_share_to_all):
            query['DefaultShareToAll'] = request.default_share_to_all
        if not DaraCore.is_null(request.only_admin_create_datasource):
            query['OnlyAdminCreateDatasource'] = request.only_admin_create_datasource
        if not DaraCore.is_null(request.use_comment):
            query['UseComment'] = request.use_comment
        if not DaraCore.is_null(request.workspace_description):
            query['WorkspaceDescription'] = request.workspace_description
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.create_workspace_with_options(request, runtime)

    async def create_workspace_async(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.create_workspace_with_options_async(request, runtime)

    def data_interpretation_with_options(
        self,
        request: main_models.DataInterpretationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DataInterpretationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.model_code):
            query['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.prompt_force_override):
            query['PromptForceOverride'] = request.prompt_force_override
        if not DaraCore.is_null(request.user_prompt):
            query['UserPrompt'] = request.user_prompt
        if not DaraCore.is_null(request.user_question):
            query['UserQuestion'] = request.user_question
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DataInterpretation',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DataInterpretationResponse(),
            self.call_api(params, req, runtime)
        )

    async def data_interpretation_with_options_async(
        self,
        request: main_models.DataInterpretationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DataInterpretationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.model_code):
            query['ModelCode'] = request.model_code
        if not DaraCore.is_null(request.prompt_force_override):
            query['PromptForceOverride'] = request.prompt_force_override
        if not DaraCore.is_null(request.user_prompt):
            query['UserPrompt'] = request.user_prompt
        if not DaraCore.is_null(request.user_question):
            query['UserQuestion'] = request.user_question
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DataInterpretation',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DataInterpretationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def data_interpretation(
        self,
        request: main_models.DataInterpretationRequest,
    ) -> main_models.DataInterpretationResponse:
        runtime = RuntimeOptions()
        return self.data_interpretation_with_options(request, runtime)

    async def data_interpretation_async(
        self,
        request: main_models.DataInterpretationRequest,
    ) -> main_models.DataInterpretationResponse:
        runtime = RuntimeOptions()
        return await self.data_interpretation_with_options_async(request, runtime)

    def data_set_blood_with_options(
        self,
        request: main_models.DataSetBloodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DataSetBloodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_set_ids):
            query['DataSetIds'] = request.data_set_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.works_type):
            query['WorksType'] = request.works_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DataSetBlood',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DataSetBloodResponse(),
            self.call_api(params, req, runtime)
        )

    async def data_set_blood_with_options_async(
        self,
        request: main_models.DataSetBloodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DataSetBloodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_set_ids):
            query['DataSetIds'] = request.data_set_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.works_type):
            query['WorksType'] = request.works_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DataSetBlood',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DataSetBloodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def data_set_blood(
        self,
        request: main_models.DataSetBloodRequest,
    ) -> main_models.DataSetBloodResponse:
        runtime = RuntimeOptions()
        return self.data_set_blood_with_options(request, runtime)

    async def data_set_blood_async(
        self,
        request: main_models.DataSetBloodRequest,
    ) -> main_models.DataSetBloodResponse:
        runtime = RuntimeOptions()
        return await self.data_set_blood_with_options_async(request, runtime)

    def data_source_blood_with_options(
        self,
        request: main_models.DataSourceBloodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DataSourceBloodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DataSourceBlood',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DataSourceBloodResponse(),
            self.call_api(params, req, runtime)
        )

    async def data_source_blood_with_options_async(
        self,
        request: main_models.DataSourceBloodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DataSourceBloodResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DataSourceBlood',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DataSourceBloodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def data_source_blood(
        self,
        request: main_models.DataSourceBloodRequest,
    ) -> main_models.DataSourceBloodResponse:
        runtime = RuntimeOptions()
        return self.data_source_blood_with_options(request, runtime)

    async def data_source_blood_async(
        self,
        request: main_models.DataSourceBloodRequest,
    ) -> main_models.DataSourceBloodResponse:
        runtime = RuntimeOptions()
        return await self.data_source_blood_with_options_async(request, runtime)

    def delay_ticket_expire_time_with_options(
        self,
        request: main_models.DelayTicketExpireTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelayTicketExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DelayTicketExpireTime',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelayTicketExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delay_ticket_expire_time_with_options_async(
        self,
        request: main_models.DelayTicketExpireTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelayTicketExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DelayTicketExpireTime',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelayTicketExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delay_ticket_expire_time(
        self,
        request: main_models.DelayTicketExpireTimeRequest,
    ) -> main_models.DelayTicketExpireTimeResponse:
        runtime = RuntimeOptions()
        return self.delay_ticket_expire_time_with_options(request, runtime)

    async def delay_ticket_expire_time_async(
        self,
        request: main_models.DelayTicketExpireTimeRequest,
    ) -> main_models.DelayTicketExpireTimeResponse:
        runtime = RuntimeOptions()
        return await self.delay_ticket_expire_time_with_options_async(request, runtime)

    def delete_data_level_permission_rule_users_with_options(
        self,
        request: main_models.DeleteDataLevelPermissionRuleUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLevelPermissionRuleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_user_model):
            query['DeleteUserModel'] = request.delete_user_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLevelPermissionRuleUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLevelPermissionRuleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_level_permission_rule_users_with_options_async(
        self,
        request: main_models.DeleteDataLevelPermissionRuleUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLevelPermissionRuleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_user_model):
            query['DeleteUserModel'] = request.delete_user_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLevelPermissionRuleUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLevelPermissionRuleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_level_permission_rule_users(
        self,
        request: main_models.DeleteDataLevelPermissionRuleUsersRequest,
    ) -> main_models.DeleteDataLevelPermissionRuleUsersResponse:
        runtime = RuntimeOptions()
        return self.delete_data_level_permission_rule_users_with_options(request, runtime)

    async def delete_data_level_permission_rule_users_async(
        self,
        request: main_models.DeleteDataLevelPermissionRuleUsersRequest,
    ) -> main_models.DeleteDataLevelPermissionRuleUsersResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_level_permission_rule_users_with_options_async(request, runtime)

    def delete_data_level_rule_config_with_options(
        self,
        request: main_models.DeleteDataLevelRuleConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLevelRuleConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLevelRuleConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLevelRuleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_level_rule_config_with_options_async(
        self,
        request: main_models.DeleteDataLevelRuleConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLevelRuleConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLevelRuleConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLevelRuleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_level_rule_config(
        self,
        request: main_models.DeleteDataLevelRuleConfigRequest,
    ) -> main_models.DeleteDataLevelRuleConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_data_level_rule_config_with_options(request, runtime)

    async def delete_data_level_rule_config_async(
        self,
        request: main_models.DeleteDataLevelRuleConfigRequest,
    ) -> main_models.DeleteDataLevelRuleConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_level_rule_config_with_options_async(request, runtime)

    def delete_ticket_with_options(
        self,
        request: main_models.DeleteTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTicket',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ticket_with_options_async(
        self,
        request: main_models.DeleteTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTicket',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ticket(
        self,
        request: main_models.DeleteTicketRequest,
    ) -> main_models.DeleteTicketResponse:
        runtime = RuntimeOptions()
        return self.delete_ticket_with_options(request, runtime)

    async def delete_ticket_async(
        self,
        request: main_models.DeleteTicketRequest,
    ) -> main_models.DeleteTicketResponse:
        runtime = RuntimeOptions()
        return await self.delete_ticket_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.transfer_user_id):
            query['TransferUserId'] = request.transfer_user_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2022-01-01',
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
        if not DaraCore.is_null(request.transfer_user_id):
            query['TransferUserId'] = request.transfer_user_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2022-01-01',
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

    def delete_user_from_workspace_with_options(
        self,
        request: main_models.DeleteUserFromWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserFromWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserFromWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserFromWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_from_workspace_with_options_async(
        self,
        request: main_models.DeleteUserFromWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserFromWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserFromWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserFromWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_from_workspace(
        self,
        request: main_models.DeleteUserFromWorkspaceRequest,
    ) -> main_models.DeleteUserFromWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.delete_user_from_workspace_with_options(request, runtime)

    async def delete_user_from_workspace_async(
        self,
        request: main_models.DeleteUserFromWorkspaceRequest,
    ) -> main_models.DeleteUserFromWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_from_workspace_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: main_models.DeleteUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroup',
            version = '2022-01-01',
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
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroup',
            version = '2022-01-01',
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

    def delete_user_group_member_with_options(
        self,
        request: main_models.DeleteUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroupMember',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_member_with_options_async(
        self,
        request: main_models.DeleteUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroupMember',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group_member(
        self,
        request: main_models.DeleteUserGroupMemberRequest,
    ) -> main_models.DeleteUserGroupMemberResponse:
        runtime = RuntimeOptions()
        return self.delete_user_group_member_with_options(request, runtime)

    async def delete_user_group_member_async(
        self,
        request: main_models.DeleteUserGroupMemberRequest,
    ) -> main_models.DeleteUserGroupMemberResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_group_member_with_options_async(request, runtime)

    def delete_user_group_members_with_options(
        self,
        request: main_models.DeleteUserGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroupMembers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_members_with_options_async(
        self,
        request: main_models.DeleteUserGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroupMembers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group_members(
        self,
        request: main_models.DeleteUserGroupMembersRequest,
    ) -> main_models.DeleteUserGroupMembersResponse:
        runtime = RuntimeOptions()
        return self.delete_user_group_members_with_options(request, runtime)

    async def delete_user_group_members_async(
        self,
        request: main_models.DeleteUserGroupMembersRequest,
    ) -> main_models.DeleteUserGroupMembersResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_group_members_with_options_async(request, runtime)

    def delete_user_tag_meta_with_options(
        self,
        request: main_models.DeleteUserTagMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserTagMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserTagMeta',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserTagMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_tag_meta_with_options_async(
        self,
        request: main_models.DeleteUserTagMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserTagMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserTagMeta',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserTagMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_tag_meta(
        self,
        request: main_models.DeleteUserTagMetaRequest,
    ) -> main_models.DeleteUserTagMetaResponse:
        runtime = RuntimeOptions()
        return self.delete_user_tag_meta_with_options(request, runtime)

    async def delete_user_tag_meta_async(
        self,
        request: main_models.DeleteUserTagMetaRequest,
    ) -> main_models.DeleteUserTagMetaResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_tag_meta_with_options_async(request, runtime)

    def get_data_source_connection_info_with_options(
        self,
        request: main_models.GetDataSourceConnectionInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataSourceConnectionInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ds_id):
            query['DsId'] = request.ds_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataSourceConnectionInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataSourceConnectionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_connection_info_with_options_async(
        self,
        request: main_models.GetDataSourceConnectionInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataSourceConnectionInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ds_id):
            query['DsId'] = request.ds_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataSourceConnectionInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataSourceConnectionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source_connection_info(
        self,
        request: main_models.GetDataSourceConnectionInfoRequest,
    ) -> main_models.GetDataSourceConnectionInfoResponse:
        runtime = RuntimeOptions()
        return self.get_data_source_connection_info_with_options(request, runtime)

    async def get_data_source_connection_info_async(
        self,
        request: main_models.GetDataSourceConnectionInfoRequest,
    ) -> main_models.GetDataSourceConnectionInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_data_source_connection_info_with_options_async(request, runtime)

    def get_mail_task_list_with_options(
        self,
        request: main_models.GetMailTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMailTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.paused):
            query['Paused'] = request.paused
        if not DaraCore.is_null(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMailTaskList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMailTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mail_task_list_with_options_async(
        self,
        request: main_models.GetMailTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMailTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.paused):
            query['Paused'] = request.paused
        if not DaraCore.is_null(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMailTaskList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMailTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mail_task_list(
        self,
        request: main_models.GetMailTaskListRequest,
    ) -> main_models.GetMailTaskListResponse:
        runtime = RuntimeOptions()
        return self.get_mail_task_list_with_options(request, runtime)

    async def get_mail_task_list_async(
        self,
        request: main_models.GetMailTaskListRequest,
    ) -> main_models.GetMailTaskListResponse:
        runtime = RuntimeOptions()
        return await self.get_mail_task_list_with_options_async(request, runtime)

    def get_mail_task_status_with_options(
        self,
        request: main_models.GetMailTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMailTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mail_id):
            query['MailId'] = request.mail_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMailTaskStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMailTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mail_task_status_with_options_async(
        self,
        request: main_models.GetMailTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMailTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mail_id):
            query['MailId'] = request.mail_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMailTaskStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMailTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mail_task_status(
        self,
        request: main_models.GetMailTaskStatusRequest,
    ) -> main_models.GetMailTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.get_mail_task_status_with_options(request, runtime)

    async def get_mail_task_status_async(
        self,
        request: main_models.GetMailTaskStatusRequest,
    ) -> main_models.GetMailTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_mail_task_status_with_options_async(request, runtime)

    def get_user_group_info_with_options(
        self,
        request: main_models.GetUserGroupInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserGroupInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserGroupInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_group_info_with_options_async(
        self,
        request: main_models.GetUserGroupInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserGroupInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserGroupInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserGroupInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_group_info(
        self,
        request: main_models.GetUserGroupInfoRequest,
    ) -> main_models.GetUserGroupInfoResponse:
        runtime = RuntimeOptions()
        return self.get_user_group_info_with_options(request, runtime)

    async def get_user_group_info_async(
        self,
        request: main_models.GetUserGroupInfoRequest,
    ) -> main_models.GetUserGroupInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_user_group_info_with_options_async(request, runtime)

    def get_works_embed_list_with_options(
        self,
        request: main_models.GetWorksEmbedListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorksEmbedListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.works_type):
            query['WorksType'] = request.works_type
        if not DaraCore.is_null(request.ws_id):
            query['WsId'] = request.ws_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorksEmbedList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorksEmbedListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_works_embed_list_with_options_async(
        self,
        request: main_models.GetWorksEmbedListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorksEmbedListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.works_type):
            query['WorksType'] = request.works_type
        if not DaraCore.is_null(request.ws_id):
            query['WsId'] = request.ws_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorksEmbedList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorksEmbedListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_works_embed_list(
        self,
        request: main_models.GetWorksEmbedListRequest,
    ) -> main_models.GetWorksEmbedListResponse:
        runtime = RuntimeOptions()
        return self.get_works_embed_list_with_options(request, runtime)

    async def get_works_embed_list_async(
        self,
        request: main_models.GetWorksEmbedListRequest,
    ) -> main_models.GetWorksEmbedListResponse:
        runtime = RuntimeOptions()
        return await self.get_works_embed_list_with_options_async(request, runtime)

    def list_acceleration_of_workspace_with_options(
        self,
        request: main_models.ListAccelerationOfWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccelerationOfWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.cube_name):
            query['CubeName'] = request.cube_name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccelerationOfWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccelerationOfWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acceleration_of_workspace_with_options_async(
        self,
        request: main_models.ListAccelerationOfWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccelerationOfWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.cube_name):
            query['CubeName'] = request.cube_name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccelerationOfWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccelerationOfWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acceleration_of_workspace(
        self,
        request: main_models.ListAccelerationOfWorkspaceRequest,
    ) -> main_models.ListAccelerationOfWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.list_acceleration_of_workspace_with_options(request, runtime)

    async def list_acceleration_of_workspace_async(
        self,
        request: main_models.ListAccelerationOfWorkspaceRequest,
    ) -> main_models.ListAccelerationOfWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.list_acceleration_of_workspace_with_options_async(request, runtime)

    def list_api_datasource_with_options(
        self,
        request: main_models.ListApiDatasourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiDatasourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiDatasource',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_datasource_with_options_async(
        self,
        request: main_models.ListApiDatasourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiDatasourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiDatasource',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_datasource(
        self,
        request: main_models.ListApiDatasourceRequest,
    ) -> main_models.ListApiDatasourceResponse:
        runtime = RuntimeOptions()
        return self.list_api_datasource_with_options(request, runtime)

    async def list_api_datasource_async(
        self,
        request: main_models.ListApiDatasourceRequest,
    ) -> main_models.ListApiDatasourceResponse:
        runtime = RuntimeOptions()
        return await self.list_api_datasource_with_options_async(request, runtime)

    def list_by_user_group_id_with_options(
        self,
        request: main_models.ListByUserGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListByUserGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListByUserGroupId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListByUserGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_by_user_group_id_with_options_async(
        self,
        request: main_models.ListByUserGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListByUserGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListByUserGroupId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListByUserGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_by_user_group_id(
        self,
        request: main_models.ListByUserGroupIdRequest,
    ) -> main_models.ListByUserGroupIdResponse:
        runtime = RuntimeOptions()
        return self.list_by_user_group_id_with_options(request, runtime)

    async def list_by_user_group_id_async(
        self,
        request: main_models.ListByUserGroupIdRequest,
    ) -> main_models.ListByUserGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.list_by_user_group_id_with_options_async(request, runtime)

    def list_collections_with_options(
        self,
        request: main_models.ListCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCollections',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_collections_with_options_async(
        self,
        request: main_models.ListCollectionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCollectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCollections',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_collections(
        self,
        request: main_models.ListCollectionsRequest,
    ) -> main_models.ListCollectionsResponse:
        runtime = RuntimeOptions()
        return self.list_collections_with_options(request, runtime)

    async def list_collections_async(
        self,
        request: main_models.ListCollectionsRequest,
    ) -> main_models.ListCollectionsResponse:
        runtime = RuntimeOptions()
        return await self.list_collections_with_options_async(request, runtime)

    def list_cube_data_level_permission_config_with_options(
        self,
        request: main_models.ListCubeDataLevelPermissionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCubeDataLevelPermissionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCubeDataLevelPermissionConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCubeDataLevelPermissionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cube_data_level_permission_config_with_options_async(
        self,
        request: main_models.ListCubeDataLevelPermissionConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCubeDataLevelPermissionConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCubeDataLevelPermissionConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCubeDataLevelPermissionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cube_data_level_permission_config(
        self,
        request: main_models.ListCubeDataLevelPermissionConfigRequest,
    ) -> main_models.ListCubeDataLevelPermissionConfigResponse:
        runtime = RuntimeOptions()
        return self.list_cube_data_level_permission_config_with_options(request, runtime)

    async def list_cube_data_level_permission_config_async(
        self,
        request: main_models.ListCubeDataLevelPermissionConfigRequest,
    ) -> main_models.ListCubeDataLevelPermissionConfigResponse:
        runtime = RuntimeOptions()
        return await self.list_cube_data_level_permission_config_with_options_async(request, runtime)

    def list_data_level_permission_white_list_with_options(
        self,
        request: main_models.ListDataLevelPermissionWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLevelPermissionWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLevelPermissionWhiteList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLevelPermissionWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_level_permission_white_list_with_options_async(
        self,
        request: main_models.ListDataLevelPermissionWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLevelPermissionWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLevelPermissionWhiteList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLevelPermissionWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_level_permission_white_list(
        self,
        request: main_models.ListDataLevelPermissionWhiteListRequest,
    ) -> main_models.ListDataLevelPermissionWhiteListResponse:
        runtime = RuntimeOptions()
        return self.list_data_level_permission_white_list_with_options(request, runtime)

    async def list_data_level_permission_white_list_async(
        self,
        request: main_models.ListDataLevelPermissionWhiteListRequest,
    ) -> main_models.ListDataLevelPermissionWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.list_data_level_permission_white_list_with_options_async(request, runtime)

    def list_data_source_with_options(
        self,
        request: main_models.ListDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ds_type):
            query['DsType'] = request.ds_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSource',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_with_options_async(
        self,
        request: main_models.ListDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ds_type):
            query['DsType'] = request.ds_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSource',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source(
        self,
        request: main_models.ListDataSourceRequest,
    ) -> main_models.ListDataSourceResponse:
        runtime = RuntimeOptions()
        return self.list_data_source_with_options(request, runtime)

    async def list_data_source_async(
        self,
        request: main_models.ListDataSourceRequest,
    ) -> main_models.ListDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.list_data_source_with_options_async(request, runtime)

    def list_favorite_reports_with_options(
        self,
        request: main_models.ListFavoriteReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFavoriteReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tree_type):
            query['TreeType'] = request.tree_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFavoriteReports',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFavoriteReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_favorite_reports_with_options_async(
        self,
        request: main_models.ListFavoriteReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFavoriteReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tree_type):
            query['TreeType'] = request.tree_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFavoriteReports',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFavoriteReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_favorite_reports(
        self,
        request: main_models.ListFavoriteReportsRequest,
    ) -> main_models.ListFavoriteReportsResponse:
        runtime = RuntimeOptions()
        return self.list_favorite_reports_with_options(request, runtime)

    async def list_favorite_reports_async(
        self,
        request: main_models.ListFavoriteReportsRequest,
    ) -> main_models.ListFavoriteReportsResponse:
        runtime = RuntimeOptions()
        return await self.list_favorite_reports_with_options_async(request, runtime)

    def list_organization_role_users_with_options(
        self,
        request: main_models.ListOrganizationRoleUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationRoleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationRoleUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organization_role_users_with_options_async(
        self,
        request: main_models.ListOrganizationRoleUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationRoleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationRoleUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organization_role_users(
        self,
        request: main_models.ListOrganizationRoleUsersRequest,
    ) -> main_models.ListOrganizationRoleUsersResponse:
        runtime = RuntimeOptions()
        return self.list_organization_role_users_with_options(request, runtime)

    async def list_organization_role_users_async(
        self,
        request: main_models.ListOrganizationRoleUsersRequest,
    ) -> main_models.ListOrganizationRoleUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_organization_role_users_with_options_async(request, runtime)

    def list_organization_roles_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationRolesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListOrganizationRoles',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organization_roles_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationRolesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListOrganizationRoles',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organization_roles(self) -> main_models.ListOrganizationRolesResponse:
        runtime = RuntimeOptions()
        return self.list_organization_roles_with_options(runtime)

    async def list_organization_roles_async(self) -> main_models.ListOrganizationRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_organization_roles_with_options_async(runtime)

    def list_portal_menu_authorization_with_options(
        self,
        request: main_models.ListPortalMenuAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPortalMenuAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPortalMenuAuthorization',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPortalMenuAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_portal_menu_authorization_with_options_async(
        self,
        request: main_models.ListPortalMenuAuthorizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPortalMenuAuthorizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPortalMenuAuthorization',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPortalMenuAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_portal_menu_authorization(
        self,
        request: main_models.ListPortalMenuAuthorizationRequest,
    ) -> main_models.ListPortalMenuAuthorizationResponse:
        runtime = RuntimeOptions()
        return self.list_portal_menu_authorization_with_options(request, runtime)

    async def list_portal_menu_authorization_async(
        self,
        request: main_models.ListPortalMenuAuthorizationRequest,
    ) -> main_models.ListPortalMenuAuthorizationResponse:
        runtime = RuntimeOptions()
        return await self.list_portal_menu_authorization_with_options_async(request, runtime)

    def list_portal_menus_with_options(
        self,
        request: main_models.ListPortalMenusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPortalMenusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPortalMenus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPortalMenusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_portal_menus_with_options_async(
        self,
        request: main_models.ListPortalMenusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPortalMenusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPortalMenus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPortalMenusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_portal_menus(
        self,
        request: main_models.ListPortalMenusRequest,
    ) -> main_models.ListPortalMenusResponse:
        runtime = RuntimeOptions()
        return self.list_portal_menus_with_options(request, runtime)

    async def list_portal_menus_async(
        self,
        request: main_models.ListPortalMenusRequest,
    ) -> main_models.ListPortalMenusResponse:
        runtime = RuntimeOptions()
        return await self.list_portal_menus_with_options_async(request, runtime)

    def list_recent_view_reports_with_options(
        self,
        request: main_models.ListRecentViewReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentViewReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.offset_day):
            query['OffsetDay'] = request.offset_day
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not DaraCore.is_null(request.tree_type):
            query['TreeType'] = request.tree_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecentViewReports',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentViewReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recent_view_reports_with_options_async(
        self,
        request: main_models.ListRecentViewReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentViewReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.offset_day):
            query['OffsetDay'] = request.offset_day
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not DaraCore.is_null(request.tree_type):
            query['TreeType'] = request.tree_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecentViewReports',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentViewReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recent_view_reports(
        self,
        request: main_models.ListRecentViewReportsRequest,
    ) -> main_models.ListRecentViewReportsResponse:
        runtime = RuntimeOptions()
        return self.list_recent_view_reports_with_options(request, runtime)

    async def list_recent_view_reports_async(
        self,
        request: main_models.ListRecentViewReportsRequest,
    ) -> main_models.ListRecentViewReportsResponse:
        runtime = RuntimeOptions()
        return await self.list_recent_view_reports_with_options_async(request, runtime)

    def list_shared_reports_with_options(
        self,
        request: main_models.ListSharedReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSharedReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tree_type):
            query['TreeType'] = request.tree_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSharedReports',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSharedReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_reports_with_options_async(
        self,
        request: main_models.ListSharedReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSharedReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tree_type):
            query['TreeType'] = request.tree_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSharedReports',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSharedReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_reports(
        self,
        request: main_models.ListSharedReportsRequest,
    ) -> main_models.ListSharedReportsResponse:
        runtime = RuntimeOptions()
        return self.list_shared_reports_with_options(request, runtime)

    async def list_shared_reports_async(
        self,
        request: main_models.ListSharedReportsRequest,
    ) -> main_models.ListSharedReportsResponse:
        runtime = RuntimeOptions()
        return await self.list_shared_reports_with_options_async(request, runtime)

    def list_user_groups_by_user_id_with_options(
        self,
        request: main_models.ListUserGroupsByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupsByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_by_user_id_with_options_async(
        self,
        request: main_models.ListUserGroupsByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupsByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups_by_user_id(
        self,
        request: main_models.ListUserGroupsByUserIdRequest,
    ) -> main_models.ListUserGroupsByUserIdResponse:
        runtime = RuntimeOptions()
        return self.list_user_groups_by_user_id_with_options(request, runtime)

    async def list_user_groups_by_user_id_async(
        self,
        request: main_models.ListUserGroupsByUserIdRequest,
    ) -> main_models.ListUserGroupsByUserIdResponse:
        runtime = RuntimeOptions()
        return await self.list_user_groups_by_user_id_with_options_async(request, runtime)

    def list_white_portal_menu_with_options(
        self,
        request: main_models.ListWhitePortalMenuRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWhitePortalMenuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataportal_id):
            query['DataportalId'] = request.dataportal_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWhitePortalMenu',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWhitePortalMenuResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_white_portal_menu_with_options_async(
        self,
        request: main_models.ListWhitePortalMenuRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWhitePortalMenuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataportal_id):
            query['DataportalId'] = request.dataportal_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWhitePortalMenu',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWhitePortalMenuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_white_portal_menu(
        self,
        request: main_models.ListWhitePortalMenuRequest,
    ) -> main_models.ListWhitePortalMenuResponse:
        runtime = RuntimeOptions()
        return self.list_white_portal_menu_with_options(request, runtime)

    async def list_white_portal_menu_async(
        self,
        request: main_models.ListWhitePortalMenuRequest,
    ) -> main_models.ListWhitePortalMenuResponse:
        runtime = RuntimeOptions()
        return await self.list_white_portal_menu_with_options_async(request, runtime)

    def list_workspace_role_users_with_options(
        self,
        request: main_models.ListWorkspaceRoleUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceRoleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceRoleUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_role_users_with_options_async(
        self,
        request: main_models.ListWorkspaceRoleUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceRoleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceRoleUsers',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_role_users(
        self,
        request: main_models.ListWorkspaceRoleUsersRequest,
    ) -> main_models.ListWorkspaceRoleUsersResponse:
        runtime = RuntimeOptions()
        return self.list_workspace_role_users_with_options(request, runtime)

    async def list_workspace_role_users_async(
        self,
        request: main_models.ListWorkspaceRoleUsersRequest,
    ) -> main_models.ListWorkspaceRoleUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_workspace_role_users_with_options_async(request, runtime)

    def list_workspace_roles_with_options(
        self,
        request: main_models.ListWorkspaceRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceRoles',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_roles_with_options_async(
        self,
        request: main_models.ListWorkspaceRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceRoles',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_roles(
        self,
        request: main_models.ListWorkspaceRolesRequest,
    ) -> main_models.ListWorkspaceRolesResponse:
        runtime = RuntimeOptions()
        return self.list_workspace_roles_with_options(request, runtime)

    async def list_workspace_roles_async(
        self,
        request: main_models.ListWorkspaceRolesRequest,
    ) -> main_models.ListWorkspaceRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_workspace_roles_with_options_async(request, runtime)

    def list_workspace_user_roles_by_user_id_with_options(
        self,
        request: main_models.ListWorkspaceUserRolesByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceUserRolesByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceUserRolesByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceUserRolesByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_user_roles_by_user_id_with_options_async(
        self,
        request: main_models.ListWorkspaceUserRolesByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceUserRolesByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceUserRolesByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceUserRolesByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_user_roles_by_user_id(
        self,
        request: main_models.ListWorkspaceUserRolesByUserIdRequest,
    ) -> main_models.ListWorkspaceUserRolesByUserIdResponse:
        runtime = RuntimeOptions()
        return self.list_workspace_user_roles_by_user_id_with_options(request, runtime)

    async def list_workspace_user_roles_by_user_id_async(
        self,
        request: main_models.ListWorkspaceUserRolesByUserIdRequest,
    ) -> main_models.ListWorkspaceUserRolesByUserIdResponse:
        runtime = RuntimeOptions()
        return await self.list_workspace_user_roles_by_user_id_with_options_async(request, runtime)

    def manual_run_mail_task_with_options(
        self,
        request: main_models.ManualRunMailTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualRunMailTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mail_id):
            query['MailId'] = request.mail_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ManualRunMailTask',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualRunMailTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def manual_run_mail_task_with_options_async(
        self,
        request: main_models.ManualRunMailTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualRunMailTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mail_id):
            query['MailId'] = request.mail_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ManualRunMailTask',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualRunMailTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manual_run_mail_task(
        self,
        request: main_models.ManualRunMailTaskRequest,
    ) -> main_models.ManualRunMailTaskResponse:
        runtime = RuntimeOptions()
        return self.manual_run_mail_task_with_options(request, runtime)

    async def manual_run_mail_task_async(
        self,
        request: main_models.ManualRunMailTaskRequest,
    ) -> main_models.ManualRunMailTaskResponse:
        runtime = RuntimeOptions()
        return await self.manual_run_mail_task_with_options_async(request, runtime)

    def modify_api_datasource_parameters_with_options(
        self,
        request: main_models.ModifyApiDatasourceParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiDatasourceParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiDatasourceParameters',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiDatasourceParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_datasource_parameters_with_options_async(
        self,
        request: main_models.ModifyApiDatasourceParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyApiDatasourceParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyApiDatasourceParameters',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyApiDatasourceParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_datasource_parameters(
        self,
        request: main_models.ModifyApiDatasourceParametersRequest,
    ) -> main_models.ModifyApiDatasourceParametersResponse:
        runtime = RuntimeOptions()
        return self.modify_api_datasource_parameters_with_options(request, runtime)

    async def modify_api_datasource_parameters_async(
        self,
        request: main_models.ModifyApiDatasourceParametersRequest,
    ) -> main_models.ModifyApiDatasourceParametersResponse:
        runtime = RuntimeOptions()
        return await self.modify_api_datasource_parameters_with_options_async(request, runtime)

    def modify_copilot_embed_config_with_options(
        self,
        request: main_models.ModifyCopilotEmbedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCopilotEmbedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.copilot_id):
            query['CopilotId'] = request.copilot_id
        if not DaraCore.is_null(request.data_range):
            query['DataRange'] = request.data_range
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCopilotEmbedConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCopilotEmbedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_copilot_embed_config_with_options_async(
        self,
        request: main_models.ModifyCopilotEmbedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCopilotEmbedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_name):
            query['AgentName'] = request.agent_name
        if not DaraCore.is_null(request.copilot_id):
            query['CopilotId'] = request.copilot_id
        if not DaraCore.is_null(request.data_range):
            query['DataRange'] = request.data_range
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCopilotEmbedConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCopilotEmbedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_copilot_embed_config(
        self,
        request: main_models.ModifyCopilotEmbedConfigRequest,
    ) -> main_models.ModifyCopilotEmbedConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_copilot_embed_config_with_options(request, runtime)

    async def modify_copilot_embed_config_async(
        self,
        request: main_models.ModifyCopilotEmbedConfigRequest,
    ) -> main_models.ModifyCopilotEmbedConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_copilot_embed_config_with_options_async(request, runtime)

    def modify_dashboard_nl_2sql_status_with_options(
        self,
        request: main_models.ModifyDashboardNl2sqlStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDashboardNl2sqlStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dashboard_ids):
            query['DashboardIds'] = request.dashboard_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDashboardNl2sqlStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDashboardNl2sqlStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dashboard_nl_2sql_status_with_options_async(
        self,
        request: main_models.ModifyDashboardNl2sqlStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDashboardNl2sqlStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dashboard_ids):
            query['DashboardIds'] = request.dashboard_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDashboardNl2sqlStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDashboardNl2sqlStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dashboard_nl_2sql_status(
        self,
        request: main_models.ModifyDashboardNl2sqlStatusRequest,
    ) -> main_models.ModifyDashboardNl2sqlStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_dashboard_nl_2sql_status_with_options(request, runtime)

    async def modify_dashboard_nl_2sql_status_async(
        self,
        request: main_models.ModifyDashboardNl2sqlStatusRequest,
    ) -> main_models.ModifyDashboardNl2sqlStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_dashboard_nl_2sql_status_with_options_async(request, runtime)

    def query_acceleration_log_by_cube_id_with_options(
        self,
        request: main_models.QueryAccelerationLogByCubeIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccelerationLogByCubeIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccelerationLogByCubeId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccelerationLogByCubeIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_acceleration_log_by_cube_id_with_options_async(
        self,
        request: main_models.QueryAccelerationLogByCubeIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccelerationLogByCubeIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccelerationLogByCubeId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccelerationLogByCubeIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_acceleration_log_by_cube_id(
        self,
        request: main_models.QueryAccelerationLogByCubeIdRequest,
    ) -> main_models.QueryAccelerationLogByCubeIdResponse:
        runtime = RuntimeOptions()
        return self.query_acceleration_log_by_cube_id_with_options(request, runtime)

    async def query_acceleration_log_by_cube_id_async(
        self,
        request: main_models.QueryAccelerationLogByCubeIdRequest,
    ) -> main_models.QueryAccelerationLogByCubeIdResponse:
        runtime = RuntimeOptions()
        return await self.query_acceleration_log_by_cube_id_with_options_async(request, runtime)

    def query_approval_info_with_options(
        self,
        request: main_models.QueryApprovalInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryApprovalInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryApprovalInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryApprovalInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_approval_info_with_options_async(
        self,
        request: main_models.QueryApprovalInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryApprovalInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryApprovalInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryApprovalInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_approval_info(
        self,
        request: main_models.QueryApprovalInfoRequest,
    ) -> main_models.QueryApprovalInfoResponse:
        runtime = RuntimeOptions()
        return self.query_approval_info_with_options(request, runtime)

    async def query_approval_info_async(
        self,
        request: main_models.QueryApprovalInfoRequest,
    ) -> main_models.QueryApprovalInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_approval_info_with_options_async(request, runtime)

    def query_audit_log_with_options(
        self,
        request: main_models.QueryAuditLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuditLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_source_flag):
            query['AccessSourceFlag'] = request.access_source_flag
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.operator_id):
            query['OperatorId'] = request.operator_id
        if not DaraCore.is_null(request.operator_types):
            query['OperatorTypes'] = request.operator_types
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.user_access_device):
            query['UserAccessDevice'] = request.user_access_device
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuditLog',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuditLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_audit_log_with_options_async(
        self,
        request: main_models.QueryAuditLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuditLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_source_flag):
            query['AccessSourceFlag'] = request.access_source_flag
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.operator_id):
            query['OperatorId'] = request.operator_id
        if not DaraCore.is_null(request.operator_types):
            query['OperatorTypes'] = request.operator_types
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.user_access_device):
            query['UserAccessDevice'] = request.user_access_device
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuditLog',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuditLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_audit_log(
        self,
        request: main_models.QueryAuditLogRequest,
    ) -> main_models.QueryAuditLogResponse:
        runtime = RuntimeOptions()
        return self.query_audit_log_with_options(request, runtime)

    async def query_audit_log_async(
        self,
        request: main_models.QueryAuditLogRequest,
    ) -> main_models.QueryAuditLogResponse:
        runtime = RuntimeOptions()
        return await self.query_audit_log_with_options_async(request, runtime)

    def query_component_performance_with_options(
        self,
        request: main_models.QueryComponentPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryComponentPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryComponentPerformance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryComponentPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_component_performance_with_options_async(
        self,
        request: main_models.QueryComponentPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryComponentPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryComponentPerformance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryComponentPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_component_performance(
        self,
        request: main_models.QueryComponentPerformanceRequest,
    ) -> main_models.QueryComponentPerformanceResponse:
        runtime = RuntimeOptions()
        return self.query_component_performance_with_options(request, runtime)

    async def query_component_performance_async(
        self,
        request: main_models.QueryComponentPerformanceRequest,
    ) -> main_models.QueryComponentPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.query_component_performance_with_options_async(request, runtime)

    def query_copilot_embed_config_with_options(
        self,
        request: main_models.QueryCopilotEmbedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCopilotEmbedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCopilotEmbedConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCopilotEmbedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_copilot_embed_config_with_options_async(
        self,
        request: main_models.QueryCopilotEmbedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCopilotEmbedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCopilotEmbedConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCopilotEmbedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_copilot_embed_config(
        self,
        request: main_models.QueryCopilotEmbedConfigRequest,
    ) -> main_models.QueryCopilotEmbedConfigResponse:
        runtime = RuntimeOptions()
        return self.query_copilot_embed_config_with_options(request, runtime)

    async def query_copilot_embed_config_async(
        self,
        request: main_models.QueryCopilotEmbedConfigRequest,
    ) -> main_models.QueryCopilotEmbedConfigResponse:
        runtime = RuntimeOptions()
        return await self.query_copilot_embed_config_with_options_async(request, runtime)

    def query_cube_optimization_with_options(
        self,
        request: main_models.QueryCubeOptimizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCubeOptimizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCubeOptimization',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCubeOptimizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cube_optimization_with_options_async(
        self,
        request: main_models.QueryCubeOptimizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCubeOptimizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCubeOptimization',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCubeOptimizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cube_optimization(
        self,
        request: main_models.QueryCubeOptimizationRequest,
    ) -> main_models.QueryCubeOptimizationResponse:
        runtime = RuntimeOptions()
        return self.query_cube_optimization_with_options(request, runtime)

    async def query_cube_optimization_async(
        self,
        request: main_models.QueryCubeOptimizationRequest,
    ) -> main_models.QueryCubeOptimizationResponse:
        runtime = RuntimeOptions()
        return await self.query_cube_optimization_with_options_async(request, runtime)

    def query_cube_performance_with_options(
        self,
        request: main_models.QueryCubePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCubePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCubePerformance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCubePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cube_performance_with_options_async(
        self,
        request: main_models.QueryCubePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCubePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCubePerformance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCubePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cube_performance(
        self,
        request: main_models.QueryCubePerformanceRequest,
    ) -> main_models.QueryCubePerformanceResponse:
        runtime = RuntimeOptions()
        return self.query_cube_performance_with_options(request, runtime)

    async def query_cube_performance_async(
        self,
        request: main_models.QueryCubePerformanceRequest,
    ) -> main_models.QueryCubePerformanceResponse:
        runtime = RuntimeOptions()
        return await self.query_cube_performance_with_options_async(request, runtime)

    def query_dashboard_nl_2sql_with_options(
        self,
        request: main_models.QueryDashboardNl2sqlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDashboardNl2sqlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDashboardNl2sql',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDashboardNl2sqlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dashboard_nl_2sql_with_options_async(
        self,
        request: main_models.QueryDashboardNl2sqlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDashboardNl2sqlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDashboardNl2sql',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDashboardNl2sqlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dashboard_nl_2sql(
        self,
        request: main_models.QueryDashboardNl2sqlRequest,
    ) -> main_models.QueryDashboardNl2sqlResponse:
        runtime = RuntimeOptions()
        return self.query_dashboard_nl_2sql_with_options(request, runtime)

    async def query_dashboard_nl_2sql_async(
        self,
        request: main_models.QueryDashboardNl2sqlRequest,
    ) -> main_models.QueryDashboardNl2sqlResponse:
        runtime = RuntimeOptions()
        return await self.query_dashboard_nl_2sql_with_options_async(request, runtime)

    def query_data_with_options(
        self,
        request: main_models.QueryDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.conditions):
            query['Conditions'] = request.conditions
        if not DaraCore.is_null(request.return_fields):
            query['ReturnFields'] = request.return_fields
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryData',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_with_options_async(
        self,
        request: main_models.QueryDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.conditions):
            query['Conditions'] = request.conditions
        if not DaraCore.is_null(request.return_fields):
            query['ReturnFields'] = request.return_fields
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryData',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data(
        self,
        request: main_models.QueryDataRequest,
    ) -> main_models.QueryDataResponse:
        runtime = RuntimeOptions()
        return self.query_data_with_options(request, runtime)

    async def query_data_async(
        self,
        request: main_models.QueryDataRequest,
    ) -> main_models.QueryDataResponse:
        runtime = RuntimeOptions()
        return await self.query_data_with_options_async(request, runtime)

    def query_data_range_with_options(
        self,
        request: main_models.QueryDataRangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDataRangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDataRange',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDataRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_range_with_options_async(
        self,
        request: main_models.QueryDataRangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDataRangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDataRange',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDataRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_range(
        self,
        request: main_models.QueryDataRangeRequest,
    ) -> main_models.QueryDataRangeResponse:
        runtime = RuntimeOptions()
        return self.query_data_range_with_options(request, runtime)

    async def query_data_range_async(
        self,
        request: main_models.QueryDataRangeRequest,
    ) -> main_models.QueryDataRangeResponse:
        runtime = RuntimeOptions()
        return await self.query_data_range_with_options_async(request, runtime)

    def query_data_service_with_options(
        self,
        request: main_models.QueryDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.conditions):
            query['Conditions'] = request.conditions
        if not DaraCore.is_null(request.return_fields):
            query['ReturnFields'] = request.return_fields
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDataService',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_service_with_options_async(
        self,
        request: main_models.QueryDataServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDataServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.conditions):
            query['Conditions'] = request.conditions
        if not DaraCore.is_null(request.return_fields):
            query['ReturnFields'] = request.return_fields
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDataService',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_service(
        self,
        request: main_models.QueryDataServiceRequest,
    ) -> main_models.QueryDataServiceResponse:
        runtime = RuntimeOptions()
        return self.query_data_service_with_options(request, runtime)

    async def query_data_service_async(
        self,
        request: main_models.QueryDataServiceRequest,
    ) -> main_models.QueryDataServiceResponse:
        runtime = RuntimeOptions()
        return await self.query_data_service_with_options_async(request, runtime)

    def query_data_service_list_with_options(
        self,
        request: main_models.QueryDataServiceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDataServiceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDataServiceList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDataServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_service_list_with_options_async(
        self,
        request: main_models.QueryDataServiceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDataServiceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDataServiceList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDataServiceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_service_list(
        self,
        request: main_models.QueryDataServiceListRequest,
    ) -> main_models.QueryDataServiceListResponse:
        runtime = RuntimeOptions()
        return self.query_data_service_list_with_options(request, runtime)

    async def query_data_service_list_async(
        self,
        request: main_models.QueryDataServiceListRequest,
    ) -> main_models.QueryDataServiceListResponse:
        runtime = RuntimeOptions()
        return await self.query_data_service_list_with_options_async(request, runtime)

    def query_dataset_detail_info_with_options(
        self,
        request: main_models.QueryDatasetDetailInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetDetailInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetDetailInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetDetailInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_detail_info_with_options_async(
        self,
        request: main_models.QueryDatasetDetailInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetDetailInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetDetailInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetDetailInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_detail_info(
        self,
        request: main_models.QueryDatasetDetailInfoRequest,
    ) -> main_models.QueryDatasetDetailInfoResponse:
        runtime = RuntimeOptions()
        return self.query_dataset_detail_info_with_options(request, runtime)

    async def query_dataset_detail_info_async(
        self,
        request: main_models.QueryDatasetDetailInfoRequest,
    ) -> main_models.QueryDatasetDetailInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_dataset_detail_info_with_options_async(request, runtime)

    def query_dataset_info_with_options(
        self,
        request: main_models.QueryDatasetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_info_with_options_async(
        self,
        request: main_models.QueryDatasetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_info(
        self,
        request: main_models.QueryDatasetInfoRequest,
    ) -> main_models.QueryDatasetInfoResponse:
        runtime = RuntimeOptions()
        return self.query_dataset_info_with_options(request, runtime)

    async def query_dataset_info_async(
        self,
        request: main_models.QueryDatasetInfoRequest,
    ) -> main_models.QueryDatasetInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_dataset_info_with_options_async(request, runtime)

    def query_dataset_list_with_options(
        self,
        request: main_models.QueryDatasetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.with_children):
            query['WithChildren'] = request.with_children
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_list_with_options_async(
        self,
        request: main_models.QueryDatasetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.with_children):
            query['WithChildren'] = request.with_children
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_list(
        self,
        request: main_models.QueryDatasetListRequest,
    ) -> main_models.QueryDatasetListResponse:
        runtime = RuntimeOptions()
        return self.query_dataset_list_with_options(request, runtime)

    async def query_dataset_list_async(
        self,
        request: main_models.QueryDatasetListRequest,
    ) -> main_models.QueryDatasetListResponse:
        runtime = RuntimeOptions()
        return await self.query_dataset_list_with_options_async(request, runtime)

    def query_dataset_smartq_status_with_options(
        self,
        request: main_models.QueryDatasetSmartqStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetSmartqStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetSmartqStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetSmartqStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_smartq_status_with_options_async(
        self,
        request: main_models.QueryDatasetSmartqStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetSmartqStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetSmartqStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetSmartqStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_smartq_status(
        self,
        request: main_models.QueryDatasetSmartqStatusRequest,
    ) -> main_models.QueryDatasetSmartqStatusResponse:
        runtime = RuntimeOptions()
        return self.query_dataset_smartq_status_with_options(request, runtime)

    async def query_dataset_smartq_status_async(
        self,
        request: main_models.QueryDatasetSmartqStatusRequest,
    ) -> main_models.QueryDatasetSmartqStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_dataset_smartq_status_with_options_async(request, runtime)

    def query_dataset_switch_info_with_options(
        self,
        request: main_models.QueryDatasetSwitchInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetSwitchInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetSwitchInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetSwitchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_switch_info_with_options_async(
        self,
        request: main_models.QueryDatasetSwitchInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetSwitchInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDatasetSwitchInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetSwitchInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_switch_info(
        self,
        request: main_models.QueryDatasetSwitchInfoRequest,
    ) -> main_models.QueryDatasetSwitchInfoResponse:
        runtime = RuntimeOptions()
        return self.query_dataset_switch_info_with_options(request, runtime)

    async def query_dataset_switch_info_async(
        self,
        request: main_models.QueryDatasetSwitchInfoRequest,
    ) -> main_models.QueryDatasetSwitchInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_dataset_switch_info_with_options_async(request, runtime)

    def query_embedded_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEmbeddedInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryEmbeddedInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEmbeddedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_embedded_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEmbeddedInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryEmbeddedInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEmbeddedInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_embedded_info(self) -> main_models.QueryEmbeddedInfoResponse:
        runtime = RuntimeOptions()
        return self.query_embedded_info_with_options(runtime)

    async def query_embedded_info_async(self) -> main_models.QueryEmbeddedInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_embedded_info_with_options_async(runtime)

    def query_embedded_status_with_options(
        self,
        request: main_models.QueryEmbeddedStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEmbeddedStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEmbeddedStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEmbeddedStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_embedded_status_with_options_async(
        self,
        request: main_models.QueryEmbeddedStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEmbeddedStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEmbeddedStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEmbeddedStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_embedded_status(
        self,
        request: main_models.QueryEmbeddedStatusRequest,
    ) -> main_models.QueryEmbeddedStatusResponse:
        runtime = RuntimeOptions()
        return self.query_embedded_status_with_options(request, runtime)

    async def query_embedded_status_async(
        self,
        request: main_models.QueryEmbeddedStatusRequest,
    ) -> main_models.QueryEmbeddedStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_embedded_status_with_options_async(request, runtime)

    def query_last_acceleration_engine_job_with_options(
        self,
        request: main_models.QueryLastAccelerationEngineJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLastAccelerationEngineJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLastAccelerationEngineJob',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLastAccelerationEngineJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_last_acceleration_engine_job_with_options_async(
        self,
        request: main_models.QueryLastAccelerationEngineJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLastAccelerationEngineJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLastAccelerationEngineJob',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLastAccelerationEngineJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_last_acceleration_engine_job(
        self,
        request: main_models.QueryLastAccelerationEngineJobRequest,
    ) -> main_models.QueryLastAccelerationEngineJobResponse:
        runtime = RuntimeOptions()
        return self.query_last_acceleration_engine_job_with_options(request, runtime)

    async def query_last_acceleration_engine_job_async(
        self,
        request: main_models.QueryLastAccelerationEngineJobRequest,
    ) -> main_models.QueryLastAccelerationEngineJobResponse:
        runtime = RuntimeOptions()
        return await self.query_last_acceleration_engine_job_with_options_async(request, runtime)

    def query_llm_cube_with_theme_list_by_user_id_with_options(
        self,
        request: main_models.QueryLlmCubeWithThemeListByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLlmCubeWithThemeListByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLlmCubeWithThemeListByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLlmCubeWithThemeListByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_llm_cube_with_theme_list_by_user_id_with_options_async(
        self,
        request: main_models.QueryLlmCubeWithThemeListByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLlmCubeWithThemeListByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLlmCubeWithThemeListByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLlmCubeWithThemeListByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_llm_cube_with_theme_list_by_user_id(
        self,
        request: main_models.QueryLlmCubeWithThemeListByUserIdRequest,
    ) -> main_models.QueryLlmCubeWithThemeListByUserIdResponse:
        runtime = RuntimeOptions()
        return self.query_llm_cube_with_theme_list_by_user_id_with_options(request, runtime)

    async def query_llm_cube_with_theme_list_by_user_id_async(
        self,
        request: main_models.QueryLlmCubeWithThemeListByUserIdRequest,
    ) -> main_models.QueryLlmCubeWithThemeListByUserIdResponse:
        runtime = RuntimeOptions()
        return await self.query_llm_cube_with_theme_list_by_user_id_with_options_async(request, runtime)

    def query_organization_role_config_with_options(
        self,
        request: main_models.QueryOrganizationRoleConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrganizationRoleConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrganizationRoleConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrganizationRoleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_organization_role_config_with_options_async(
        self,
        request: main_models.QueryOrganizationRoleConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrganizationRoleConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrganizationRoleConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrganizationRoleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_organization_role_config(
        self,
        request: main_models.QueryOrganizationRoleConfigRequest,
    ) -> main_models.QueryOrganizationRoleConfigResponse:
        runtime = RuntimeOptions()
        return self.query_organization_role_config_with_options(request, runtime)

    async def query_organization_role_config_async(
        self,
        request: main_models.QueryOrganizationRoleConfigRequest,
    ) -> main_models.QueryOrganizationRoleConfigResponse:
        runtime = RuntimeOptions()
        return await self.query_organization_role_config_with_options_async(request, runtime)

    def query_organization_workspace_list_with_options(
        self,
        request: main_models.QueryOrganizationWorkspaceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrganizationWorkspaceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrganizationWorkspaceList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrganizationWorkspaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_organization_workspace_list_with_options_async(
        self,
        request: main_models.QueryOrganizationWorkspaceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrganizationWorkspaceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrganizationWorkspaceList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrganizationWorkspaceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_organization_workspace_list(
        self,
        request: main_models.QueryOrganizationWorkspaceListRequest,
    ) -> main_models.QueryOrganizationWorkspaceListResponse:
        runtime = RuntimeOptions()
        return self.query_organization_workspace_list_with_options(request, runtime)

    async def query_organization_workspace_list_async(
        self,
        request: main_models.QueryOrganizationWorkspaceListRequest,
    ) -> main_models.QueryOrganizationWorkspaceListResponse:
        runtime = RuntimeOptions()
        return await self.query_organization_workspace_list_with_options_async(request, runtime)

    def query_readable_resources_list_by_user_id_with_options(
        self,
        request: main_models.QueryReadableResourcesListByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReadableResourcesListByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReadableResourcesListByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReadableResourcesListByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_readable_resources_list_by_user_id_with_options_async(
        self,
        request: main_models.QueryReadableResourcesListByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReadableResourcesListByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReadableResourcesListByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReadableResourcesListByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_readable_resources_list_by_user_id(
        self,
        request: main_models.QueryReadableResourcesListByUserIdRequest,
    ) -> main_models.QueryReadableResourcesListByUserIdResponse:
        runtime = RuntimeOptions()
        return self.query_readable_resources_list_by_user_id_with_options(request, runtime)

    async def query_readable_resources_list_by_user_id_async(
        self,
        request: main_models.QueryReadableResourcesListByUserIdRequest,
    ) -> main_models.QueryReadableResourcesListByUserIdResponse:
        runtime = RuntimeOptions()
        return await self.query_readable_resources_list_by_user_id_with_options_async(request, runtime)

    def query_readable_resources_list_by_user_id_v2with_options(
        self,
        request: main_models.QueryReadableResourcesListByUserIdV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReadableResourcesListByUserIdV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.work_type):
            query['WorkType'] = request.work_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReadableResourcesListByUserIdV2',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReadableResourcesListByUserIdV2Response(),
            self.call_api(params, req, runtime)
        )

    async def query_readable_resources_list_by_user_id_v2with_options_async(
        self,
        request: main_models.QueryReadableResourcesListByUserIdV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReadableResourcesListByUserIdV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.work_type):
            query['WorkType'] = request.work_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReadableResourcesListByUserIdV2',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReadableResourcesListByUserIdV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def query_readable_resources_list_by_user_id_v2(
        self,
        request: main_models.QueryReadableResourcesListByUserIdV2Request,
    ) -> main_models.QueryReadableResourcesListByUserIdV2Response:
        runtime = RuntimeOptions()
        return self.query_readable_resources_list_by_user_id_v2with_options(request, runtime)

    async def query_readable_resources_list_by_user_id_v2_async(
        self,
        request: main_models.QueryReadableResourcesListByUserIdV2Request,
    ) -> main_models.QueryReadableResourcesListByUserIdV2Response:
        runtime = RuntimeOptions()
        return await self.query_readable_resources_list_by_user_id_v2with_options_async(request, runtime)

    def query_report_performance_with_options(
        self,
        request: main_models.QueryReportPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReportPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReportPerformance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReportPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_report_performance_with_options_async(
        self,
        request: main_models.QueryReportPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReportPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReportPerformance',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReportPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_report_performance(
        self,
        request: main_models.QueryReportPerformanceRequest,
    ) -> main_models.QueryReportPerformanceResponse:
        runtime = RuntimeOptions()
        return self.query_report_performance_with_options(request, runtime)

    async def query_report_performance_async(
        self,
        request: main_models.QueryReportPerformanceRequest,
    ) -> main_models.QueryReportPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.query_report_performance_with_options_async(request, runtime)

    def query_share_list_with_options(
        self,
        request: main_models.QueryShareListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryShareListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryShareList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryShareListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_share_list_with_options_async(
        self,
        request: main_models.QueryShareListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryShareListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryShareList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryShareListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_share_list(
        self,
        request: main_models.QueryShareListRequest,
    ) -> main_models.QueryShareListResponse:
        runtime = RuntimeOptions()
        return self.query_share_list_with_options(request, runtime)

    async def query_share_list_async(
        self,
        request: main_models.QueryShareListRequest,
    ) -> main_models.QueryShareListResponse:
        runtime = RuntimeOptions()
        return await self.query_share_list_with_options_async(request, runtime)

    def query_shares_to_user_list_with_options(
        self,
        request: main_models.QuerySharesToUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySharesToUserListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySharesToUserList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySharesToUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_shares_to_user_list_with_options_async(
        self,
        request: main_models.QuerySharesToUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySharesToUserListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySharesToUserList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySharesToUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_shares_to_user_list(
        self,
        request: main_models.QuerySharesToUserListRequest,
    ) -> main_models.QuerySharesToUserListResponse:
        runtime = RuntimeOptions()
        return self.query_shares_to_user_list_with_options(request, runtime)

    async def query_shares_to_user_list_async(
        self,
        request: main_models.QuerySharesToUserListRequest,
    ) -> main_models.QuerySharesToUserListResponse:
        runtime = RuntimeOptions()
        return await self.query_shares_to_user_list_with_options_async(request, runtime)

    def query_smartq_permission_by_cube_id_with_options(
        self,
        request: main_models.QuerySmartqPermissionByCubeIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmartqPermissionByCubeIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmartqPermissionByCubeId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmartqPermissionByCubeIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_smartq_permission_by_cube_id_with_options_async(
        self,
        request: main_models.QuerySmartqPermissionByCubeIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmartqPermissionByCubeIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmartqPermissionByCubeId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmartqPermissionByCubeIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_smartq_permission_by_cube_id(
        self,
        request: main_models.QuerySmartqPermissionByCubeIdRequest,
    ) -> main_models.QuerySmartqPermissionByCubeIdResponse:
        runtime = RuntimeOptions()
        return self.query_smartq_permission_by_cube_id_with_options(request, runtime)

    async def query_smartq_permission_by_cube_id_async(
        self,
        request: main_models.QuerySmartqPermissionByCubeIdRequest,
    ) -> main_models.QuerySmartqPermissionByCubeIdResponse:
        runtime = RuntimeOptions()
        return await self.query_smartq_permission_by_cube_id_with_options_async(request, runtime)

    def query_ticket_info_with_options(
        self,
        request: main_models.QueryTicketInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTicketInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTicketInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTicketInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ticket_info_with_options_async(
        self,
        request: main_models.QueryTicketInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTicketInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTicketInfo',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTicketInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ticket_info(
        self,
        request: main_models.QueryTicketInfoRequest,
    ) -> main_models.QueryTicketInfoResponse:
        runtime = RuntimeOptions()
        return self.query_ticket_info_with_options(request, runtime)

    async def query_ticket_info_async(
        self,
        request: main_models.QueryTicketInfoRequest,
    ) -> main_models.QueryTicketInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_ticket_info_with_options_async(request, runtime)

    def query_user_by_mobile_account_with_options(
        self,
        request: main_models.QueryUserByMobileAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserByMobileAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mobile_type):
            query['MobileType'] = request.mobile_type
        if not DaraCore.is_null(request.mobile_user_id):
            query['MobileUserId'] = request.mobile_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserByMobileAccount',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserByMobileAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_by_mobile_account_with_options_async(
        self,
        request: main_models.QueryUserByMobileAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserByMobileAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mobile_type):
            query['MobileType'] = request.mobile_type
        if not DaraCore.is_null(request.mobile_user_id):
            query['MobileUserId'] = request.mobile_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserByMobileAccount',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserByMobileAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_by_mobile_account(
        self,
        request: main_models.QueryUserByMobileAccountRequest,
    ) -> main_models.QueryUserByMobileAccountResponse:
        runtime = RuntimeOptions()
        return self.query_user_by_mobile_account_with_options(request, runtime)

    async def query_user_by_mobile_account_async(
        self,
        request: main_models.QueryUserByMobileAccountRequest,
    ) -> main_models.QueryUserByMobileAccountResponse:
        runtime = RuntimeOptions()
        return await self.query_user_by_mobile_account_with_options_async(request, runtime)

    def query_user_group_list_by_parent_id_with_options(
        self,
        request: main_models.QueryUserGroupListByParentIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserGroupListByParentIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserGroupListByParentId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserGroupListByParentIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_group_list_by_parent_id_with_options_async(
        self,
        request: main_models.QueryUserGroupListByParentIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserGroupListByParentIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserGroupListByParentId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserGroupListByParentIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_group_list_by_parent_id(
        self,
        request: main_models.QueryUserGroupListByParentIdRequest,
    ) -> main_models.QueryUserGroupListByParentIdResponse:
        runtime = RuntimeOptions()
        return self.query_user_group_list_by_parent_id_with_options(request, runtime)

    async def query_user_group_list_by_parent_id_async(
        self,
        request: main_models.QueryUserGroupListByParentIdRequest,
    ) -> main_models.QueryUserGroupListByParentIdResponse:
        runtime = RuntimeOptions()
        return await self.query_user_group_list_by_parent_id_with_options_async(request, runtime)

    def query_user_group_member_with_options(
        self,
        request: main_models.QueryUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserGroupMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserGroupMember',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_group_member_with_options_async(
        self,
        request: main_models.QueryUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserGroupMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserGroupMember',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_group_member(
        self,
        request: main_models.QueryUserGroupMemberRequest,
    ) -> main_models.QueryUserGroupMemberResponse:
        runtime = RuntimeOptions()
        return self.query_user_group_member_with_options(request, runtime)

    async def query_user_group_member_async(
        self,
        request: main_models.QueryUserGroupMemberRequest,
    ) -> main_models.QueryUserGroupMemberResponse:
        runtime = RuntimeOptions()
        return await self.query_user_group_member_with_options_async(request, runtime)

    def query_user_info_by_account_with_options(
        self,
        request: main_models.QueryUserInfoByAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserInfoByAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.parent_account_name):
            query['ParentAccountName'] = request.parent_account_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserInfoByAccount',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserInfoByAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_info_by_account_with_options_async(
        self,
        request: main_models.QueryUserInfoByAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserInfoByAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.parent_account_name):
            query['ParentAccountName'] = request.parent_account_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserInfoByAccount',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserInfoByAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_info_by_account(
        self,
        request: main_models.QueryUserInfoByAccountRequest,
    ) -> main_models.QueryUserInfoByAccountResponse:
        runtime = RuntimeOptions()
        return self.query_user_info_by_account_with_options(request, runtime)

    async def query_user_info_by_account_async(
        self,
        request: main_models.QueryUserInfoByAccountRequest,
    ) -> main_models.QueryUserInfoByAccountResponse:
        runtime = RuntimeOptions()
        return await self.query_user_info_by_account_with_options_async(request, runtime)

    def query_user_info_by_user_id_with_options(
        self,
        request: main_models.QueryUserInfoByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserInfoByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserInfoByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserInfoByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_info_by_user_id_with_options_async(
        self,
        request: main_models.QueryUserInfoByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserInfoByUserIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserInfoByUserId',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserInfoByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_info_by_user_id(
        self,
        request: main_models.QueryUserInfoByUserIdRequest,
    ) -> main_models.QueryUserInfoByUserIdResponse:
        runtime = RuntimeOptions()
        return self.query_user_info_by_user_id_with_options(request, runtime)

    async def query_user_info_by_user_id_async(
        self,
        request: main_models.QueryUserInfoByUserIdRequest,
    ) -> main_models.QueryUserInfoByUserIdResponse:
        runtime = RuntimeOptions()
        return await self.query_user_info_by_user_id_with_options_async(request, runtime)

    def query_user_list_with_options(
        self,
        request: main_models.QueryUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_list_with_options_async(
        self,
        request: main_models.QueryUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_list(
        self,
        request: main_models.QueryUserListRequest,
    ) -> main_models.QueryUserListResponse:
        runtime = RuntimeOptions()
        return self.query_user_list_with_options(request, runtime)

    async def query_user_list_async(
        self,
        request: main_models.QueryUserListRequest,
    ) -> main_models.QueryUserListResponse:
        runtime = RuntimeOptions()
        return await self.query_user_list_with_options_async(request, runtime)

    def query_user_role_info_in_workspace_with_options(
        self,
        request: main_models.QueryUserRoleInfoInWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserRoleInfoInWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserRoleInfoInWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserRoleInfoInWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_role_info_in_workspace_with_options_async(
        self,
        request: main_models.QueryUserRoleInfoInWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserRoleInfoInWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserRoleInfoInWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserRoleInfoInWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_role_info_in_workspace(
        self,
        request: main_models.QueryUserRoleInfoInWorkspaceRequest,
    ) -> main_models.QueryUserRoleInfoInWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.query_user_role_info_in_workspace_with_options(request, runtime)

    async def query_user_role_info_in_workspace_async(
        self,
        request: main_models.QueryUserRoleInfoInWorkspaceRequest,
    ) -> main_models.QueryUserRoleInfoInWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.query_user_role_info_in_workspace_with_options_async(request, runtime)

    def query_user_tag_meta_list_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserTagMetaListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryUserTagMetaList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserTagMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_tag_meta_list_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserTagMetaListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryUserTagMetaList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserTagMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_tag_meta_list(self) -> main_models.QueryUserTagMetaListResponse:
        runtime = RuntimeOptions()
        return self.query_user_tag_meta_list_with_options(runtime)

    async def query_user_tag_meta_list_async(self) -> main_models.QueryUserTagMetaListResponse:
        runtime = RuntimeOptions()
        return await self.query_user_tag_meta_list_with_options_async(runtime)

    def query_user_tag_value_list_with_options(
        self,
        request: main_models.QueryUserTagValueListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserTagValueListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserTagValueList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserTagValueListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_tag_value_list_with_options_async(
        self,
        request: main_models.QueryUserTagValueListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserTagValueListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserTagValueList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserTagValueListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_tag_value_list(
        self,
        request: main_models.QueryUserTagValueListRequest,
    ) -> main_models.QueryUserTagValueListResponse:
        runtime = RuntimeOptions()
        return self.query_user_tag_value_list_with_options(request, runtime)

    async def query_user_tag_value_list_async(
        self,
        request: main_models.QueryUserTagValueListRequest,
    ) -> main_models.QueryUserTagValueListResponse:
        runtime = RuntimeOptions()
        return await self.query_user_tag_value_list_with_options_async(request, runtime)

    def query_works_with_options(
        self,
        request: main_models.QueryWorksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorks',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorksResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_works_with_options_async(
        self,
        request: main_models.QueryWorksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorks',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_works(
        self,
        request: main_models.QueryWorksRequest,
    ) -> main_models.QueryWorksResponse:
        runtime = RuntimeOptions()
        return self.query_works_with_options(request, runtime)

    async def query_works_async(
        self,
        request: main_models.QueryWorksRequest,
    ) -> main_models.QueryWorksResponse:
        runtime = RuntimeOptions()
        return await self.query_works_with_options_async(request, runtime)

    def query_works_blood_relationship_with_options(
        self,
        request: main_models.QueryWorksBloodRelationshipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorksBloodRelationshipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorksBloodRelationship',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorksBloodRelationshipResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_works_blood_relationship_with_options_async(
        self,
        request: main_models.QueryWorksBloodRelationshipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorksBloodRelationshipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorksBloodRelationship',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorksBloodRelationshipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_works_blood_relationship(
        self,
        request: main_models.QueryWorksBloodRelationshipRequest,
    ) -> main_models.QueryWorksBloodRelationshipResponse:
        runtime = RuntimeOptions()
        return self.query_works_blood_relationship_with_options(request, runtime)

    async def query_works_blood_relationship_async(
        self,
        request: main_models.QueryWorksBloodRelationshipRequest,
    ) -> main_models.QueryWorksBloodRelationshipResponse:
        runtime = RuntimeOptions()
        return await self.query_works_blood_relationship_with_options_async(request, runtime)

    def query_works_by_organization_with_options(
        self,
        request: main_models.QueryWorksByOrganizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorksByOrganizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not DaraCore.is_null(request.works_type):
            query['WorksType'] = request.works_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorksByOrganization',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorksByOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_works_by_organization_with_options_async(
        self,
        request: main_models.QueryWorksByOrganizationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorksByOrganizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not DaraCore.is_null(request.works_type):
            query['WorksType'] = request.works_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorksByOrganization',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorksByOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_works_by_organization(
        self,
        request: main_models.QueryWorksByOrganizationRequest,
    ) -> main_models.QueryWorksByOrganizationResponse:
        runtime = RuntimeOptions()
        return self.query_works_by_organization_with_options(request, runtime)

    async def query_works_by_organization_async(
        self,
        request: main_models.QueryWorksByOrganizationRequest,
    ) -> main_models.QueryWorksByOrganizationResponse:
        runtime = RuntimeOptions()
        return await self.query_works_by_organization_with_options_async(request, runtime)

    def query_works_by_workspace_with_options(
        self,
        request: main_models.QueryWorksByWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorksByWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not DaraCore.is_null(request.works_type):
            query['WorksType'] = request.works_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorksByWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorksByWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_works_by_workspace_with_options_async(
        self,
        request: main_models.QueryWorksByWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorksByWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not DaraCore.is_null(request.works_type):
            query['WorksType'] = request.works_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorksByWorkspace',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorksByWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_works_by_workspace(
        self,
        request: main_models.QueryWorksByWorkspaceRequest,
    ) -> main_models.QueryWorksByWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.query_works_by_workspace_with_options(request, runtime)

    async def query_works_by_workspace_async(
        self,
        request: main_models.QueryWorksByWorkspaceRequest,
    ) -> main_models.QueryWorksByWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.query_works_by_workspace_with_options_async(request, runtime)

    def query_workspace_role_config_with_options(
        self,
        request: main_models.QueryWorkspaceRoleConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorkspaceRoleConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorkspaceRoleConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorkspaceRoleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_workspace_role_config_with_options_async(
        self,
        request: main_models.QueryWorkspaceRoleConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorkspaceRoleConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorkspaceRoleConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorkspaceRoleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_workspace_role_config(
        self,
        request: main_models.QueryWorkspaceRoleConfigRequest,
    ) -> main_models.QueryWorkspaceRoleConfigResponse:
        runtime = RuntimeOptions()
        return self.query_workspace_role_config_with_options(request, runtime)

    async def query_workspace_role_config_async(
        self,
        request: main_models.QueryWorkspaceRoleConfigRequest,
    ) -> main_models.QueryWorkspaceRoleConfigResponse:
        runtime = RuntimeOptions()
        return await self.query_workspace_role_config_with_options_async(request, runtime)

    def query_workspace_user_list_with_options(
        self,
        request: main_models.QueryWorkspaceUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorkspaceUserListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorkspaceUserList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorkspaceUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_workspace_user_list_with_options_async(
        self,
        request: main_models.QueryWorkspaceUserListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWorkspaceUserListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWorkspaceUserList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWorkspaceUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_workspace_user_list(
        self,
        request: main_models.QueryWorkspaceUserListRequest,
    ) -> main_models.QueryWorkspaceUserListResponse:
        runtime = RuntimeOptions()
        return self.query_workspace_user_list_with_options(request, runtime)

    async def query_workspace_user_list_async(
        self,
        request: main_models.QueryWorkspaceUserListRequest,
    ) -> main_models.QueryWorkspaceUserListResponse:
        runtime = RuntimeOptions()
        return await self.query_workspace_user_list_with_options_async(request, runtime)

    def result_callback_with_options(
        self,
        request: main_models.ResultCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResultCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.handle_reason):
            query['HandleReason'] = request.handle_reason
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResultCallback',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResultCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def result_callback_with_options_async(
        self,
        request: main_models.ResultCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResultCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.handle_reason):
            query['HandleReason'] = request.handle_reason
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResultCallback',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResultCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def result_callback(
        self,
        request: main_models.ResultCallbackRequest,
    ) -> main_models.ResultCallbackResponse:
        runtime = RuntimeOptions()
        return self.result_callback_with_options(request, runtime)

    async def result_callback_async(
        self,
        request: main_models.ResultCallbackRequest,
    ) -> main_models.ResultCallbackResponse:
        runtime = RuntimeOptions()
        return await self.result_callback_with_options_async(request, runtime)

    def save_favorites_with_options(
        self,
        request: main_models.SaveFavoritesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveFavoritesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveFavorites',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveFavoritesResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_favorites_with_options_async(
        self,
        request: main_models.SaveFavoritesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveFavoritesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveFavorites',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveFavoritesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_favorites(
        self,
        request: main_models.SaveFavoritesRequest,
    ) -> main_models.SaveFavoritesResponse:
        runtime = RuntimeOptions()
        return self.save_favorites_with_options(request, runtime)

    async def save_favorites_async(
        self,
        request: main_models.SaveFavoritesRequest,
    ) -> main_models.SaveFavoritesResponse:
        runtime = RuntimeOptions()
        return await self.save_favorites_with_options_async(request, runtime)

    def set_data_level_permission_extra_config_with_options(
        self,
        request: main_models.SetDataLevelPermissionExtraConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDataLevelPermissionExtraConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.miss_hit_policy):
            query['MissHitPolicy'] = request.miss_hit_policy
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDataLevelPermissionExtraConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDataLevelPermissionExtraConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_data_level_permission_extra_config_with_options_async(
        self,
        request: main_models.SetDataLevelPermissionExtraConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDataLevelPermissionExtraConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.miss_hit_policy):
            query['MissHitPolicy'] = request.miss_hit_policy
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDataLevelPermissionExtraConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDataLevelPermissionExtraConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_data_level_permission_extra_config(
        self,
        request: main_models.SetDataLevelPermissionExtraConfigRequest,
    ) -> main_models.SetDataLevelPermissionExtraConfigResponse:
        runtime = RuntimeOptions()
        return self.set_data_level_permission_extra_config_with_options(request, runtime)

    async def set_data_level_permission_extra_config_async(
        self,
        request: main_models.SetDataLevelPermissionExtraConfigRequest,
    ) -> main_models.SetDataLevelPermissionExtraConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_data_level_permission_extra_config_with_options_async(request, runtime)

    def set_data_level_permission_rule_config_with_options(
        self,
        request: main_models.SetDataLevelPermissionRuleConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDataLevelPermissionRuleConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_model):
            query['RuleModel'] = request.rule_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDataLevelPermissionRuleConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDataLevelPermissionRuleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_data_level_permission_rule_config_with_options_async(
        self,
        request: main_models.SetDataLevelPermissionRuleConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDataLevelPermissionRuleConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_model):
            query['RuleModel'] = request.rule_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDataLevelPermissionRuleConfig',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDataLevelPermissionRuleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_data_level_permission_rule_config(
        self,
        request: main_models.SetDataLevelPermissionRuleConfigRequest,
    ) -> main_models.SetDataLevelPermissionRuleConfigResponse:
        runtime = RuntimeOptions()
        return self.set_data_level_permission_rule_config_with_options(request, runtime)

    async def set_data_level_permission_rule_config_async(
        self,
        request: main_models.SetDataLevelPermissionRuleConfigRequest,
    ) -> main_models.SetDataLevelPermissionRuleConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_data_level_permission_rule_config_with_options_async(request, runtime)

    def set_data_level_permission_white_list_with_options(
        self,
        request: main_models.SetDataLevelPermissionWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDataLevelPermissionWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.white_list_model):
            query['WhiteListModel'] = request.white_list_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDataLevelPermissionWhiteList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDataLevelPermissionWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_data_level_permission_white_list_with_options_async(
        self,
        request: main_models.SetDataLevelPermissionWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDataLevelPermissionWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.white_list_model):
            query['WhiteListModel'] = request.white_list_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDataLevelPermissionWhiteList',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDataLevelPermissionWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_data_level_permission_white_list(
        self,
        request: main_models.SetDataLevelPermissionWhiteListRequest,
    ) -> main_models.SetDataLevelPermissionWhiteListResponse:
        runtime = RuntimeOptions()
        return self.set_data_level_permission_white_list_with_options(request, runtime)

    async def set_data_level_permission_white_list_async(
        self,
        request: main_models.SetDataLevelPermissionWhiteListRequest,
    ) -> main_models.SetDataLevelPermissionWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.set_data_level_permission_white_list_with_options_async(request, runtime)

    def smartq_auth_transfer_with_options(
        self,
        request: main_models.SmartqAuthTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartqAuthTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.origin_user_id):
            query['OriginUserId'] = request.origin_user_id
        if not DaraCore.is_null(request.target_user_ids):
            query['TargetUserIds'] = request.target_user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartqAuthTransfer',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartqAuthTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def smartq_auth_transfer_with_options_async(
        self,
        request: main_models.SmartqAuthTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartqAuthTransferResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.origin_user_id):
            query['OriginUserId'] = request.origin_user_id
        if not DaraCore.is_null(request.target_user_ids):
            query['TargetUserIds'] = request.target_user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartqAuthTransfer',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartqAuthTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def smartq_auth_transfer(
        self,
        request: main_models.SmartqAuthTransferRequest,
    ) -> main_models.SmartqAuthTransferResponse:
        runtime = RuntimeOptions()
        return self.smartq_auth_transfer_with_options(request, runtime)

    async def smartq_auth_transfer_async(
        self,
        request: main_models.SmartqAuthTransferRequest,
    ) -> main_models.SmartqAuthTransferResponse:
        runtime = RuntimeOptions()
        return await self.smartq_auth_transfer_with_options_async(request, runtime)

    def smartq_authorize_with_options(
        self,
        request: main_models.SmartqAuthorizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartqAuthorizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_ids):
            query['CubeIds'] = request.cube_ids
        if not DaraCore.is_null(request.expire_day):
            query['ExpireDay'] = request.expire_day
        if not DaraCore.is_null(request.llm_cube_themes):
            query['LlmCubeThemes'] = request.llm_cube_themes
        if not DaraCore.is_null(request.llm_cubes):
            query['LlmCubes'] = request.llm_cubes
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartqAuthorize',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartqAuthorizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def smartq_authorize_with_options_async(
        self,
        request: main_models.SmartqAuthorizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartqAuthorizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_ids):
            query['CubeIds'] = request.cube_ids
        if not DaraCore.is_null(request.expire_day):
            query['ExpireDay'] = request.expire_day
        if not DaraCore.is_null(request.llm_cube_themes):
            query['LlmCubeThemes'] = request.llm_cube_themes
        if not DaraCore.is_null(request.llm_cubes):
            query['LlmCubes'] = request.llm_cubes
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartqAuthorize',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartqAuthorizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def smartq_authorize(
        self,
        request: main_models.SmartqAuthorizeRequest,
    ) -> main_models.SmartqAuthorizeResponse:
        runtime = RuntimeOptions()
        return self.smartq_authorize_with_options(request, runtime)

    async def smartq_authorize_async(
        self,
        request: main_models.SmartqAuthorizeRequest,
    ) -> main_models.SmartqAuthorizeResponse:
        runtime = RuntimeOptions()
        return await self.smartq_authorize_with_options_async(request, runtime)

    def smartq_query_ability_with_options(
        self,
        request: main_models.SmartqQueryAbilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartqQueryAbilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.multiple_cube_ids):
            query['MultipleCubeIds'] = request.multiple_cube_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_question):
            query['UserQuestion'] = request.user_question
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartqQueryAbility',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartqQueryAbilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def smartq_query_ability_with_options_async(
        self,
        request: main_models.SmartqQueryAbilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartqQueryAbilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.multiple_cube_ids):
            query['MultipleCubeIds'] = request.multiple_cube_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_question):
            query['UserQuestion'] = request.user_question
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartqQueryAbility',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartqQueryAbilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def smartq_query_ability(
        self,
        request: main_models.SmartqQueryAbilityRequest,
    ) -> main_models.SmartqQueryAbilityResponse:
        runtime = RuntimeOptions()
        return self.smartq_query_ability_with_options(request, runtime)

    async def smartq_query_ability_async(
        self,
        request: main_models.SmartqQueryAbilityRequest,
    ) -> main_models.SmartqQueryAbilityResponse:
        runtime = RuntimeOptions()
        return await self.smartq_query_ability_with_options_async(request, runtime)

    def update_cube_by_sql_with_options(
        self,
        request: main_models.UpdateCubeBySqlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCubeBySqlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.custom_sql):
            query['CustomSql'] = request.custom_sql
        if not DaraCore.is_null(request.ds_id):
            query['DsId'] = request.ds_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCubeBySql',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCubeBySqlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cube_by_sql_with_options_async(
        self,
        request: main_models.UpdateCubeBySqlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCubeBySqlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.custom_sql):
            query['CustomSql'] = request.custom_sql
        if not DaraCore.is_null(request.ds_id):
            query['DsId'] = request.ds_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCubeBySql',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCubeBySqlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cube_by_sql(
        self,
        request: main_models.UpdateCubeBySqlRequest,
    ) -> main_models.UpdateCubeBySqlResponse:
        runtime = RuntimeOptions()
        return self.update_cube_by_sql_with_options(request, runtime)

    async def update_cube_by_sql_async(
        self,
        request: main_models.UpdateCubeBySqlRequest,
    ) -> main_models.UpdateCubeBySqlResponse:
        runtime = RuntimeOptions()
        return await self.update_cube_by_sql_with_options_async(request, runtime)

    def update_data_level_permission_status_with_options(
        self,
        request: main_models.UpdateDataLevelPermissionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLevelPermissionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.is_open):
            query['IsOpen'] = request.is_open
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLevelPermissionStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLevelPermissionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_level_permission_status_with_options_async(
        self,
        request: main_models.UpdateDataLevelPermissionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLevelPermissionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cube_id):
            query['CubeId'] = request.cube_id
        if not DaraCore.is_null(request.is_open):
            query['IsOpen'] = request.is_open
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLevelPermissionStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLevelPermissionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_level_permission_status(
        self,
        request: main_models.UpdateDataLevelPermissionStatusRequest,
    ) -> main_models.UpdateDataLevelPermissionStatusResponse:
        runtime = RuntimeOptions()
        return self.update_data_level_permission_status_with_options(request, runtime)

    async def update_data_level_permission_status_async(
        self,
        request: main_models.UpdateDataLevelPermissionStatusRequest,
    ) -> main_models.UpdateDataLevelPermissionStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_data_level_permission_status_with_options_async(request, runtime)

    def update_data_source_with_options(
        self,
        request: main_models.UpdateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.update_model):
            query['UpdateModel'] = request.update_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSource',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_with_options_async(
        self,
        request: main_models.UpdateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.update_model):
            query['UpdateModel'] = request.update_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSource',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source(
        self,
        request: main_models.UpdateDataSourceRequest,
    ) -> main_models.UpdateDataSourceResponse:
        runtime = RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    async def update_data_source_async(
        self,
        request: main_models.UpdateDataSourceRequest,
    ) -> main_models.UpdateDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.update_data_source_with_options_async(request, runtime)

    def update_embedded_status_with_options(
        self,
        request: main_models.UpdateEmbeddedStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEmbeddedStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEmbeddedStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEmbeddedStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_embedded_status_with_options_async(
        self,
        request: main_models.UpdateEmbeddedStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEmbeddedStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not DaraCore.is_null(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEmbeddedStatus',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEmbeddedStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_embedded_status(
        self,
        request: main_models.UpdateEmbeddedStatusRequest,
    ) -> main_models.UpdateEmbeddedStatusResponse:
        runtime = RuntimeOptions()
        return self.update_embedded_status_with_options(request, runtime)

    async def update_embedded_status_async(
        self,
        request: main_models.UpdateEmbeddedStatusRequest,
    ) -> main_models.UpdateEmbeddedStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_embedded_status_with_options_async(request, runtime)

    def update_ticket_num_with_options(
        self,
        request: main_models.UpdateTicketNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTicketNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        if not DaraCore.is_null(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTicketNum',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTicketNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ticket_num_with_options_async(
        self,
        request: main_models.UpdateTicketNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTicketNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        if not DaraCore.is_null(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTicketNum',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTicketNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ticket_num(
        self,
        request: main_models.UpdateTicketNumRequest,
    ) -> main_models.UpdateTicketNumResponse:
        runtime = RuntimeOptions()
        return self.update_ticket_num_with_options(request, runtime)

    async def update_ticket_num_async(
        self,
        request: main_models.UpdateTicketNumRequest,
    ) -> main_models.UpdateTicketNumResponse:
        runtime = RuntimeOptions()
        return await self.update_ticket_num_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not DaraCore.is_null(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not DaraCore.is_null(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not DaraCore.is_null(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not DaraCore.is_null(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        request: main_models.UpdateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserGroup',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_group_with_options_async(
        self,
        request: main_models.UpdateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not DaraCore.is_null(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserGroup',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_group(
        self,
        request: main_models.UpdateUserGroupRequest,
    ) -> main_models.UpdateUserGroupResponse:
        runtime = RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    async def update_user_group_async(
        self,
        request: main_models.UpdateUserGroupRequest,
    ) -> main_models.UpdateUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_user_group_with_options_async(request, runtime)

    def update_user_tag_meta_with_options(
        self,
        request: main_models.UpdateUserTagMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserTagMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserTagMeta',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserTagMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_tag_meta_with_options_async(
        self,
        request: main_models.UpdateUserTagMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserTagMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        if not DaraCore.is_null(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserTagMeta',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserTagMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_tag_meta(
        self,
        request: main_models.UpdateUserTagMetaRequest,
    ) -> main_models.UpdateUserTagMetaResponse:
        runtime = RuntimeOptions()
        return self.update_user_tag_meta_with_options(request, runtime)

    async def update_user_tag_meta_async(
        self,
        request: main_models.UpdateUserTagMetaRequest,
    ) -> main_models.UpdateUserTagMetaResponse:
        runtime = RuntimeOptions()
        return await self.update_user_tag_meta_with_options_async(request, runtime)

    def update_user_tag_value_with_options(
        self,
        request: main_models.UpdateUserTagValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserTagValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        if not DaraCore.is_null(request.tag_value):
            query['TagValue'] = request.tag_value
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserTagValue',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserTagValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_tag_value_with_options_async(
        self,
        request: main_models.UpdateUserTagValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserTagValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        if not DaraCore.is_null(request.tag_value):
            query['TagValue'] = request.tag_value
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserTagValue',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserTagValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_tag_value(
        self,
        request: main_models.UpdateUserTagValueRequest,
    ) -> main_models.UpdateUserTagValueResponse:
        runtime = RuntimeOptions()
        return self.update_user_tag_value_with_options(request, runtime)

    async def update_user_tag_value_async(
        self,
        request: main_models.UpdateUserTagValueRequest,
    ) -> main_models.UpdateUserTagValueResponse:
        runtime = RuntimeOptions()
        return await self.update_user_tag_value_with_options_async(request, runtime)

    def update_workspace_user_role_with_options(
        self,
        request: main_models.UpdateWorkspaceUserRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceUserRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspaceUserRole',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceUserRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_user_role_with_options_async(
        self,
        request: main_models.UpdateWorkspaceUserRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceUserRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspaceUserRole',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceUserRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace_user_role(
        self,
        request: main_models.UpdateWorkspaceUserRoleRequest,
    ) -> main_models.UpdateWorkspaceUserRoleResponse:
        runtime = RuntimeOptions()
        return self.update_workspace_user_role_with_options(request, runtime)

    async def update_workspace_user_role_async(
        self,
        request: main_models.UpdateWorkspaceUserRoleRequest,
    ) -> main_models.UpdateWorkspaceUserRoleResponse:
        runtime = RuntimeOptions()
        return await self.update_workspace_user_role_with_options_async(request, runtime)

    def update_workspace_users_role_with_options(
        self,
        request: main_models.UpdateWorkspaceUsersRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceUsersRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspaceUsersRole',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceUsersRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_users_role_with_options_async(
        self,
        request: main_models.UpdateWorkspaceUsersRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkspaceUsersRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkspaceUsersRole',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkspaceUsersRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace_users_role(
        self,
        request: main_models.UpdateWorkspaceUsersRoleRequest,
    ) -> main_models.UpdateWorkspaceUsersRoleResponse:
        runtime = RuntimeOptions()
        return self.update_workspace_users_role_with_options(request, runtime)

    async def update_workspace_users_role_async(
        self,
        request: main_models.UpdateWorkspaceUsersRoleRequest,
    ) -> main_models.UpdateWorkspaceUsersRoleResponse:
        runtime = RuntimeOptions()
        return await self.update_workspace_users_role_with_options_async(request, runtime)

    def withdraw_all_user_groups_with_options(
        self,
        request: main_models.WithdrawAllUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawAllUserGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawAllUserGroups',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawAllUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def withdraw_all_user_groups_with_options_async(
        self,
        request: main_models.WithdrawAllUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawAllUserGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawAllUserGroups',
            version = '2022-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawAllUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def withdraw_all_user_groups(
        self,
        request: main_models.WithdrawAllUserGroupsRequest,
    ) -> main_models.WithdrawAllUserGroupsResponse:
        runtime = RuntimeOptions()
        return self.withdraw_all_user_groups_with_options(request, runtime)

    async def withdraw_all_user_groups_async(
        self,
        request: main_models.WithdrawAllUserGroupsRequest,
    ) -> main_models.WithdrawAllUserGroupsResponse:
        runtime = RuntimeOptions()
        return await self.withdraw_all_user_groups_with_options_async(request, runtime)
