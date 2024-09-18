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
        """
        @summary Add selected groups of people incrementally for a single row and column permission rule.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.\\n
        
        @param request: AddDataLevelPermissionRuleUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDataLevelPermissionRuleUsersResponse
        """
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
        """
        @summary Add selected groups of people incrementally for a single row and column permission rule.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.\\n
        
        @param request: AddDataLevelPermissionRuleUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDataLevelPermissionRuleUsersResponse
        """
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
        """
        @summary Add selected groups of people incrementally for a single row and column permission rule.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.\\n
        
        @param request: AddDataLevelPermissionRuleUsersRequest
        @return: AddDataLevelPermissionRuleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_data_level_permission_rule_users_with_options(request, runtime)

    async def add_data_level_permission_rule_users_async(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersRequest,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionRuleUsersResponse:
        """
        @summary Add selected groups of people incrementally for a single row and column permission rule.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.\\n
        
        @param request: AddDataLevelPermissionRuleUsersRequest
        @return: AddDataLevelPermissionRuleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_data_level_permission_rule_users_with_options_async(request, runtime)

    def add_data_level_permission_white_list_with_options(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionWhiteListResponse:
        """
        @summary 43342**435,1553a****41231
        
        @description ROW_LEVEL
        
        @param request: AddDataLevelPermissionWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDataLevelPermissionWhiteListResponse
        """
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
        """
        @summary 43342**435,1553a****41231
        
        @description ROW_LEVEL
        
        @param request: AddDataLevelPermissionWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDataLevelPermissionWhiteListResponse
        """
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
        """
        @summary 43342**435,1553a****41231
        
        @description ROW_LEVEL
        
        @param request: AddDataLevelPermissionWhiteListRequest
        @return: AddDataLevelPermissionWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_data_level_permission_white_list_with_options(request, runtime)

    async def add_data_level_permission_white_list_async(
        self,
        request: quickbi_public_20220101_models.AddDataLevelPermissionWhiteListRequest,
    ) -> quickbi_public_20220101_models.AddDataLevelPermissionWhiteListResponse:
        """
        @summary 43342**435,1553a****41231
        
        @description ROW_LEVEL
        
        @param request: AddDataLevelPermissionWhiteListRequest
        @return: AddDataLevelPermissionWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_data_level_permission_white_list_with_options_async(request, runtime)

    def add_share_report_with_options(
        self,
        request: quickbi_public_20220101_models.AddShareReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddShareReportResponse:
        """
        @summary Add a sharing configuration for data works.
        
        @param request: AddShareReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShareReportResponse
        """
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
        """
        @summary Add a sharing configuration for data works.
        
        @param request: AddShareReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShareReportResponse
        """
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
        """
        @summary Add a sharing configuration for data works.
        
        @param request: AddShareReportRequest
        @return: AddShareReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_share_report_with_options(request, runtime)

    async def add_share_report_async(
        self,
        request: quickbi_public_20220101_models.AddShareReportRequest,
    ) -> quickbi_public_20220101_models.AddShareReportResponse:
        """
        @summary Add a sharing configuration for data works.
        
        @param request: AddShareReportRequest
        @return: AddShareReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_share_report_with_options_async(request, runtime)

    def add_user_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserResponse:
        """
        @summary auditing
        
        @param request: AddUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserResponse
        """
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
        body = {}
        if not UtilClient.is_unset(request.role_ids):
            body['RoleIds'] = request.role_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary auditing
        
        @param request: AddUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserResponse
        """
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
        body = {}
        if not UtilClient.is_unset(request.role_ids):
            body['RoleIds'] = request.role_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary auditing
        
        @param request: AddUserRequest
        @return: AddUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_with_options(request, runtime)

    async def add_user_async(
        self,
        request: quickbi_public_20220101_models.AddUserRequest,
    ) -> quickbi_public_20220101_models.AddUserResponse:
        """
        @summary auditing
        
        @param request: AddUserRequest
        @return: AddUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_with_options_async(request, runtime)

    def add_user_group_member_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserGroupMemberResponse:
        """
        @summary The ID of the request.
        
        @param request: AddUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserGroupMemberResponse
        """
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
        """
        @summary The ID of the request.
        
        @param request: AddUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserGroupMemberResponse
        """
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
        """
        @summary The ID of the request.
        
        @param request: AddUserGroupMemberRequest
        @return: AddUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_group_member_with_options(request, runtime)

    async def add_user_group_member_async(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMemberRequest,
    ) -> quickbi_public_20220101_models.AddUserGroupMemberResponse:
        """
        @summary The ID of the request.
        
        @param request: AddUserGroupMemberRequest
        @return: AddUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_group_member_with_options_async(request, runtime)

    def add_user_group_members_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserGroupMembersResponse:
        """
        @summary Add users to a specified user group at a time.
        
        @param request: AddUserGroupMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserGroupMembersResponse
        """
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
        """
        @summary Add users to a specified user group at a time.
        
        @param request: AddUserGroupMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserGroupMembersResponse
        """
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
        """
        @summary Add users to a specified user group at a time.
        
        @param request: AddUserGroupMembersRequest
        @return: AddUserGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_group_members_with_options(request, runtime)

    async def add_user_group_members_async(
        self,
        request: quickbi_public_20220101_models.AddUserGroupMembersRequest,
    ) -> quickbi_public_20220101_models.AddUserGroupMembersResponse:
        """
        @summary Add users to a specified user group at a time.
        
        @param request: AddUserGroupMembersRequest
        @return: AddUserGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_group_members_with_options_async(request, runtime)

    def add_user_tag_meta_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserTagMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserTagMetaResponse:
        """
        @summary Add the metadata of an organization member tag.
        
        @param request: AddUserTagMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserTagMetaResponse
        """
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
        """
        @summary Add the metadata of an organization member tag.
        
        @param request: AddUserTagMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserTagMetaResponse
        """
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
        """
        @summary Add the metadata of an organization member tag.
        
        @param request: AddUserTagMetaRequest
        @return: AddUserTagMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_tag_meta_with_options(request, runtime)

    async def add_user_tag_meta_async(
        self,
        request: quickbi_public_20220101_models.AddUserTagMetaRequest,
    ) -> quickbi_public_20220101_models.AddUserTagMetaResponse:
        """
        @summary Add the metadata of an organization member tag.
        
        @param request: AddUserTagMetaRequest
        @return: AddUserTagMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_tag_meta_with_options_async(request, runtime)

    def add_user_to_workspace_with_options(
        self,
        request: quickbi_public_20220101_models.AddUserToWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddUserToWorkspaceResponse:
        """
        @summary 添加成员到指定工作空间。
        
        @param request: AddUserToWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToWorkspaceResponse
        """
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
        """
        @summary 添加成员到指定工作空间。
        
        @param request: AddUserToWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToWorkspaceResponse
        """
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
        """
        @summary 添加成员到指定工作空间。
        
        @param request: AddUserToWorkspaceRequest
        @return: AddUserToWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_workspace_with_options(request, runtime)

    async def add_user_to_workspace_async(
        self,
        request: quickbi_public_20220101_models.AddUserToWorkspaceRequest,
    ) -> quickbi_public_20220101_models.AddUserToWorkspaceResponse:
        """
        @summary 添加成员到指定工作空间。
        
        @param request: AddUserToWorkspaceRequest
        @return: AddUserToWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_workspace_with_options_async(request, runtime)

    def add_workspace_users_with_options(
        self,
        request: quickbi_public_20220101_models.AddWorkspaceUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AddWorkspaceUsersResponse:
        """
        @summary 批量添加成员到工作空间。
        
        @param request: AddWorkspaceUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddWorkspaceUsersResponse
        """
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
        """
        @summary 批量添加成员到工作空间。
        
        @param request: AddWorkspaceUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddWorkspaceUsersResponse
        """
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
        """
        @summary 批量添加成员到工作空间。
        
        @param request: AddWorkspaceUsersRequest
        @return: AddWorkspaceUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_workspace_users_with_options(request, runtime)

    async def add_workspace_users_async(
        self,
        request: quickbi_public_20220101_models.AddWorkspaceUsersRequest,
    ) -> quickbi_public_20220101_models.AddWorkspaceUsersResponse:
        """
        @summary 批量添加成员到工作空间。
        
        @param request: AddWorkspaceUsersRequest
        @return: AddWorkspaceUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_workspace_users_with_options_async(request, runtime)

    def allot_dataset_acceleration_task_with_options(
        self,
        request: quickbi_public_20220101_models.AllotDatasetAccelerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AllotDatasetAccelerationTaskResponse:
        """
        @summary 触发数据集抽取加速。
        
        @param request: AllotDatasetAccelerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllotDatasetAccelerationTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllotDatasetAccelerationTask',
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
            quickbi_public_20220101_models.AllotDatasetAccelerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def allot_dataset_acceleration_task_with_options_async(
        self,
        request: quickbi_public_20220101_models.AllotDatasetAccelerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AllotDatasetAccelerationTaskResponse:
        """
        @summary 触发数据集抽取加速。
        
        @param request: AllotDatasetAccelerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllotDatasetAccelerationTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllotDatasetAccelerationTask',
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
            quickbi_public_20220101_models.AllotDatasetAccelerationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allot_dataset_acceleration_task(
        self,
        request: quickbi_public_20220101_models.AllotDatasetAccelerationTaskRequest,
    ) -> quickbi_public_20220101_models.AllotDatasetAccelerationTaskResponse:
        """
        @summary 触发数据集抽取加速。
        
        @param request: AllotDatasetAccelerationTaskRequest
        @return: AllotDatasetAccelerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allot_dataset_acceleration_task_with_options(request, runtime)

    async def allot_dataset_acceleration_task_async(
        self,
        request: quickbi_public_20220101_models.AllotDatasetAccelerationTaskRequest,
    ) -> quickbi_public_20220101_models.AllotDatasetAccelerationTaskResponse:
        """
        @summary 触发数据集抽取加速。
        
        @param request: AllotDatasetAccelerationTaskRequest
        @return: AllotDatasetAccelerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allot_dataset_acceleration_task_with_options_async(request, runtime)

    def authorize_menu_with_options(
        self,
        request: quickbi_public_20220101_models.AuthorizeMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.AuthorizeMenuResponse:
        """
        @summary Batch authorization of BI portal menu will be skipped automatically.
        
        @param request: AuthorizeMenuRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeMenuResponse
        """
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
        """
        @summary Batch authorization of BI portal menu will be skipped automatically.
        
        @param request: AuthorizeMenuRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeMenuResponse
        """
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
        """
        @summary Batch authorization of BI portal menu will be skipped automatically.
        
        @param request: AuthorizeMenuRequest
        @return: AuthorizeMenuResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_menu_with_options(request, runtime)

    async def authorize_menu_async(
        self,
        request: quickbi_public_20220101_models.AuthorizeMenuRequest,
    ) -> quickbi_public_20220101_models.AuthorizeMenuResponse:
        """
        @summary Batch authorization of BI portal menu will be skipped automatically.
        
        @param request: AuthorizeMenuRequest
        @return: AuthorizeMenuResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_menu_with_options_async(request, runtime)

    def batch_add_feishu_users_with_options(
        self,
        request: quickbi_public_20220101_models.BatchAddFeishuUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.BatchAddFeishuUsersResponse:
        """
        @summary 批量添加飞书用户。
        
        @param request: BatchAddFeishuUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddFeishuUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feishu_users):
            query['FeishuUsers'] = request.feishu_users
        if not UtilClient.is_unset(request.is_admin):
            query['IsAdmin'] = request.is_admin
        if not UtilClient.is_unset(request.is_auth_admin):
            query['IsAuthAdmin'] = request.is_auth_admin
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddFeishuUsers',
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
            quickbi_public_20220101_models.BatchAddFeishuUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_feishu_users_with_options_async(
        self,
        request: quickbi_public_20220101_models.BatchAddFeishuUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.BatchAddFeishuUsersResponse:
        """
        @summary 批量添加飞书用户。
        
        @param request: BatchAddFeishuUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchAddFeishuUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feishu_users):
            query['FeishuUsers'] = request.feishu_users
        if not UtilClient.is_unset(request.is_admin):
            query['IsAdmin'] = request.is_admin
        if not UtilClient.is_unset(request.is_auth_admin):
            query['IsAuthAdmin'] = request.is_auth_admin
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddFeishuUsers',
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
            quickbi_public_20220101_models.BatchAddFeishuUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_feishu_users(
        self,
        request: quickbi_public_20220101_models.BatchAddFeishuUsersRequest,
    ) -> quickbi_public_20220101_models.BatchAddFeishuUsersResponse:
        """
        @summary 批量添加飞书用户。
        
        @param request: BatchAddFeishuUsersRequest
        @return: BatchAddFeishuUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_add_feishu_users_with_options(request, runtime)

    async def batch_add_feishu_users_async(
        self,
        request: quickbi_public_20220101_models.BatchAddFeishuUsersRequest,
    ) -> quickbi_public_20220101_models.BatchAddFeishuUsersResponse:
        """
        @summary 批量添加飞书用户。
        
        @param request: BatchAddFeishuUsersRequest
        @return: BatchAddFeishuUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_feishu_users_with_options_async(request, runtime)

    def cancel_authorization_menu_with_options(
        self,
        request: quickbi_public_20220101_models.CancelAuthorizationMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CancelAuthorizationMenuResponse:
        """
        @summary 根据门户菜单ID，取消指定用户、用户组的授权记录。
        
        @param request: CancelAuthorizationMenuRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAuthorizationMenuResponse
        """
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
        """
        @summary 根据门户菜单ID，取消指定用户、用户组的授权记录。
        
        @param request: CancelAuthorizationMenuRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAuthorizationMenuResponse
        """
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
        """
        @summary 根据门户菜单ID，取消指定用户、用户组的授权记录。
        
        @param request: CancelAuthorizationMenuRequest
        @return: CancelAuthorizationMenuResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_authorization_menu_with_options(request, runtime)

    async def cancel_authorization_menu_async(
        self,
        request: quickbi_public_20220101_models.CancelAuthorizationMenuRequest,
    ) -> quickbi_public_20220101_models.CancelAuthorizationMenuResponse:
        """
        @summary 根据门户菜单ID，取消指定用户、用户组的授权记录。
        
        @param request: CancelAuthorizationMenuRequest
        @return: CancelAuthorizationMenuResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_authorization_menu_with_options_async(request, runtime)

    def cancel_collection_with_options(
        self,
        request: quickbi_public_20220101_models.CancelCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CancelCollectionResponse:
        """
        @summary Cancel the data works from the user\\"s collection.
        
        @param request: CancelCollectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelCollectionResponse
        """
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
        """
        @summary Cancel the data works from the user\\"s collection.
        
        @param request: CancelCollectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelCollectionResponse
        """
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
        """
        @summary Cancel the data works from the user\\"s collection.
        
        @param request: CancelCollectionRequest
        @return: CancelCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_collection_with_options(request, runtime)

    async def cancel_collection_async(
        self,
        request: quickbi_public_20220101_models.CancelCollectionRequest,
    ) -> quickbi_public_20220101_models.CancelCollectionResponse:
        """
        @summary Cancel the data works from the user\\"s collection.
        
        @param request: CancelCollectionRequest
        @return: CancelCollectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_collection_with_options_async(request, runtime)

    def cancel_report_share_with_options(
        self,
        request: quickbi_public_20220101_models.CancelReportShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CancelReportShareResponse:
        """
        @summary Delete a share authorization for a data work.
        
        @param request: CancelReportShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelReportShareResponse
        """
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
        """
        @summary Delete a share authorization for a data work.
        
        @param request: CancelReportShareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelReportShareResponse
        """
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
        """
        @summary Delete a share authorization for a data work.
        
        @param request: CancelReportShareRequest
        @return: CancelReportShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_report_share_with_options(request, runtime)

    async def cancel_report_share_async(
        self,
        request: quickbi_public_20220101_models.CancelReportShareRequest,
    ) -> quickbi_public_20220101_models.CancelReportShareResponse:
        """
        @summary Delete a share authorization for a data work.
        
        @param request: CancelReportShareRequest
        @return: CancelReportShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_report_share_with_options_async(request, runtime)

    def change_visibility_model_with_options(
        self,
        request: quickbi_public_20220101_models.ChangeVisibilityModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ChangeVisibilityModelResponse:
        """
        @summary The ID of the request.
        
        @param request: ChangeVisibilityModelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeVisibilityModelResponse
        """
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
        """
        @summary The ID of the request.
        
        @param request: ChangeVisibilityModelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeVisibilityModelResponse
        """
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
        """
        @summary The ID of the request.
        
        @param request: ChangeVisibilityModelRequest
        @return: ChangeVisibilityModelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_visibility_model_with_options(request, runtime)

    async def change_visibility_model_async(
        self,
        request: quickbi_public_20220101_models.ChangeVisibilityModelRequest,
    ) -> quickbi_public_20220101_models.ChangeVisibilityModelResponse:
        """
        @summary The ID of the request.
        
        @param request: ChangeVisibilityModelRequest
        @return: ChangeVisibilityModelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_visibility_model_with_options_async(request, runtime)

    def check_readable_with_options(
        self,
        request: quickbi_public_20220101_models.CheckReadableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CheckReadableResponse:
        """
        @summary Queries whether a user has permissions to view data works, such as dashboards and workbooks.
        
        @param request: CheckReadableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckReadableResponse
        """
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
        """
        @summary Queries whether a user has permissions to view data works, such as dashboards and workbooks.
        
        @param request: CheckReadableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckReadableResponse
        """
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
        """
        @summary Queries whether a user has permissions to view data works, such as dashboards and workbooks.
        
        @param request: CheckReadableRequest
        @return: CheckReadableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_readable_with_options(request, runtime)

    async def check_readable_async(
        self,
        request: quickbi_public_20220101_models.CheckReadableRequest,
    ) -> quickbi_public_20220101_models.CheckReadableResponse:
        """
        @summary Queries whether a user has permissions to view data works, such as dashboards and workbooks.
        
        @param request: CheckReadableRequest
        @return: CheckReadableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_readable_with_options_async(request, runtime)

    def create_ticket_with_options(
        self,
        request: quickbi_public_20220101_models.CreateTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CreateTicketResponse:
        """
        @summary 生成三方嵌入的ticket。
        
        @param request: CreateTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTicketResponse
        """
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
        """
        @summary 生成三方嵌入的ticket。
        
        @param request: CreateTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTicketResponse
        """
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
        """
        @summary 生成三方嵌入的ticket。
        
        @param request: CreateTicketRequest
        @return: CreateTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ticket_with_options(request, runtime)

    async def create_ticket_async(
        self,
        request: quickbi_public_20220101_models.CreateTicketRequest,
    ) -> quickbi_public_20220101_models.CreateTicketResponse:
        """
        @summary 生成三方嵌入的ticket。
        
        @param request: CreateTicketRequest
        @return: CreateTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ticket_with_options_async(request, runtime)

    def create_ticket_4copilot_with_options(
        self,
        request: quickbi_public_20220101_models.CreateTicket4CopilotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CreateTicket4CopilotResponse:
        """
        @summary 生成智能小Q嵌入ticket。
        
        @param request: CreateTicket4CopilotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTicket4CopilotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.copilot_id):
            query['CopilotId'] = request.copilot_id
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTicket4Copilot',
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
            quickbi_public_20220101_models.CreateTicket4CopilotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ticket_4copilot_with_options_async(
        self,
        request: quickbi_public_20220101_models.CreateTicket4CopilotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CreateTicket4CopilotResponse:
        """
        @summary 生成智能小Q嵌入ticket。
        
        @param request: CreateTicket4CopilotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTicket4CopilotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.copilot_id):
            query['CopilotId'] = request.copilot_id
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.ticket_num):
            query['TicketNum'] = request.ticket_num
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTicket4Copilot',
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
            quickbi_public_20220101_models.CreateTicket4CopilotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ticket_4copilot(
        self,
        request: quickbi_public_20220101_models.CreateTicket4CopilotRequest,
    ) -> quickbi_public_20220101_models.CreateTicket4CopilotResponse:
        """
        @summary 生成智能小Q嵌入ticket。
        
        @param request: CreateTicket4CopilotRequest
        @return: CreateTicket4CopilotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ticket_4copilot_with_options(request, runtime)

    async def create_ticket_4copilot_async(
        self,
        request: quickbi_public_20220101_models.CreateTicket4CopilotRequest,
    ) -> quickbi_public_20220101_models.CreateTicket4CopilotResponse:
        """
        @summary 生成智能小Q嵌入ticket。
        
        @param request: CreateTicket4CopilotRequest
        @return: CreateTicket4CopilotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ticket_4copilot_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: quickbi_public_20220101_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.CreateUserGroupResponse:
        """
        @summary Create a user group. You can specify a parent user group.
        
        @param request: CreateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserGroupResponse
        """
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
        """
        @summary Create a user group. You can specify a parent user group.
        
        @param request: CreateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserGroupResponse
        """
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
        """
        @summary Create a user group. You can specify a parent user group.
        
        @param request: CreateUserGroupRequest
        @return: CreateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: quickbi_public_20220101_models.CreateUserGroupRequest,
    ) -> quickbi_public_20220101_models.CreateUserGroupResponse:
        """
        @summary Create a user group. You can specify a parent user group.
        
        @param request: CreateUserGroupRequest
        @return: CreateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def data_set_blood_with_options(
        self,
        request: quickbi_public_20220101_models.DataSetBloodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DataSetBloodResponse:
        """
        @summary 查询引用指定数据集下的作品信息。
        
        @param request: DataSetBloodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DataSetBloodResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_set_ids):
            query['DataSetIds'] = request.data_set_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_type):
            query['WorksType'] = request.works_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DataSetBlood',
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
            quickbi_public_20220101_models.DataSetBloodResponse(),
            self.call_api(params, req, runtime)
        )

    async def data_set_blood_with_options_async(
        self,
        request: quickbi_public_20220101_models.DataSetBloodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DataSetBloodResponse:
        """
        @summary 查询引用指定数据集下的作品信息。
        
        @param request: DataSetBloodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DataSetBloodResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_set_ids):
            query['DataSetIds'] = request.data_set_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.works_type):
            query['WorksType'] = request.works_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DataSetBlood',
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
            quickbi_public_20220101_models.DataSetBloodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def data_set_blood(
        self,
        request: quickbi_public_20220101_models.DataSetBloodRequest,
    ) -> quickbi_public_20220101_models.DataSetBloodResponse:
        """
        @summary 查询引用指定数据集下的作品信息。
        
        @param request: DataSetBloodRequest
        @return: DataSetBloodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.data_set_blood_with_options(request, runtime)

    async def data_set_blood_async(
        self,
        request: quickbi_public_20220101_models.DataSetBloodRequest,
    ) -> quickbi_public_20220101_models.DataSetBloodResponse:
        """
        @summary 查询引用指定数据集下的作品信息。
        
        @param request: DataSetBloodRequest
        @return: DataSetBloodResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.data_set_blood_with_options_async(request, runtime)

    def data_source_blood_with_options(
        self,
        request: quickbi_public_20220101_models.DataSourceBloodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DataSourceBloodResponse:
        """
        @summary 查询引用指定数据源下的数据集信息。
        
        @param request: DataSourceBloodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DataSourceBloodResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DataSourceBlood',
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
            quickbi_public_20220101_models.DataSourceBloodResponse(),
            self.call_api(params, req, runtime)
        )

    async def data_source_blood_with_options_async(
        self,
        request: quickbi_public_20220101_models.DataSourceBloodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DataSourceBloodResponse:
        """
        @summary 查询引用指定数据源下的数据集信息。
        
        @param request: DataSourceBloodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DataSourceBloodResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DataSourceBlood',
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
            quickbi_public_20220101_models.DataSourceBloodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def data_source_blood(
        self,
        request: quickbi_public_20220101_models.DataSourceBloodRequest,
    ) -> quickbi_public_20220101_models.DataSourceBloodResponse:
        """
        @summary 查询引用指定数据源下的数据集信息。
        
        @param request: DataSourceBloodRequest
        @return: DataSourceBloodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.data_source_blood_with_options(request, runtime)

    async def data_source_blood_async(
        self,
        request: quickbi_public_20220101_models.DataSourceBloodRequest,
    ) -> quickbi_public_20220101_models.DataSourceBloodResponse:
        """
        @summary 查询引用指定数据源下的数据集信息。
        
        @param request: DataSourceBloodRequest
        @return: DataSourceBloodResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.data_source_blood_with_options_async(request, runtime)

    def delay_ticket_expire_time_with_options(
        self,
        request: quickbi_public_20220101_models.DelayTicketExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DelayTicketExpireTimeResponse:
        """
        @summary Update the expiration time of the ticket embedded in the report.
        
        @param request: DelayTicketExpireTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelayTicketExpireTimeResponse
        """
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
        """
        @summary Update the expiration time of the ticket embedded in the report.
        
        @param request: DelayTicketExpireTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelayTicketExpireTimeResponse
        """
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
        """
        @summary Update the expiration time of the ticket embedded in the report.
        
        @param request: DelayTicketExpireTimeRequest
        @return: DelayTicketExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delay_ticket_expire_time_with_options(request, runtime)

    async def delay_ticket_expire_time_async(
        self,
        request: quickbi_public_20220101_models.DelayTicketExpireTimeRequest,
    ) -> quickbi_public_20220101_models.DelayTicketExpireTimeResponse:
        """
        @summary Update the expiration time of the ticket embedded in the report.
        
        @param request: DelayTicketExpireTimeRequest
        @return: DelayTicketExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delay_ticket_expire_time_with_options_async(request, runtime)

    def delete_data_level_permission_rule_users_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersResponse:
        """
        @summary { "ruleId": "a5bb24da- **-a891683e14da", // The ID of the row-column permission rule. "cubeId": "7c7223ae- ***-3c744528014b", // The ID of the dataset. "delModel": { "userGroups": [ "0d5fb19b- ***-1248 fc27ca51", // Delete the user group ID of the user group. "3d2c23d4-***-f6390f325c2d" ], "users": [ "4334 ***358", // Delete the UserID of the user group. "Huang***3fa822" ] } }
        
        @description {"ruleId":"a5bb24da-**-a891683e14da","cubeId":"7c7223ae-***-3c744528014b","delModel":{"userGroups":["0d5fb19b-***-1248fc27ca51","3d2c23d4-***-f6390f325c2d"],"users":["4334***358","Huang***3fa822"]}}
        
        @param request: DeleteDataLevelPermissionRuleUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLevelPermissionRuleUsersResponse
        """
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
        """
        @summary { "ruleId": "a5bb24da- **-a891683e14da", // The ID of the row-column permission rule. "cubeId": "7c7223ae- ***-3c744528014b", // The ID of the dataset. "delModel": { "userGroups": [ "0d5fb19b- ***-1248 fc27ca51", // Delete the user group ID of the user group. "3d2c23d4-***-f6390f325c2d" ], "users": [ "4334 ***358", // Delete the UserID of the user group. "Huang***3fa822" ] } }
        
        @description {"ruleId":"a5bb24da-**-a891683e14da","cubeId":"7c7223ae-***-3c744528014b","delModel":{"userGroups":["0d5fb19b-***-1248fc27ca51","3d2c23d4-***-f6390f325c2d"],"users":["4334***358","Huang***3fa822"]}}
        
        @param request: DeleteDataLevelPermissionRuleUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLevelPermissionRuleUsersResponse
        """
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
        """
        @summary { "ruleId": "a5bb24da- **-a891683e14da", // The ID of the row-column permission rule. "cubeId": "7c7223ae- ***-3c744528014b", // The ID of the dataset. "delModel": { "userGroups": [ "0d5fb19b- ***-1248 fc27ca51", // Delete the user group ID of the user group. "3d2c23d4-***-f6390f325c2d" ], "users": [ "4334 ***358", // Delete the UserID of the user group. "Huang***3fa822" ] } }
        
        @description {"ruleId":"a5bb24da-**-a891683e14da","cubeId":"7c7223ae-***-3c744528014b","delModel":{"userGroups":["0d5fb19b-***-1248fc27ca51","3d2c23d4-***-f6390f325c2d"],"users":["4334***358","Huang***3fa822"]}}
        
        @param request: DeleteDataLevelPermissionRuleUsersRequest
        @return: DeleteDataLevelPermissionRuleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_level_permission_rule_users_with_options(request, runtime)

    async def delete_data_level_permission_rule_users_async(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersRequest,
    ) -> quickbi_public_20220101_models.DeleteDataLevelPermissionRuleUsersResponse:
        """
        @summary { "ruleId": "a5bb24da- **-a891683e14da", // The ID of the row-column permission rule. "cubeId": "7c7223ae- ***-3c744528014b", // The ID of the dataset. "delModel": { "userGroups": [ "0d5fb19b- ***-1248 fc27ca51", // Delete the user group ID of the user group. "3d2c23d4-***-f6390f325c2d" ], "users": [ "4334 ***358", // Delete the UserID of the user group. "Huang***3fa822" ] } }
        
        @description {"ruleId":"a5bb24da-**-a891683e14da","cubeId":"7c7223ae-***-3c744528014b","delModel":{"userGroups":["0d5fb19b-***-1248fc27ca51","3d2c23d4-***-f6390f325c2d"],"users":["4334***358","Huang***3fa822"]}}
        
        @param request: DeleteDataLevelPermissionRuleUsersRequest
        @return: DeleteDataLevelPermissionRuleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_level_permission_rule_users_with_options_async(request, runtime)

    def delete_data_level_rule_config_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelRuleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteDataLevelRuleConfigResponse:
        """
        @summary The ID of the request.
        
        @description The ID of the training dataset that you want to remove from the specified custom linguistic model.
        
        @param request: DeleteDataLevelRuleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLevelRuleConfigResponse
        """
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
        """
        @summary The ID of the request.
        
        @description The ID of the training dataset that you want to remove from the specified custom linguistic model.
        
        @param request: DeleteDataLevelRuleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLevelRuleConfigResponse
        """
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
        """
        @summary The ID of the request.
        
        @description The ID of the training dataset that you want to remove from the specified custom linguistic model.
        
        @param request: DeleteDataLevelRuleConfigRequest
        @return: DeleteDataLevelRuleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_level_rule_config_with_options(request, runtime)

    async def delete_data_level_rule_config_async(
        self,
        request: quickbi_public_20220101_models.DeleteDataLevelRuleConfigRequest,
    ) -> quickbi_public_20220101_models.DeleteDataLevelRuleConfigResponse:
        """
        @summary The ID of the request.
        
        @description The ID of the training dataset that you want to remove from the specified custom linguistic model.
        
        @param request: DeleteDataLevelRuleConfigRequest
        @return: DeleteDataLevelRuleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_level_rule_config_with_options_async(request, runtime)

    def delete_ticket_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteTicketResponse:
        """
        @summary auditing
        
        @param request: DeleteTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTicketResponse
        """
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
        """
        @summary auditing
        
        @param request: DeleteTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTicketResponse
        """
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
        """
        @summary auditing
        
        @param request: DeleteTicketRequest
        @return: DeleteTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ticket_with_options(request, runtime)

    async def delete_ticket_async(
        self,
        request: quickbi_public_20220101_models.DeleteTicketRequest,
    ) -> quickbi_public_20220101_models.DeleteTicketResponse:
        """
        @summary auditing
        
        @param request: DeleteTicketRequest
        @return: DeleteTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ticket_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserResponse:
        """
        @summary auditing
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
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
        """
        @summary auditing
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
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
        """
        @summary auditing
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserRequest,
    ) -> quickbi_public_20220101_models.DeleteUserResponse:
        """
        @summary auditing
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_from_workspace_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserFromWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserFromWorkspaceResponse:
        """
        @summary 删除指定工作空间的成员。
        
        @param request: DeleteUserFromWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserFromWorkspaceResponse
        """
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
        """
        @summary 删除指定工作空间的成员。
        
        @param request: DeleteUserFromWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserFromWorkspaceResponse
        """
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
        """
        @summary 删除指定工作空间的成员。
        
        @param request: DeleteUserFromWorkspaceRequest
        @return: DeleteUserFromWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_from_workspace_with_options(request, runtime)

    async def delete_user_from_workspace_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserFromWorkspaceRequest,
    ) -> quickbi_public_20220101_models.DeleteUserFromWorkspaceResponse:
        """
        @summary 删除指定工作空间的成员。
        
        @param request: DeleteUserFromWorkspaceRequest
        @return: DeleteUserFromWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_from_workspace_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserGroupResponse:
        """
        @summary Deletes a user group in an organization.
        
        @param request: DeleteUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupResponse
        """
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
        """
        @summary Deletes a user group in an organization.
        
        @param request: DeleteUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupResponse
        """
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
        """
        @summary Deletes a user group in an organization.
        
        @param request: DeleteUserGroupRequest
        @return: DeleteUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupRequest,
    ) -> quickbi_public_20220101_models.DeleteUserGroupResponse:
        """
        @summary Deletes a user group in an organization.
        
        @param request: DeleteUserGroupRequest
        @return: DeleteUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def delete_user_group_member_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMemberResponse:
        """
        @summary Deletes a specified member from a specified user group.
        
        @param request: DeleteUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupMemberResponse
        """
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
        """
        @summary Deletes a specified member from a specified user group.
        
        @param request: DeleteUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupMemberResponse
        """
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
        """
        @summary Deletes a specified member from a specified user group.
        
        @param request: DeleteUserGroupMemberRequest
        @return: DeleteUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_member_with_options(request, runtime)

    async def delete_user_group_member_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMemberRequest,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMemberResponse:
        """
        @summary Deletes a specified member from a specified user group.
        
        @param request: DeleteUserGroupMemberRequest
        @return: DeleteUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_member_with_options_async(request, runtime)

    def delete_user_group_members_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMembersResponse:
        """
        @summary Indicates whether the request is successful. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @param request: DeleteUserGroupMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupMembersResponse
        """
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
        """
        @summary Indicates whether the request is successful. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @param request: DeleteUserGroupMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupMembersResponse
        """
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
        """
        @summary Indicates whether the request is successful. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @param request: DeleteUserGroupMembersRequest
        @return: DeleteUserGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_members_with_options(request, runtime)

    async def delete_user_group_members_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserGroupMembersRequest,
    ) -> quickbi_public_20220101_models.DeleteUserGroupMembersResponse:
        """
        @summary Indicates whether the request is successful. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @param request: DeleteUserGroupMembersRequest
        @return: DeleteUserGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_members_with_options_async(request, runtime)

    def delete_user_tag_meta_with_options(
        self,
        request: quickbi_public_20220101_models.DeleteUserTagMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.DeleteUserTagMetaResponse:
        """
        @summary Deletes the tag metadata of an organization member.
        
        @param request: DeleteUserTagMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserTagMetaResponse
        """
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
        """
        @summary Deletes the tag metadata of an organization member.
        
        @param request: DeleteUserTagMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserTagMetaResponse
        """
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
        """
        @summary Deletes the tag metadata of an organization member.
        
        @param request: DeleteUserTagMetaRequest
        @return: DeleteUserTagMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_tag_meta_with_options(request, runtime)

    async def delete_user_tag_meta_async(
        self,
        request: quickbi_public_20220101_models.DeleteUserTagMetaRequest,
    ) -> quickbi_public_20220101_models.DeleteUserTagMetaResponse:
        """
        @summary Deletes the tag metadata of an organization member.
        
        @param request: DeleteUserTagMetaRequest
        @return: DeleteUserTagMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_tag_meta_with_options_async(request, runtime)

    def get_user_group_info_with_options(
        self,
        request: quickbi_public_20220101_models.GetUserGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.GetUserGroupInfoResponse:
        """
        @summary Test description
        
        @param request: GetUserGroupInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGroupInfoResponse
        """
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
        """
        @summary Test description
        
        @param request: GetUserGroupInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGroupInfoResponse
        """
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
        """
        @summary Test description
        
        @param request: GetUserGroupInfoRequest
        @return: GetUserGroupInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_info_with_options(request, runtime)

    async def get_user_group_info_async(
        self,
        request: quickbi_public_20220101_models.GetUserGroupInfoRequest,
    ) -> quickbi_public_20220101_models.GetUserGroupInfoResponse:
        """
        @summary Test description
        
        @param request: GetUserGroupInfoRequest
        @return: GetUserGroupInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_group_info_with_options_async(request, runtime)

    def list_api_datasource_with_options(
        self,
        request: quickbi_public_20220101_models.ListApiDatasourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListApiDatasourceResponse:
        """
        @summary 查询API数据源列表。
        
        @param request: ListApiDatasourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiDatasourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
            action='ListApiDatasource',
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
            quickbi_public_20220101_models.ListApiDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_datasource_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListApiDatasourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListApiDatasourceResponse:
        """
        @summary 查询API数据源列表。
        
        @param request: ListApiDatasourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiDatasourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
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
            action='ListApiDatasource',
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
            quickbi_public_20220101_models.ListApiDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_datasource(
        self,
        request: quickbi_public_20220101_models.ListApiDatasourceRequest,
    ) -> quickbi_public_20220101_models.ListApiDatasourceResponse:
        """
        @summary 查询API数据源列表。
        
        @param request: ListApiDatasourceRequest
        @return: ListApiDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_api_datasource_with_options(request, runtime)

    async def list_api_datasource_async(
        self,
        request: quickbi_public_20220101_models.ListApiDatasourceRequest,
    ) -> quickbi_public_20220101_models.ListApiDatasourceResponse:
        """
        @summary 查询API数据源列表。
        
        @param request: ListApiDatasourceRequest
        @return: ListApiDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_api_datasource_with_options_async(request, runtime)

    def list_by_user_group_id_with_options(
        self,
        request: quickbi_public_20220101_models.ListByUserGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListByUserGroupIdResponse:
        """
        @summary Queries user group information at a time by user group ID.
        
        @param request: ListByUserGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListByUserGroupIdResponse
        """
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
        """
        @summary Queries user group information at a time by user group ID.
        
        @param request: ListByUserGroupIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListByUserGroupIdResponse
        """
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
        """
        @summary Queries user group information at a time by user group ID.
        
        @param request: ListByUserGroupIdRequest
        @return: ListByUserGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_by_user_group_id_with_options(request, runtime)

    async def list_by_user_group_id_async(
        self,
        request: quickbi_public_20220101_models.ListByUserGroupIdRequest,
    ) -> quickbi_public_20220101_models.ListByUserGroupIdResponse:
        """
        @summary Queries user group information at a time by user group ID.
        
        @param request: ListByUserGroupIdRequest
        @return: ListByUserGroupIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_by_user_group_id_with_options_async(request, runtime)

    def list_collections_with_options(
        self,
        request: quickbi_public_20220101_models.ListCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListCollectionsResponse:
        """
        @summary The ID of the work.
        
        @param request: ListCollectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCollectionsResponse
        """
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
        """
        @summary The ID of the work.
        
        @param request: ListCollectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCollectionsResponse
        """
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
        """
        @summary The ID of the work.
        
        @param request: ListCollectionsRequest
        @return: ListCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_collections_with_options(request, runtime)

    async def list_collections_async(
        self,
        request: quickbi_public_20220101_models.ListCollectionsRequest,
    ) -> quickbi_public_20220101_models.ListCollectionsResponse:
        """
        @summary The ID of the work.
        
        @param request: ListCollectionsRequest
        @return: ListCollectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_collections_with_options_async(request, runtime)

    def list_cube_data_level_permission_config_with_options(
        self,
        request: quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigResponse:
        """
        @summary You can this operation to obtain a list of row and column permission configurations for a specified dataset.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.
        
        @param request: ListCubeDataLevelPermissionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCubeDataLevelPermissionConfigResponse
        """
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
        """
        @summary You can this operation to obtain a list of row and column permission configurations for a specified dataset.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.
        
        @param request: ListCubeDataLevelPermissionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCubeDataLevelPermissionConfigResponse
        """
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
        """
        @summary You can this operation to obtain a list of row and column permission configurations for a specified dataset.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.
        
        @param request: ListCubeDataLevelPermissionConfigRequest
        @return: ListCubeDataLevelPermissionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cube_data_level_permission_config_with_options(request, runtime)

    async def list_cube_data_level_permission_config_async(
        self,
        request: quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigRequest,
    ) -> quickbi_public_20220101_models.ListCubeDataLevelPermissionConfigResponse:
        """
        @summary You can this operation to obtain a list of row and column permission configurations for a specified dataset.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.
        
        @param request: ListCubeDataLevelPermissionConfigRequest
        @return: ListCubeDataLevelPermissionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cube_data_level_permission_config_with_options_async(request, runtime)

    def list_data_level_permission_white_list_with_options(
        self,
        request: quickbi_public_20220101_models.ListDataLevelPermissionWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListDataLevelPermissionWhiteListResponse:
        """
        @summary 根据行列权限种类，获取数据集行列权限的白名单列表。
        
        @param request: ListDataLevelPermissionWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLevelPermissionWhiteListResponse
        """
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
        """
        @summary 根据行列权限种类，获取数据集行列权限的白名单列表。
        
        @param request: ListDataLevelPermissionWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLevelPermissionWhiteListResponse
        """
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
        """
        @summary 根据行列权限种类，获取数据集行列权限的白名单列表。
        
        @param request: ListDataLevelPermissionWhiteListRequest
        @return: ListDataLevelPermissionWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_level_permission_white_list_with_options(request, runtime)

    async def list_data_level_permission_white_list_async(
        self,
        request: quickbi_public_20220101_models.ListDataLevelPermissionWhiteListRequest,
    ) -> quickbi_public_20220101_models.ListDataLevelPermissionWhiteListResponse:
        """
        @summary 根据行列权限种类，获取数据集行列权限的白名单列表。
        
        @param request: ListDataLevelPermissionWhiteListRequest
        @return: ListDataLevelPermissionWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_level_permission_white_list_with_options_async(request, runtime)

    def list_favorite_reports_with_options(
        self,
        request: quickbi_public_20220101_models.ListFavoriteReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListFavoriteReportsResponse:
        """
        @summary 获取指定用户在首页看板中展示的收藏作品列表。
        
        @param request: ListFavoriteReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFavoriteReportsResponse
        """
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
        """
        @summary 获取指定用户在首页看板中展示的收藏作品列表。
        
        @param request: ListFavoriteReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFavoriteReportsResponse
        """
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
        """
        @summary 获取指定用户在首页看板中展示的收藏作品列表。
        
        @param request: ListFavoriteReportsRequest
        @return: ListFavoriteReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_favorite_reports_with_options(request, runtime)

    async def list_favorite_reports_async(
        self,
        request: quickbi_public_20220101_models.ListFavoriteReportsRequest,
    ) -> quickbi_public_20220101_models.ListFavoriteReportsResponse:
        """
        @summary 获取指定用户在首页看板中展示的收藏作品列表。
        
        @param request: ListFavoriteReportsRequest
        @return: ListFavoriteReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_favorite_reports_with_options_async(request, runtime)

    def list_organization_role_users_with_options(
        self,
        request: quickbi_public_20220101_models.ListOrganizationRoleUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListOrganizationRoleUsersResponse:
        """
        @summary 获取指定组织角色下的用户列表。
        
        @param request: ListOrganizationRoleUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationRoleUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationRoleUsers',
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
            quickbi_public_20220101_models.ListOrganizationRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organization_role_users_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListOrganizationRoleUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListOrganizationRoleUsersResponse:
        """
        @summary 获取指定组织角色下的用户列表。
        
        @param request: ListOrganizationRoleUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationRoleUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationRoleUsers',
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
            quickbi_public_20220101_models.ListOrganizationRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organization_role_users(
        self,
        request: quickbi_public_20220101_models.ListOrganizationRoleUsersRequest,
    ) -> quickbi_public_20220101_models.ListOrganizationRoleUsersResponse:
        """
        @summary 获取指定组织角色下的用户列表。
        
        @param request: ListOrganizationRoleUsersRequest
        @return: ListOrganizationRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_organization_role_users_with_options(request, runtime)

    async def list_organization_role_users_async(
        self,
        request: quickbi_public_20220101_models.ListOrganizationRoleUsersRequest,
    ) -> quickbi_public_20220101_models.ListOrganizationRoleUsersResponse:
        """
        @summary 获取指定组织角色下的用户列表。
        
        @param request: ListOrganizationRoleUsersRequest
        @return: ListOrganizationRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_organization_role_users_with_options_async(request, runtime)

    def list_organization_roles_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListOrganizationRolesResponse:
        """
        @summary 获取组织级别自定义角色列表。
        
        @param request: ListOrganizationRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationRolesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListOrganizationRoles',
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
            quickbi_public_20220101_models.ListOrganizationRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organization_roles_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListOrganizationRolesResponse:
        """
        @summary 获取组织级别自定义角色列表。
        
        @param request: ListOrganizationRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationRolesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListOrganizationRoles',
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
            quickbi_public_20220101_models.ListOrganizationRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organization_roles(self) -> quickbi_public_20220101_models.ListOrganizationRolesResponse:
        """
        @summary 获取组织级别自定义角色列表。
        
        @return: ListOrganizationRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_organization_roles_with_options(runtime)

    async def list_organization_roles_async(self) -> quickbi_public_20220101_models.ListOrganizationRolesResponse:
        """
        @summary 获取组织级别自定义角色列表。
        
        @return: ListOrganizationRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_organization_roles_with_options_async(runtime)

    def list_portal_menu_authorization_with_options(
        self,
        request: quickbi_public_20220101_models.ListPortalMenuAuthorizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListPortalMenuAuthorizationResponse:
        """
        @summary Obtains the list of authorization details for a BI portal menu.
        
        @param request: ListPortalMenuAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPortalMenuAuthorizationResponse
        """
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
        """
        @summary Obtains the list of authorization details for a BI portal menu.
        
        @param request: ListPortalMenuAuthorizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPortalMenuAuthorizationResponse
        """
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
        """
        @summary Obtains the list of authorization details for a BI portal menu.
        
        @param request: ListPortalMenuAuthorizationRequest
        @return: ListPortalMenuAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_portal_menu_authorization_with_options(request, runtime)

    async def list_portal_menu_authorization_async(
        self,
        request: quickbi_public_20220101_models.ListPortalMenuAuthorizationRequest,
    ) -> quickbi_public_20220101_models.ListPortalMenuAuthorizationResponse:
        """
        @summary Obtains the list of authorization details for a BI portal menu.
        
        @param request: ListPortalMenuAuthorizationRequest
        @return: ListPortalMenuAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_portal_menu_authorization_with_options_async(request, runtime)

    def list_portal_menus_with_options(
        self,
        request: quickbi_public_20220101_models.ListPortalMenusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListPortalMenusResponse:
        """
        @summary Gets a hierarchical list of menus under a specific BI portal.
        
        @param request: ListPortalMenusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPortalMenusResponse
        """
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
        """
        @summary Gets a hierarchical list of menus under a specific BI portal.
        
        @param request: ListPortalMenusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPortalMenusResponse
        """
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
        """
        @summary Gets a hierarchical list of menus under a specific BI portal.
        
        @param request: ListPortalMenusRequest
        @return: ListPortalMenusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_portal_menus_with_options(request, runtime)

    async def list_portal_menus_async(
        self,
        request: quickbi_public_20220101_models.ListPortalMenusRequest,
    ) -> quickbi_public_20220101_models.ListPortalMenusResponse:
        """
        @summary Gets a hierarchical list of menus under a specific BI portal.
        
        @param request: ListPortalMenusRequest
        @return: ListPortalMenusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_portal_menus_with_options_async(request, runtime)

    def list_recent_view_reports_with_options(
        self,
        request: quickbi_public_20220101_models.ListRecentViewReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListRecentViewReportsResponse:
        """
        @summary 获取首页看板常看和足迹列表。
        
        @param request: ListRecentViewReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentViewReportsResponse
        """
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
        """
        @summary 获取首页看板常看和足迹列表。
        
        @param request: ListRecentViewReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentViewReportsResponse
        """
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
        """
        @summary 获取首页看板常看和足迹列表。
        
        @param request: ListRecentViewReportsRequest
        @return: ListRecentViewReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_recent_view_reports_with_options(request, runtime)

    async def list_recent_view_reports_async(
        self,
        request: quickbi_public_20220101_models.ListRecentViewReportsRequest,
    ) -> quickbi_public_20220101_models.ListRecentViewReportsResponse:
        """
        @summary 获取首页看板常看和足迹列表。
        
        @param request: ListRecentViewReportsRequest
        @return: ListRecentViewReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_recent_view_reports_with_options_async(request, runtime)

    def list_shared_reports_with_options(
        self,
        request: quickbi_public_20220101_models.ListSharedReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListSharedReportsResponse:
        """
        @summary 获取指定用户在首页看板中展示的被授权的作品列表。
        
        @param request: ListSharedReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSharedReportsResponse
        """
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
        """
        @summary 获取指定用户在首页看板中展示的被授权的作品列表。
        
        @param request: ListSharedReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSharedReportsResponse
        """
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
        """
        @summary 获取指定用户在首页看板中展示的被授权的作品列表。
        
        @param request: ListSharedReportsRequest
        @return: ListSharedReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_shared_reports_with_options(request, runtime)

    async def list_shared_reports_async(
        self,
        request: quickbi_public_20220101_models.ListSharedReportsRequest,
    ) -> quickbi_public_20220101_models.ListSharedReportsResponse:
        """
        @summary 获取指定用户在首页看板中展示的被授权的作品列表。
        
        @param request: ListSharedReportsRequest
        @return: ListSharedReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_shared_reports_with_options_async(request, runtime)

    def list_user_groups_by_user_id_with_options(
        self,
        request: quickbi_public_20220101_models.ListUserGroupsByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListUserGroupsByUserIdResponse:
        """
        @summary Description
        
        @param request: ListUserGroupsByUserIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsByUserIdResponse
        """
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
        """
        @summary Description
        
        @param request: ListUserGroupsByUserIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsByUserIdResponse
        """
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
        """
        @summary Description
        
        @param request: ListUserGroupsByUserIdRequest
        @return: ListUserGroupsByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_by_user_id_with_options(request, runtime)

    async def list_user_groups_by_user_id_async(
        self,
        request: quickbi_public_20220101_models.ListUserGroupsByUserIdRequest,
    ) -> quickbi_public_20220101_models.ListUserGroupsByUserIdResponse:
        """
        @summary Description
        
        @param request: ListUserGroupsByUserIdRequest
        @return: ListUserGroupsByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_by_user_id_with_options_async(request, runtime)

    def list_workspace_role_users_with_options(
        self,
        request: quickbi_public_20220101_models.ListWorkspaceRoleUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListWorkspaceRoleUsersResponse:
        """
        @summary 获取指定空间角色下的用户列表。
        
        @param request: ListWorkspaceRoleUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceRoleUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceRoleUsers',
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
            quickbi_public_20220101_models.ListWorkspaceRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_role_users_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListWorkspaceRoleUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListWorkspaceRoleUsersResponse:
        """
        @summary 获取指定空间角色下的用户列表。
        
        @param request: ListWorkspaceRoleUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceRoleUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceRoleUsers',
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
            quickbi_public_20220101_models.ListWorkspaceRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_role_users(
        self,
        request: quickbi_public_20220101_models.ListWorkspaceRoleUsersRequest,
    ) -> quickbi_public_20220101_models.ListWorkspaceRoleUsersResponse:
        """
        @summary 获取指定空间角色下的用户列表。
        
        @param request: ListWorkspaceRoleUsersRequest
        @return: ListWorkspaceRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_workspace_role_users_with_options(request, runtime)

    async def list_workspace_role_users_async(
        self,
        request: quickbi_public_20220101_models.ListWorkspaceRoleUsersRequest,
    ) -> quickbi_public_20220101_models.ListWorkspaceRoleUsersResponse:
        """
        @summary 获取指定空间角色下的用户列表。
        
        @param request: ListWorkspaceRoleUsersRequest
        @return: ListWorkspaceRoleUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_workspace_role_users_with_options_async(request, runtime)

    def list_workspace_roles_with_options(
        self,
        request: quickbi_public_20220101_models.ListWorkspaceRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListWorkspaceRolesResponse:
        """
        @summary 获取空间角色列表。
        
        @param request: ListWorkspaceRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceRoles',
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
            quickbi_public_20220101_models.ListWorkspaceRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_roles_with_options_async(
        self,
        request: quickbi_public_20220101_models.ListWorkspaceRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ListWorkspaceRolesResponse:
        """
        @summary 获取空间角色列表。
        
        @param request: ListWorkspaceRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceRoles',
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
            quickbi_public_20220101_models.ListWorkspaceRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_roles(
        self,
        request: quickbi_public_20220101_models.ListWorkspaceRolesRequest,
    ) -> quickbi_public_20220101_models.ListWorkspaceRolesResponse:
        """
        @summary 获取空间角色列表。
        
        @param request: ListWorkspaceRolesRequest
        @return: ListWorkspaceRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_workspace_roles_with_options(request, runtime)

    async def list_workspace_roles_async(
        self,
        request: quickbi_public_20220101_models.ListWorkspaceRolesRequest,
    ) -> quickbi_public_20220101_models.ListWorkspaceRolesResponse:
        """
        @summary 获取空间角色列表。
        
        @param request: ListWorkspaceRolesRequest
        @return: ListWorkspaceRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_workspace_roles_with_options_async(request, runtime)

    def modify_api_datasource_parameters_with_options(
        self,
        request: quickbi_public_20220101_models.ModifyApiDatasourceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ModifyApiDatasourceParametersResponse:
        """
        @summary 修改指定API数据源参数值。
        
        @param request: ModifyApiDatasourceParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApiDatasourceParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiDatasourceParameters',
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
            quickbi_public_20220101_models.ModifyApiDatasourceParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_datasource_parameters_with_options_async(
        self,
        request: quickbi_public_20220101_models.ModifyApiDatasourceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ModifyApiDatasourceParametersResponse:
        """
        @summary 修改指定API数据源参数值。
        
        @param request: ModifyApiDatasourceParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApiDatasourceParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiDatasourceParameters',
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
            quickbi_public_20220101_models.ModifyApiDatasourceParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_datasource_parameters(
        self,
        request: quickbi_public_20220101_models.ModifyApiDatasourceParametersRequest,
    ) -> quickbi_public_20220101_models.ModifyApiDatasourceParametersResponse:
        """
        @summary 修改指定API数据源参数值。
        
        @param request: ModifyApiDatasourceParametersRequest
        @return: ModifyApiDatasourceParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_api_datasource_parameters_with_options(request, runtime)

    async def modify_api_datasource_parameters_async(
        self,
        request: quickbi_public_20220101_models.ModifyApiDatasourceParametersRequest,
    ) -> quickbi_public_20220101_models.ModifyApiDatasourceParametersResponse:
        """
        @summary 修改指定API数据源参数值。
        
        @param request: ModifyApiDatasourceParametersRequest
        @return: ModifyApiDatasourceParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_datasource_parameters_with_options_async(request, runtime)

    def modify_copilot_embed_config_with_options(
        self,
        request: quickbi_public_20220101_models.ModifyCopilotEmbedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ModifyCopilotEmbedConfigResponse:
        """
        @summary 修改智能问数嵌入配置。
        
        @param request: ModifyCopilotEmbedConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCopilotEmbedConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_name):
            query['AgentName'] = request.agent_name
        if not UtilClient.is_unset(request.copilot_id):
            query['CopilotId'] = request.copilot_id
        if not UtilClient.is_unset(request.data_range):
            query['DataRange'] = request.data_range
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCopilotEmbedConfig',
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
            quickbi_public_20220101_models.ModifyCopilotEmbedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_copilot_embed_config_with_options_async(
        self,
        request: quickbi_public_20220101_models.ModifyCopilotEmbedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ModifyCopilotEmbedConfigResponse:
        """
        @summary 修改智能问数嵌入配置。
        
        @param request: ModifyCopilotEmbedConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCopilotEmbedConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_name):
            query['AgentName'] = request.agent_name
        if not UtilClient.is_unset(request.copilot_id):
            query['CopilotId'] = request.copilot_id
        if not UtilClient.is_unset(request.data_range):
            query['DataRange'] = request.data_range
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCopilotEmbedConfig',
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
            quickbi_public_20220101_models.ModifyCopilotEmbedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_copilot_embed_config(
        self,
        request: quickbi_public_20220101_models.ModifyCopilotEmbedConfigRequest,
    ) -> quickbi_public_20220101_models.ModifyCopilotEmbedConfigResponse:
        """
        @summary 修改智能问数嵌入配置。
        
        @param request: ModifyCopilotEmbedConfigRequest
        @return: ModifyCopilotEmbedConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_copilot_embed_config_with_options(request, runtime)

    async def modify_copilot_embed_config_async(
        self,
        request: quickbi_public_20220101_models.ModifyCopilotEmbedConfigRequest,
    ) -> quickbi_public_20220101_models.ModifyCopilotEmbedConfigResponse:
        """
        @summary 修改智能问数嵌入配置。
        
        @param request: ModifyCopilotEmbedConfigRequest
        @return: ModifyCopilotEmbedConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_copilot_embed_config_with_options_async(request, runtime)

    def query_approval_info_with_options(
        self,
        request: quickbi_public_20220101_models.QueryApprovalInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryApprovalInfoResponse:
        """
        @summary 根据审批人获取相应的审批流信息。
        
        @param request: QueryApprovalInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryApprovalInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryApprovalInfo',
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
            quickbi_public_20220101_models.QueryApprovalInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_approval_info_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryApprovalInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryApprovalInfoResponse:
        """
        @summary 根据审批人获取相应的审批流信息。
        
        @param request: QueryApprovalInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryApprovalInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryApprovalInfo',
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
            quickbi_public_20220101_models.QueryApprovalInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_approval_info(
        self,
        request: quickbi_public_20220101_models.QueryApprovalInfoRequest,
    ) -> quickbi_public_20220101_models.QueryApprovalInfoResponse:
        """
        @summary 根据审批人获取相应的审批流信息。
        
        @param request: QueryApprovalInfoRequest
        @return: QueryApprovalInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_approval_info_with_options(request, runtime)

    async def query_approval_info_async(
        self,
        request: quickbi_public_20220101_models.QueryApprovalInfoRequest,
    ) -> quickbi_public_20220101_models.QueryApprovalInfoResponse:
        """
        @summary 根据审批人获取相应的审批流信息。
        
        @param request: QueryApprovalInfoRequest
        @return: QueryApprovalInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_approval_info_with_options_async(request, runtime)

    def query_audit_log_with_options(
        self,
        request: quickbi_public_20220101_models.QueryAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryAuditLogResponse:
        """
        @summary 查询审计日志信息。
        
        @param request: QueryAuditLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAuditLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.operator_id):
            query['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_types):
            query['OperatorTypes'] = request.operator_types
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAuditLog',
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
            quickbi_public_20220101_models.QueryAuditLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_audit_log_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryAuditLogResponse:
        """
        @summary 查询审计日志信息。
        
        @param request: QueryAuditLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAuditLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.operator_id):
            query['OperatorId'] = request.operator_id
        if not UtilClient.is_unset(request.operator_types):
            query['OperatorTypes'] = request.operator_types
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAuditLog',
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
            quickbi_public_20220101_models.QueryAuditLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_audit_log(
        self,
        request: quickbi_public_20220101_models.QueryAuditLogRequest,
    ) -> quickbi_public_20220101_models.QueryAuditLogResponse:
        """
        @summary 查询审计日志信息。
        
        @param request: QueryAuditLogRequest
        @return: QueryAuditLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_audit_log_with_options(request, runtime)

    async def query_audit_log_async(
        self,
        request: quickbi_public_20220101_models.QueryAuditLogRequest,
    ) -> quickbi_public_20220101_models.QueryAuditLogResponse:
        """
        @summary 查询审计日志信息。
        
        @param request: QueryAuditLogRequest
        @return: QueryAuditLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_audit_log_with_options_async(request, runtime)

    def query_component_performance_with_options(
        self,
        request: quickbi_public_20220101_models.QueryComponentPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryComponentPerformanceResponse:
        """
        @summary 查询组件性能列表。
        
        @param request: QueryComponentPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryComponentPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryComponentPerformance',
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
            quickbi_public_20220101_models.QueryComponentPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_component_performance_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryComponentPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryComponentPerformanceResponse:
        """
        @summary 查询组件性能列表。
        
        @param request: QueryComponentPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryComponentPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryComponentPerformance',
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
            quickbi_public_20220101_models.QueryComponentPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_component_performance(
        self,
        request: quickbi_public_20220101_models.QueryComponentPerformanceRequest,
    ) -> quickbi_public_20220101_models.QueryComponentPerformanceResponse:
        """
        @summary 查询组件性能列表。
        
        @param request: QueryComponentPerformanceRequest
        @return: QueryComponentPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_component_performance_with_options(request, runtime)

    async def query_component_performance_async(
        self,
        request: quickbi_public_20220101_models.QueryComponentPerformanceRequest,
    ) -> quickbi_public_20220101_models.QueryComponentPerformanceResponse:
        """
        @summary 查询组件性能列表。
        
        @param request: QueryComponentPerformanceRequest
        @return: QueryComponentPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_component_performance_with_options_async(request, runtime)

    def query_copilot_embed_config_with_options(
        self,
        request: quickbi_public_20220101_models.QueryCopilotEmbedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryCopilotEmbedConfigResponse:
        """
        @summary 获取开通小Q嵌入的配置列表。
        
        @param request: QueryCopilotEmbedConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCopilotEmbedConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCopilotEmbedConfig',
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
            quickbi_public_20220101_models.QueryCopilotEmbedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_copilot_embed_config_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryCopilotEmbedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryCopilotEmbedConfigResponse:
        """
        @summary 获取开通小Q嵌入的配置列表。
        
        @param request: QueryCopilotEmbedConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCopilotEmbedConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCopilotEmbedConfig',
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
            quickbi_public_20220101_models.QueryCopilotEmbedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_copilot_embed_config(
        self,
        request: quickbi_public_20220101_models.QueryCopilotEmbedConfigRequest,
    ) -> quickbi_public_20220101_models.QueryCopilotEmbedConfigResponse:
        """
        @summary 获取开通小Q嵌入的配置列表。
        
        @param request: QueryCopilotEmbedConfigRequest
        @return: QueryCopilotEmbedConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_copilot_embed_config_with_options(request, runtime)

    async def query_copilot_embed_config_async(
        self,
        request: quickbi_public_20220101_models.QueryCopilotEmbedConfigRequest,
    ) -> quickbi_public_20220101_models.QueryCopilotEmbedConfigResponse:
        """
        @summary 获取开通小Q嵌入的配置列表。
        
        @param request: QueryCopilotEmbedConfigRequest
        @return: QueryCopilotEmbedConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_copilot_embed_config_with_options_async(request, runtime)

    def query_cube_optimization_with_options(
        self,
        request: quickbi_public_20220101_models.QueryCubeOptimizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryCubeOptimizationResponse:
        """
        @summary 查询数据集优化建议。
        
        @param request: QueryCubeOptimizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCubeOptimizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCubeOptimization',
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
            quickbi_public_20220101_models.QueryCubeOptimizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cube_optimization_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryCubeOptimizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryCubeOptimizationResponse:
        """
        @summary 查询数据集优化建议。
        
        @param request: QueryCubeOptimizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCubeOptimizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCubeOptimization',
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
            quickbi_public_20220101_models.QueryCubeOptimizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cube_optimization(
        self,
        request: quickbi_public_20220101_models.QueryCubeOptimizationRequest,
    ) -> quickbi_public_20220101_models.QueryCubeOptimizationResponse:
        """
        @summary 查询数据集优化建议。
        
        @param request: QueryCubeOptimizationRequest
        @return: QueryCubeOptimizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_cube_optimization_with_options(request, runtime)

    async def query_cube_optimization_async(
        self,
        request: quickbi_public_20220101_models.QueryCubeOptimizationRequest,
    ) -> quickbi_public_20220101_models.QueryCubeOptimizationResponse:
        """
        @summary 查询数据集优化建议。
        
        @param request: QueryCubeOptimizationRequest
        @return: QueryCubeOptimizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_cube_optimization_with_options_async(request, runtime)

    def query_cube_performance_with_options(
        self,
        request: quickbi_public_20220101_models.QueryCubePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryCubePerformanceResponse:
        """
        @summary 查询数据集性能。
        
        @param request: QueryCubePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCubePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCubePerformance',
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
            quickbi_public_20220101_models.QueryCubePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cube_performance_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryCubePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryCubePerformanceResponse:
        """
        @summary 查询数据集性能。
        
        @param request: QueryCubePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCubePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not UtilClient.is_unset(request.cube_id):
            query['CubeId'] = request.cube_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCubePerformance',
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
            quickbi_public_20220101_models.QueryCubePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cube_performance(
        self,
        request: quickbi_public_20220101_models.QueryCubePerformanceRequest,
    ) -> quickbi_public_20220101_models.QueryCubePerformanceResponse:
        """
        @summary 查询数据集性能。
        
        @param request: QueryCubePerformanceRequest
        @return: QueryCubePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_cube_performance_with_options(request, runtime)

    async def query_cube_performance_async(
        self,
        request: quickbi_public_20220101_models.QueryCubePerformanceRequest,
    ) -> quickbi_public_20220101_models.QueryCubePerformanceResponse:
        """
        @summary 查询数据集性能。
        
        @param request: QueryCubePerformanceRequest
        @return: QueryCubePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_cube_performance_with_options_async(request, runtime)

    def query_data_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDataResponse:
        """
        @summary 调用开放数据服务API。
        
        @param request: QueryDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.conditions):
            query['Conditions'] = request.conditions
        if not UtilClient.is_unset(request.return_fields):
            query['ReturnFields'] = request.return_fields
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryData',
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
            quickbi_public_20220101_models.QueryDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDataResponse:
        """
        @summary 调用开放数据服务API。
        
        @param request: QueryDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.conditions):
            query['Conditions'] = request.conditions
        if not UtilClient.is_unset(request.return_fields):
            query['ReturnFields'] = request.return_fields
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryData',
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
            quickbi_public_20220101_models.QueryDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data(
        self,
        request: quickbi_public_20220101_models.QueryDataRequest,
    ) -> quickbi_public_20220101_models.QueryDataResponse:
        """
        @summary 调用开放数据服务API。
        
        @param request: QueryDataRequest
        @return: QueryDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_data_with_options(request, runtime)

    async def query_data_async(
        self,
        request: quickbi_public_20220101_models.QueryDataRequest,
    ) -> quickbi_public_20220101_models.QueryDataResponse:
        """
        @summary 调用开放数据服务API。
        
        @param request: QueryDataRequest
        @return: QueryDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_data_with_options_async(request, runtime)

    def query_data_range_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDataRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDataRangeResponse:
        """
        @summary 获取数据范围目录列表。
        
        @param request: QueryDataRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataRangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataRange',
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
            quickbi_public_20220101_models.QueryDataRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_range_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryDataRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDataRangeResponse:
        """
        @summary 获取数据范围目录列表。
        
        @param request: QueryDataRangeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataRangeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataRange',
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
            quickbi_public_20220101_models.QueryDataRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_range(
        self,
        request: quickbi_public_20220101_models.QueryDataRangeRequest,
    ) -> quickbi_public_20220101_models.QueryDataRangeResponse:
        """
        @summary 获取数据范围目录列表。
        
        @param request: QueryDataRangeRequest
        @return: QueryDataRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_data_range_with_options(request, runtime)

    async def query_data_range_async(
        self,
        request: quickbi_public_20220101_models.QueryDataRangeRequest,
    ) -> quickbi_public_20220101_models.QueryDataRangeResponse:
        """
        @summary 获取数据范围目录列表。
        
        @param request: QueryDataRangeRequest
        @return: QueryDataRangeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_data_range_with_options_async(request, runtime)

    def query_data_service_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDataServiceResponse:
        """
        @summary The operator for the aggregate operation. Metric fields are available, such as SUM, AVG, and MAX.
        
        @description f4cc43bc3**\
        
        @param request: QueryDataServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataServiceResponse
        """
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
        """
        @summary The operator for the aggregate operation. Metric fields are available, such as SUM, AVG, and MAX.
        
        @description f4cc43bc3**\
        
        @param request: QueryDataServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataServiceResponse
        """
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
        """
        @summary The operator for the aggregate operation. Metric fields are available, such as SUM, AVG, and MAX.
        
        @description f4cc43bc3**\
        
        @param request: QueryDataServiceRequest
        @return: QueryDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_data_service_with_options(request, runtime)

    async def query_data_service_async(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceRequest,
    ) -> quickbi_public_20220101_models.QueryDataServiceResponse:
        """
        @summary The operator for the aggregate operation. Metric fields are available, such as SUM, AVG, and MAX.
        
        @description f4cc43bc3**\
        
        @param request: QueryDataServiceRequest
        @return: QueryDataServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_data_service_with_options_async(request, runtime)

    def query_data_service_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDataServiceListResponse:
        """
        @summary 查询数据服务API列表。
        
        @param request: QueryDataServiceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataServiceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataServiceList',
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
            quickbi_public_20220101_models.QueryDataServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_data_service_list_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDataServiceListResponse:
        """
        @summary 查询数据服务API列表。
        
        @param request: QueryDataServiceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDataServiceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataServiceList',
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
            quickbi_public_20220101_models.QueryDataServiceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_data_service_list(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceListRequest,
    ) -> quickbi_public_20220101_models.QueryDataServiceListResponse:
        """
        @summary 查询数据服务API列表。
        
        @param request: QueryDataServiceListRequest
        @return: QueryDataServiceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_data_service_list_with_options(request, runtime)

    async def query_data_service_list_async(
        self,
        request: quickbi_public_20220101_models.QueryDataServiceListRequest,
    ) -> quickbi_public_20220101_models.QueryDataServiceListResponse:
        """
        @summary 查询数据服务API列表。
        
        @param request: QueryDataServiceListRequest
        @return: QueryDataServiceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_data_service_list_with_options_async(request, runtime)

    def query_dataset_detail_info_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDatasetDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetDetailInfoResponse:
        """
        @summary Queries the details of a specified dataset, including the data source, directory, and dataset model.
        
        @description The data source, directory, and dataset model (including dimensions, measures, physical fields, custom SQL text, and association relationships).
        
        @param request: QueryDatasetDetailInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDatasetDetailInfoResponse
        """
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
        """
        @summary Queries the details of a specified dataset, including the data source, directory, and dataset model.
        
        @description The data source, directory, and dataset model (including dimensions, measures, physical fields, custom SQL text, and association relationships).
        
        @param request: QueryDatasetDetailInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDatasetDetailInfoResponse
        """
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
        """
        @summary Queries the details of a specified dataset, including the data source, directory, and dataset model.
        
        @description The data source, directory, and dataset model (including dimensions, measures, physical fields, custom SQL text, and association relationships).
        
        @param request: QueryDatasetDetailInfoRequest
        @return: QueryDatasetDetailInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_detail_info_with_options(request, runtime)

    async def query_dataset_detail_info_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetDetailInfoRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetDetailInfoResponse:
        """
        @summary Queries the details of a specified dataset, including the data source, directory, and dataset model.
        
        @description The data source, directory, and dataset model (including dimensions, measures, physical fields, custom SQL text, and association relationships).
        
        @param request: QueryDatasetDetailInfoRequest
        @return: QueryDatasetDetailInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_detail_info_with_options_async(request, runtime)

    def query_dataset_info_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDatasetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetInfoResponse:
        """
        @summary Indicates whether the table is a custom SQL table. Valid values:
        true: custom SQL table
        false: non-custom SQL table
        
        @param request: QueryDatasetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDatasetInfoResponse
        """
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
        """
        @summary Indicates whether the table is a custom SQL table. Valid values:
        true: custom SQL table
        false: non-custom SQL table
        
        @param request: QueryDatasetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDatasetInfoResponse
        """
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
        """
        @summary Indicates whether the table is a custom SQL table. Valid values:
        true: custom SQL table
        false: non-custom SQL table
        
        @param request: QueryDatasetInfoRequest
        @return: QueryDatasetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_info_with_options(request, runtime)

    async def query_dataset_info_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetInfoRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetInfoResponse:
        """
        @summary Indicates whether the table is a custom SQL table. Valid values:
        true: custom SQL table
        false: non-custom SQL table
        
        @param request: QueryDatasetInfoRequest
        @return: QueryDatasetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_info_with_options_async(request, runtime)

    def query_dataset_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDatasetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetListResponse:
        """
        @summary The name of the training dataset.
        
        @param request: QueryDatasetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDatasetListResponse
        """
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
        """
        @summary The name of the training dataset.
        
        @param request: QueryDatasetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDatasetListResponse
        """
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
        """
        @summary The name of the training dataset.
        
        @param request: QueryDatasetListRequest
        @return: QueryDatasetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_list_with_options(request, runtime)

    async def query_dataset_list_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetListRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetListResponse:
        """
        @summary The name of the training dataset.
        
        @param request: QueryDatasetListRequest
        @return: QueryDatasetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_list_with_options_async(request, runtime)

    def query_dataset_switch_info_with_options(
        self,
        request: quickbi_public_20220101_models.QueryDatasetSwitchInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryDatasetSwitchInfoResponse:
        """
        @summary 获取指定数据集的行级权限开关状态。
        
        @param request: QueryDatasetSwitchInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDatasetSwitchInfoResponse
        """
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
        """
        @summary 获取指定数据集的行级权限开关状态。
        
        @param request: QueryDatasetSwitchInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDatasetSwitchInfoResponse
        """
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
        """
        @summary 获取指定数据集的行级权限开关状态。
        
        @param request: QueryDatasetSwitchInfoRequest
        @return: QueryDatasetSwitchInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_switch_info_with_options(request, runtime)

    async def query_dataset_switch_info_async(
        self,
        request: quickbi_public_20220101_models.QueryDatasetSwitchInfoRequest,
    ) -> quickbi_public_20220101_models.QueryDatasetSwitchInfoResponse:
        """
        @summary 获取指定数据集的行级权限开关状态。
        
        @param request: QueryDatasetSwitchInfoRequest
        @return: QueryDatasetSwitchInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_switch_info_with_options_async(request, runtime)

    def query_embedded_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryEmbeddedInfoResponse:
        """
        @summary The number of reports that are currently embedded.
        
        @param request: QueryEmbeddedInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEmbeddedInfoResponse
        """
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
        """
        @summary The number of reports that are currently embedded.
        
        @param request: QueryEmbeddedInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEmbeddedInfoResponse
        """
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
        """
        @summary The number of reports that are currently embedded.
        
        @return: QueryEmbeddedInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_embedded_info_with_options(runtime)

    async def query_embedded_info_async(self) -> quickbi_public_20220101_models.QueryEmbeddedInfoResponse:
        """
        @summary The number of reports that are currently embedded.
        
        @return: QueryEmbeddedInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_embedded_info_with_options_async(runtime)

    def query_embedded_status_with_options(
        self,
        request: quickbi_public_20220101_models.QueryEmbeddedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryEmbeddedStatusResponse:
        """
        @summary Queries whether embedding is enabled for a report.
        
        @param request: QueryEmbeddedStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEmbeddedStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEmbeddedStatus',
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
            quickbi_public_20220101_models.QueryEmbeddedStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_embedded_status_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryEmbeddedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryEmbeddedStatusResponse:
        """
        @summary Queries whether embedding is enabled for a report.
        
        @param request: QueryEmbeddedStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEmbeddedStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.works_id):
            query['WorksId'] = request.works_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEmbeddedStatus',
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
            quickbi_public_20220101_models.QueryEmbeddedStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_embedded_status(
        self,
        request: quickbi_public_20220101_models.QueryEmbeddedStatusRequest,
    ) -> quickbi_public_20220101_models.QueryEmbeddedStatusResponse:
        """
        @summary Queries whether embedding is enabled for a report.
        
        @param request: QueryEmbeddedStatusRequest
        @return: QueryEmbeddedStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_embedded_status_with_options(request, runtime)

    async def query_embedded_status_async(
        self,
        request: quickbi_public_20220101_models.QueryEmbeddedStatusRequest,
    ) -> quickbi_public_20220101_models.QueryEmbeddedStatusResponse:
        """
        @summary Queries whether embedding is enabled for a report.
        
        @param request: QueryEmbeddedStatusRequest
        @return: QueryEmbeddedStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_embedded_status_with_options_async(request, runtime)

    def query_organization_role_config_with_options(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationRoleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryOrganizationRoleConfigResponse:
        """
        @summary 获取指定组织角色的配置信息
        
        @param request: QueryOrganizationRoleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrganizationRoleConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrganizationRoleConfig',
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
            quickbi_public_20220101_models.QueryOrganizationRoleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_organization_role_config_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationRoleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryOrganizationRoleConfigResponse:
        """
        @summary 获取指定组织角色的配置信息
        
        @param request: QueryOrganizationRoleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrganizationRoleConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrganizationRoleConfig',
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
            quickbi_public_20220101_models.QueryOrganizationRoleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_organization_role_config(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationRoleConfigRequest,
    ) -> quickbi_public_20220101_models.QueryOrganizationRoleConfigResponse:
        """
        @summary 获取指定组织角色的配置信息
        
        @param request: QueryOrganizationRoleConfigRequest
        @return: QueryOrganizationRoleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_organization_role_config_with_options(request, runtime)

    async def query_organization_role_config_async(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationRoleConfigRequest,
    ) -> quickbi_public_20220101_models.QueryOrganizationRoleConfigResponse:
        """
        @summary 获取指定组织角色的配置信息
        
        @param request: QueryOrganizationRoleConfigRequest
        @return: QueryOrganizationRoleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_organization_role_config_with_options_async(request, runtime)

    def query_organization_workspace_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationWorkspaceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryOrganizationWorkspaceListResponse:
        """
        @summary 获取当前组织下的工作空间列表信息。
        
        @param request: QueryOrganizationWorkspaceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrganizationWorkspaceListResponse
        """
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
        """
        @summary 获取当前组织下的工作空间列表信息。
        
        @param request: QueryOrganizationWorkspaceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrganizationWorkspaceListResponse
        """
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
        """
        @summary 获取当前组织下的工作空间列表信息。
        
        @param request: QueryOrganizationWorkspaceListRequest
        @return: QueryOrganizationWorkspaceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_organization_workspace_list_with_options(request, runtime)

    async def query_organization_workspace_list_async(
        self,
        request: quickbi_public_20220101_models.QueryOrganizationWorkspaceListRequest,
    ) -> quickbi_public_20220101_models.QueryOrganizationWorkspaceListResponse:
        """
        @summary 获取当前组织下的工作空间列表信息。
        
        @param request: QueryOrganizationWorkspaceListRequest
        @return: QueryOrganizationWorkspaceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_organization_workspace_list_with_options_async(request, runtime)

    def query_readable_resources_list_by_user_id_with_options(
        self,
        request: quickbi_public_20220101_models.QueryReadableResourcesListByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryReadableResourcesListByUserIdResponse:
        """
        @summary The Alibaba Cloud account name of the owner.
        
        @param request: QueryReadableResourcesListByUserIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryReadableResourcesListByUserIdResponse
        """
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
        """
        @summary The Alibaba Cloud account name of the owner.
        
        @param request: QueryReadableResourcesListByUserIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryReadableResourcesListByUserIdResponse
        """
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
        """
        @summary The Alibaba Cloud account name of the owner.
        
        @param request: QueryReadableResourcesListByUserIdRequest
        @return: QueryReadableResourcesListByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_readable_resources_list_by_user_id_with_options(request, runtime)

    async def query_readable_resources_list_by_user_id_async(
        self,
        request: quickbi_public_20220101_models.QueryReadableResourcesListByUserIdRequest,
    ) -> quickbi_public_20220101_models.QueryReadableResourcesListByUserIdResponse:
        """
        @summary The Alibaba Cloud account name of the owner.
        
        @param request: QueryReadableResourcesListByUserIdRequest
        @return: QueryReadableResourcesListByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_readable_resources_list_by_user_id_with_options_async(request, runtime)

    def query_report_performance_with_options(
        self,
        request: quickbi_public_20220101_models.QueryReportPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryReportPerformanceResponse:
        """
        @summary 查询报表性能列表
        
        @param request: QueryReportPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryReportPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReportPerformance',
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
            quickbi_public_20220101_models.QueryReportPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_report_performance_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryReportPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryReportPerformanceResponse:
        """
        @summary 查询报表性能列表
        
        @param request: QueryReportPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryReportPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cost_time_avg_min):
            query['CostTimeAvgMin'] = request.cost_time_avg_min
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.report_id):
            query['ReportId'] = request.report_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReportPerformance',
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
            quickbi_public_20220101_models.QueryReportPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_report_performance(
        self,
        request: quickbi_public_20220101_models.QueryReportPerformanceRequest,
    ) -> quickbi_public_20220101_models.QueryReportPerformanceResponse:
        """
        @summary 查询报表性能列表
        
        @param request: QueryReportPerformanceRequest
        @return: QueryReportPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_report_performance_with_options(request, runtime)

    async def query_report_performance_async(
        self,
        request: quickbi_public_20220101_models.QueryReportPerformanceRequest,
    ) -> quickbi_public_20220101_models.QueryReportPerformanceResponse:
        """
        @summary 查询报表性能列表
        
        @param request: QueryReportPerformanceRequest
        @return: QueryReportPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_report_performance_with_options_async(request, runtime)

    def query_share_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryShareListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryShareListResponse:
        """
        @summary Xiao Zhang
        
        @param request: QueryShareListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShareListResponse
        """
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
        """
        @summary Xiao Zhang
        
        @param request: QueryShareListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShareListResponse
        """
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
        """
        @summary Xiao Zhang
        
        @param request: QueryShareListRequest
        @return: QueryShareListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_share_list_with_options(request, runtime)

    async def query_share_list_async(
        self,
        request: quickbi_public_20220101_models.QueryShareListRequest,
    ) -> quickbi_public_20220101_models.QueryShareListResponse:
        """
        @summary Xiao Zhang
        
        @param request: QueryShareListRequest
        @return: QueryShareListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_share_list_with_options_async(request, runtime)

    def query_shares_to_user_list_with_options(
        self,
        request: quickbi_public_20220101_models.QuerySharesToUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QuerySharesToUserListResponse:
        """
        @summary You can call this operation to query the list of works authorized to a user.
        
        @param request: QuerySharesToUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySharesToUserListResponse
        """
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
        """
        @summary You can call this operation to query the list of works authorized to a user.
        
        @param request: QuerySharesToUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySharesToUserListResponse
        """
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
        """
        @summary You can call this operation to query the list of works authorized to a user.
        
        @param request: QuerySharesToUserListRequest
        @return: QuerySharesToUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_shares_to_user_list_with_options(request, runtime)

    async def query_shares_to_user_list_async(
        self,
        request: quickbi_public_20220101_models.QuerySharesToUserListRequest,
    ) -> quickbi_public_20220101_models.QuerySharesToUserListResponse:
        """
        @summary You can call this operation to query the list of works authorized to a user.
        
        @param request: QuerySharesToUserListRequest
        @return: QuerySharesToUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_shares_to_user_list_with_options_async(request, runtime)

    def query_ticket_info_with_options(
        self,
        request: quickbi_public_20220101_models.QueryTicketInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryTicketInfoResponse:
        """
        @summary auditing
        
        @param request: QueryTicketInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTicketInfoResponse
        """
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
        """
        @summary auditing
        
        @param request: QueryTicketInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTicketInfoResponse
        """
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
        """
        @summary auditing
        
        @param request: QueryTicketInfoRequest
        @return: QueryTicketInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_ticket_info_with_options(request, runtime)

    async def query_ticket_info_async(
        self,
        request: quickbi_public_20220101_models.QueryTicketInfoRequest,
    ) -> quickbi_public_20220101_models.QueryTicketInfoResponse:
        """
        @summary auditing
        
        @param request: QueryTicketInfoRequest
        @return: QueryTicketInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_ticket_info_with_options_async(request, runtime)

    def query_user_group_list_by_parent_id_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupListByParentIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserGroupListByParentIdResponse:
        """
        @summary You can this operation to obtain information about child user groups under a specified parent user group.
        
        @param request: QueryUserGroupListByParentIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserGroupListByParentIdResponse
        """
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
        """
        @summary You can this operation to obtain information about child user groups under a specified parent user group.
        
        @param request: QueryUserGroupListByParentIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserGroupListByParentIdResponse
        """
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
        """
        @summary You can this operation to obtain information about child user groups under a specified parent user group.
        
        @param request: QueryUserGroupListByParentIdRequest
        @return: QueryUserGroupListByParentIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_group_list_by_parent_id_with_options(request, runtime)

    async def query_user_group_list_by_parent_id_async(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupListByParentIdRequest,
    ) -> quickbi_public_20220101_models.QueryUserGroupListByParentIdResponse:
        """
        @summary You can this operation to obtain information about child user groups under a specified parent user group.
        
        @param request: QueryUserGroupListByParentIdRequest
        @return: QueryUserGroupListByParentIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_user_group_list_by_parent_id_with_options_async(request, runtime)

    def query_user_group_member_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserGroupMemberResponse:
        """
        @summary 获取用户组下的成员列表信息。
        
        @param request: QueryUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserGroupMemberResponse
        """
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
        """
        @summary 获取用户组下的成员列表信息。
        
        @param request: QueryUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserGroupMemberResponse
        """
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
        """
        @summary 获取用户组下的成员列表信息。
        
        @param request: QueryUserGroupMemberRequest
        @return: QueryUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_group_member_with_options(request, runtime)

    async def query_user_group_member_async(
        self,
        request: quickbi_public_20220101_models.QueryUserGroupMemberRequest,
    ) -> quickbi_public_20220101_models.QueryUserGroupMemberResponse:
        """
        @summary 获取用户组下的成员列表信息。
        
        @param request: QueryUserGroupMemberRequest
        @return: QueryUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_user_group_member_with_options_async(request, runtime)

    def query_user_info_by_account_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserInfoByAccountResponse:
        """
        @summary Queries user information based on the Alibaba Cloud ID or Alibaba Cloud account name.
        
        @param request: QueryUserInfoByAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserInfoByAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.parent_account_name):
            query['ParentAccountName'] = request.parent_account_name
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
        """
        @summary Queries user information based on the Alibaba Cloud ID or Alibaba Cloud account name.
        
        @param request: QueryUserInfoByAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserInfoByAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.parent_account_name):
            query['ParentAccountName'] = request.parent_account_name
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
        """
        @summary Queries user information based on the Alibaba Cloud ID or Alibaba Cloud account name.
        
        @param request: QueryUserInfoByAccountRequest
        @return: QueryUserInfoByAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_info_by_account_with_options(request, runtime)

    async def query_user_info_by_account_async(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByAccountRequest,
    ) -> quickbi_public_20220101_models.QueryUserInfoByAccountResponse:
        """
        @summary Queries user information based on the Alibaba Cloud ID or Alibaba Cloud account name.
        
        @param request: QueryUserInfoByAccountRequest
        @return: QueryUserInfoByAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_user_info_by_account_with_options_async(request, runtime)

    def query_user_info_by_user_id_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByUserIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserInfoByUserIdResponse:
        """
        @summary Queries user information based on the user ID.
        
        @param request: QueryUserInfoByUserIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserInfoByUserIdResponse
        """
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
        """
        @summary Queries user information based on the user ID.
        
        @param request: QueryUserInfoByUserIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserInfoByUserIdResponse
        """
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
        """
        @summary Queries user information based on the user ID.
        
        @param request: QueryUserInfoByUserIdRequest
        @return: QueryUserInfoByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_info_by_user_id_with_options(request, runtime)

    async def query_user_info_by_user_id_async(
        self,
        request: quickbi_public_20220101_models.QueryUserInfoByUserIdRequest,
    ) -> quickbi_public_20220101_models.QueryUserInfoByUserIdResponse:
        """
        @summary Queries user information based on the user ID.
        
        @param request: QueryUserInfoByUserIdRequest
        @return: QueryUserInfoByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_user_info_by_user_id_with_options_async(request, runtime)

    def query_user_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserListResponse:
        """
        @summary 查询组织成员列表信息。
        
        @param request: QueryUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserListResponse
        """
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
        """
        @summary 查询组织成员列表信息。
        
        @param request: QueryUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserListResponse
        """
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
        """
        @summary 查询组织成员列表信息。
        
        @param request: QueryUserListRequest
        @return: QueryUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_list_with_options(request, runtime)

    async def query_user_list_async(
        self,
        request: quickbi_public_20220101_models.QueryUserListRequest,
    ) -> quickbi_public_20220101_models.QueryUserListResponse:
        """
        @summary 查询组织成员列表信息。
        
        @param request: QueryUserListRequest
        @return: QueryUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_user_list_with_options_async(request, runtime)

    def query_user_role_info_in_workspace_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceResponse:
        """
        @summary 获取指定工作空间成员的预置空间角色信息。
        
        @param request: QueryUserRoleInfoInWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserRoleInfoInWorkspaceResponse
        """
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
        """
        @summary 获取指定工作空间成员的预置空间角色信息。
        
        @param request: QueryUserRoleInfoInWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserRoleInfoInWorkspaceResponse
        """
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
        """
        @summary 获取指定工作空间成员的预置空间角色信息。
        
        @param request: QueryUserRoleInfoInWorkspaceRequest
        @return: QueryUserRoleInfoInWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_role_info_in_workspace_with_options(request, runtime)

    async def query_user_role_info_in_workspace_async(
        self,
        request: quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceRequest,
    ) -> quickbi_public_20220101_models.QueryUserRoleInfoInWorkspaceResponse:
        """
        @summary 获取指定工作空间成员的预置空间角色信息。
        
        @param request: QueryUserRoleInfoInWorkspaceRequest
        @return: QueryUserRoleInfoInWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_user_role_info_in_workspace_with_options_async(request, runtime)

    def query_user_tag_meta_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserTagMetaListResponse:
        """
        @summary auditing
        
        @param request: QueryUserTagMetaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserTagMetaListResponse
        """
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
        """
        @summary auditing
        
        @param request: QueryUserTagMetaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserTagMetaListResponse
        """
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
        """
        @summary auditing
        
        @return: QueryUserTagMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_tag_meta_list_with_options(runtime)

    async def query_user_tag_meta_list_async(self) -> quickbi_public_20220101_models.QueryUserTagMetaListResponse:
        """
        @summary auditing
        
        @return: QueryUserTagMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_user_tag_meta_list_with_options_async(runtime)

    def query_user_tag_value_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryUserTagValueListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryUserTagValueListResponse:
        """
        @summary Queries the list of tag values for a specific user.
        
        @param request: QueryUserTagValueListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserTagValueListResponse
        """
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
        """
        @summary Queries the list of tag values for a specific user.
        
        @param request: QueryUserTagValueListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserTagValueListResponse
        """
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
        """
        @summary Queries the list of tag values for a specific user.
        
        @param request: QueryUserTagValueListRequest
        @return: QueryUserTagValueListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_tag_value_list_with_options(request, runtime)

    async def query_user_tag_value_list_async(
        self,
        request: quickbi_public_20220101_models.QueryUserTagValueListRequest,
    ) -> quickbi_public_20220101_models.QueryUserTagValueListResponse:
        """
        @summary Queries the list of tag values for a specific user.
        
        @param request: QueryUserTagValueListRequest
        @return: QueryUserTagValueListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_user_tag_value_list_with_options_async(request, runtime)

    def query_works_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksResponse:
        """
        @summary 获取报表详情
        
        @param request: QueryWorksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorksResponse
        """
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
        """
        @summary 获取报表详情
        
        @param request: QueryWorksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorksResponse
        """
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
        """
        @summary 获取报表详情
        
        @param request: QueryWorksRequest
        @return: QueryWorksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_works_with_options(request, runtime)

    async def query_works_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksRequest,
    ) -> quickbi_public_20220101_models.QueryWorksResponse:
        """
        @summary 获取报表详情
        
        @param request: QueryWorksRequest
        @return: QueryWorksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_works_with_options_async(request, runtime)

    def query_works_blood_relationship_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorksBloodRelationshipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksBloodRelationshipResponse:
        """
        @summary abcd***\
        
        @param request: QueryWorksBloodRelationshipRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorksBloodRelationshipResponse
        """
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
        """
        @summary abcd***\
        
        @param request: QueryWorksBloodRelationshipRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorksBloodRelationshipResponse
        """
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
        """
        @summary abcd***\
        
        @param request: QueryWorksBloodRelationshipRequest
        @return: QueryWorksBloodRelationshipResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_works_blood_relationship_with_options(request, runtime)

    async def query_works_blood_relationship_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksBloodRelationshipRequest,
    ) -> quickbi_public_20220101_models.QueryWorksBloodRelationshipResponse:
        """
        @summary abcd***\
        
        @param request: QueryWorksBloodRelationshipRequest
        @return: QueryWorksBloodRelationshipResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_works_blood_relationship_with_options_async(request, runtime)

    def query_works_by_organization_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorksByOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksByOrganizationResponse:
        """
        @summary The total number of rows in the table.
        
        @param request: QueryWorksByOrganizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorksByOrganizationResponse
        """
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
        """
        @summary The total number of rows in the table.
        
        @param request: QueryWorksByOrganizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorksByOrganizationResponse
        """
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
        """
        @summary The total number of rows in the table.
        
        @param request: QueryWorksByOrganizationRequest
        @return: QueryWorksByOrganizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_works_by_organization_with_options(request, runtime)

    async def query_works_by_organization_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksByOrganizationRequest,
    ) -> quickbi_public_20220101_models.QueryWorksByOrganizationResponse:
        """
        @summary The total number of rows in the table.
        
        @param request: QueryWorksByOrganizationRequest
        @return: QueryWorksByOrganizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_works_by_organization_with_options_async(request, runtime)

    def query_works_by_workspace_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorksByWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorksByWorkspaceResponse:
        """
        @summary The name of the directory.
        
        @param request: QueryWorksByWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorksByWorkspaceResponse
        """
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
        """
        @summary The name of the directory.
        
        @param request: QueryWorksByWorkspaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorksByWorkspaceResponse
        """
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
        """
        @summary The name of the directory.
        
        @param request: QueryWorksByWorkspaceRequest
        @return: QueryWorksByWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_works_by_workspace_with_options(request, runtime)

    async def query_works_by_workspace_async(
        self,
        request: quickbi_public_20220101_models.QueryWorksByWorkspaceRequest,
    ) -> quickbi_public_20220101_models.QueryWorksByWorkspaceResponse:
        """
        @summary The name of the directory.
        
        @param request: QueryWorksByWorkspaceRequest
        @return: QueryWorksByWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_works_by_workspace_with_options_async(request, runtime)

    def query_workspace_role_config_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceRoleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorkspaceRoleConfigResponse:
        """
        @summary 获取指定空间角色的配置信息
        
        @param request: QueryWorkspaceRoleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorkspaceRoleConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorkspaceRoleConfig',
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
            quickbi_public_20220101_models.QueryWorkspaceRoleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_workspace_role_config_with_options_async(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceRoleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorkspaceRoleConfigResponse:
        """
        @summary 获取指定空间角色的配置信息
        
        @param request: QueryWorkspaceRoleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorkspaceRoleConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWorkspaceRoleConfig',
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
            quickbi_public_20220101_models.QueryWorkspaceRoleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_workspace_role_config(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceRoleConfigRequest,
    ) -> quickbi_public_20220101_models.QueryWorkspaceRoleConfigResponse:
        """
        @summary 获取指定空间角色的配置信息
        
        @param request: QueryWorkspaceRoleConfigRequest
        @return: QueryWorkspaceRoleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_workspace_role_config_with_options(request, runtime)

    async def query_workspace_role_config_async(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceRoleConfigRequest,
    ) -> quickbi_public_20220101_models.QueryWorkspaceRoleConfigResponse:
        """
        @summary 获取指定空间角色的配置信息
        
        @param request: QueryWorkspaceRoleConfigRequest
        @return: QueryWorkspaceRoleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_workspace_role_config_with_options_async(request, runtime)

    def query_workspace_user_list_with_options(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceUserListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.QueryWorkspaceUserListResponse:
        """
        @summary 查询指定工作空间下的成员列表信息。
        
        @param request: QueryWorkspaceUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorkspaceUserListResponse
        """
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
        """
        @summary 查询指定工作空间下的成员列表信息。
        
        @param request: QueryWorkspaceUserListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWorkspaceUserListResponse
        """
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
        """
        @summary 查询指定工作空间下的成员列表信息。
        
        @param request: QueryWorkspaceUserListRequest
        @return: QueryWorkspaceUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_workspace_user_list_with_options(request, runtime)

    async def query_workspace_user_list_async(
        self,
        request: quickbi_public_20220101_models.QueryWorkspaceUserListRequest,
    ) -> quickbi_public_20220101_models.QueryWorkspaceUserListResponse:
        """
        @summary 查询指定工作空间下的成员列表信息。
        
        @param request: QueryWorkspaceUserListRequest
        @return: QueryWorkspaceUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_workspace_user_list_with_options_async(request, runtime)

    def result_callback_with_options(
        self,
        request: quickbi_public_20220101_models.ResultCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.ResultCallbackResponse:
        """
        @summary 第三方资源审批回调接口
        
        @param request: ResultCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResultCallbackResponse
        """
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
        """
        @summary 第三方资源审批回调接口
        
        @param request: ResultCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResultCallbackResponse
        """
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
        """
        @summary 第三方资源审批回调接口
        
        @param request: ResultCallbackRequest
        @return: ResultCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.result_callback_with_options(request, runtime)

    async def result_callback_async(
        self,
        request: quickbi_public_20220101_models.ResultCallbackRequest,
    ) -> quickbi_public_20220101_models.ResultCallbackResponse:
        """
        @summary 第三方资源审批回调接口
        
        @param request: ResultCallbackRequest
        @return: ResultCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.result_callback_with_options_async(request, runtime)

    def save_favorites_with_options(
        self,
        request: quickbi_public_20220101_models.SaveFavoritesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SaveFavoritesResponse:
        """
        @summary Add the user\\"s collection data works.
        
        @param request: SaveFavoritesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveFavoritesResponse
        """
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
        """
        @summary Add the user\\"s collection data works.
        
        @param request: SaveFavoritesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveFavoritesResponse
        """
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
        """
        @summary Add the user\\"s collection data works.
        
        @param request: SaveFavoritesRequest
        @return: SaveFavoritesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_favorites_with_options(request, runtime)

    async def save_favorites_async(
        self,
        request: quickbi_public_20220101_models.SaveFavoritesRequest,
    ) -> quickbi_public_20220101_models.SaveFavoritesResponse:
        """
        @summary Add the user\\"s collection data works.
        
        @param request: SaveFavoritesRequest
        @return: SaveFavoritesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_favorites_with_options_async(request, runtime)

    def set_data_level_permission_extra_config_with_options(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigResponse:
        """
        @summary 设置行列权限的额外配置
        
        @param request: SetDataLevelPermissionExtraConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDataLevelPermissionExtraConfigResponse
        """
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
        """
        @summary 设置行列权限的额外配置
        
        @param request: SetDataLevelPermissionExtraConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDataLevelPermissionExtraConfigResponse
        """
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
        """
        @summary 设置行列权限的额外配置
        
        @param request: SetDataLevelPermissionExtraConfigRequest
        @return: SetDataLevelPermissionExtraConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_data_level_permission_extra_config_with_options(request, runtime)

    async def set_data_level_permission_extra_config_async(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigRequest,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionExtraConfigResponse:
        """
        @summary 设置行列权限的额外配置
        
        @param request: SetDataLevelPermissionExtraConfigRequest
        @return: SetDataLevelPermissionExtraConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_data_level_permission_extra_config_with_options_async(request, runtime)

    def set_data_level_permission_rule_config_with_options(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigResponse:
        """
        @summary 设置单条数据集行列权限配置信息（新增和更新）
        
        @param request: SetDataLevelPermissionRuleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDataLevelPermissionRuleConfigResponse
        """
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
        """
        @summary 设置单条数据集行列权限配置信息（新增和更新）
        
        @param request: SetDataLevelPermissionRuleConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDataLevelPermissionRuleConfigResponse
        """
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
        """
        @summary 设置单条数据集行列权限配置信息（新增和更新）
        
        @param request: SetDataLevelPermissionRuleConfigRequest
        @return: SetDataLevelPermissionRuleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_data_level_permission_rule_config_with_options(request, runtime)

    async def set_data_level_permission_rule_config_async(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigRequest,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionRuleConfigResponse:
        """
        @summary 设置单条数据集行列权限配置信息（新增和更新）
        
        @param request: SetDataLevelPermissionRuleConfigRequest
        @return: SetDataLevelPermissionRuleConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_data_level_permission_rule_config_with_options_async(request, runtime)

    def set_data_level_permission_white_list_with_options(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionWhiteListResponse:
        """
        @summary Sets the whitelist for the specified row-level permissions.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.
        
        @param request: SetDataLevelPermissionWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDataLevelPermissionWhiteListResponse
        """
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
        """
        @summary Sets the whitelist for the specified row-level permissions.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.
        
        @param request: SetDataLevelPermissionWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDataLevelPermissionWhiteListResponse
        """
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
        """
        @summary Sets the whitelist for the specified row-level permissions.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.
        
        @param request: SetDataLevelPermissionWhiteListRequest
        @return: SetDataLevelPermissionWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_data_level_permission_white_list_with_options(request, runtime)

    async def set_data_level_permission_white_list_async(
        self,
        request: quickbi_public_20220101_models.SetDataLevelPermissionWhiteListRequest,
    ) -> quickbi_public_20220101_models.SetDataLevelPermissionWhiteListResponse:
        """
        @summary Sets the whitelist for the specified row-level permissions.
        
        @description > : You can only Quick BI the new row-column permission model. If you are still using the old row-column permission model, migrate to the new row-column permission model before you call this operation. To migrate row-level permissions to the new row-level permission model, perform the following steps: Choose Organizations> Security Configurations> Upgrade Row-Level Permissions. On the Upgrade Row-Level Permissions page, click *Upgrade**.
        
        @param request: SetDataLevelPermissionWhiteListRequest
        @return: SetDataLevelPermissionWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_data_level_permission_white_list_with_options_async(request, runtime)

    def update_data_level_permission_status_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateDataLevelPermissionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateDataLevelPermissionStatusResponse:
        """
        @summary Indicates whether the request is successful. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @description The execution result of the interface. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @param request: UpdateDataLevelPermissionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLevelPermissionStatusResponse
        """
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
        """
        @summary Indicates whether the request is successful. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @description The execution result of the interface. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @param request: UpdateDataLevelPermissionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLevelPermissionStatusResponse
        """
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
        """
        @summary Indicates whether the request is successful. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @description The execution result of the interface. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @param request: UpdateDataLevelPermissionStatusRequest
        @return: UpdateDataLevelPermissionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_level_permission_status_with_options(request, runtime)

    async def update_data_level_permission_status_async(
        self,
        request: quickbi_public_20220101_models.UpdateDataLevelPermissionStatusRequest,
    ) -> quickbi_public_20220101_models.UpdateDataLevelPermissionStatusResponse:
        """
        @summary Indicates whether the request is successful. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @description The execution result of the interface. Valid values:
        true: The request was successful.
        false: The request failed.
        
        @param request: UpdateDataLevelPermissionStatusRequest
        @return: UpdateDataLevelPermissionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_level_permission_status_with_options_async(request, runtime)

    def update_embedded_status_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateEmbeddedStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateEmbeddedStatusResponse:
        """
        @summary The ID of the request.
        
        @param request: UpdateEmbeddedStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEmbeddedStatusResponse
        """
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
        """
        @summary The ID of the request.
        
        @param request: UpdateEmbeddedStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateEmbeddedStatusResponse
        """
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
        """
        @summary The ID of the request.
        
        @param request: UpdateEmbeddedStatusRequest
        @return: UpdateEmbeddedStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_embedded_status_with_options(request, runtime)

    async def update_embedded_status_async(
        self,
        request: quickbi_public_20220101_models.UpdateEmbeddedStatusRequest,
    ) -> quickbi_public_20220101_models.UpdateEmbeddedStatusResponse:
        """
        @summary The ID of the request.
        
        @param request: UpdateEmbeddedStatusRequest
        @return: UpdateEmbeddedStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_embedded_status_with_options_async(request, runtime)

    def update_ticket_num_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateTicketNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateTicketNumResponse:
        """
        @summary 更新三方嵌入ticket的票据数量
        
        @param request: UpdateTicketNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTicketNumResponse
        """
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
        """
        @summary 更新三方嵌入ticket的票据数量
        
        @param request: UpdateTicketNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTicketNumResponse
        """
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
        """
        @summary 更新三方嵌入ticket的票据数量
        
        @param request: UpdateTicketNumRequest
        @return: UpdateTicketNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ticket_num_with_options(request, runtime)

    async def update_ticket_num_async(
        self,
        request: quickbi_public_20220101_models.UpdateTicketNumRequest,
    ) -> quickbi_public_20220101_models.UpdateTicketNumResponse:
        """
        @summary 更新三方嵌入ticket的票据数量
        
        @param request: UpdateTicketNumRequest
        @return: UpdateTicketNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ticket_num_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserResponse:
        """
        @summary Updates the information of a specified member in an organization.
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not UtilClient.is_unset(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not UtilClient.is_unset(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.role_ids):
            query['RoleIds'] = request.role_ids
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
        """
        @summary Updates the information of a specified member in an organization.
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_user):
            query['AdminUser'] = request.admin_user
        if not UtilClient.is_unset(request.auth_admin_user):
            query['AuthAdminUser'] = request.auth_admin_user
        if not UtilClient.is_unset(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not UtilClient.is_unset(request.nick_name):
            query['NickName'] = request.nick_name
        if not UtilClient.is_unset(request.role_ids):
            query['RoleIds'] = request.role_ids
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
        """
        @summary Updates the information of a specified member in an organization.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserRequest,
    ) -> quickbi_public_20220101_models.UpdateUserResponse:
        """
        @summary Updates the information of a specified member in an organization.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserGroupResponse:
        """
        @summary Updates information about a specified user group in an organization.
        
        @param request: UpdateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserGroupResponse
        """
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
        """
        @summary Updates information about a specified user group in an organization.
        
        @param request: UpdateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserGroupResponse
        """
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
        """
        @summary Updates information about a specified user group in an organization.
        
        @param request: UpdateUserGroupRequest
        @return: UpdateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    async def update_user_group_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserGroupRequest,
    ) -> quickbi_public_20220101_models.UpdateUserGroupResponse:
        """
        @summary Updates information about a specified user group in an organization.
        
        @param request: UpdateUserGroupRequest
        @return: UpdateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_group_with_options_async(request, runtime)

    def update_user_tag_meta_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserTagMetaResponse:
        """
        @summary 用于更新组织成员标签元信息
        
        @param request: UpdateUserTagMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserTagMetaResponse
        """
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
        """
        @summary 用于更新组织成员标签元信息
        
        @param request: UpdateUserTagMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserTagMetaResponse
        """
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
        """
        @summary 用于更新组织成员标签元信息
        
        @param request: UpdateUserTagMetaRequest
        @return: UpdateUserTagMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_tag_meta_with_options(request, runtime)

    async def update_user_tag_meta_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagMetaRequest,
    ) -> quickbi_public_20220101_models.UpdateUserTagMetaResponse:
        """
        @summary 用于更新组织成员标签元信息
        
        @param request: UpdateUserTagMetaRequest
        @return: UpdateUserTagMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_tag_meta_with_options_async(request, runtime)

    def update_user_tag_value_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateUserTagValueResponse:
        """
        @summary 更新组织成员标签值
        
        @param request: UpdateUserTagValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserTagValueResponse
        """
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
        """
        @summary 更新组织成员标签值
        
        @param request: UpdateUserTagValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserTagValueResponse
        """
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
        """
        @summary 更新组织成员标签值
        
        @param request: UpdateUserTagValueRequest
        @return: UpdateUserTagValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_tag_value_with_options(request, runtime)

    async def update_user_tag_value_async(
        self,
        request: quickbi_public_20220101_models.UpdateUserTagValueRequest,
    ) -> quickbi_public_20220101_models.UpdateUserTagValueResponse:
        """
        @summary 更新组织成员标签值
        
        @param request: UpdateUserTagValueRequest
        @return: UpdateUserTagValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_tag_value_with_options_async(request, runtime)

    def update_workspace_user_role_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUserRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUserRoleResponse:
        """
        @summary 修改工作空间下指定成员的角色，已有的角色会被覆盖
        
        @param request: UpdateWorkspaceUserRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceUserRoleResponse
        """
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
        """
        @summary 修改工作空间下指定成员的角色，已有的角色会被覆盖
        
        @param request: UpdateWorkspaceUserRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceUserRoleResponse
        """
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
        """
        @summary 修改工作空间下指定成员的角色，已有的角色会被覆盖
        
        @param request: UpdateWorkspaceUserRoleRequest
        @return: UpdateWorkspaceUserRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_user_role_with_options(request, runtime)

    async def update_workspace_user_role_async(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUserRoleRequest,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUserRoleResponse:
        """
        @summary 修改工作空间下指定成员的角色，已有的角色会被覆盖
        
        @param request: UpdateWorkspaceUserRoleRequest
        @return: UpdateWorkspaceUserRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_workspace_user_role_with_options_async(request, runtime)

    def update_workspace_users_role_with_options(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUsersRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUsersRoleResponse:
        """
        @summary 批量更新工作空间成员的角色信息，已有角色会被覆盖
        
        @param request: UpdateWorkspaceUsersRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceUsersRoleResponse
        """
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
        """
        @summary 批量更新工作空间成员的角色信息，已有角色会被覆盖
        
        @param request: UpdateWorkspaceUsersRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkspaceUsersRoleResponse
        """
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
        """
        @summary 批量更新工作空间成员的角色信息，已有角色会被覆盖
        
        @param request: UpdateWorkspaceUsersRoleRequest
        @return: UpdateWorkspaceUsersRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_users_role_with_options(request, runtime)

    async def update_workspace_users_role_async(
        self,
        request: quickbi_public_20220101_models.UpdateWorkspaceUsersRoleRequest,
    ) -> quickbi_public_20220101_models.UpdateWorkspaceUsersRoleResponse:
        """
        @summary 批量更新工作空间成员的角色信息，已有角色会被覆盖
        
        @param request: UpdateWorkspaceUsersRoleRequest
        @return: UpdateWorkspaceUsersRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_workspace_users_role_with_options_async(request, runtime)

    def withdraw_all_user_groups_with_options(
        self,
        request: quickbi_public_20220101_models.WithdrawAllUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> quickbi_public_20220101_models.WithdrawAllUserGroupsResponse:
        """
        @summary Make the user exit all user groups. This process is irreversible. Exercise caution when performing this operation.
        
        @param request: WithdrawAllUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: WithdrawAllUserGroupsResponse
        """
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
        """
        @summary Make the user exit all user groups. This process is irreversible. Exercise caution when performing this operation.
        
        @param request: WithdrawAllUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: WithdrawAllUserGroupsResponse
        """
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
        """
        @summary Make the user exit all user groups. This process is irreversible. Exercise caution when performing this operation.
        
        @param request: WithdrawAllUserGroupsRequest
        @return: WithdrawAllUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.withdraw_all_user_groups_with_options(request, runtime)

    async def withdraw_all_user_groups_async(
        self,
        request: quickbi_public_20220101_models.WithdrawAllUserGroupsRequest,
    ) -> quickbi_public_20220101_models.WithdrawAllUserGroupsResponse:
        """
        @summary Make the user exit all user groups. This process is irreversible. Exercise caution when performing this operation.
        
        @param request: WithdrawAllUserGroupsRequest
        @return: WithdrawAllUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.withdraw_all_user_groups_with_options_async(request, runtime)
