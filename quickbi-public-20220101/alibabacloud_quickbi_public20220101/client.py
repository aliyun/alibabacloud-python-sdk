# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_quickbi_public20220101 import models as quickbi_public_20220101_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_data_level_permission_rule_users_with_options(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_user_model):
            query['AddUserModel'] = request.add_user_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDataLevelPermissionRuleUsers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_level_permission_rule_users_with_options_async(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_user_model):
            query['AddUserModel'] = request.add_user_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDataLevelPermissionRuleUsers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_level_permission_rule_users(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersRequest,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_data_level_permission_rule_users_with_options(request, runtime)

    async def add_data_level_permission_rule_users_async(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersRequest,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_data_level_permission_rule_users_with_options_async(request, runtime)

    def add_data_level_permission_white_list_with_options(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.target_ids):
            query['TargetIds'] = request.target_ids
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDataLevelPermissionWhiteList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddDataLevelPermissionWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_level_permission_white_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.target_ids):
            query['TargetIds'] = request.target_ids
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDataLevelPermissionWhiteList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddDataLevelPermissionWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_level_permission_white_list(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionWhiteListRequest,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_data_level_permission_white_list_with_options(request, runtime)

    async def add_data_level_permission_white_list_async(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionWhiteListRequest,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_data_level_permission_white_list_with_options_async(request, runtime)

    def add_share_report_with_options(
        self,
        request: quickbi_public_20220101_models.AddShareReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddShareReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_point):
            query['AuthPoint'] = request.auth_point
        if not UtilClient.is_unset(request.expire_date):
            query['ExpireDate'] = request.expire_date
        if not UtilClient.is_unset(request.share_to_id):
            query['ShareToId'] = request.share_to_id
        if not UtilClient.is_unset(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShareReport',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddShareReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_share_report_with_options_async(
        self,
        request: quickbi_public_20220101_models.AddShareReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddShareReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_point):
            query['AuthPoint'] = request.auth_point
        if not UtilClient.is_unset(request.expire_date):
            query['ExpireDate'] = request.expire_date
        if not UtilClient.is_unset(request.share_to_id):
            query['ShareToId'] = request.share_to_id
        if not UtilClient.is_unset(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShareReport',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddShareReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_share_report(
        self,
        request: quickbi_public_20220101_models.AddShareReportRequest,
    ) -> quickbi_public_20220101_models.AddShareReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_share_report_with_options(request, runtime)

    async def add_share_report_async(
        self,
        request: quickbi_public_20220101_models.AddShareReportRequest,
    ) -> quickbi_public_20220101_models.AddShareReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_share_report_with_options_async(request, runtime)

    def add_user_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not UtilClient.is_unset(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_with_options_async(
        self,
        request: quickbi_public_20220101_models.AddUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not UtilClient.is_unset(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user(
        self,
        request: quickbi_public_20220101_models.AddUserRequest,
    ) -> quickbi_public_20220101_models.AddUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_with_options(request, runtime)

    async def add_user_async(
        self,
        request: quickbi_public_20220101_models.AddUserRequest,
    ) -> quickbi_public_20220101_models.AddUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_with_options_async(request, runtime)

    def add_user_group_member_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserGroupMember',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_group_member_with_options_async(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserGroupMember',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_group_member(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMemberRequest,
    ) -> quickbi_public_20220101_models.AddUserGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_group_member_with_options(request, runtime)

    async def add_user_group_member_async(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMemberRequest,
    ) -> quickbi_public_20220101_models.AddUserGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_group_member_with_options_async(request, runtime)

    def add_user_group_members_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserGroupMembers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_group_members_with_options_async(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserGroupMembers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_group_members(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMembersRequest,
    ) -> quickbi_public_20220101_models.AddUserGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_group_members_with_options(request, runtime)

    async def add_user_group_members_async(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMembersRequest,
    ) -> quickbi_public_20220101_models.AddUserGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_group_members_with_options_async(request, runtime)

    def add_user_tag_meta_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserTagMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserTagMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserTagMeta',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserTagMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_tag_meta_with_options_async(
        self,
        request: quickbi_public_20220101_models.AddUserTagMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserTagMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserTagMeta',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserTagMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_tag_meta(
        self,
        request: quickbi_public_20220101_models.AddUserTagMetaRequest,
    ) -> quickbi_public_20220101_models.AddUserTagMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_tag_meta_with_options(request, runtime)

    async def add_user_tag_meta_async(
        self,
        request: quickbi_public_20220101_models.AddUserTagMetaRequest,
    ) -> quickbi_public_20220101_models.AddUserTagMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_tag_meta_with_options_async(request, runtime)

    def add_user_to_workspace_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserToWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserToWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserToWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_workspace_with_options_async(
        self,
        request: quickbi_public_20220101_models.AddUserToWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserToWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddUserToWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_workspace(
        self,
        request: quickbi_public_20220101_models.AddUserToWorkspaceRequest,
    ) -> quickbi_public_20220101_models.AddUserToWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_workspace_with_options(request, runtime)

    async def add_user_to_workspace_async(
        self,
        request: quickbi_public_20220101_models.AddUserToWorkspaceRequest,
    ) -> quickbi_public_20220101_models.AddUserToWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_workspace_with_options_async(request, runtime)

    def add_workspace_users_with_options(
        self,
        request: quickbi_public_20220101_models.AddWorkspaceUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddWorkspaceUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWorkspaceUsers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddWorkspaceUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_workspace_users_with_options_async(
        self,
        request: quickbi_public_20220101_models.AddWorkspaceUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddWorkspaceUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWorkspaceUsers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AddWorkspaceUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_workspace_users(
        self,
        request: quickbi_public_20220101_models.AddWorkspaceUsersRequest,
    ) -> quickbi_public_20220101_models.AddWorkspaceUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_workspace_users_with_options(request, runtime)

    async def add_workspace_users_async(
        self,
        request: quickbi_public_20220101_models.AddWorkspaceUsersRequest,
    ) -> quickbi_public_20220101_models.AddWorkspaceUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_workspace_users_with_options_async(request, runtime)

    def authorize_menu_with_options(
        self,
        request: quickbi_public_20220101_models.AuthorizeMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AuthorizeMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_points_value):
            query['AuthPointsValue'] = request.auth_points_value
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeMenu',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AuthorizeMenuResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_menu_with_options_async(
        self,
        request: quickbi_public_20220101_models.AuthorizeMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AuthorizeMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_points_value):
            query['AuthPointsValue'] = request.auth_points_value
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeMenu',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.AuthorizeMenuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_menu(
        self,
        request: quickbi_public_20220101_models.AuthorizeMenuRequest,
    ) -> quickbi_public_20220101_models.AuthorizeMenuResponse:
        runtime = util_models.RuntimeOptions()
        return self.authorize_menu_with_options(request, runtime)

    async def authorize_menu_async(
        self,
        request: quickbi_public_20220101_models.AuthorizeMenuRequest,
    ) -> quickbi_public_20220101_models.AuthorizeMenuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.authorize_menu_with_options_async(request, runtime)

    def cancel_authorization_menu_with_options(
        self,
        request: quickbi_public_20220101_models.CancelAuthorizationMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CancelAuthorizationMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAuthorizationMenu',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CancelAuthorizationMenuResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_authorization_menu_with_options_async(
        self,
        request: quickbi_public_20220101_models.CancelAuthorizationMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CancelAuthorizationMenuResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAuthorizationMenu',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CancelAuthorizationMenuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_authorization_menu(
        self,
        request: quickbi_public_20220101_models.CancelAuthorizationMenuRequest,
    ) -> quickbi_public_20220101_models.CancelAuthorizationMenuResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_authorization_menu_with_options(request, runtime)

    async def cancel_authorization_menu_async(
        self,
        request: quickbi_public_20220101_models.CancelAuthorizationMenuRequest,
    ) -> quickbi_public_20220101_models.CancelAuthorizationMenuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_authorization_menu_with_options_async(request, runtime)

    def cancel_collection_with_options(
        self,
        request: quickbi_public_20220101_models.CancelCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CancelCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCollection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CancelCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_collection_with_options_async(
        self,
        request: quickbi_public_20220101_models.CancelCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CancelCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCollection',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CancelCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_collection(
        self,
        request: quickbi_public_20220101_models.CancelCollectionRequest,
    ) -> quickbi_public_20220101_models.CancelCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_collection_with_options(request, runtime)

    async def cancel_collection_async(
        self,
        request: quickbi_public_20220101_models.CancelCollectionRequest,
    ) -> quickbi_public_20220101_models.CancelCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_collection_with_options_async(request, runtime)

    def cancel_report_share_with_options(
        self,
        request: quickbi_public_20220101_models.CancelReportShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CancelReportShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.share_to_ids):
            query['ShareToIds'] = request.share_to_ids
        if not UtilClient.is_unset(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelReportShare',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CancelReportShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_report_share_with_options_async(
        self,
        request: quickbi_public_20220101_models.CancelReportShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CancelReportShareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.share_to_ids):
            query['ShareToIds'] = request.share_to_ids
        if not UtilClient.is_unset(request.share_to_type):
            query['ShareToType'] = request.share_to_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelReportShare',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CancelReportShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_report_share(
        self,
        request: quickbi_public_20220101_models.CancelReportShareRequest,
    ) -> quickbi_public_20220101_models.CancelReportShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_report_share_with_options(request, runtime)

    async def cancel_report_share_async(
        self,
        request: quickbi_public_20220101_models.CancelReportShareRequest,
    ) -> quickbi_public_20220101_models.CancelReportShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_report_share_with_options_async(request, runtime)

    def change_visibility_model_with_options(
        self,
        request: quickbi_public_20220101_models.ChangeVisibilityModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ChangeVisibilityModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.show_only_with_access):
            query['ShowOnlyWithAccess'] = request.show_only_with_access
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeVisibilityModel',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ChangeVisibilityModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_visibility_model_with_options_async(
        self,
        request: quickbi_public_20220101_models.ChangeVisibilityModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ChangeVisibilityModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.menu_ids):
            query['MenuIds'] = request.menu_ids
        if not UtilClient.is_unset(request.show_only_with_access):
            query['ShowOnlyWithAccess'] = request.show_only_with_access
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeVisibilityModel',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ChangeVisibilityModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_visibility_model(
        self,
        request: quickbi_public_20220101_models.ChangeVisibilityModelRequest,
    ) -> quickbi_public_20220101_models.ChangeVisibilityModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_visibility_model_with_options(request, runtime)

    async def change_visibility_model_async(
        self,
        request: quickbi_public_20220101_models.ChangeVisibilityModelRequest,
    ) -> quickbi_public_20220101_models.ChangeVisibilityModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_visibility_model_with_options_async(request, runtime)

    def check_readable_with_options(
        self,
        request: quickbi_public_20220101_models.CheckReadableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CheckReadableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckReadable',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CheckReadableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_readable_with_options_async(
        self,
        request: quickbi_public_20220101_models.CheckReadableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CheckReadableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckReadable',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CheckReadableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_readable(
        self,
        request: quickbi_public_20220101_models.CheckReadableRequest,
    ) -> quickbi_public_20220101_models.CheckReadableResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_readable_with_options(request, runtime)

    async def check_readable_async(
        self,
        request: quickbi_public_20220101_models.CheckReadableRequest,
    ) -> quickbi_public_20220101_models.CheckReadableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_readable_with_options_async(request, runtime)

    def create_ticket_with_options(
        self,
        request: quickbi_public_20220101_models.CreateTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CreateTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.cmpt_id):
            query['CmptId'] = request.cmpt_id
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.global_param):
            query['GlobalParam'] = request.global_param
        if not UtilClient.is_unset(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.watermark_param):
            query['WatermarkParam'] = request.watermark_param
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTicket',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CreateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        request: quickbi_public_20220101_models.CreateTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CreateTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.cmpt_id):
            query['CmptId'] = request.cmpt_id
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.global_param):
            query['GlobalParam'] = request.global_param
        if not UtilClient.is_unset(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.watermark_param):
            query['WatermarkParam'] = request.watermark_param
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTicket',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CreateTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ticket(
        self,
        request: quickbi_public_20220101_models.CreateTicketRequest,
    ) -> quickbi_public_20220101_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ticket_with_options(request, runtime)

    async def create_ticket_async(
        self,
        request: quickbi_public_20220101_models.CreateTicketRequest,
    ) -> quickbi_public_20220101_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ticket_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: quickbi_public_20220101_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CreateUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        if not UtilClient.is_unset(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_group_with_options_async(
        self,
        request: quickbi_public_20220101_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CreateUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        if not UtilClient.is_unset(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.CreateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_group(
        self,
        request: quickbi_public_20220101_models.CreateUserGroupRequest,
    ) -> quickbi_public_20220101_models.CreateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: quickbi_public_20220101_models.CreateUserGroupRequest,
    ) -> quickbi_public_20220101_models.CreateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def delay_ticket_expire_time_with_options(
        self,
        request: quickbi_public_20220101_models.DelayTicketExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DelayTicketExpireTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelayTicketExpireTime',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DelayTicketExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delay_ticket_expire_time_with_options_async(
        self,
        request: quickbi_public_20220101_models.DelayTicketExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DelayTicketExpireTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelayTicketExpireTime',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DelayTicketExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delay_ticket_expire_time(
        self,
        request: quickbi_public_20220101_models.DelayTicketExpireTimeRequest,
    ) -> quickbi_public_20220101_models.DelayTicketExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delay_ticket_expire_time_with_options(request, runtime)

    async def delay_ticket_expire_time_async(
        self,
        request: quickbi_public_20220101_models.DelayTicketExpireTimeRequest,
    ) -> quickbi_public_20220101_models.DelayTicketExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delay_ticket_expire_time_with_options_async(request, runtime)

    def delete_data_level_permission_rule_users_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_user_model):
            query['DeleteUserModel'] = request.delete_user_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLevelPermissionRuleUsers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_level_permission_rule_users_with_options_async(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_user_model):
            query['DeleteUserModel'] = request.delete_user_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLevelPermissionRuleUsers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_level_permission_rule_users(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersRequest,
    ) -> quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_level_permission_rule_users_with_options(request, runtime)

    async def delete_data_level_permission_rule_users_async(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersRequest,
    ) -> quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_level_permission_rule_users_with_options_async(request, runtime)

    def delete_data_level_rule_config_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelRuleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteDataLevelRuleConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLevelRuleConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteDataLevelRuleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_level_rule_config_with_options_async(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelRuleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteDataLevelRuleConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLevelRuleConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteDataLevelRuleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_level_rule_config(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelRuleConfigRequest,
    ) -> quickbi_public_20220101_models.DeleteDataLevelRuleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_level_rule_config_with_options(request, runtime)

    async def delete_data_level_rule_config_async(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelRuleConfigRequest,
    ) -> quickbi_public_20220101_models.DeleteDataLevelRuleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_level_rule_config_with_options_async(request, runtime)

    def delete_ticket_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTicket',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ticket_with_options_async(
        self,
        request: quickbi_public_20220101_models.DeleteTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTicket',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ticket(
        self,
        request: quickbi_public_20220101_models.DeleteTicketRequest,
    ) -> quickbi_public_20220101_models.DeleteTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ticket_with_options(request, runtime)

    async def delete_ticket_async(
        self,
        request: quickbi_public_20220101_models.DeleteTicketRequest,
    ) -> quickbi_public_20220101_models.DeleteTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ticket_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.transfer_user_id):
            query['TransferUserId'] = request.transfer_user_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.transfer_user_id):
            query['TransferUserId'] = request.transfer_user_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: quickbi_public_20220101_models.DeleteUserRequest,
    ) -> quickbi_public_20220101_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserRequest,
    ) -> quickbi_public_20220101_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_from_workspace_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserFromWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserFromWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserFromWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserFromWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_from_workspace_with_options_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserFromWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserFromWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserFromWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserFromWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_from_workspace(
        self,
        request: quickbi_public_20220101_models.DeleteUserFromWorkspaceRequest,
    ) -> quickbi_public_20220101_models.DeleteUserFromWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_from_workspace_with_options(request, runtime)

    async def delete_user_from_workspace_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserFromWorkspaceRequest,
    ) -> quickbi_public_20220101_models.DeleteUserFromWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_from_workspace_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupRequest,
    ) -> quickbi_public_20220101_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupRequest,
    ) -> quickbi_public_20220101_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def delete_user_group_member_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroupMember',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_member_with_options_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroupMember',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group_member(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMemberRequest,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_member_with_options(request, runtime)

    async def delete_user_group_member_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMemberRequest,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_member_with_options_async(request, runtime)

    def delete_user_group_members_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroupMembers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_members_with_options_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroupMembers',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group_members(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMembersRequest,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_members_with_options(request, runtime)

    async def delete_user_group_members_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMembersRequest,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_members_with_options_async(request, runtime)

    def delete_user_tag_meta_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserTagMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserTagMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserTagMeta',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserTagMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_tag_meta_with_options_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserTagMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserTagMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserTagMeta',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.DeleteUserTagMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_tag_meta(
        self,
        request: quickbi_public_20220101_models.DeleteUserTagMetaRequest,
    ) -> quickbi_public_20220101_models.DeleteUserTagMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_tag_meta_with_options(request, runtime)

    async def delete_user_tag_meta_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserTagMetaRequest,
    ) -> quickbi_public_20220101_models.DeleteUserTagMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_tag_meta_with_options_async(request, runtime)

    def get_user_group_info_with_options(
        self,
        request: quickbi_public_20220101_models.GetUserGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.GetUserGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroupInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.GetUserGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_group_info_with_options_async(
        self,
        request: quickbi_public_20220101_models.GetUserGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.GetUserGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroupInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.GetUserGroupInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_group_info(
        self,
        request: quickbi_public_20220101_models.GetUserGroupInfoRequest,
    ) -> quickbi_public_20220101_models.GetUserGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_info_with_options(request, runtime)

    async def get_user_group_info_async(
        self,
        request: quickbi_public_20220101_models.GetUserGroupInfoRequest,
    ) -> quickbi_public_20220101_models.GetUserGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_group_info_with_options_async(request, runtime)

    def list_by_user_group_id_with_options(
        self,
        request: quickbi_public_20220101_models.ListByUserGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListByUserGroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListByUserGroupId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListByUserGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_by_user_group_id_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListByUserGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListByUserGroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListByUserGroupId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListByUserGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_by_user_group_id(
        self,
        request: quickbi_public_20220101_models.ListByUserGroupIdRequest,
    ) -> quickbi_public_20220101_models.ListByUserGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_by_user_group_id_with_options(request, runtime)

    async def list_by_user_group_id_async(
        self,
        request: quickbi_public_20220101_models.ListByUserGroupIdRequest,
    ) -> quickbi_public_20220101_models.ListByUserGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_by_user_group_id_with_options_async(request, runtime)

    def list_collections_with_options(
        self,
        request: quickbi_public_20220101_models.ListCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListCollectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollections',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_collections_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListCollectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollections',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_collections(
        self,
        request: quickbi_public_20220101_models.ListCollectionsRequest,
    ) -> quickbi_public_20220101_models.ListCollectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_collections_with_options(request, runtime)

    async def list_collections_async(
        self,
        request: quickbi_public_20220101_models.ListCollectionsRequest,
    ) -> quickbi_public_20220101_models.ListCollectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_collections_with_options_async(request, runtime)

    def list_cube_data_level_permission_config_with_options(
        self,
        request: quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCubeDataLevelPermissionConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cube_data_level_permission_config_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCubeDataLevelPermissionConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cube_data_level_permission_config(
        self,
        request: quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigRequest,
    ) -> quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cube_data_level_permission_config_with_options(request, runtime)

    async def list_cube_data_level_permission_config_async(
        self,
        request: quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigRequest,
    ) -> quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cube_data_level_permission_config_with_options_async(request, runtime)

    def list_data_level_permission_white_list_with_options(
        self,
        request: quickbi_public_20220101_models.ListDataLevelPermissionWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListDataLevelPermissionWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLevelPermissionWhiteList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListDataLevelPermissionWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_level_permission_white_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListDataLevelPermissionWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListDataLevelPermissionWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLevelPermissionWhiteList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListDataLevelPermissionWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_level_permission_white_list(
        self,
        request: quickbi_public_20220101_models.ListDataLevelPermissionWhiteListRequest,
    ) -> quickbi_public_20220101_models.ListDataLevelPermissionWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_level_permission_white_list_with_options(request, runtime)

    async def list_data_level_permission_white_list_async(
        self,
        request: quickbi_public_20220101_models.ListDataLevelPermissionWhiteListRequest,
    ) -> quickbi_public_20220101_models.ListDataLevelPermissionWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_level_permission_white_list_with_options_async(request, runtime)

    def list_favorite_reports_with_options(
        self,
        request: quickbi_public_20220101_models.ListFavoriteReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListFavoriteReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tree_type):
            query['TreeType'] = request.tree_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFavoriteReports',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListFavoriteReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_favorite_reports_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListFavoriteReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListFavoriteReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tree_type):
            query['TreeType'] = request.tree_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFavoriteReports',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListFavoriteReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_favorite_reports(
        self,
        request: quickbi_public_20220101_models.ListFavoriteReportsRequest,
    ) -> quickbi_public_20220101_models.ListFavoriteReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_favorite_reports_with_options(request, runtime)

    async def list_favorite_reports_async(
        self,
        request: quickbi_public_20220101_models.ListFavoriteReportsRequest,
    ) -> quickbi_public_20220101_models.ListFavoriteReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_favorite_reports_with_options_async(request, runtime)

    def list_portal_menu_authorization_with_options(
        self,
        request: quickbi_public_20220101_models.ListPortalMenuAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListPortalMenuAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenuAuthorization',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListPortalMenuAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_portal_menu_authorization_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListPortalMenuAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListPortalMenuAuthorizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenuAuthorization',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListPortalMenuAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_portal_menu_authorization(
        self,
        request: quickbi_public_20220101_models.ListPortalMenuAuthorizationRequest,
    ) -> quickbi_public_20220101_models.ListPortalMenuAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_portal_menu_authorization_with_options(request, runtime)

    async def list_portal_menu_authorization_async(
        self,
        request: quickbi_public_20220101_models.ListPortalMenuAuthorizationRequest,
    ) -> quickbi_public_20220101_models.ListPortalMenuAuthorizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_portal_menu_authorization_with_options_async(request, runtime)

    def list_portal_menus_with_options(
        self,
        request: quickbi_public_20220101_models.ListPortalMenusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListPortalMenusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListPortalMenusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_portal_menus_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListPortalMenusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListPortalMenusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_portal_id):
            query['DataPortalId'] = request.data_portal_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPortalMenus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListPortalMenusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_portal_menus(
        self,
        request: quickbi_public_20220101_models.ListPortalMenusRequest,
    ) -> quickbi_public_20220101_models.ListPortalMenusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_portal_menus_with_options(request, runtime)

    async def list_portal_menus_async(
        self,
        request: quickbi_public_20220101_models.ListPortalMenusRequest,
    ) -> quickbi_public_20220101_models.ListPortalMenusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_portal_menus_with_options_async(request, runtime)

    def list_recent_view_reports_with_options(
        self,
        request: quickbi_public_20220101_models.ListRecentViewReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListRecentViewReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.offset_day):
            query['OffsetDay'] = request.offset_day
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.tree_type):
            query['TreeType'] = request.tree_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecentViewReports',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListRecentViewReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recent_view_reports_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListRecentViewReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListRecentViewReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.offset_day):
            query['OffsetDay'] = request.offset_day
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.tree_type):
            query['TreeType'] = request.tree_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecentViewReports',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListRecentViewReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recent_view_reports(
        self,
        request: quickbi_public_20220101_models.ListRecentViewReportsRequest,
    ) -> quickbi_public_20220101_models.ListRecentViewReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_recent_view_reports_with_options(request, runtime)

    async def list_recent_view_reports_async(
        self,
        request: quickbi_public_20220101_models.ListRecentViewReportsRequest,
    ) -> quickbi_public_20220101_models.ListRecentViewReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_recent_view_reports_with_options_async(request, runtime)

    def list_shared_reports_with_options(
        self,
        request: quickbi_public_20220101_models.ListSharedReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListSharedReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tree_type):
            query['TreeType'] = request.tree_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedReports',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListSharedReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_shared_reports_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListSharedReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListSharedReportsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tree_type):
            query['TreeType'] = request.tree_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedReports',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListSharedReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_shared_reports(
        self,
        request: quickbi_public_20220101_models.ListSharedReportsRequest,
    ) -> quickbi_public_20220101_models.ListSharedReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_shared_reports_with_options(request, runtime)

    async def list_shared_reports_async(
        self,
        request: quickbi_public_20220101_models.ListSharedReportsRequest,
    ) -> quickbi_public_20220101_models.ListSharedReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_shared_reports_with_options_async(request, runtime)

    def list_user_groups_by_user_id_with_options(
        self,
        request: quickbi_public_20220101_models.ListUserGroupsByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListUserGroupsByUserIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsByUserId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListUserGroupsByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_by_user_id_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListUserGroupsByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListUserGroupsByUserIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsByUserId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ListUserGroupsByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups_by_user_id(
        self,
        request: quickbi_public_20220101_models.ListUserGroupsByUserIdRequest,
    ) -> quickbi_public_20220101_models.ListUserGroupsByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_by_user_id_with_options(request, runtime)

    async def list_user_groups_by_user_id_async(
        self,
        request: quickbi_public_20220101_models.ListUserGroupsByUserIdRequest,
    ) -> quickbi_public_20220101_models.ListUserGroupsByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_by_user_id_with_options_async(request, runtime)

    def query_data_service_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDataServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.conditions):
            query['Conditions'] = request.conditions
        if not UtilClient.is_unset(request.return_fields):
            query['ReturnFields'] = request.return_fields
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataService',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDataServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_service_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDataServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.conditions):
            query['Conditions'] = request.conditions
        if not UtilClient.is_unset(request.return_fields):
            query['ReturnFields'] = request.return_fields
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataService',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDataServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_service(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceRequest,
    ) -> quickbi_public_20220101_models.QueryDataServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_data_service_with_options(request, runtime)

    async def query_data_service_async(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceRequest,
    ) -> quickbi_public_20220101_models.QueryDataServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_data_service_with_options_async(request, runtime)

    def query_dataset_detail_info_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDatasetDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetDetailInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetDetailInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetDetailInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_detail_info_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetDetailInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetDetailInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetDetailInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_detail_info(
        self,
        request: quickbi_public_20220101_models.QueryDatasetDetailInfoRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_detail_info_with_options(request, runtime)

    async def query_dataset_detail_info_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetDetailInfoRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_detail_info_with_options_async(request, runtime)

    def query_dataset_info_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDatasetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_info_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_info(
        self,
        request: quickbi_public_20220101_models.QueryDatasetInfoRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_info_with_options(request, runtime)

    async def query_dataset_info_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetInfoRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_info_with_options_async(request, runtime)

    def query_dataset_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDatasetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.with_children):
            query['WithChildren'] = request.with_children
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.with_children):
            query['WithChildren'] = request.with_children
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_list(
        self,
        request: quickbi_public_20220101_models.QueryDatasetListRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_list_with_options(request, runtime)

    async def query_dataset_list_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetListRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_list_with_options_async(request, runtime)

    def query_dataset_switch_info_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDatasetSwitchInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetSwitchInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetSwitchInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetSwitchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_switch_info_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetSwitchInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetSwitchInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDatasetSwitchInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryDatasetSwitchInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset_switch_info(
        self,
        request: quickbi_public_20220101_models.QueryDatasetSwitchInfoRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetSwitchInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_switch_info_with_options(request, runtime)

    async def query_dataset_switch_info_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetSwitchInfoRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetSwitchInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_switch_info_with_options_async(request, runtime)

    def query_embedded_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryEmbeddedInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryEmbeddedInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryEmbeddedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_embedded_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryEmbeddedInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryEmbeddedInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryEmbeddedInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_embedded_info(self) -> quickbi_public_20220101_models.QueryEmbeddedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_embedded_info_with_options(runtime)

    async def query_embedded_info_async(self) -> quickbi_public_20220101_models.QueryEmbeddedInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_embedded_info_with_options_async(runtime)

    def query_embedded_staus_with_options(
        self,
        request: quickbi_public_20220101_models.QueryEmbeddedStausRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryEmbeddedStausResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEmbeddedStaus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryEmbeddedStausResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_embedded_staus_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryEmbeddedStausRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryEmbeddedStausResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEmbeddedStaus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryEmbeddedStausResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_embedded_staus(
        self,
        request: quickbi_public_20220101_models.QueryEmbeddedStausRequest,
    ) -> quickbi_public_20220101_models.QueryEmbeddedStausResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_embedded_staus_with_options(request, runtime)

    async def query_embedded_staus_async(
        self,
        request: quickbi_public_20220101_models.QueryEmbeddedStausRequest,
    ) -> quickbi_public_20220101_models.QueryEmbeddedStausResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_embedded_staus_with_options_async(request, runtime)

    def query_organization_workspace_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationWorkspaceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryOrganizationWorkspaceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrganizationWorkspaceList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryOrganizationWorkspaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_organization_workspace_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationWorkspaceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryOrganizationWorkspaceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrganizationWorkspaceList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryOrganizationWorkspaceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_organization_workspace_list(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationWorkspaceListRequest,
    ) -> quickbi_public_20220101_models.QueryOrganizationWorkspaceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_organization_workspace_list_with_options(request, runtime)

    async def query_organization_workspace_list_async(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationWorkspaceListRequest,
    ) -> quickbi_public_20220101_models.QueryOrganizationWorkspaceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_organization_workspace_list_with_options_async(request, runtime)

    def query_readable_resources_list_by_user_id_with_options(
        self,
        request: quickbi_public_20220101_models.QueryReadableResourcesListByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryReadableResourcesListByUserIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReadableResourcesListByUserId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryReadableResourcesListByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_readable_resources_list_by_user_id_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryReadableResourcesListByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryReadableResourcesListByUserIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReadableResourcesListByUserId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryReadableResourcesListByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_readable_resources_list_by_user_id(
        self,
        request: quickbi_public_20220101_models.QueryReadableResourcesListByUserIdRequest,
    ) -> quickbi_public_20220101_models.QueryReadableResourcesListByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_readable_resources_list_by_user_id_with_options(request, runtime)

    async def query_readable_resources_list_by_user_id_async(
        self,
        request: quickbi_public_20220101_models.QueryReadableResourcesListByUserIdRequest,
    ) -> quickbi_public_20220101_models.QueryReadableResourcesListByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_readable_resources_list_by_user_id_with_options_async(request, runtime)

    def query_share_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryShareListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryShareListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryShareList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryShareListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_share_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryShareListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryShareListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryShareList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryShareListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_share_list(
        self,
        request: quickbi_public_20220101_models.QueryShareListRequest,
    ) -> quickbi_public_20220101_models.QueryShareListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_share_list_with_options(request, runtime)

    async def query_share_list_async(
        self,
        request: quickbi_public_20220101_models.QueryShareListRequest,
    ) -> quickbi_public_20220101_models.QueryShareListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_share_list_with_options_async(request, runtime)

    def query_shares_to_user_list_with_options(
        self,
        request: quickbi_public_20220101_models.QuerySharesToUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QuerySharesToUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySharesToUserList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QuerySharesToUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_shares_to_user_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.QuerySharesToUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QuerySharesToUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySharesToUserList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QuerySharesToUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_shares_to_user_list(
        self,
        request: quickbi_public_20220101_models.QuerySharesToUserListRequest,
    ) -> quickbi_public_20220101_models.QuerySharesToUserListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_shares_to_user_list_with_options(request, runtime)

    async def query_shares_to_user_list_async(
        self,
        request: quickbi_public_20220101_models.QuerySharesToUserListRequest,
    ) -> quickbi_public_20220101_models.QuerySharesToUserListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_shares_to_user_list_with_options_async(request, runtime)

    def query_ticket_info_with_options(
        self,
        request: quickbi_public_20220101_models.QueryTicketInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryTicketInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTicketInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryTicketInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ticket_info_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryTicketInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryTicketInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTicketInfo',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryTicketInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ticket_info(
        self,
        request: quickbi_public_20220101_models.QueryTicketInfoRequest,
    ) -> quickbi_public_20220101_models.QueryTicketInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_ticket_info_with_options(request, runtime)

    async def query_ticket_info_async(
        self,
        request: quickbi_public_20220101_models.QueryTicketInfoRequest,
    ) -> quickbi_public_20220101_models.QueryTicketInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_ticket_info_with_options_async(request, runtime)

    def query_user_group_list_by_parent_id_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupListByParentIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserGroupListByParentIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserGroupListByParentId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserGroupListByParentIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_group_list_by_parent_id_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupListByParentIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserGroupListByParentIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_user_group_id):
            query['ParentUserGroupId'] = request.parent_user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserGroupListByParentId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserGroupListByParentIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_group_list_by_parent_id(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupListByParentIdRequest,
    ) -> quickbi_public_20220101_models.QueryUserGroupListByParentIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_group_list_by_parent_id_with_options(request, runtime)

    async def query_user_group_list_by_parent_id_async(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupListByParentIdRequest,
    ) -> quickbi_public_20220101_models.QueryUserGroupListByParentIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_group_list_by_parent_id_with_options_async(request, runtime)

    def query_user_group_member_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserGroupMember',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_group_member_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserGroupMemberResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserGroupMember',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_group_member(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupMemberRequest,
    ) -> quickbi_public_20220101_models.QueryUserGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_group_member_with_options(request, runtime)

    async def query_user_group_member_async(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupMemberRequest,
    ) -> quickbi_public_20220101_models.QueryUserGroupMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_group_member_with_options_async(request, runtime)

    def query_user_info_by_account_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserInfoByAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserInfoByAccount',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserInfoByAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_info_by_account_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserInfoByAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserInfoByAccount',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserInfoByAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_info_by_account(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByAccountRequest,
    ) -> quickbi_public_20220101_models.QueryUserInfoByAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_info_by_account_with_options(request, runtime)

    async def query_user_info_by_account_async(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByAccountRequest,
    ) -> quickbi_public_20220101_models.QueryUserInfoByAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_info_by_account_with_options_async(request, runtime)

    def query_user_info_by_user_id_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserInfoByUserIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserInfoByUserId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserInfoByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_info_by_user_id_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserInfoByUserIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserInfoByUserId',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserInfoByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_info_by_user_id(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByUserIdRequest,
    ) -> quickbi_public_20220101_models.QueryUserInfoByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_info_by_user_id_with_options(request, runtime)

    async def query_user_info_by_user_id_async(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByUserIdRequest,
    ) -> quickbi_public_20220101_models.QueryUserInfoByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_info_by_user_id_with_options_async(request, runtime)

    def query_user_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_list(
        self,
        request: quickbi_public_20220101_models.QueryUserListRequest,
    ) -> quickbi_public_20220101_models.QueryUserListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_list_with_options(request, runtime)

    async def query_user_list_async(
        self,
        request: quickbi_public_20220101_models.QueryUserListRequest,
    ) -> quickbi_public_20220101_models.QueryUserListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_list_with_options_async(request, runtime)

    def query_user_role_info_in_workspace_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserRoleInfoInWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_role_info_in_workspace_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserRoleInfoInWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_role_info_in_workspace(
        self,
        request: quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceRequest,
    ) -> quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_role_info_in_workspace_with_options(request, runtime)

    async def query_user_role_info_in_workspace_async(
        self,
        request: quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceRequest,
    ) -> quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_role_info_in_workspace_with_options_async(request, runtime)

    def query_user_tag_meta_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserTagMetaListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryUserTagMetaList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserTagMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_tag_meta_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserTagMetaListResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryUserTagMetaList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserTagMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_tag_meta_list(self) -> quickbi_public_20220101_models.QueryUserTagMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_tag_meta_list_with_options(runtime)

    async def query_user_tag_meta_list_async(self) -> quickbi_public_20220101_models.QueryUserTagMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_tag_meta_list_with_options_async(runtime)

    def query_user_tag_value_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserTagValueListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserTagValueListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserTagValueList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserTagValueListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_tag_value_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryUserTagValueListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserTagValueListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserTagValueList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryUserTagValueListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_tag_value_list(
        self,
        request: quickbi_public_20220101_models.QueryUserTagValueListRequest,
    ) -> quickbi_public_20220101_models.QueryUserTagValueListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_tag_value_list_with_options(request, runtime)

    async def query_user_tag_value_list_async(
        self,
        request: quickbi_public_20220101_models.QueryUserTagValueListRequest,
    ) -> quickbi_public_20220101_models.QueryUserTagValueListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_tag_value_list_with_options_async(request, runtime)

    def query_works_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorks',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_works_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorks',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_works(
        self,
        request: quickbi_public_20220101_models.QueryWorksRequest,
    ) -> quickbi_public_20220101_models.QueryWorksResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_works_with_options(request, runtime)

    async def query_works_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksRequest,
    ) -> quickbi_public_20220101_models.QueryWorksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_works_with_options_async(request, runtime)

    def query_works_blood_relationship_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorksBloodRelationshipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksBloodRelationshipResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorksBloodRelationship',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksBloodRelationshipResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_works_blood_relationship_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksBloodRelationshipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksBloodRelationshipResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorksBloodRelationship',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksBloodRelationshipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_works_blood_relationship(
        self,
        request: quickbi_public_20220101_models.QueryWorksBloodRelationshipRequest,
    ) -> quickbi_public_20220101_models.QueryWorksBloodRelationshipResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_works_blood_relationship_with_options(request, runtime)

    async def query_works_blood_relationship_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksBloodRelationshipRequest,
    ) -> quickbi_public_20220101_models.QueryWorksBloodRelationshipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_works_blood_relationship_with_options_async(request, runtime)

    def query_works_by_organization_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorksByOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksByOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not UtilClient.is_unset(request.works_type):
            query['WorksType'] = request.works_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorksByOrganization',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksByOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_works_by_organization_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksByOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksByOrganizationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not UtilClient.is_unset(request.works_type):
            query['WorksType'] = request.works_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorksByOrganization',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksByOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_works_by_organization(
        self,
        request: quickbi_public_20220101_models.QueryWorksByOrganizationRequest,
    ) -> quickbi_public_20220101_models.QueryWorksByOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_works_by_organization_with_options(request, runtime)

    async def query_works_by_organization_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksByOrganizationRequest,
    ) -> quickbi_public_20220101_models.QueryWorksByOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_works_by_organization_with_options_async(request, runtime)

    def query_works_by_workspace_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorksByWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksByWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not UtilClient.is_unset(request.works_type):
            query['WorksType'] = request.works_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorksByWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksByWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_works_by_workspace_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksByWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksByWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not UtilClient.is_unset(request.works_type):
            query['WorksType'] = request.works_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorksByWorkspace',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorksByWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_works_by_workspace(
        self,
        request: quickbi_public_20220101_models.QueryWorksByWorkspaceRequest,
    ) -> quickbi_public_20220101_models.QueryWorksByWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_works_by_workspace_with_options(request, runtime)

    async def query_works_by_workspace_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksByWorkspaceRequest,
    ) -> quickbi_public_20220101_models.QueryWorksByWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_works_by_workspace_with_options_async(request, runtime)

    def query_workspace_user_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorkspaceUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorkspaceUserList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorkspaceUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_workspace_user_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorkspaceUserListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorkspaceUserList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.QueryWorkspaceUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_workspace_user_list(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceUserListRequest,
    ) -> quickbi_public_20220101_models.QueryWorkspaceUserListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_workspace_user_list_with_options(request, runtime)

    async def query_workspace_user_list_async(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceUserListRequest,
    ) -> quickbi_public_20220101_models.QueryWorkspaceUserListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_workspace_user_list_with_options_async(request, runtime)

    def result_callback_with_options(
        self,
        request: quickbi_public_20220101_models.ResultCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ResultCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.handle_reason):
            query['HandleReason'] = request.handle_reason
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResultCallback',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ResultCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def result_callback_with_options_async(
        self,
        request: quickbi_public_20220101_models.ResultCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ResultCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.handle_reason):
            query['HandleReason'] = request.handle_reason
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResultCallback',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.ResultCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def result_callback(
        self,
        request: quickbi_public_20220101_models.ResultCallbackRequest,
    ) -> quickbi_public_20220101_models.ResultCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.result_callback_with_options(request, runtime)

    async def result_callback_async(
        self,
        request: quickbi_public_20220101_models.ResultCallbackRequest,
    ) -> quickbi_public_20220101_models.ResultCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.result_callback_with_options_async(request, runtime)

    def save_favorites_with_options(
        self,
        request: quickbi_public_20220101_models.SaveFavoritesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SaveFavoritesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveFavorites',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SaveFavoritesResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_favorites_with_options_async(
        self,
        request: quickbi_public_20220101_models.SaveFavoritesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SaveFavoritesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveFavorites',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SaveFavoritesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_favorites(
        self,
        request: quickbi_public_20220101_models.SaveFavoritesRequest,
    ) -> quickbi_public_20220101_models.SaveFavoritesResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_favorites_with_options(request, runtime)

    async def save_favorites_async(
        self,
        request: quickbi_public_20220101_models.SaveFavoritesRequest,
    ) -> quickbi_public_20220101_models.SaveFavoritesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_favorites_with_options_async(request, runtime)

    def set_data_level_permission_extra_config_with_options(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.miss_hit_policy):
            query['MissHitPolicy'] = request.miss_hit_policy
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataLevelPermissionExtraConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_data_level_permission_extra_config_with_options_async(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.miss_hit_policy):
            query['MissHitPolicy'] = request.miss_hit_policy
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataLevelPermissionExtraConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_data_level_permission_extra_config(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigRequest,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_data_level_permission_extra_config_with_options(request, runtime)

    async def set_data_level_permission_extra_config_async(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigRequest,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_data_level_permission_extra_config_with_options_async(request, runtime)

    def set_data_level_permission_rule_config_with_options(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_model):
            query['RuleModel'] = request.rule_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataLevelPermissionRuleConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_data_level_permission_rule_config_with_options_async(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule_model):
            query['RuleModel'] = request.rule_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataLevelPermissionRuleConfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_data_level_permission_rule_config(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigRequest,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_data_level_permission_rule_config_with_options(request, runtime)

    async def set_data_level_permission_rule_config_async(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigRequest,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_data_level_permission_rule_config_with_options_async(request, runtime)

    def set_data_level_permission_white_list_with_options(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.white_list_model):
            query['WhiteListModel'] = request.white_list_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataLevelPermissionWhiteList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SetDataLevelPermissionWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_data_level_permission_white_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.white_list_model):
            query['WhiteListModel'] = request.white_list_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataLevelPermissionWhiteList',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.SetDataLevelPermissionWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_data_level_permission_white_list(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionWhiteListRequest,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_data_level_permission_white_list_with_options(request, runtime)

    async def set_data_level_permission_white_list_async(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionWhiteListRequest,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_data_level_permission_white_list_with_options_async(request, runtime)

    def update_data_level_permission_status_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateDataLevelPermissionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateDataLevelPermissionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.is_open):
            query['IsOpen'] = request.is_open
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataLevelPermissionStatus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateDataLevelPermissionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_level_permission_status_with_options_async(
        self,
        request: quickbi_public_20220101_models.UpdateDataLevelPermissionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateDataLevelPermissionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.is_open):
            query['IsOpen'] = request.is_open
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataLevelPermissionStatus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateDataLevelPermissionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_level_permission_status(
        self,
        request: quickbi_public_20220101_models.UpdateDataLevelPermissionStatusRequest,
    ) -> quickbi_public_20220101_models.UpdateDataLevelPermissionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_data_level_permission_status_with_options(request, runtime)

    async def update_data_level_permission_status_async(
        self,
        request: quickbi_public_20220101_models.UpdateDataLevelPermissionStatusRequest,
    ) -> quickbi_public_20220101_models.UpdateDataLevelPermissionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_data_level_permission_status_with_options_async(request, runtime)

    def update_embedded_status_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateEmbeddedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateEmbeddedStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEmbeddedStatus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateEmbeddedStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_embedded_status_with_options_async(
        self,
        request: quickbi_public_20220101_models.UpdateEmbeddedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateEmbeddedStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.third_part_auth_flag):
            query['ThirdPartAuthFlag'] = request.third_part_auth_flag
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEmbeddedStatus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateEmbeddedStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_embedded_status(
        self,
        request: quickbi_public_20220101_models.UpdateEmbeddedStatusRequest,
    ) -> quickbi_public_20220101_models.UpdateEmbeddedStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_embedded_status_with_options(request, runtime)

    async def update_embedded_status_async(
        self,
        request: quickbi_public_20220101_models.UpdateEmbeddedStatusRequest,
    ) -> quickbi_public_20220101_models.UpdateEmbeddedStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_embedded_status_with_options_async(request, runtime)

    def update_ticket_num_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateTicketNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateTicketNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        if not UtilClient.is_unset(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTicketNum',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateTicketNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ticket_num_with_options_async(
        self,
        request: quickbi_public_20220101_models.UpdateTicketNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateTicketNumResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket):
            query['Ticket'] = request.ticket
        if not UtilClient.is_unset(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTicketNum',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateTicketNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ticket_num(
        self,
        request: quickbi_public_20220101_models.UpdateTicketNumRequest,
    ) -> quickbi_public_20220101_models.UpdateTicketNumResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ticket_num_with_options(request, runtime)

    async def update_ticket_num_async(
        self,
        request: quickbi_public_20220101_models.UpdateTicketNumRequest,
    ) -> quickbi_public_20220101_models.UpdateTicketNumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ticket_num_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not UtilClient.is_unset(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not UtilClient.is_unset(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: quickbi_public_20220101_models.UpdateUserRequest,
    ) -> quickbi_public_20220101_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserRequest,
    ) -> quickbi_public_20220101_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_group_with_options_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_group_description):
            query['UserGroupDescription'] = request.user_group_description
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_group(
        self,
        request: quickbi_public_20220101_models.UpdateUserGroupRequest,
    ) -> quickbi_public_20220101_models.UpdateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    async def update_user_group_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserGroupRequest,
    ) -> quickbi_public_20220101_models.UpdateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_group_with_options_async(request, runtime)

    def update_user_tag_meta_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserTagMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserTagMeta',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserTagMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_tag_meta_with_options_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserTagMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_description):
            query['TagDescription'] = request.tag_description
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserTagMeta',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserTagMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_tag_meta(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagMetaRequest,
    ) -> quickbi_public_20220101_models.UpdateUserTagMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_tag_meta_with_options(request, runtime)

    async def update_user_tag_meta_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagMetaRequest,
    ) -> quickbi_public_20220101_models.UpdateUserTagMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_tag_meta_with_options_async(request, runtime)

    def update_user_tag_value_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserTagValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserTagValue',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserTagValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_tag_value_with_options_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserTagValueResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserTagValue',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateUserTagValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_tag_value(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagValueRequest,
    ) -> quickbi_public_20220101_models.UpdateUserTagValueResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_tag_value_with_options(request, runtime)

    async def update_user_tag_value_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagValueRequest,
    ) -> quickbi_public_20220101_models.UpdateUserTagValueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_tag_value_with_options_async(request, runtime)

    def update_workspace_user_role_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUserRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUserRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceUserRole',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateWorkspaceUserRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_user_role_with_options_async(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUserRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUserRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceUserRole',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateWorkspaceUserRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace_user_role(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUserRoleRequest,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUserRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_user_role_with_options(request, runtime)

    async def update_workspace_user_role_async(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUserRoleRequest,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUserRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_workspace_user_role_with_options_async(request, runtime)

    def update_workspace_users_role_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUsersRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUsersRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceUsersRole',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateWorkspaceUsersRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_users_role_with_options_async(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUsersRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUsersRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkspaceUsersRole',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.UpdateWorkspaceUsersRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace_users_role(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUsersRoleRequest,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUsersRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_users_role_with_options(request, runtime)

    async def update_workspace_users_role_async(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUsersRoleRequest,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUsersRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_workspace_users_role_with_options_async(request, runtime)

    def withdraw_all_user_groups_with_options(
        self,
        request: quickbi_public_20220101_models.WithdrawAllUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.WithdrawAllUserGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WithdrawAllUserGroups',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.WithdrawAllUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def withdraw_all_user_groups_with_options_async(
        self,
        request: quickbi_public_20220101_models.WithdrawAllUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.WithdrawAllUserGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WithdrawAllUserGroups',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            quickbi_public_20220101_models.WithdrawAllUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def withdraw_all_user_groups(
        self,
        request: quickbi_public_20220101_models.WithdrawAllUserGroupsRequest,
    ) -> quickbi_public_20220101_models.WithdrawAllUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.withdraw_all_user_groups_with_options(request, runtime)

    async def withdraw_all_user_groups_async(
        self,
        request: quickbi_public_20220101_models.WithdrawAllUserGroupsRequest,
    ) -> quickbi_public_20220101_models.WithdrawAllUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.withdraw_all_user_groups_with_options_async(request, runtime)
