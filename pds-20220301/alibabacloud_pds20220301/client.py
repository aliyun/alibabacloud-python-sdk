# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_pds.client import Client as GatewayClientClient
from alibabacloud_pds20220301 import models as pds_20220301_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
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
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._disable_http_2 = True
        self._endpoint_rule = ''

    def add_group_member_with_options(
        self,
        request: pds_20220301_models.AddGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AddGroupMemberResponse:
        """
        @summary Adds a member to a group.
        
        @param request: AddGroupMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGroupMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.member_id):
            body['member_id'] = request.member_id
        if not UtilClient.is_unset(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupMember',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/add_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.AddGroupMemberResponse(),
            self.execute(params, req, runtime)
        )

    async def add_group_member_with_options_async(
        self,
        request: pds_20220301_models.AddGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AddGroupMemberResponse:
        """
        @summary Adds a member to a group.
        
        @param request: AddGroupMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGroupMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.member_id):
            body['member_id'] = request.member_id
        if not UtilClient.is_unset(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddGroupMember',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/add_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.AddGroupMemberResponse(),
            await self.execute_async(params, req, runtime)
        )

    def add_group_member(
        self,
        request: pds_20220301_models.AddGroupMemberRequest,
    ) -> pds_20220301_models.AddGroupMemberResponse:
        """
        @summary Adds a member to a group.
        
        @param request: AddGroupMemberRequest
        @return: AddGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_group_member_with_options(request, headers, runtime)

    async def add_group_member_async(
        self,
        request: pds_20220301_models.AddGroupMemberRequest,
    ) -> pds_20220301_models.AddGroupMemberResponse:
        """
        @summary Adds a member to a group.
        
        @param request: AddGroupMemberRequest
        @return: AddGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_group_member_with_options_async(request, headers, runtime)

    def add_story_files_with_options(
        self,
        request: pds_20220301_models.AddStoryFilesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AddStoryFilesResponse:
        """
        @summary 故事添加文件
        
        @param request: AddStoryFilesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddStoryFilesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddStoryFiles',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/add_story_files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.AddStoryFilesResponse(),
            self.execute(params, req, runtime)
        )

    async def add_story_files_with_options_async(
        self,
        request: pds_20220301_models.AddStoryFilesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AddStoryFilesResponse:
        """
        @summary 故事添加文件
        
        @param request: AddStoryFilesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddStoryFilesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddStoryFiles',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/add_story_files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.AddStoryFilesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def add_story_files(
        self,
        request: pds_20220301_models.AddStoryFilesRequest,
    ) -> pds_20220301_models.AddStoryFilesResponse:
        """
        @summary 故事添加文件
        
        @param request: AddStoryFilesRequest
        @return: AddStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_story_files_with_options(request, headers, runtime)

    async def add_story_files_async(
        self,
        request: pds_20220301_models.AddStoryFilesRequest,
    ) -> pds_20220301_models.AddStoryFilesResponse:
        """
        @summary 故事添加文件
        
        @param request: AddStoryFilesRequest
        @return: AddStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_story_files_with_options_async(request, headers, runtime)

    def assign_role_with_options(
        self,
        request: pds_20220301_models.AssignRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AssignRoleResponse:
        """
        @summary Assigns a group administrator role to a user.
        
        @description You can call this operation to assign a group administrator role to a user.
        
        @param request: AssignRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not UtilClient.is_unset(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not UtilClient.is_unset(request.role_id):
            body['role_id'] = request.role_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignRole',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/role/assign',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.AssignRoleResponse(),
            self.execute(params, req, runtime)
        )

    async def assign_role_with_options_async(
        self,
        request: pds_20220301_models.AssignRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AssignRoleResponse:
        """
        @summary Assigns a group administrator role to a user.
        
        @description You can call this operation to assign a group administrator role to a user.
        
        @param request: AssignRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not UtilClient.is_unset(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not UtilClient.is_unset(request.role_id):
            body['role_id'] = request.role_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignRole',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/role/assign',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.AssignRoleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def assign_role(
        self,
        request: pds_20220301_models.AssignRoleRequest,
    ) -> pds_20220301_models.AssignRoleResponse:
        """
        @summary Assigns a group administrator role to a user.
        
        @description You can call this operation to assign a group administrator role to a user.
        
        @param request: AssignRoleRequest
        @return: AssignRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.assign_role_with_options(request, headers, runtime)

    async def assign_role_async(
        self,
        request: pds_20220301_models.AssignRoleRequest,
    ) -> pds_20220301_models.AssignRoleResponse:
        """
        @summary Assigns a group administrator role to a user.
        
        @description You can call this operation to assign a group administrator role to a user.
        
        @param request: AssignRoleRequest
        @return: AssignRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.assign_role_with_options_async(request, headers, runtime)

    def authorize_with_options(
        self,
        tmp_req: pds_20220301_models.AuthorizeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AuthorizeResponse:
        """
        @summary Requests permissions by using OAuth 2.0.
        
        @description For more information, see "OAuth 2.0 For Web Server Applications" at [OAuth 2.0 For Web Server Applications](https://www.alibabacloud.com/help/en/pds/drive-and-photo-service-dev/user-guide/oauth-2-0-access-process-for-web-server-applications) in User Guide.
        
        @param tmp_req: AuthorizeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pds_20220301_models.AuthorizeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scope):
            request.scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scope, 'scope', 'simple')
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.hide_consent):
            query['hide_consent'] = request.hide_consent
        if not UtilClient.is_unset(request.login_type):
            query['login_type'] = request.login_type
        if not UtilClient.is_unset(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.response_type):
            query['response_type'] = request.response_type
        if not UtilClient.is_unset(request.scope_shrink):
            query['scope'] = request.scope_shrink
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Authorize',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/oauth/authorize',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='binary'
        )
        return TeaCore.from_map(
            pds_20220301_models.AuthorizeResponse(),
            self.execute(params, req, runtime)
        )

    async def authorize_with_options_async(
        self,
        tmp_req: pds_20220301_models.AuthorizeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.AuthorizeResponse:
        """
        @summary Requests permissions by using OAuth 2.0.
        
        @description For more information, see "OAuth 2.0 For Web Server Applications" at [OAuth 2.0 For Web Server Applications](https://www.alibabacloud.com/help/en/pds/drive-and-photo-service-dev/user-guide/oauth-2-0-access-process-for-web-server-applications) in User Guide.
        
        @param tmp_req: AuthorizeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pds_20220301_models.AuthorizeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scope):
            request.scope_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scope, 'scope', 'simple')
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.hide_consent):
            query['hide_consent'] = request.hide_consent
        if not UtilClient.is_unset(request.login_type):
            query['login_type'] = request.login_type
        if not UtilClient.is_unset(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.response_type):
            query['response_type'] = request.response_type
        if not UtilClient.is_unset(request.scope_shrink):
            query['scope'] = request.scope_shrink
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Authorize',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/oauth/authorize',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='binary'
        )
        return TeaCore.from_map(
            pds_20220301_models.AuthorizeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def authorize(
        self,
        request: pds_20220301_models.AuthorizeRequest,
    ) -> pds_20220301_models.AuthorizeResponse:
        """
        @summary Requests permissions by using OAuth 2.0.
        
        @description For more information, see "OAuth 2.0 For Web Server Applications" at [OAuth 2.0 For Web Server Applications](https://www.alibabacloud.com/help/en/pds/drive-and-photo-service-dev/user-guide/oauth-2-0-access-process-for-web-server-applications) in User Guide.
        
        @param request: AuthorizeRequest
        @return: AuthorizeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.authorize_with_options(request, headers, runtime)

    async def authorize_async(
        self,
        request: pds_20220301_models.AuthorizeRequest,
    ) -> pds_20220301_models.AuthorizeResponse:
        """
        @summary Requests permissions by using OAuth 2.0.
        
        @description For more information, see "OAuth 2.0 For Web Server Applications" at [OAuth 2.0 For Web Server Applications](https://www.alibabacloud.com/help/en/pds/drive-and-photo-service-dev/user-guide/oauth-2-0-access-process-for-web-server-applications) in User Guide.
        
        @param request: AuthorizeRequest
        @return: AuthorizeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.authorize_with_options_async(request, headers, runtime)

    def batch_with_options(
        self,
        request: pds_20220301_models.BatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.BatchResponse:
        """
        @summary Calls multiple operations at a time to improve call efficiency.
        
        @param request: BatchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.requests):
            body['requests'] = request.requests
        if not UtilClient.is_unset(request.resource):
            body['resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Batch',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/batch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.BatchResponse(),
            self.execute(params, req, runtime)
        )

    async def batch_with_options_async(
        self,
        request: pds_20220301_models.BatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.BatchResponse:
        """
        @summary Calls multiple operations at a time to improve call efficiency.
        
        @param request: BatchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.requests):
            body['requests'] = request.requests
        if not UtilClient.is_unset(request.resource):
            body['resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Batch',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/batch',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.BatchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def batch(
        self,
        request: pds_20220301_models.BatchRequest,
    ) -> pds_20220301_models.BatchResponse:
        """
        @summary Calls multiple operations at a time to improve call efficiency.
        
        @param request: BatchRequest
        @return: BatchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_with_options(request, headers, runtime)

    async def batch_async(
        self,
        request: pds_20220301_models.BatchRequest,
    ) -> pds_20220301_models.BatchResponse:
        """
        @summary Calls multiple operations at a time to improve call efficiency.
        
        @param request: BatchRequest
        @return: BatchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_with_options_async(request, headers, runtime)

    def cancel_assign_role_with_options(
        self,
        request: pds_20220301_models.CancelAssignRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CancelAssignRoleResponse:
        """
        @summary Cancels a role.
        
        @description You can cancel only the group administrator role.
        
        @param request: CancelAssignRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAssignRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not UtilClient.is_unset(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not UtilClient.is_unset(request.role_id):
            body['role_id'] = request.role_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelAssignRole',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/role/cancel_assign',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CancelAssignRoleResponse(),
            self.execute(params, req, runtime)
        )

    async def cancel_assign_role_with_options_async(
        self,
        request: pds_20220301_models.CancelAssignRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CancelAssignRoleResponse:
        """
        @summary Cancels a role.
        
        @description You can cancel only the group administrator role.
        
        @param request: CancelAssignRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAssignRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not UtilClient.is_unset(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not UtilClient.is_unset(request.role_id):
            body['role_id'] = request.role_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelAssignRole',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/role/cancel_assign',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CancelAssignRoleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def cancel_assign_role(
        self,
        request: pds_20220301_models.CancelAssignRoleRequest,
    ) -> pds_20220301_models.CancelAssignRoleResponse:
        """
        @summary Cancels a role.
        
        @description You can cancel only the group administrator role.
        
        @param request: CancelAssignRoleRequest
        @return: CancelAssignRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_assign_role_with_options(request, headers, runtime)

    async def cancel_assign_role_async(
        self,
        request: pds_20220301_models.CancelAssignRoleRequest,
    ) -> pds_20220301_models.CancelAssignRoleResponse:
        """
        @summary Cancels a role.
        
        @description You can cancel only the group administrator role.
        
        @param request: CancelAssignRoleRequest
        @return: CancelAssignRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_assign_role_with_options_async(request, headers, runtime)

    def cancel_share_link_with_options(
        self,
        request: pds_20220301_models.CancelShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CancelShareLinkResponse:
        """
        @summary Deletes a share link.
        
        @param request: CancelShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CancelShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def cancel_share_link_with_options_async(
        self,
        request: pds_20220301_models.CancelShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CancelShareLinkResponse:
        """
        @summary Deletes a share link.
        
        @param request: CancelShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CancelShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def cancel_share_link(
        self,
        request: pds_20220301_models.CancelShareLinkRequest,
    ) -> pds_20220301_models.CancelShareLinkResponse:
        """
        @summary Deletes a share link.
        
        @param request: CancelShareLinkRequest
        @return: CancelShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_share_link_with_options(request, headers, runtime)

    async def cancel_share_link_async(
        self,
        request: pds_20220301_models.CancelShareLinkRequest,
    ) -> pds_20220301_models.CancelShareLinkResponse:
        """
        @summary Deletes a share link.
        
        @param request: CancelShareLinkRequest
        @return: CancelShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_share_link_with_options_async(request, headers, runtime)

    def clear_recyclebin_with_options(
        self,
        request: pds_20220301_models.ClearRecyclebinRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ClearRecyclebinResponse:
        """
        @summary Empties the recycle bin.
        
        @param request: ClearRecyclebinRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearRecyclebinResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClearRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ClearRecyclebinResponse(),
            self.execute(params, req, runtime)
        )

    async def clear_recyclebin_with_options_async(
        self,
        request: pds_20220301_models.ClearRecyclebinRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ClearRecyclebinResponse:
        """
        @summary Empties the recycle bin.
        
        @param request: ClearRecyclebinRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearRecyclebinResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ClearRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ClearRecyclebinResponse(),
            await self.execute_async(params, req, runtime)
        )

    def clear_recyclebin(
        self,
        request: pds_20220301_models.ClearRecyclebinRequest,
    ) -> pds_20220301_models.ClearRecyclebinResponse:
        """
        @summary Empties the recycle bin.
        
        @param request: ClearRecyclebinRequest
        @return: ClearRecyclebinResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clear_recyclebin_with_options(request, headers, runtime)

    async def clear_recyclebin_async(
        self,
        request: pds_20220301_models.ClearRecyclebinRequest,
    ) -> pds_20220301_models.ClearRecyclebinResponse:
        """
        @summary Empties the recycle bin.
        
        @param request: ClearRecyclebinRequest
        @return: ClearRecyclebinResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clear_recyclebin_with_options_async(request, headers, runtime)

    def complete_file_with_options(
        self,
        request: pds_20220301_models.CompleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CompleteFileResponse:
        """
        @summary Completes the upload of a file.
        
        @param request: CompleteFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompleteFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/complete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CompleteFileResponse(),
            self.execute(params, req, runtime)
        )

    async def complete_file_with_options_async(
        self,
        request: pds_20220301_models.CompleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CompleteFileResponse:
        """
        @summary Completes the upload of a file.
        
        @param request: CompleteFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompleteFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/complete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CompleteFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def complete_file(
        self,
        request: pds_20220301_models.CompleteFileRequest,
    ) -> pds_20220301_models.CompleteFileResponse:
        """
        @summary Completes the upload of a file.
        
        @param request: CompleteFileRequest
        @return: CompleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.complete_file_with_options(request, headers, runtime)

    async def complete_file_async(
        self,
        request: pds_20220301_models.CompleteFileRequest,
    ) -> pds_20220301_models.CompleteFileResponse:
        """
        @summary Completes the upload of a file.
        
        @param request: CompleteFileRequest
        @return: CompleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.complete_file_with_options_async(request, headers, runtime)

    def copy_file_with_options(
        self,
        request: pds_20220301_models.CopyFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CopyFileResponse:
        """
        @summary Copies a file or folder.
        
        @param request: CopyFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_rename):
            body['auto_rename'] = request.auto_rename
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.to_drive_id):
            body['to_drive_id'] = request.to_drive_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/copy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CopyFileResponse(),
            self.execute(params, req, runtime)
        )

    async def copy_file_with_options_async(
        self,
        request: pds_20220301_models.CopyFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CopyFileResponse:
        """
        @summary Copies a file or folder.
        
        @param request: CopyFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_rename):
            body['auto_rename'] = request.auto_rename
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.to_drive_id):
            body['to_drive_id'] = request.to_drive_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/copy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CopyFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def copy_file(
        self,
        request: pds_20220301_models.CopyFileRequest,
    ) -> pds_20220301_models.CopyFileResponse:
        """
        @summary Copies a file or folder.
        
        @param request: CopyFileRequest
        @return: CopyFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.copy_file_with_options(request, headers, runtime)

    async def copy_file_async(
        self,
        request: pds_20220301_models.CopyFileRequest,
    ) -> pds_20220301_models.CopyFileResponse:
        """
        @summary Copies a file or folder.
        
        @param request: CopyFileRequest
        @return: CopyFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.copy_file_with_options_async(request, headers, runtime)

    def create_customized_story_with_options(
        self,
        request: pds_20220301_models.CreateCustomizedStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateCustomizedStoryResponse:
        """
        @summary 创建自定义故事
        
        @param request: CreateCustomizedStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomizedStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.story_cover):
            body['story_cover'] = request.story_cover
        if not UtilClient.is_unset(request.story_files):
            body['story_files'] = request.story_files
        if not UtilClient.is_unset(request.story_name):
            body['story_name'] = request.story_name
        if not UtilClient.is_unset(request.story_sub_type):
            body['story_sub_type'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['story_type'] = request.story_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomizedStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/create_customized_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateCustomizedStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def create_customized_story_with_options_async(
        self,
        request: pds_20220301_models.CreateCustomizedStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateCustomizedStoryResponse:
        """
        @summary 创建自定义故事
        
        @param request: CreateCustomizedStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomizedStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.story_cover):
            body['story_cover'] = request.story_cover
        if not UtilClient.is_unset(request.story_files):
            body['story_files'] = request.story_files
        if not UtilClient.is_unset(request.story_name):
            body['story_name'] = request.story_name
        if not UtilClient.is_unset(request.story_sub_type):
            body['story_sub_type'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['story_type'] = request.story_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomizedStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/create_customized_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateCustomizedStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_customized_story(
        self,
        request: pds_20220301_models.CreateCustomizedStoryRequest,
    ) -> pds_20220301_models.CreateCustomizedStoryResponse:
        """
        @summary 创建自定义故事
        
        @param request: CreateCustomizedStoryRequest
        @return: CreateCustomizedStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_customized_story_with_options(request, headers, runtime)

    async def create_customized_story_async(
        self,
        request: pds_20220301_models.CreateCustomizedStoryRequest,
    ) -> pds_20220301_models.CreateCustomizedStoryResponse:
        """
        @summary 创建自定义故事
        
        @param request: CreateCustomizedStoryRequest
        @return: CreateCustomizedStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_customized_story_with_options_async(request, headers, runtime)

    def create_domain_with_options(
        self,
        request: pds_20220301_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateDomainResponse:
        """
        @summary test_domain
        
        @description The description of the domain.
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_name):
            body['domain_name'] = request.domain_name
        if not UtilClient.is_unset(request.init_drive_enable):
            body['init_drive_enable'] = request.init_drive_enable
        if not UtilClient.is_unset(request.init_drive_size):
            body['init_drive_size'] = request.init_drive_size
        if not UtilClient.is_unset(request.parent_domain_id):
            body['parent_domain_id'] = request.parent_domain_id
        if not UtilClient.is_unset(request.size_quota):
            body['size_quota'] = request.size_quota
        if not UtilClient.is_unset(request.user_count_quota):
            body['user_count_quota'] = request.user_count_quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: pds_20220301_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateDomainResponse:
        """
        @summary test_domain
        
        @description The description of the domain.
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_name):
            body['domain_name'] = request.domain_name
        if not UtilClient.is_unset(request.init_drive_enable):
            body['init_drive_enable'] = request.init_drive_enable
        if not UtilClient.is_unset(request.init_drive_size):
            body['init_drive_size'] = request.init_drive_size
        if not UtilClient.is_unset(request.parent_domain_id):
            body['parent_domain_id'] = request.parent_domain_id
        if not UtilClient.is_unset(request.size_quota):
            body['size_quota'] = request.size_quota
        if not UtilClient.is_unset(request.user_count_quota):
            body['user_count_quota'] = request.user_count_quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: pds_20220301_models.CreateDomainRequest,
    ) -> pds_20220301_models.CreateDomainResponse:
        """
        @summary test_domain
        
        @description The description of the domain.
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(request, headers, runtime)

    async def create_domain_async(
        self,
        request: pds_20220301_models.CreateDomainRequest,
    ) -> pds_20220301_models.CreateDomainResponse:
        """
        @summary test_domain
        
        @description The description of the domain.
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_domain_with_options_async(request, headers, runtime)

    def create_drive_with_options(
        self,
        request: pds_20220301_models.CreateDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateDriveResponse:
        """
        @summary Creates a drive.
        
        @param request: CreateDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.default):
            body['default'] = request.default
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.drive_type):
            body['drive_type'] = request.drive_type
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def create_drive_with_options_async(
        self,
        request: pds_20220301_models.CreateDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateDriveResponse:
        """
        @summary Creates a drive.
        
        @param request: CreateDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.default):
            body['default'] = request.default
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.drive_type):
            body['drive_type'] = request.drive_type
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_drive(
        self,
        request: pds_20220301_models.CreateDriveRequest,
    ) -> pds_20220301_models.CreateDriveResponse:
        """
        @summary Creates a drive.
        
        @param request: CreateDriveRequest
        @return: CreateDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_drive_with_options(request, headers, runtime)

    async def create_drive_async(
        self,
        request: pds_20220301_models.CreateDriveRequest,
    ) -> pds_20220301_models.CreateDriveResponse:
        """
        @summary Creates a drive.
        
        @param request: CreateDriveRequest
        @return: CreateDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_drive_with_options_async(request, headers, runtime)

    def create_file_with_options(
        self,
        request: pds_20220301_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateFileResponse:
        """
        @summary Creates a file or folder.
        
        @param request: CreateFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.content_hash):
            body['content_hash'] = request.content_hash
        if not UtilClient.is_unset(request.content_hash_name):
            body['content_hash_name'] = request.content_hash_name
        if not UtilClient.is_unset(request.content_type):
            body['content_type'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.image_media_metadata):
            body['image_media_metadata'] = request.image_media_metadata
        if not UtilClient.is_unset(request.local_created_at):
            body['local_created_at'] = request.local_created_at
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parallel_upload):
            body['parallel_upload'] = request.parallel_upload
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.pre_hash):
            body['pre_hash'] = request.pre_hash
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        if not UtilClient.is_unset(request.video_media_metadata):
            body['video_media_metadata'] = request.video_media_metadata
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateFileResponse(),
            self.execute(params, req, runtime)
        )

    async def create_file_with_options_async(
        self,
        request: pds_20220301_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateFileResponse:
        """
        @summary Creates a file or folder.
        
        @param request: CreateFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.content_hash):
            body['content_hash'] = request.content_hash
        if not UtilClient.is_unset(request.content_hash_name):
            body['content_hash_name'] = request.content_hash_name
        if not UtilClient.is_unset(request.content_type):
            body['content_type'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.image_media_metadata):
            body['image_media_metadata'] = request.image_media_metadata
        if not UtilClient.is_unset(request.local_created_at):
            body['local_created_at'] = request.local_created_at
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parallel_upload):
            body['parallel_upload'] = request.parallel_upload
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.pre_hash):
            body['pre_hash'] = request.pre_hash
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.size):
            body['size'] = request.size
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        if not UtilClient.is_unset(request.video_media_metadata):
            body['video_media_metadata'] = request.video_media_metadata
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_file(
        self,
        request: pds_20220301_models.CreateFileRequest,
    ) -> pds_20220301_models.CreateFileResponse:
        """
        @summary Creates a file or folder.
        
        @param request: CreateFileRequest
        @return: CreateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_file_with_options(request, headers, runtime)

    async def create_file_async(
        self,
        request: pds_20220301_models.CreateFileRequest,
    ) -> pds_20220301_models.CreateFileResponse:
        """
        @summary Creates a file or folder.
        
        @param request: CreateFileRequest
        @return: CreateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_file_with_options_async(request, headers, runtime)

    def create_group_with_options(
        self,
        request: pds_20220301_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateGroupResponse:
        """
        @summary Creates a group.
        
        @param request: CreateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.is_root):
            body['is_root'] = request.is_root
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: pds_20220301_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateGroupResponse:
        """
        @summary Creates a group.
        
        @param request: CreateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.is_root):
            body['is_root'] = request.is_root
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_group(
        self,
        request: pds_20220301_models.CreateGroupRequest,
    ) -> pds_20220301_models.CreateGroupResponse:
        """
        @summary Creates a group.
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: pds_20220301_models.CreateGroupRequest,
    ) -> pds_20220301_models.CreateGroupResponse:
        """
        @summary Creates a group.
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_group_with_options_async(request, headers, runtime)

    def create_identity_to_benefit_pkg_mapping_with_options(
        self,
        request: pds_20220301_models.CreateIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateIdentityToBenefitPkgMappingResponse:
        """
        @summary Creates a mapping between an entity and a benefit package. You can call this operation to associate a benefit package with a user.
        
        @description If you need to manage a large number of users based on Drive and Photo Service, you can control the features and quotas that users can use based on the benefits to which they are entitled. For more information, join the DingTalk group (ID 23146118).
        
        @param request: CreateIdentityToBenefitPkgMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIdentityToBenefitPkgMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['amount'] = request.amount
        if not UtilClient.is_unset(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not UtilClient.is_unset(request.expire_time):
            body['expire_time'] = request.expire_time
        if not UtilClient.is_unset(request.identity_id):
            body['identity_id'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIdentityToBenefitPkgMapping',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/benefit/identity_to_benefit_pkg_mapping/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateIdentityToBenefitPkgMappingResponse(),
            self.execute(params, req, runtime)
        )

    async def create_identity_to_benefit_pkg_mapping_with_options_async(
        self,
        request: pds_20220301_models.CreateIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateIdentityToBenefitPkgMappingResponse:
        """
        @summary Creates a mapping between an entity and a benefit package. You can call this operation to associate a benefit package with a user.
        
        @description If you need to manage a large number of users based on Drive and Photo Service, you can control the features and quotas that users can use based on the benefits to which they are entitled. For more information, join the DingTalk group (ID 23146118).
        
        @param request: CreateIdentityToBenefitPkgMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIdentityToBenefitPkgMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['amount'] = request.amount
        if not UtilClient.is_unset(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not UtilClient.is_unset(request.expire_time):
            body['expire_time'] = request.expire_time
        if not UtilClient.is_unset(request.identity_id):
            body['identity_id'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIdentityToBenefitPkgMapping',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/benefit/identity_to_benefit_pkg_mapping/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateIdentityToBenefitPkgMappingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_identity_to_benefit_pkg_mapping(
        self,
        request: pds_20220301_models.CreateIdentityToBenefitPkgMappingRequest,
    ) -> pds_20220301_models.CreateIdentityToBenefitPkgMappingResponse:
        """
        @summary Creates a mapping between an entity and a benefit package. You can call this operation to associate a benefit package with a user.
        
        @description If you need to manage a large number of users based on Drive and Photo Service, you can control the features and quotas that users can use based on the benefits to which they are entitled. For more information, join the DingTalk group (ID 23146118).
        
        @param request: CreateIdentityToBenefitPkgMappingRequest
        @return: CreateIdentityToBenefitPkgMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_identity_to_benefit_pkg_mapping_with_options(request, headers, runtime)

    async def create_identity_to_benefit_pkg_mapping_async(
        self,
        request: pds_20220301_models.CreateIdentityToBenefitPkgMappingRequest,
    ) -> pds_20220301_models.CreateIdentityToBenefitPkgMappingResponse:
        """
        @summary Creates a mapping between an entity and a benefit package. You can call this operation to associate a benefit package with a user.
        
        @description If you need to manage a large number of users based on Drive and Photo Service, you can control the features and quotas that users can use based on the benefits to which they are entitled. For more information, join the DingTalk group (ID 23146118).
        
        @param request: CreateIdentityToBenefitPkgMappingRequest
        @return: CreateIdentityToBenefitPkgMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_identity_to_benefit_pkg_mapping_with_options_async(request, headers, runtime)

    def create_order_with_options(
        self,
        request: pds_20220301_models.CreateOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateOrderResponse:
        """
        @summary 创建凌霄订单
        
        @param request: CreateOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_pay):
            body['auto_pay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            body['auto_renew'] = request.auto_renew
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.instance_id):
            body['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            body['order_type'] = request.order_type
        if not UtilClient.is_unset(request.package):
            body['package'] = request.package
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['period_unit'] = request.period_unit
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        if not UtilClient.is_unset(request.user_count):
            body['user_count'] = request.user_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/create_order',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateOrderResponse(),
            self.execute(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: pds_20220301_models.CreateOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateOrderResponse:
        """
        @summary 创建凌霄订单
        
        @param request: CreateOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_pay):
            body['auto_pay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            body['auto_renew'] = request.auto_renew
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.instance_id):
            body['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            body['order_type'] = request.order_type
        if not UtilClient.is_unset(request.package):
            body['package'] = request.package
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['period_unit'] = request.period_unit
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        if not UtilClient.is_unset(request.user_count):
            body['user_count'] = request.user_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/create_order',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateOrderResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_order(
        self,
        request: pds_20220301_models.CreateOrderRequest,
    ) -> pds_20220301_models.CreateOrderResponse:
        """
        @summary 创建凌霄订单
        
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_order_with_options(request, headers, runtime)

    async def create_order_async(
        self,
        request: pds_20220301_models.CreateOrderRequest,
    ) -> pds_20220301_models.CreateOrderResponse:
        """
        @summary 创建凌霄订单
        
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_order_with_options_async(request, headers, runtime)

    def create_share_link_with_options(
        self,
        request: pds_20220301_models.CreateShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateShareLinkResponse:
        """
        @summary Creates a share URL.
        
        @description A share is a file view container. You can grant anonymous users the permissions to access files in the user drive by using the share URL. Anonymous users can access the files based on the granted permissions.
        
        @param request: CreateShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creatable):
            body['creatable'] = request.creatable
        if not UtilClient.is_unset(request.creatable_file_id_list):
            body['creatable_file_id_list'] = request.creatable_file_id_list
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.file_id_list):
            body['file_id_list'] = request.file_id_list
        if not UtilClient.is_unset(request.office_editable):
            body['office_editable'] = request.office_editable
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.require_login):
            body['require_login'] = request.require_login
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_all_files):
            body['share_all_files'] = request.share_all_files
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def create_share_link_with_options_async(
        self,
        request: pds_20220301_models.CreateShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateShareLinkResponse:
        """
        @summary Creates a share URL.
        
        @description A share is a file view container. You can grant anonymous users the permissions to access files in the user drive by using the share URL. Anonymous users can access the files based on the granted permissions.
        
        @param request: CreateShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creatable):
            body['creatable'] = request.creatable
        if not UtilClient.is_unset(request.creatable_file_id_list):
            body['creatable_file_id_list'] = request.creatable_file_id_list
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.file_id_list):
            body['file_id_list'] = request.file_id_list
        if not UtilClient.is_unset(request.office_editable):
            body['office_editable'] = request.office_editable
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.require_login):
            body['require_login'] = request.require_login
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_all_files):
            body['share_all_files'] = request.share_all_files
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_share_link(
        self,
        request: pds_20220301_models.CreateShareLinkRequest,
    ) -> pds_20220301_models.CreateShareLinkResponse:
        """
        @summary Creates a share URL.
        
        @description A share is a file view container. You can grant anonymous users the permissions to access files in the user drive by using the share URL. Anonymous users can access the files based on the granted permissions.
        
        @param request: CreateShareLinkRequest
        @return: CreateShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_share_link_with_options(request, headers, runtime)

    async def create_share_link_async(
        self,
        request: pds_20220301_models.CreateShareLinkRequest,
    ) -> pds_20220301_models.CreateShareLinkResponse:
        """
        @summary Creates a share URL.
        
        @description A share is a file view container. You can grant anonymous users the permissions to access files in the user drive by using the share URL. Anonymous users can access the files based on the granted permissions.
        
        @param request: CreateShareLinkRequest
        @return: CreateShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_share_link_with_options_async(request, headers, runtime)

    def create_similar_image_cluster_task_with_options(
        self,
        request: pds_20220301_models.CreateSimilarImageClusterTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateSimilarImageClusterTaskResponse:
        """
        @summary 创建相似图片聚类任务
        
        @param request: CreateSimilarImageClusterTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSimilarImageClusterTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSimilarImageClusterTask',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/create_similar_image_cluster_task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateSimilarImageClusterTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_similar_image_cluster_task_with_options_async(
        self,
        request: pds_20220301_models.CreateSimilarImageClusterTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateSimilarImageClusterTaskResponse:
        """
        @summary 创建相似图片聚类任务
        
        @param request: CreateSimilarImageClusterTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSimilarImageClusterTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSimilarImageClusterTask',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/create_similar_image_cluster_task',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateSimilarImageClusterTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_similar_image_cluster_task(
        self,
        request: pds_20220301_models.CreateSimilarImageClusterTaskRequest,
    ) -> pds_20220301_models.CreateSimilarImageClusterTaskResponse:
        """
        @summary 创建相似图片聚类任务
        
        @param request: CreateSimilarImageClusterTaskRequest
        @return: CreateSimilarImageClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_similar_image_cluster_task_with_options(request, headers, runtime)

    async def create_similar_image_cluster_task_async(
        self,
        request: pds_20220301_models.CreateSimilarImageClusterTaskRequest,
    ) -> pds_20220301_models.CreateSimilarImageClusterTaskResponse:
        """
        @summary 创建相似图片聚类任务
        
        @param request: CreateSimilarImageClusterTaskRequest
        @return: CreateSimilarImageClusterTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_similar_image_cluster_task_with_options_async(request, headers, runtime)

    def create_story_with_options(
        self,
        request: pds_20220301_models.CreateStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateStoryResponse:
        """
        @summary 创建推荐故事
        
        @param request: CreateStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.max_image_count):
            body['max_image_count'] = request.max_image_count
        if not UtilClient.is_unset(request.min_image_count):
            body['min_image_count'] = request.min_image_count
        if not UtilClient.is_unset(request.story_end_time):
            body['story_end_time'] = request.story_end_time
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        if not UtilClient.is_unset(request.story_name):
            body['story_name'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time):
            body['story_start_time'] = request.story_start_time
        if not UtilClient.is_unset(request.story_sub_type):
            body['story_sub_type'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['story_type'] = request.story_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/create_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def create_story_with_options_async(
        self,
        request: pds_20220301_models.CreateStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateStoryResponse:
        """
        @summary 创建推荐故事
        
        @param request: CreateStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.max_image_count):
            body['max_image_count'] = request.max_image_count
        if not UtilClient.is_unset(request.min_image_count):
            body['min_image_count'] = request.min_image_count
        if not UtilClient.is_unset(request.story_end_time):
            body['story_end_time'] = request.story_end_time
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        if not UtilClient.is_unset(request.story_name):
            body['story_name'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time):
            body['story_start_time'] = request.story_start_time
        if not UtilClient.is_unset(request.story_sub_type):
            body['story_sub_type'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['story_type'] = request.story_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/create_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_story(
        self,
        request: pds_20220301_models.CreateStoryRequest,
    ) -> pds_20220301_models.CreateStoryResponse:
        """
        @summary 创建推荐故事
        
        @param request: CreateStoryRequest
        @return: CreateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_story_with_options(request, headers, runtime)

    async def create_story_async(
        self,
        request: pds_20220301_models.CreateStoryRequest,
    ) -> pds_20220301_models.CreateStoryResponse:
        """
        @summary 创建推荐故事
        
        @param request: CreateStoryRequest
        @return: CreateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_story_with_options_async(request, headers, runtime)

    def create_user_with_options(
        self,
        request: pds_20220301_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateUserResponse:
        """
        @summary Creates a user.
        
        @param request: CreateUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateUserResponse(),
            self.execute(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: pds_20220301_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CreateUserResponse:
        """
        @summary Creates a user.
        
        @param request: CreateUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CreateUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_user(
        self,
        request: pds_20220301_models.CreateUserRequest,
    ) -> pds_20220301_models.CreateUserResponse:
        """
        @summary Creates a user.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_with_options(request, headers, runtime)

    async def create_user_async(
        self,
        request: pds_20220301_models.CreateUserRequest,
    ) -> pds_20220301_models.CreateUserResponse:
        """
        @summary Creates a user.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(request, headers, runtime)

    def csi_get_file_info_with_options(
        self,
        request: pds_20220301_models.CsiGetFileInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CsiGetFileInfoResponse:
        """
        @summary 获取文件内容安全信息
        
        @param request: CsiGetFileInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CsiGetFileInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CsiGetFileInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/csi/get_file_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CsiGetFileInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def csi_get_file_info_with_options_async(
        self,
        request: pds_20220301_models.CsiGetFileInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.CsiGetFileInfoResponse:
        """
        @summary 获取文件内容安全信息
        
        @param request: CsiGetFileInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CsiGetFileInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CsiGetFileInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/csi/get_file_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.CsiGetFileInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def csi_get_file_info(
        self,
        request: pds_20220301_models.CsiGetFileInfoRequest,
    ) -> pds_20220301_models.CsiGetFileInfoResponse:
        """
        @summary 获取文件内容安全信息
        
        @param request: CsiGetFileInfoRequest
        @return: CsiGetFileInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.csi_get_file_info_with_options(request, headers, runtime)

    async def csi_get_file_info_async(
        self,
        request: pds_20220301_models.CsiGetFileInfoRequest,
    ) -> pds_20220301_models.CsiGetFileInfoResponse:
        """
        @summary 获取文件内容安全信息
        
        @param request: CsiGetFileInfoRequest
        @return: CsiGetFileInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.csi_get_file_info_with_options_async(request, headers, runtime)

    def delete_domain_with_options(
        self,
        request: pds_20220301_models.DeleteDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteDomainResponse:
        """
        @summary Delete the domain
        
        @param request: DeleteDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_id):
            body['domain_id'] = request.domain_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: pds_20220301_models.DeleteDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteDomainResponse:
        """
        @summary Delete the domain
        
        @param request: DeleteDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_id):
            body['domain_id'] = request.domain_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: pds_20220301_models.DeleteDomainRequest,
    ) -> pds_20220301_models.DeleteDomainResponse:
        """
        @summary Delete the domain
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(request, headers, runtime)

    async def delete_domain_async(
        self,
        request: pds_20220301_models.DeleteDomainRequest,
    ) -> pds_20220301_models.DeleteDomainResponse:
        """
        @summary Delete the domain
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_domain_with_options_async(request, headers, runtime)

    def delete_drive_with_options(
        self,
        request: pds_20220301_models.DeleteDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteDriveResponse:
        """
        @summary Deletes a drive.
        
        @param request: DeleteDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_drive_with_options_async(
        self,
        request: pds_20220301_models.DeleteDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteDriveResponse:
        """
        @summary Deletes a drive.
        
        @param request: DeleteDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_drive(
        self,
        request: pds_20220301_models.DeleteDriveRequest,
    ) -> pds_20220301_models.DeleteDriveResponse:
        """
        @summary Deletes a drive.
        
        @param request: DeleteDriveRequest
        @return: DeleteDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_drive_with_options(request, headers, runtime)

    async def delete_drive_async(
        self,
        request: pds_20220301_models.DeleteDriveRequest,
    ) -> pds_20220301_models.DeleteDriveResponse:
        """
        @summary Deletes a drive.
        
        @param request: DeleteDriveRequest
        @return: DeleteDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_drive_with_options_async(request, headers, runtime)

    def delete_file_with_options(
        self,
        request: pds_20220301_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteFileResponse:
        """
        @summary Deletes a file or folder.
        
        @param request: DeleteFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteFileResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: pds_20220301_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteFileResponse:
        """
        @summary Deletes a file or folder.
        
        @param request: DeleteFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_file(
        self,
        request: pds_20220301_models.DeleteFileRequest,
    ) -> pds_20220301_models.DeleteFileResponse:
        """
        @summary Deletes a file or folder.
        
        @param request: DeleteFileRequest
        @return: DeleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(request, headers, runtime)

    async def delete_file_async(
        self,
        request: pds_20220301_models.DeleteFileRequest,
    ) -> pds_20220301_models.DeleteFileResponse:
        """
        @summary Deletes a file or folder.
        
        @param request: DeleteFileRequest
        @return: DeleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_file_with_options_async(request, headers, runtime)

    def delete_group_with_options(
        self,
        request: pds_20220301_models.DeleteGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteGroupResponse:
        """
        @summary Deletes groups. Before you delete a group, make sure that no other groups or users exist in the group. Otherwise, the group fails to be deleted.
        
        @param request: DeleteGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: pds_20220301_models.DeleteGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteGroupResponse:
        """
        @summary Deletes groups. Before you delete a group, make sure that no other groups or users exist in the group. Otherwise, the group fails to be deleted.
        
        @param request: DeleteGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: pds_20220301_models.DeleteGroupRequest,
    ) -> pds_20220301_models.DeleteGroupResponse:
        """
        @summary Deletes groups. Before you delete a group, make sure that no other groups or users exist in the group. Otherwise, the group fails to be deleted.
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(request, headers, runtime)

    async def delete_group_async(
        self,
        request: pds_20220301_models.DeleteGroupRequest,
    ) -> pds_20220301_models.DeleteGroupResponse:
        """
        @summary Deletes groups. Before you delete a group, make sure that no other groups or users exist in the group. Otherwise, the group fails to be deleted.
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_group_with_options_async(request, headers, runtime)

    def delete_revision_with_options(
        self,
        request: pds_20220301_models.DeleteRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteRevisionResponse:
        """
        @summary Deletes a historical version of a file. You cannot delete the latest version of a file.
        
        @param request: DeleteRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_revision_with_options_async(
        self,
        request: pds_20220301_models.DeleteRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteRevisionResponse:
        """
        @summary Deletes a historical version of a file. You cannot delete the latest version of a file.
        
        @param request: DeleteRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_revision(
        self,
        request: pds_20220301_models.DeleteRevisionRequest,
    ) -> pds_20220301_models.DeleteRevisionResponse:
        """
        @summary Deletes a historical version of a file. You cannot delete the latest version of a file.
        
        @param request: DeleteRevisionRequest
        @return: DeleteRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_revision_with_options(request, headers, runtime)

    async def delete_revision_async(
        self,
        request: pds_20220301_models.DeleteRevisionRequest,
    ) -> pds_20220301_models.DeleteRevisionResponse:
        """
        @summary Deletes a historical version of a file. You cannot delete the latest version of a file.
        
        @param request: DeleteRevisionRequest
        @return: DeleteRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_revision_with_options_async(request, headers, runtime)

    def delete_story_with_options(
        self,
        request: pds_20220301_models.DeleteStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteStoryResponse:
        """
        @summary 删除故事
        
        @param request: DeleteStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/delete_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_story_with_options_async(
        self,
        request: pds_20220301_models.DeleteStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteStoryResponse:
        """
        @summary 删除故事
        
        @param request: DeleteStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/delete_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_story(
        self,
        request: pds_20220301_models.DeleteStoryRequest,
    ) -> pds_20220301_models.DeleteStoryResponse:
        """
        @summary 删除故事
        
        @param request: DeleteStoryRequest
        @return: DeleteStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_story_with_options(request, headers, runtime)

    async def delete_story_async(
        self,
        request: pds_20220301_models.DeleteStoryRequest,
    ) -> pds_20220301_models.DeleteStoryResponse:
        """
        @summary 删除故事
        
        @param request: DeleteStoryRequest
        @return: DeleteStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_story_with_options_async(request, headers, runtime)

    def delete_user_with_options(
        self,
        request: pds_20220301_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteUserResponse:
        """
        @summary Deletes a user.
        
        @param request: DeleteUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteUserResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: pds_20220301_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeleteUserResponse:
        """
        @summary Deletes a user.
        
        @param request: DeleteUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeleteUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: pds_20220301_models.DeleteUserRequest,
    ) -> pds_20220301_models.DeleteUserResponse:
        """
        @summary Deletes a user.
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(request, headers, runtime)

    async def delete_user_async(
        self,
        request: pds_20220301_models.DeleteUserRequest,
    ) -> pds_20220301_models.DeleteUserResponse:
        """
        @summary Deletes a user.
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_user_with_options_async(request, headers, runtime)

    def delta_get_last_cursor_with_options(
        self,
        request: pds_20220301_models.DeltaGetLastCursorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeltaGetLastCursorResponse:
        """
        @summary Queries the cursor of incremental information.
        
        @param request: DeltaGetLastCursorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeltaGetLastCursorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeltaGetLastCursor',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_last_cursor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeltaGetLastCursorResponse(),
            self.execute(params, req, runtime)
        )

    async def delta_get_last_cursor_with_options_async(
        self,
        request: pds_20220301_models.DeltaGetLastCursorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DeltaGetLastCursorResponse:
        """
        @summary Queries the cursor of incremental information.
        
        @param request: DeltaGetLastCursorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeltaGetLastCursorResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeltaGetLastCursor',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_last_cursor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.DeltaGetLastCursorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delta_get_last_cursor(
        self,
        request: pds_20220301_models.DeltaGetLastCursorRequest,
    ) -> pds_20220301_models.DeltaGetLastCursorResponse:
        """
        @summary Queries the cursor of incremental information.
        
        @param request: DeltaGetLastCursorRequest
        @return: DeltaGetLastCursorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delta_get_last_cursor_with_options(request, headers, runtime)

    async def delta_get_last_cursor_async(
        self,
        request: pds_20220301_models.DeltaGetLastCursorRequest,
    ) -> pds_20220301_models.DeltaGetLastCursorResponse:
        """
        @summary Queries the cursor of incremental information.
        
        @param request: DeltaGetLastCursorRequest
        @return: DeltaGetLastCursorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delta_get_last_cursor_with_options_async(request, headers, runtime)

    def download_file_with_options(
        self,
        request: pds_20220301_models.DownloadFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DownloadFileResponse:
        """
        @summary Downloads a file.
        
        @description For information about best practices for downloading a file.
        
        @param request: DownloadFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drive_id):
            query['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            query['file_id'] = request.file_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            query['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.office_thumbnail_process):
            query['office_thumbnail_process'] = request.office_thumbnail_process
        if not UtilClient.is_unset(request.share_id):
            query['share_id'] = request.share_id
        if not UtilClient.is_unset(request.video_thumbnail_process):
            query['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/download',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='binary'
        )
        return TeaCore.from_map(
            pds_20220301_models.DownloadFileResponse(),
            self.execute(params, req, runtime)
        )

    async def download_file_with_options_async(
        self,
        request: pds_20220301_models.DownloadFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.DownloadFileResponse:
        """
        @summary Downloads a file.
        
        @description For information about best practices for downloading a file.
        
        @param request: DownloadFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drive_id):
            query['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            query['file_id'] = request.file_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            query['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.office_thumbnail_process):
            query['office_thumbnail_process'] = request.office_thumbnail_process
        if not UtilClient.is_unset(request.share_id):
            query['share_id'] = request.share_id
        if not UtilClient.is_unset(request.video_thumbnail_process):
            query['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/download',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='binary'
        )
        return TeaCore.from_map(
            pds_20220301_models.DownloadFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def download_file(
        self,
        request: pds_20220301_models.DownloadFileRequest,
    ) -> pds_20220301_models.DownloadFileResponse:
        """
        @summary Downloads a file.
        
        @description For information about best practices for downloading a file.
        
        @param request: DownloadFileRequest
        @return: DownloadFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.download_file_with_options(request, headers, runtime)

    async def download_file_async(
        self,
        request: pds_20220301_models.DownloadFileRequest,
    ) -> pds_20220301_models.DownloadFileResponse:
        """
        @summary Downloads a file.
        
        @description For information about best practices for downloading a file.
        
        @param request: DownloadFileRequest
        @return: DownloadFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.download_file_with_options_async(request, headers, runtime)

    def file_add_permission_with_options(
        self,
        request: pds_20220301_models.FileAddPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileAddPermissionResponse:
        """
        @summary Grants permissions to access files to a user or group.
        
        @param request: FileAddPermissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileAddPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileAddPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/add_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileAddPermissionResponse(),
            self.execute(params, req, runtime)
        )

    async def file_add_permission_with_options_async(
        self,
        request: pds_20220301_models.FileAddPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileAddPermissionResponse:
        """
        @summary Grants permissions to access files to a user or group.
        
        @param request: FileAddPermissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileAddPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileAddPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/add_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileAddPermissionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_add_permission(
        self,
        request: pds_20220301_models.FileAddPermissionRequest,
    ) -> pds_20220301_models.FileAddPermissionResponse:
        """
        @summary Grants permissions to access files to a user or group.
        
        @param request: FileAddPermissionRequest
        @return: FileAddPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_add_permission_with_options(request, headers, runtime)

    async def file_add_permission_async(
        self,
        request: pds_20220301_models.FileAddPermissionRequest,
    ) -> pds_20220301_models.FileAddPermissionResponse:
        """
        @summary Grants permissions to access files to a user or group.
        
        @param request: FileAddPermissionRequest
        @return: FileAddPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_add_permission_with_options_async(request, headers, runtime)

    def file_delete_user_tags_with_options(
        self,
        request: pds_20220301_models.FileDeleteUserTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileDeleteUserTagsResponse:
        """
        @summary Removes custom tags from a file.
        
        @param request: FileDeleteUserTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileDeleteUserTagsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.key_list):
            body['key_list'] = request.key_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileDeleteUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/delete_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileDeleteUserTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def file_delete_user_tags_with_options_async(
        self,
        request: pds_20220301_models.FileDeleteUserTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileDeleteUserTagsResponse:
        """
        @summary Removes custom tags from a file.
        
        @param request: FileDeleteUserTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileDeleteUserTagsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.key_list):
            body['key_list'] = request.key_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileDeleteUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/delete_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileDeleteUserTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_delete_user_tags(
        self,
        request: pds_20220301_models.FileDeleteUserTagsRequest,
    ) -> pds_20220301_models.FileDeleteUserTagsResponse:
        """
        @summary Removes custom tags from a file.
        
        @param request: FileDeleteUserTagsRequest
        @return: FileDeleteUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_delete_user_tags_with_options(request, headers, runtime)

    async def file_delete_user_tags_async(
        self,
        request: pds_20220301_models.FileDeleteUserTagsRequest,
    ) -> pds_20220301_models.FileDeleteUserTagsResponse:
        """
        @summary Removes custom tags from a file.
        
        @param request: FileDeleteUserTagsRequest
        @return: FileDeleteUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_delete_user_tags_with_options_async(request, headers, runtime)

    def file_list_permission_with_options(
        self,
        request: pds_20220301_models.FileListPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileListPermissionResponse:
        """
        @summary Queries the sharing authorization records of a file.
        
        @param request: FileListPermissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileListPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileListPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileListPermissionResponse(),
            self.execute(params, req, runtime)
        )

    async def file_list_permission_with_options_async(
        self,
        request: pds_20220301_models.FileListPermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileListPermissionResponse:
        """
        @summary Queries the sharing authorization records of a file.
        
        @param request: FileListPermissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileListPermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileListPermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileListPermissionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_list_permission(
        self,
        request: pds_20220301_models.FileListPermissionRequest,
    ) -> pds_20220301_models.FileListPermissionResponse:
        """
        @summary Queries the sharing authorization records of a file.
        
        @param request: FileListPermissionRequest
        @return: FileListPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_list_permission_with_options(request, headers, runtime)

    async def file_list_permission_async(
        self,
        request: pds_20220301_models.FileListPermissionRequest,
    ) -> pds_20220301_models.FileListPermissionResponse:
        """
        @summary Queries the sharing authorization records of a file.
        
        @param request: FileListPermissionRequest
        @return: FileListPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_list_permission_with_options_async(request, headers, runtime)

    def file_put_user_tags_with_options(
        self,
        request: pds_20220301_models.FilePutUserTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FilePutUserTagsResponse:
        """
        @summary Adds custom tags to a file.
        
        @description This operation is an incremental update operation. Take note of the following items:
        If a tag name specified in the request is the same as an existing tag name, the existing tag is overwritten.
        If a tag name specified in the request is different from the existing tag names, the specified tag is added.
        The existing tags with unique names are not affected.
        
        @param request: FilePutUserTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FilePutUserTagsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FilePutUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/put_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FilePutUserTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def file_put_user_tags_with_options_async(
        self,
        request: pds_20220301_models.FilePutUserTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FilePutUserTagsResponse:
        """
        @summary Adds custom tags to a file.
        
        @description This operation is an incremental update operation. Take note of the following items:
        If a tag name specified in the request is the same as an existing tag name, the existing tag is overwritten.
        If a tag name specified in the request is different from the existing tag names, the specified tag is added.
        The existing tags with unique names are not affected.
        
        @param request: FilePutUserTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FilePutUserTagsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.user_tags):
            body['user_tags'] = request.user_tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FilePutUserTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/put_usertags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FilePutUserTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_put_user_tags(
        self,
        request: pds_20220301_models.FilePutUserTagsRequest,
    ) -> pds_20220301_models.FilePutUserTagsResponse:
        """
        @summary Adds custom tags to a file.
        
        @description This operation is an incremental update operation. Take note of the following items:
        If a tag name specified in the request is the same as an existing tag name, the existing tag is overwritten.
        If a tag name specified in the request is different from the existing tag names, the specified tag is added.
        The existing tags with unique names are not affected.
        
        @param request: FilePutUserTagsRequest
        @return: FilePutUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_put_user_tags_with_options(request, headers, runtime)

    async def file_put_user_tags_async(
        self,
        request: pds_20220301_models.FilePutUserTagsRequest,
    ) -> pds_20220301_models.FilePutUserTagsResponse:
        """
        @summary Adds custom tags to a file.
        
        @description This operation is an incremental update operation. Take note of the following items:
        If a tag name specified in the request is the same as an existing tag name, the existing tag is overwritten.
        If a tag name specified in the request is different from the existing tag names, the specified tag is added.
        The existing tags with unique names are not affected.
        
        @param request: FilePutUserTagsRequest
        @return: FilePutUserTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_put_user_tags_with_options_async(request, headers, runtime)

    def file_remove_permission_with_options(
        self,
        request: pds_20220301_models.FileRemovePermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileRemovePermissionResponse:
        """
        @summary Cancels the permissions on a shared file.
        
        @param request: FileRemovePermissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileRemovePermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileRemovePermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/remove_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileRemovePermissionResponse(),
            self.execute(params, req, runtime)
        )

    async def file_remove_permission_with_options_async(
        self,
        request: pds_20220301_models.FileRemovePermissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.FileRemovePermissionResponse:
        """
        @summary Cancels the permissions on a shared file.
        
        @param request: FileRemovePermissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileRemovePermissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FileRemovePermission',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/remove_permission',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.FileRemovePermissionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_remove_permission(
        self,
        request: pds_20220301_models.FileRemovePermissionRequest,
    ) -> pds_20220301_models.FileRemovePermissionResponse:
        """
        @summary Cancels the permissions on a shared file.
        
        @param request: FileRemovePermissionRequest
        @return: FileRemovePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_remove_permission_with_options(request, headers, runtime)

    async def file_remove_permission_async(
        self,
        request: pds_20220301_models.FileRemovePermissionRequest,
    ) -> pds_20220301_models.FileRemovePermissionResponse:
        """
        @summary Cancels the permissions on a shared file.
        
        @param request: FileRemovePermissionRequest
        @return: FileRemovePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_remove_permission_with_options_async(request, headers, runtime)

    def get_async_task_with_options(
        self,
        request: pds_20220301_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetAsyncTaskResponse:
        """
        @summary Queries the information about an asynchronous task.
        
        @param request: GetAsyncTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.async_task_id):
            body['async_task_id'] = request.async_task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncTask',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/async_task/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetAsyncTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def get_async_task_with_options_async(
        self,
        request: pds_20220301_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetAsyncTaskResponse:
        """
        @summary Queries the information about an asynchronous task.
        
        @param request: GetAsyncTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsyncTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.async_task_id):
            body['async_task_id'] = request.async_task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAsyncTask',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/async_task/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetAsyncTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_async_task(
        self,
        request: pds_20220301_models.GetAsyncTaskRequest,
    ) -> pds_20220301_models.GetAsyncTaskResponse:
        """
        @summary Queries the information about an asynchronous task.
        
        @param request: GetAsyncTaskRequest
        @return: GetAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_async_task_with_options(request, headers, runtime)

    async def get_async_task_async(
        self,
        request: pds_20220301_models.GetAsyncTaskRequest,
    ) -> pds_20220301_models.GetAsyncTaskResponse:
        """
        @summary Queries the information about an asynchronous task.
        
        @param request: GetAsyncTaskRequest
        @return: GetAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_async_task_with_options_async(request, headers, runtime)

    def get_default_drive_with_options(
        self,
        request: pds_20220301_models.GetDefaultDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDefaultDriveResponse:
        """
        @summary Queries the default drive of a user.
        
        @param request: GetDefaultDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDefaultDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDefaultDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/get_default_drive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDefaultDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def get_default_drive_with_options_async(
        self,
        request: pds_20220301_models.GetDefaultDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDefaultDriveResponse:
        """
        @summary Queries the default drive of a user.
        
        @param request: GetDefaultDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDefaultDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDefaultDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/get_default_drive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDefaultDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_default_drive(
        self,
        request: pds_20220301_models.GetDefaultDriveRequest,
    ) -> pds_20220301_models.GetDefaultDriveResponse:
        """
        @summary Queries the default drive of a user.
        
        @param request: GetDefaultDriveRequest
        @return: GetDefaultDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_default_drive_with_options(request, headers, runtime)

    async def get_default_drive_async(
        self,
        request: pds_20220301_models.GetDefaultDriveRequest,
    ) -> pds_20220301_models.GetDefaultDriveResponse:
        """
        @summary Queries the default drive of a user.
        
        @param request: GetDefaultDriveRequest
        @return: GetDefaultDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_default_drive_with_options_async(request, headers, runtime)

    def get_domain_with_options(
        self,
        request: pds_20220301_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDomainResponse:
        """
        @summary Get domain information.
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_id):
            body['domain_id'] = request.domain_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.get_quota_used):
            body['get_quota_used'] = request.get_quota_used
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        request: pds_20220301_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDomainResponse:
        """
        @summary Get domain information.
        
        @param request: GetDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.domain_id):
            body['domain_id'] = request.domain_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.get_quota_used):
            body['get_quota_used'] = request.get_quota_used
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_domain(
        self,
        request: pds_20220301_models.GetDomainRequest,
    ) -> pds_20220301_models.GetDomainResponse:
        """
        @summary Get domain information.
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(request, headers, runtime)

    async def get_domain_async(
        self,
        request: pds_20220301_models.GetDomainRequest,
    ) -> pds_20220301_models.GetDomainResponse:
        """
        @summary Get domain information.
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(request, headers, runtime)

    def get_domain_quota_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDomainQuotaResponse:
        """
        @summary 获取domain限额
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainQuotaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDomainQuota',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/get_quota',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDomainQuotaResponse(),
            self.execute(params, req, runtime)
        )

    async def get_domain_quota_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDomainQuotaResponse:
        """
        @summary 获取domain限额
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainQuotaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDomainQuota',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/get_quota',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDomainQuotaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_domain_quota(self) -> pds_20220301_models.GetDomainQuotaResponse:
        """
        @summary 获取domain限额
        
        @return: GetDomainQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_domain_quota_with_options(headers, runtime)

    async def get_domain_quota_async(self) -> pds_20220301_models.GetDomainQuotaResponse:
        """
        @summary 获取domain限额
        
        @return: GetDomainQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_domain_quota_with_options_async(headers, runtime)

    def get_download_url_with_options(
        self,
        request: pds_20220301_models.GetDownloadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDownloadUrlResponse:
        """
        @summary Queries the download URL of a file. For more information about best practices, visit https://help.aliyun.com/document_detail/175889.html.
        
        @param request: GetDownloadUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            body['file_name'] = request.file_name
        if not UtilClient.is_unset(request.response_content_type):
            body['response_content_type'] = request.response_content_type
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDownloadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_download_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDownloadUrlResponse(),
            self.execute(params, req, runtime)
        )

    async def get_download_url_with_options_async(
        self,
        request: pds_20220301_models.GetDownloadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDownloadUrlResponse:
        """
        @summary Queries the download URL of a file. For more information about best practices, visit https://help.aliyun.com/document_detail/175889.html.
        
        @param request: GetDownloadUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.file_name):
            body['file_name'] = request.file_name
        if not UtilClient.is_unset(request.response_content_type):
            body['response_content_type'] = request.response_content_type
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDownloadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_download_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDownloadUrlResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_download_url(
        self,
        request: pds_20220301_models.GetDownloadUrlRequest,
    ) -> pds_20220301_models.GetDownloadUrlResponse:
        """
        @summary Queries the download URL of a file. For more information about best practices, visit https://help.aliyun.com/document_detail/175889.html.
        
        @param request: GetDownloadUrlRequest
        @return: GetDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_download_url_with_options(request, headers, runtime)

    async def get_download_url_async(
        self,
        request: pds_20220301_models.GetDownloadUrlRequest,
    ) -> pds_20220301_models.GetDownloadUrlResponse:
        """
        @summary Queries the download URL of a file. For more information about best practices, visit https://help.aliyun.com/document_detail/175889.html.
        
        @param request: GetDownloadUrlRequest
        @return: GetDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_download_url_with_options_async(request, headers, runtime)

    def get_drive_with_options(
        self,
        request: pds_20220301_models.GetDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDriveResponse:
        """
        @summary Queries the information about a drive.
        
        @param request: GetDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def get_drive_with_options_async(
        self,
        request: pds_20220301_models.GetDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetDriveResponse:
        """
        @summary Queries the information about a drive.
        
        @param request: GetDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_drive(
        self,
        request: pds_20220301_models.GetDriveRequest,
    ) -> pds_20220301_models.GetDriveResponse:
        """
        @summary Queries the information about a drive.
        
        @param request: GetDriveRequest
        @return: GetDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_drive_with_options(request, headers, runtime)

    async def get_drive_async(
        self,
        request: pds_20220301_models.GetDriveRequest,
    ) -> pds_20220301_models.GetDriveResponse:
        """
        @summary Queries the information about a drive.
        
        @param request: GetDriveRequest
        @return: GetDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_drive_with_options_async(request, headers, runtime)

    def get_file_with_options(
        self,
        request: pds_20220301_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetFileResponse:
        """
        @summary Queries the information about a file.
        
        @param request: GetFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetFileResponse(),
            self.execute(params, req, runtime)
        )

    async def get_file_with_options_async(
        self,
        request: pds_20220301_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetFileResponse:
        """
        @summary Queries the information about a file.
        
        @param request: GetFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_file(
        self,
        request: pds_20220301_models.GetFileRequest,
    ) -> pds_20220301_models.GetFileResponse:
        """
        @summary Queries the information about a file.
        
        @param request: GetFileRequest
        @return: GetFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_with_options(request, headers, runtime)

    async def get_file_async(
        self,
        request: pds_20220301_models.GetFileRequest,
    ) -> pds_20220301_models.GetFileResponse:
        """
        @summary Queries the information about a file.
        
        @param request: GetFileRequest
        @return: GetFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_with_options_async(request, headers, runtime)

    def get_group_with_options(
        self,
        request: pds_20220301_models.GetGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetGroupResponse:
        """
        @summary Queries the information about a group.
        
        @param request: GetGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: pds_20220301_models.GetGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetGroupResponse:
        """
        @summary Queries the information about a group.
        
        @param request: GetGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_group(
        self,
        request: pds_20220301_models.GetGroupRequest,
    ) -> pds_20220301_models.GetGroupResponse:
        """
        @summary Queries the information about a group.
        
        @param request: GetGroupRequest
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_with_options(request, headers, runtime)

    async def get_group_async(
        self,
        request: pds_20220301_models.GetGroupRequest,
    ) -> pds_20220301_models.GetGroupResponse:
        """
        @summary Queries the information about a group.
        
        @param request: GetGroupRequest
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_group_with_options_async(request, headers, runtime)

    def get_identity_to_benefit_pkg_mapping_with_options(
        self,
        request: pds_20220301_models.GetIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetIdentityToBenefitPkgMappingResponse:
        """
        @summary Queries the mapping between an entity and a benefit package. You can call this operation to query the benefit package that is associated with a user.
        
        @param request: GetIdentityToBenefitPkgMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdentityToBenefitPkgMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not UtilClient.is_unset(request.identity_id):
            body['identity_id'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIdentityToBenefitPkgMapping',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/benefit/identity_to_benefit_pkg_mapping/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetIdentityToBenefitPkgMappingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_identity_to_benefit_pkg_mapping_with_options_async(
        self,
        request: pds_20220301_models.GetIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetIdentityToBenefitPkgMappingResponse:
        """
        @summary Queries the mapping between an entity and a benefit package. You can call this operation to query the benefit package that is associated with a user.
        
        @param request: GetIdentityToBenefitPkgMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdentityToBenefitPkgMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not UtilClient.is_unset(request.identity_id):
            body['identity_id'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIdentityToBenefitPkgMapping',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/benefit/identity_to_benefit_pkg_mapping/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetIdentityToBenefitPkgMappingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_identity_to_benefit_pkg_mapping(
        self,
        request: pds_20220301_models.GetIdentityToBenefitPkgMappingRequest,
    ) -> pds_20220301_models.GetIdentityToBenefitPkgMappingResponse:
        """
        @summary Queries the mapping between an entity and a benefit package. You can call this operation to query the benefit package that is associated with a user.
        
        @param request: GetIdentityToBenefitPkgMappingRequest
        @return: GetIdentityToBenefitPkgMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_identity_to_benefit_pkg_mapping_with_options(request, headers, runtime)

    async def get_identity_to_benefit_pkg_mapping_async(
        self,
        request: pds_20220301_models.GetIdentityToBenefitPkgMappingRequest,
    ) -> pds_20220301_models.GetIdentityToBenefitPkgMappingResponse:
        """
        @summary Queries the mapping between an entity and a benefit package. You can call this operation to query the benefit package that is associated with a user.
        
        @param request: GetIdentityToBenefitPkgMappingRequest
        @return: GetIdentityToBenefitPkgMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_identity_to_benefit_pkg_mapping_with_options_async(request, headers, runtime)

    def get_link_info_with_options(
        self,
        request: pds_20220301_models.GetLinkInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetLinkInfoResponse:
        """
        @summary 获取用户认证方式详情
        
        @param request: GetLinkInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLinkInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/get_link_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def get_link_info_with_options_async(
        self,
        request: pds_20220301_models.GetLinkInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetLinkInfoResponse:
        """
        @summary 获取用户认证方式详情
        
        @param request: GetLinkInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLinkInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/get_link_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_link_info(
        self,
        request: pds_20220301_models.GetLinkInfoRequest,
    ) -> pds_20220301_models.GetLinkInfoResponse:
        """
        @summary 获取用户认证方式详情
        
        @param request: GetLinkInfoRequest
        @return: GetLinkInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_link_info_with_options(request, headers, runtime)

    async def get_link_info_async(
        self,
        request: pds_20220301_models.GetLinkInfoRequest,
    ) -> pds_20220301_models.GetLinkInfoResponse:
        """
        @summary 获取用户认证方式详情
        
        @param request: GetLinkInfoRequest
        @return: GetLinkInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_link_info_with_options_async(request, headers, runtime)

    def get_link_info_by_user_id_with_options(
        self,
        request: pds_20220301_models.GetLinkInfoByUserIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetLinkInfoByUserIdResponse:
        """
        @summary Queries the information about a user based on the user ID.
        
        @param request: GetLinkInfoByUserIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLinkInfoByUserIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfoByUserId',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/get_link_info_by_user_id',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoByUserIdResponse(),
            self.execute(params, req, runtime)
        )

    async def get_link_info_by_user_id_with_options_async(
        self,
        request: pds_20220301_models.GetLinkInfoByUserIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetLinkInfoByUserIdResponse:
        """
        @summary Queries the information about a user based on the user ID.
        
        @param request: GetLinkInfoByUserIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLinkInfoByUserIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLinkInfoByUserId',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/get_link_info_by_user_id',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetLinkInfoByUserIdResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_link_info_by_user_id(
        self,
        request: pds_20220301_models.GetLinkInfoByUserIdRequest,
    ) -> pds_20220301_models.GetLinkInfoByUserIdResponse:
        """
        @summary Queries the information about a user based on the user ID.
        
        @param request: GetLinkInfoByUserIdRequest
        @return: GetLinkInfoByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_link_info_by_user_id_with_options(request, headers, runtime)

    async def get_link_info_by_user_id_async(
        self,
        request: pds_20220301_models.GetLinkInfoByUserIdRequest,
    ) -> pds_20220301_models.GetLinkInfoByUserIdResponse:
        """
        @summary Queries the information about a user based on the user ID.
        
        @param request: GetLinkInfoByUserIdRequest
        @return: GetLinkInfoByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_link_info_by_user_id_with_options_async(request, headers, runtime)

    def get_revision_with_options(
        self,
        request: pds_20220301_models.GetRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetRevisionResponse:
        """
        @summary Queries the information about a version.
        
        @param request: GetRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_revision_with_options_async(
        self,
        request: pds_20220301_models.GetRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetRevisionResponse:
        """
        @summary Queries the information about a version.
        
        @param request: GetRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_revision(
        self,
        request: pds_20220301_models.GetRevisionRequest,
    ) -> pds_20220301_models.GetRevisionResponse:
        """
        @summary Queries the information about a version.
        
        @param request: GetRevisionRequest
        @return: GetRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_revision_with_options(request, headers, runtime)

    async def get_revision_async(
        self,
        request: pds_20220301_models.GetRevisionRequest,
    ) -> pds_20220301_models.GetRevisionResponse:
        """
        @summary Queries the information about a version.
        
        @param request: GetRevisionRequest
        @return: GetRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_revision_with_options_async(request, headers, runtime)

    def get_share_link_with_options(
        self,
        request: pds_20220301_models.GetShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkResponse:
        """
        @summary Queries the share URL of a file.
        
        @param request: GetShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def get_share_link_with_options_async(
        self,
        request: pds_20220301_models.GetShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkResponse:
        """
        @summary Queries the share URL of a file.
        
        @param request: GetShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_share_link(
        self,
        request: pds_20220301_models.GetShareLinkRequest,
    ) -> pds_20220301_models.GetShareLinkResponse:
        """
        @summary Queries the share URL of a file.
        
        @param request: GetShareLinkRequest
        @return: GetShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_share_link_with_options(request, headers, runtime)

    async def get_share_link_async(
        self,
        request: pds_20220301_models.GetShareLinkRequest,
    ) -> pds_20220301_models.GetShareLinkResponse:
        """
        @summary Queries the share URL of a file.
        
        @param request: GetShareLinkRequest
        @return: GetShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_share_link_with_options_async(request, headers, runtime)

    def get_share_link_by_anonymous_with_options(
        self,
        request: pds_20220301_models.GetShareLinkByAnonymousRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkByAnonymousResponse:
        """
        @summary Queries the information about a share link anonymously.
        
        @param request: GetShareLinkByAnonymousRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShareLinkByAnonymousResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkByAnonymous',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get_by_anonymous',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkByAnonymousResponse(),
            self.execute(params, req, runtime)
        )

    async def get_share_link_by_anonymous_with_options_async(
        self,
        request: pds_20220301_models.GetShareLinkByAnonymousRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkByAnonymousResponse:
        """
        @summary Queries the information about a share link anonymously.
        
        @param request: GetShareLinkByAnonymousRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShareLinkByAnonymousResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkByAnonymous',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get_by_anonymous',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkByAnonymousResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_share_link_by_anonymous(
        self,
        request: pds_20220301_models.GetShareLinkByAnonymousRequest,
    ) -> pds_20220301_models.GetShareLinkByAnonymousResponse:
        """
        @summary Queries the information about a share link anonymously.
        
        @param request: GetShareLinkByAnonymousRequest
        @return: GetShareLinkByAnonymousResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_share_link_by_anonymous_with_options(request, headers, runtime)

    async def get_share_link_by_anonymous_async(
        self,
        request: pds_20220301_models.GetShareLinkByAnonymousRequest,
    ) -> pds_20220301_models.GetShareLinkByAnonymousResponse:
        """
        @summary Queries the information about a share link anonymously.
        
        @param request: GetShareLinkByAnonymousRequest
        @return: GetShareLinkByAnonymousResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_share_link_by_anonymous_with_options_async(request, headers, runtime)

    def get_share_link_token_with_options(
        self,
        request: pds_20220301_models.GetShareLinkTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkTokenResponse:
        """
        @summary Queries a share token anonymously.
        
        @description To access a file by using a share link, you must first obtain a share token, even if the value of share_pwd of this share is an empty string, which specifies that the share is not private.
        
        @param request: GetShareLinkTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShareLinkTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkToken',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get_share_token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkTokenResponse(),
            self.execute(params, req, runtime)
        )

    async def get_share_link_token_with_options_async(
        self,
        request: pds_20220301_models.GetShareLinkTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetShareLinkTokenResponse:
        """
        @summary Queries a share token anonymously.
        
        @description To access a file by using a share link, you must first obtain a share token, even if the value of share_pwd of this share is an empty string, which specifies that the share is not private.
        
        @param request: GetShareLinkTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShareLinkTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShareLinkToken',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/get_share_token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetShareLinkTokenResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_share_link_token(
        self,
        request: pds_20220301_models.GetShareLinkTokenRequest,
    ) -> pds_20220301_models.GetShareLinkTokenResponse:
        """
        @summary Queries a share token anonymously.
        
        @description To access a file by using a share link, you must first obtain a share token, even if the value of share_pwd of this share is an empty string, which specifies that the share is not private.
        
        @param request: GetShareLinkTokenRequest
        @return: GetShareLinkTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_share_link_token_with_options(request, headers, runtime)

    async def get_share_link_token_async(
        self,
        request: pds_20220301_models.GetShareLinkTokenRequest,
    ) -> pds_20220301_models.GetShareLinkTokenResponse:
        """
        @summary Queries a share token anonymously.
        
        @description To access a file by using a share link, you must first obtain a share token, even if the value of share_pwd of this share is an empty string, which specifies that the share is not private.
        
        @param request: GetShareLinkTokenRequest
        @return: GetShareLinkTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_share_link_token_with_options_async(request, headers, runtime)

    def get_story_with_options(
        self,
        request: pds_20220301_models.GetStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetStoryResponse:
        """
        @summary 获取故事详情
        
        @param request: GetStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cover_image_thumbnail_process):
            body['cover_image_thumbnail_process'] = request.cover_image_thumbnail_process
        if not UtilClient.is_unset(request.cover_video_thumbnail_process):
            body['cover_video_thumbnail_process'] = request.cover_video_thumbnail_process
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.image_url_process):
            body['image_url_process'] = request.image_url_process
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/get_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def get_story_with_options_async(
        self,
        request: pds_20220301_models.GetStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetStoryResponse:
        """
        @summary 获取故事详情
        
        @param request: GetStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cover_image_thumbnail_process):
            body['cover_image_thumbnail_process'] = request.cover_image_thumbnail_process
        if not UtilClient.is_unset(request.cover_video_thumbnail_process):
            body['cover_video_thumbnail_process'] = request.cover_video_thumbnail_process
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.image_url_process):
            body['image_url_process'] = request.image_url_process
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/get_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_story(
        self,
        request: pds_20220301_models.GetStoryRequest,
    ) -> pds_20220301_models.GetStoryResponse:
        """
        @summary 获取故事详情
        
        @param request: GetStoryRequest
        @return: GetStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_story_with_options(request, headers, runtime)

    async def get_story_async(
        self,
        request: pds_20220301_models.GetStoryRequest,
    ) -> pds_20220301_models.GetStoryResponse:
        """
        @summary 获取故事详情
        
        @param request: GetStoryRequest
        @return: GetStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_story_with_options_async(request, headers, runtime)

    def get_task_status_with_options(
        self,
        request: pds_20220301_models.GetTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetTaskStatusResponse:
        """
        @summary Queries the execution status of a value-added asynchronous task. You can call this operation to query the execution status of an asynchronous task that is created by calling the CreateSimilarImageClusterTask operation.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/425220.html) of Drive and Photo Service**.
        To call this operation, make sure that the value-added image processing feature is enabled.
        Before you call this operation, a value-added asynchronous task must be created. For example, you can call the CreateSimilarImageClusterTask operation to create an asynchronous task. Then, you can call this operation to query the execution status of the asynchronous task based on the task ID.
        
        @param request: GetTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.task_id):
            body['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/get_task_status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: pds_20220301_models.GetTaskStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetTaskStatusResponse:
        """
        @summary Queries the execution status of a value-added asynchronous task. You can call this operation to query the execution status of an asynchronous task that is created by calling the CreateSimilarImageClusterTask operation.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/425220.html) of Drive and Photo Service**.
        To call this operation, make sure that the value-added image processing feature is enabled.
        Before you call this operation, a value-added asynchronous task must be created. For example, you can call the CreateSimilarImageClusterTask operation to create an asynchronous task. Then, you can call this operation to query the execution status of the asynchronous task based on the task ID.
        
        @param request: GetTaskStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.task_id):
            body['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/get_task_status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_task_status(
        self,
        request: pds_20220301_models.GetTaskStatusRequest,
    ) -> pds_20220301_models.GetTaskStatusResponse:
        """
        @summary Queries the execution status of a value-added asynchronous task. You can call this operation to query the execution status of an asynchronous task that is created by calling the CreateSimilarImageClusterTask operation.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/425220.html) of Drive and Photo Service**.
        To call this operation, make sure that the value-added image processing feature is enabled.
        Before you call this operation, a value-added asynchronous task must be created. For example, you can call the CreateSimilarImageClusterTask operation to create an asynchronous task. Then, you can call this operation to query the execution status of the asynchronous task based on the task ID.
        
        @param request: GetTaskStatusRequest
        @return: GetTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_status_with_options(request, headers, runtime)

    async def get_task_status_async(
        self,
        request: pds_20220301_models.GetTaskStatusRequest,
    ) -> pds_20220301_models.GetTaskStatusResponse:
        """
        @summary Queries the execution status of a value-added asynchronous task. You can call this operation to query the execution status of an asynchronous task that is created by calling the CreateSimilarImageClusterTask operation.
        
        @description *Before you call this operation, make sure that you are familiar with the [billing](https://help.aliyun.com/document_detail/425220.html) of Drive and Photo Service**.
        To call this operation, make sure that the value-added image processing feature is enabled.
        Before you call this operation, a value-added asynchronous task must be created. For example, you can call the CreateSimilarImageClusterTask operation to create an asynchronous task. Then, you can call this operation to query the execution status of the asynchronous task based on the task ID.
        
        @param request: GetTaskStatusRequest
        @return: GetTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_status_with_options_async(request, headers, runtime)

    def get_upload_url_with_options(
        self,
        request: pds_20220301_models.GetUploadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetUploadUrlResponse:
        """
        @summary Queries the upload URL of a file.
        
        @param request: GetUploadUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_upload_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUploadUrlResponse(),
            self.execute(params, req, runtime)
        )

    async def get_upload_url_with_options_async(
        self,
        request: pds_20220301_models.GetUploadUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetUploadUrlResponse:
        """
        @summary Queries the upload URL of a file.
        
        @param request: GetUploadUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadUrl',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_upload_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUploadUrlResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_upload_url(
        self,
        request: pds_20220301_models.GetUploadUrlRequest,
    ) -> pds_20220301_models.GetUploadUrlResponse:
        """
        @summary Queries the upload URL of a file.
        
        @param request: GetUploadUrlRequest
        @return: GetUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_upload_url_with_options(request, headers, runtime)

    async def get_upload_url_async(
        self,
        request: pds_20220301_models.GetUploadUrlRequest,
    ) -> pds_20220301_models.GetUploadUrlResponse:
        """
        @summary Queries the upload URL of a file.
        
        @param request: GetUploadUrlRequest
        @return: GetUploadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_upload_url_with_options_async(request, headers, runtime)

    def get_user_with_options(
        self,
        request: pds_20220301_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetUserResponse:
        """
        @summary Queries the information about a user.
        
        @param request: GetUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUserResponse(),
            self.execute(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: pds_20220301_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetUserResponse:
        """
        @summary Queries the information about a user.
        
        @param request: GetUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_user(
        self,
        request: pds_20220301_models.GetUserRequest,
    ) -> pds_20220301_models.GetUserResponse:
        """
        @summary Queries the information about a user.
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: pds_20220301_models.GetUserRequest,
    ) -> pds_20220301_models.GetUserResponse:
        """
        @summary Queries the information about a user.
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(request, headers, runtime)

    def get_video_preview_play_info_with_options(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetVideoPreviewPlayInfoResponse:
        """
        @summary Queries the information about video playback.
        
        @description For more information about best practices, see [Preview videos online](https://help.aliyun.com/document_detail/427477.html).
        
        @param request: GetVideoPreviewPlayInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoPreviewPlayInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.get_master_url):
            body['get_master_url'] = request.get_master_url
        if not UtilClient.is_unset(request.get_without_url):
            body['get_without_url'] = request.get_without_url
        if not UtilClient.is_unset(request.re_transcode):
            body['re_transcode'] = request.re_transcode
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.template_id):
            body['template_id'] = request.template_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_video_preview_play_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def get_video_preview_play_info_with_options_async(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetVideoPreviewPlayInfoResponse:
        """
        @summary Queries the information about video playback.
        
        @description For more information about best practices, see [Preview videos online](https://help.aliyun.com/document_detail/427477.html).
        
        @param request: GetVideoPreviewPlayInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoPreviewPlayInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.get_master_url):
            body['get_master_url'] = request.get_master_url
        if not UtilClient.is_unset(request.get_without_url):
            body['get_without_url'] = request.get_without_url
        if not UtilClient.is_unset(request.re_transcode):
            body['re_transcode'] = request.re_transcode
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.template_id):
            body['template_id'] = request.template_id
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayInfo',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_video_preview_play_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_video_preview_play_info(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayInfoRequest,
    ) -> pds_20220301_models.GetVideoPreviewPlayInfoResponse:
        """
        @summary Queries the information about video playback.
        
        @description For more information about best practices, see [Preview videos online](https://help.aliyun.com/document_detail/427477.html).
        
        @param request: GetVideoPreviewPlayInfoRequest
        @return: GetVideoPreviewPlayInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_video_preview_play_info_with_options(request, headers, runtime)

    async def get_video_preview_play_info_async(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayInfoRequest,
    ) -> pds_20220301_models.GetVideoPreviewPlayInfoResponse:
        """
        @summary Queries the information about video playback.
        
        @description For more information about best practices, see [Preview videos online](https://help.aliyun.com/document_detail/427477.html).
        
        @param request: GetVideoPreviewPlayInfoRequest
        @return: GetVideoPreviewPlayInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_video_preview_play_info_with_options_async(request, headers, runtime)

    def get_video_preview_play_meta_with_options(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetVideoPreviewPlayMetaResponse:
        """
        @summary Queries the preview metadata of a video.
        
        @description For more information about best practices, see [Preview videos online](https://help.aliyun.com/document_detail/427477.html).
        
        @param request: GetVideoPreviewPlayMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoPreviewPlayMetaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayMeta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_video_preview_play_meta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayMetaResponse(),
            self.execute(params, req, runtime)
        )

    async def get_video_preview_play_meta_with_options_async(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GetVideoPreviewPlayMetaResponse:
        """
        @summary Queries the preview metadata of a video.
        
        @description For more information about best practices, see [Preview videos online](https://help.aliyun.com/document_detail/427477.html).
        
        @param request: GetVideoPreviewPlayMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoPreviewPlayMetaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoPreviewPlayMeta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/get_video_preview_play_meta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GetVideoPreviewPlayMetaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_video_preview_play_meta(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayMetaRequest,
    ) -> pds_20220301_models.GetVideoPreviewPlayMetaResponse:
        """
        @summary Queries the preview metadata of a video.
        
        @description For more information about best practices, see [Preview videos online](https://help.aliyun.com/document_detail/427477.html).
        
        @param request: GetVideoPreviewPlayMetaRequest
        @return: GetVideoPreviewPlayMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_video_preview_play_meta_with_options(request, headers, runtime)

    async def get_video_preview_play_meta_async(
        self,
        request: pds_20220301_models.GetVideoPreviewPlayMetaRequest,
    ) -> pds_20220301_models.GetVideoPreviewPlayMetaResponse:
        """
        @summary Queries the preview metadata of a video.
        
        @description For more information about best practices, see [Preview videos online](https://help.aliyun.com/document_detail/427477.html).
        
        @param request: GetVideoPreviewPlayMetaRequest
        @return: GetVideoPreviewPlayMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_video_preview_play_meta_with_options_async(request, headers, runtime)

    def group_update_name_with_options(
        self,
        request: pds_20220301_models.GroupUpdateNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GroupUpdateNameResponse:
        """
        @summary 更新用户组名字
        
        @param request: GroupUpdateNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GroupUpdateNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GroupUpdateName',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GroupUpdateNameResponse(),
            self.execute(params, req, runtime)
        )

    async def group_update_name_with_options_async(
        self,
        request: pds_20220301_models.GroupUpdateNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.GroupUpdateNameResponse:
        """
        @summary 更新用户组名字
        
        @param request: GroupUpdateNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GroupUpdateNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GroupUpdateName',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.GroupUpdateNameResponse(),
            await self.execute_async(params, req, runtime)
        )

    def group_update_name(
        self,
        request: pds_20220301_models.GroupUpdateNameRequest,
    ) -> pds_20220301_models.GroupUpdateNameResponse:
        """
        @summary 更新用户组名字
        
        @param request: GroupUpdateNameRequest
        @return: GroupUpdateNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.group_update_name_with_options(request, headers, runtime)

    async def group_update_name_async(
        self,
        request: pds_20220301_models.GroupUpdateNameRequest,
    ) -> pds_20220301_models.GroupUpdateNameResponse:
        """
        @summary 更新用户组名字
        
        @param request: GroupUpdateNameRequest
        @return: GroupUpdateNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.group_update_name_with_options_async(request, headers, runtime)

    def import_user_with_options(
        self,
        request: pds_20220301_models.ImportUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ImportUserResponse:
        """
        @summary Imports a user.
        
        @param request: ImportUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authentication_display_name):
            body['authentication_display_name'] = request.authentication_display_name
        if not UtilClient.is_unset(request.authentication_type):
            body['authentication_type'] = request.authentication_type
        if not UtilClient.is_unset(request.auto_create_drive):
            body['auto_create_drive'] = request.auto_create_drive
        if not UtilClient.is_unset(request.drive_total_size):
            body['drive_total_size'] = request.drive_total_size
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ImportUserResponse(),
            self.execute(params, req, runtime)
        )

    async def import_user_with_options_async(
        self,
        request: pds_20220301_models.ImportUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ImportUserResponse:
        """
        @summary Imports a user.
        
        @param request: ImportUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authentication_display_name):
            body['authentication_display_name'] = request.authentication_display_name
        if not UtilClient.is_unset(request.authentication_type):
            body['authentication_type'] = request.authentication_type
        if not UtilClient.is_unset(request.auto_create_drive):
            body['auto_create_drive'] = request.auto_create_drive
        if not UtilClient.is_unset(request.drive_total_size):
            body['drive_total_size'] = request.drive_total_size
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ImportUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/import',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ImportUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def import_user(
        self,
        request: pds_20220301_models.ImportUserRequest,
    ) -> pds_20220301_models.ImportUserResponse:
        """
        @summary Imports a user.
        
        @param request: ImportUserRequest
        @return: ImportUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.import_user_with_options(request, headers, runtime)

    async def import_user_async(
        self,
        request: pds_20220301_models.ImportUserRequest,
    ) -> pds_20220301_models.ImportUserResponse:
        """
        @summary Imports a user.
        
        @param request: ImportUserRequest
        @return: ImportUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.import_user_with_options_async(request, headers, runtime)

    def investigate_file_with_options(
        self,
        request: pds_20220301_models.InvestigateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.InvestigateFileResponse:
        """
        @summary 送审文件
        
        @param request: InvestigateFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvestigateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_file_ids):
            body['drive_file_ids'] = request.drive_file_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvestigateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/csi/investigate_file',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.InvestigateFileResponse(),
            self.execute(params, req, runtime)
        )

    async def investigate_file_with_options_async(
        self,
        request: pds_20220301_models.InvestigateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.InvestigateFileResponse:
        """
        @summary 送审文件
        
        @param request: InvestigateFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvestigateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_file_ids):
            body['drive_file_ids'] = request.drive_file_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvestigateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/csi/investigate_file',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.InvestigateFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def investigate_file(
        self,
        request: pds_20220301_models.InvestigateFileRequest,
    ) -> pds_20220301_models.InvestigateFileResponse:
        """
        @summary 送审文件
        
        @param request: InvestigateFileRequest
        @return: InvestigateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.investigate_file_with_options(request, headers, runtime)

    async def investigate_file_async(
        self,
        request: pds_20220301_models.InvestigateFileRequest,
    ) -> pds_20220301_models.InvestigateFileResponse:
        """
        @summary 送审文件
        
        @param request: InvestigateFileRequest
        @return: InvestigateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.investigate_file_with_options_async(request, headers, runtime)

    def link_account_with_options(
        self,
        request: pds_20220301_models.LinkAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.LinkAccountResponse:
        """
        @summary Associates an account with a user.
        
        @param request: LinkAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LinkAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkAccount',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/link',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.LinkAccountResponse(),
            self.execute(params, req, runtime)
        )

    async def link_account_with_options_async(
        self,
        request: pds_20220301_models.LinkAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.LinkAccountResponse:
        """
        @summary Associates an account with a user.
        
        @param request: LinkAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LinkAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LinkAccount',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/link',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.LinkAccountResponse(),
            await self.execute_async(params, req, runtime)
        )

    def link_account(
        self,
        request: pds_20220301_models.LinkAccountRequest,
    ) -> pds_20220301_models.LinkAccountResponse:
        """
        @summary Associates an account with a user.
        
        @param request: LinkAccountRequest
        @return: LinkAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.link_account_with_options(request, headers, runtime)

    async def link_account_async(
        self,
        request: pds_20220301_models.LinkAccountRequest,
    ) -> pds_20220301_models.LinkAccountResponse:
        """
        @summary Associates an account with a user.
        
        @param request: LinkAccountRequest
        @return: LinkAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.link_account_with_options_async(request, headers, runtime)

    def list_address_groups_with_options(
        self,
        request: pds_20220301_models.ListAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListAddressGroupsResponse:
        """
        @summary Queries location-based groups.
        
        @param request: ListAddressGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddressGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListAddressGroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_address_groups_with_options_async(
        self,
        request: pds_20220301_models.ListAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListAddressGroupsResponse:
        """
        @summary Queries location-based groups.
        
        @param request: ListAddressGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddressGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListAddressGroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_address_groups(
        self,
        request: pds_20220301_models.ListAddressGroupsRequest,
    ) -> pds_20220301_models.ListAddressGroupsResponse:
        """
        @summary Queries location-based groups.
        
        @param request: ListAddressGroupsRequest
        @return: ListAddressGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_address_groups_with_options(request, headers, runtime)

    async def list_address_groups_async(
        self,
        request: pds_20220301_models.ListAddressGroupsRequest,
    ) -> pds_20220301_models.ListAddressGroupsResponse:
        """
        @summary Queries location-based groups.
        
        @param request: ListAddressGroupsRequest
        @return: ListAddressGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_address_groups_with_options_async(request, headers, runtime)

    def list_assignment_with_options(
        self,
        request: pds_20220301_models.ListAssignmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListAssignmentResponse:
        """
        @summary Queries a list of assigned roles. For example, you can query the administrators of a group by group ID.
        
        @param request: ListAssignmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAssignmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not UtilClient.is_unset(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAssignment',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/role/list_assignment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListAssignmentResponse(),
            self.execute(params, req, runtime)
        )

    async def list_assignment_with_options_async(
        self,
        request: pds_20220301_models.ListAssignmentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListAssignmentResponse:
        """
        @summary Queries a list of assigned roles. For example, you can query the administrators of a group by group ID.
        
        @param request: ListAssignmentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAssignmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not UtilClient.is_unset(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAssignment',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/role/list_assignment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListAssignmentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_assignment(
        self,
        request: pds_20220301_models.ListAssignmentRequest,
    ) -> pds_20220301_models.ListAssignmentResponse:
        """
        @summary Queries a list of assigned roles. For example, you can query the administrators of a group by group ID.
        
        @param request: ListAssignmentRequest
        @return: ListAssignmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_assignment_with_options(request, headers, runtime)

    async def list_assignment_async(
        self,
        request: pds_20220301_models.ListAssignmentRequest,
    ) -> pds_20220301_models.ListAssignmentResponse:
        """
        @summary Queries a list of assigned roles. For example, you can query the administrators of a group by group ID.
        
        @param request: ListAssignmentRequest
        @return: ListAssignmentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_assignment_with_options_async(request, headers, runtime)

    def list_delta_with_options(
        self,
        request: pds_20220301_models.ListDeltaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDeltaResponse:
        """
        @summary Queries incremental information.
        
        @param request: ListDeltaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeltaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDelta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_delta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDeltaResponse(),
            self.execute(params, req, runtime)
        )

    async def list_delta_with_options_async(
        self,
        request: pds_20220301_models.ListDeltaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDeltaResponse:
        """
        @summary Queries incremental information.
        
        @param request: ListDeltaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeltaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cursor):
            body['cursor'] = request.cursor
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDelta',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_delta',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDeltaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_delta(
        self,
        request: pds_20220301_models.ListDeltaRequest,
    ) -> pds_20220301_models.ListDeltaResponse:
        """
        @summary Queries incremental information.
        
        @param request: ListDeltaRequest
        @return: ListDeltaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_delta_with_options(request, headers, runtime)

    async def list_delta_async(
        self,
        request: pds_20220301_models.ListDeltaRequest,
    ) -> pds_20220301_models.ListDeltaResponse:
        """
        @summary Queries incremental information.
        
        @param request: ListDeltaRequest
        @return: ListDeltaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_delta_with_options_async(request, headers, runtime)

    def list_domains_with_options(
        self,
        request: pds_20220301_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDomainsResponse:
        """
        @summary 列举 domain
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.parent_domain_id):
            body['parent_domain_id'] = request.parent_domain_id
        if not UtilClient.is_unset(request.service_code):
            body['service_code'] = request.service_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDomainsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: pds_20220301_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDomainsResponse:
        """
        @summary 列举 domain
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.parent_domain_id):
            body['parent_domain_id'] = request.parent_domain_id
        if not UtilClient.is_unset(request.service_code):
            body['service_code'] = request.service_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDomainsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: pds_20220301_models.ListDomainsRequest,
    ) -> pds_20220301_models.ListDomainsResponse:
        """
        @summary 列举 domain
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(request, headers, runtime)

    async def list_domains_async(
        self,
        request: pds_20220301_models.ListDomainsRequest,
    ) -> pds_20220301_models.ListDomainsResponse:
        """
        @summary 列举 domain
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_domains_with_options_async(request, headers, runtime)

    def list_drive_with_options(
        self,
        request: pds_20220301_models.ListDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDriveResponse:
        """
        @summary Queries a list of drives.
        
        @param request: ListDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def list_drive_with_options_async(
        self,
        request: pds_20220301_models.ListDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListDriveResponse:
        """
        @summary Queries a list of drives.
        
        @param request: ListDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_drive(
        self,
        request: pds_20220301_models.ListDriveRequest,
    ) -> pds_20220301_models.ListDriveResponse:
        """
        @summary Queries a list of drives.
        
        @param request: ListDriveRequest
        @return: ListDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_drive_with_options(request, headers, runtime)

    async def list_drive_async(
        self,
        request: pds_20220301_models.ListDriveRequest,
    ) -> pds_20220301_models.ListDriveResponse:
        """
        @summary Queries a list of drives.
        
        @param request: ListDriveRequest
        @return: ListDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_drive_with_options_async(request, headers, runtime)

    def list_facegroups_with_options(
        self,
        request: pds_20220301_models.ListFacegroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListFacegroupsResponse:
        """
        @summary Queries face-based groups.
        
        @param request: ListFacegroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFacegroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFacegroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_facegroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFacegroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_facegroups_with_options_async(
        self,
        request: pds_20220301_models.ListFacegroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListFacegroupsResponse:
        """
        @summary Queries face-based groups.
        
        @param request: ListFacegroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFacegroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFacegroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_facegroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFacegroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_facegroups(
        self,
        request: pds_20220301_models.ListFacegroupsRequest,
    ) -> pds_20220301_models.ListFacegroupsResponse:
        """
        @summary Queries face-based groups.
        
        @param request: ListFacegroupsRequest
        @return: ListFacegroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_facegroups_with_options(request, headers, runtime)

    async def list_facegroups_async(
        self,
        request: pds_20220301_models.ListFacegroupsRequest,
    ) -> pds_20220301_models.ListFacegroupsResponse:
        """
        @summary Queries face-based groups.
        
        @param request: ListFacegroupsRequest
        @return: ListFacegroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_facegroups_with_options_async(request, headers, runtime)

    def list_file_with_options(
        self,
        request: pds_20220301_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListFileResponse:
        """
        @summary Queries a list of files and folders.
        
        @param request: ListFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFileResponse(),
            self.execute(params, req, runtime)
        )

    async def list_file_with_options_async(
        self,
        request: pds_20220301_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListFileResponse:
        """
        @summary Queries a list of files and folders.
        
        @param request: ListFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['category'] = request.category
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_file(
        self,
        request: pds_20220301_models.ListFileRequest,
    ) -> pds_20220301_models.ListFileResponse:
        """
        @summary Queries a list of files and folders.
        
        @param request: ListFileRequest
        @return: ListFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_file_with_options(request, headers, runtime)

    async def list_file_async(
        self,
        request: pds_20220301_models.ListFileRequest,
    ) -> pds_20220301_models.ListFileResponse:
        """
        @summary Queries a list of files and folders.
        
        @param request: ListFileRequest
        @return: ListFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_file_with_options_async(request, headers, runtime)

    def list_group_with_options(
        self,
        request: pds_20220301_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListGroupResponse:
        """
        @summary Queries groups.
        
        @param request: ListGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def list_group_with_options_async(
        self,
        request: pds_20220301_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListGroupResponse:
        """
        @summary Queries groups.
        
        @param request: ListGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_group(
        self,
        request: pds_20220301_models.ListGroupRequest,
    ) -> pds_20220301_models.ListGroupResponse:
        """
        @summary Queries groups.
        
        @param request: ListGroupRequest
        @return: ListGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_with_options(request, headers, runtime)

    async def list_group_async(
        self,
        request: pds_20220301_models.ListGroupRequest,
    ) -> pds_20220301_models.ListGroupResponse:
        """
        @summary Queries groups.
        
        @param request: ListGroupRequest
        @return: ListGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_group_with_options_async(request, headers, runtime)

    def list_group_member_with_options(
        self,
        request: pds_20220301_models.ListGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListGroupMemberResponse:
        """
        @summary Queries the members of a group.
        
        @param request: ListGroupMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroupMember',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/list_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListGroupMemberResponse(),
            self.execute(params, req, runtime)
        )

    async def list_group_member_with_options_async(
        self,
        request: pds_20220301_models.ListGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListGroupMemberResponse:
        """
        @summary Queries the members of a group.
        
        @param request: ListGroupMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListGroupMember',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/list_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListGroupMemberResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_group_member(
        self,
        request: pds_20220301_models.ListGroupMemberRequest,
    ) -> pds_20220301_models.ListGroupMemberResponse:
        """
        @summary Queries the members of a group.
        
        @param request: ListGroupMemberRequest
        @return: ListGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_member_with_options(request, headers, runtime)

    async def list_group_member_async(
        self,
        request: pds_20220301_models.ListGroupMemberRequest,
    ) -> pds_20220301_models.ListGroupMemberResponse:
        """
        @summary Queries the members of a group.
        
        @param request: ListGroupMemberRequest
        @return: ListGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_group_member_with_options_async(request, headers, runtime)

    def list_identity_role_with_options(
        self,
        request: pds_20220301_models.ListIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListIdentityRoleResponse:
        """
        @summary 列举用户或团队已分配的角色列表
        
        @param request: ListIdentityRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdentityRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIdentityRole',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/role/list_identity_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListIdentityRoleResponse(),
            self.execute(params, req, runtime)
        )

    async def list_identity_role_with_options_async(
        self,
        request: pds_20220301_models.ListIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListIdentityRoleResponse:
        """
        @summary 列举用户或团队已分配的角色列表
        
        @param request: ListIdentityRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdentityRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIdentityRole',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/role/list_identity_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListIdentityRoleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_identity_role(
        self,
        request: pds_20220301_models.ListIdentityRoleRequest,
    ) -> pds_20220301_models.ListIdentityRoleResponse:
        """
        @summary 列举用户或团队已分配的角色列表
        
        @param request: ListIdentityRoleRequest
        @return: ListIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_identity_role_with_options(request, headers, runtime)

    async def list_identity_role_async(
        self,
        request: pds_20220301_models.ListIdentityRoleRequest,
    ) -> pds_20220301_models.ListIdentityRoleResponse:
        """
        @summary 列举用户或团队已分配的角色列表
        
        @param request: ListIdentityRoleRequest
        @return: ListIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_identity_role_with_options_async(request, headers, runtime)

    def list_identity_to_benefit_pkg_mapping_with_options(
        self,
        request: pds_20220301_models.ListIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListIdentityToBenefitPkgMappingResponse:
        """
        @summary Queries the mappings between entities and benefit packages. You can call this operation to query the benefit packages that are associated with a user.
        
        @param request: ListIdentityToBenefitPkgMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdentityToBenefitPkgMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity_id):
            body['identity_id'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            body['identity_type'] = request.identity_type
        if not UtilClient.is_unset(request.include_expired):
            body['include_expired'] = request.include_expired
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIdentityToBenefitPkgMapping',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/benefit/identity_to_benefit_pkg_mapping/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListIdentityToBenefitPkgMappingResponse(),
            self.execute(params, req, runtime)
        )

    async def list_identity_to_benefit_pkg_mapping_with_options_async(
        self,
        request: pds_20220301_models.ListIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListIdentityToBenefitPkgMappingResponse:
        """
        @summary Queries the mappings between entities and benefit packages. You can call this operation to query the benefit packages that are associated with a user.
        
        @param request: ListIdentityToBenefitPkgMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdentityToBenefitPkgMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identity_id):
            body['identity_id'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            body['identity_type'] = request.identity_type
        if not UtilClient.is_unset(request.include_expired):
            body['include_expired'] = request.include_expired
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIdentityToBenefitPkgMapping',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/benefit/identity_to_benefit_pkg_mapping/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListIdentityToBenefitPkgMappingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_identity_to_benefit_pkg_mapping(
        self,
        request: pds_20220301_models.ListIdentityToBenefitPkgMappingRequest,
    ) -> pds_20220301_models.ListIdentityToBenefitPkgMappingResponse:
        """
        @summary Queries the mappings between entities and benefit packages. You can call this operation to query the benefit packages that are associated with a user.
        
        @param request: ListIdentityToBenefitPkgMappingRequest
        @return: ListIdentityToBenefitPkgMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_identity_to_benefit_pkg_mapping_with_options(request, headers, runtime)

    async def list_identity_to_benefit_pkg_mapping_async(
        self,
        request: pds_20220301_models.ListIdentityToBenefitPkgMappingRequest,
    ) -> pds_20220301_models.ListIdentityToBenefitPkgMappingResponse:
        """
        @summary Queries the mappings between entities and benefit packages. You can call this operation to query the benefit packages that are associated with a user.
        
        @param request: ListIdentityToBenefitPkgMappingRequest
        @return: ListIdentityToBenefitPkgMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_identity_to_benefit_pkg_mapping_with_options_async(request, headers, runtime)

    def list_my_drives_with_options(
        self,
        request: pds_20220301_models.ListMyDrivesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListMyDrivesResponse:
        """
        @summary Queries the drives of the current user.
        
        @param request: ListMyDrivesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMyDrivesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMyDrives',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list_my_drives',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListMyDrivesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_my_drives_with_options_async(
        self,
        request: pds_20220301_models.ListMyDrivesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListMyDrivesResponse:
        """
        @summary Queries the drives of the current user.
        
        @param request: ListMyDrivesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMyDrivesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMyDrives',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list_my_drives',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListMyDrivesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_my_drives(
        self,
        request: pds_20220301_models.ListMyDrivesRequest,
    ) -> pds_20220301_models.ListMyDrivesResponse:
        """
        @summary Queries the drives of the current user.
        
        @param request: ListMyDrivesRequest
        @return: ListMyDrivesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_my_drives_with_options(request, headers, runtime)

    async def list_my_drives_async(
        self,
        request: pds_20220301_models.ListMyDrivesRequest,
    ) -> pds_20220301_models.ListMyDrivesResponse:
        """
        @summary Queries the drives of the current user.
        
        @param request: ListMyDrivesRequest
        @return: ListMyDrivesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_my_drives_with_options_async(request, headers, runtime)

    def list_my_group_drive_with_options(
        self,
        request: pds_20220301_models.ListMyGroupDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListMyGroupDriveResponse:
        """
        @summary Queries the team drives that can be accessed by the authorized users.
        
        @param request: ListMyGroupDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMyGroupDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMyGroupDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list_my_group_drive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListMyGroupDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def list_my_group_drive_with_options_async(
        self,
        request: pds_20220301_models.ListMyGroupDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListMyGroupDriveResponse:
        """
        @summary Queries the team drives that can be accessed by the authorized users.
        
        @param request: ListMyGroupDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMyGroupDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMyGroupDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/list_my_group_drive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListMyGroupDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_my_group_drive(
        self,
        request: pds_20220301_models.ListMyGroupDriveRequest,
    ) -> pds_20220301_models.ListMyGroupDriveResponse:
        """
        @summary Queries the team drives that can be accessed by the authorized users.
        
        @param request: ListMyGroupDriveRequest
        @return: ListMyGroupDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_my_group_drive_with_options(request, headers, runtime)

    async def list_my_group_drive_async(
        self,
        request: pds_20220301_models.ListMyGroupDriveRequest,
    ) -> pds_20220301_models.ListMyGroupDriveResponse:
        """
        @summary Queries the team drives that can be accessed by the authorized users.
        
        @param request: ListMyGroupDriveRequest
        @return: ListMyGroupDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_my_group_drive_with_options_async(request, headers, runtime)

    def list_received_file_with_options(
        self,
        request: pds_20220301_models.ListReceivedFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListReceivedFileResponse:
        """
        @summary Queries a list of files that are shared with a user. You can call this operation to query a list of files in a personal drive on which a user is granted permissions.
        
        @param request: ListReceivedFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReceivedFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListReceivedFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_received_file',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListReceivedFileResponse(),
            self.execute(params, req, runtime)
        )

    async def list_received_file_with_options_async(
        self,
        request: pds_20220301_models.ListReceivedFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListReceivedFileResponse:
        """
        @summary Queries a list of files that are shared with a user. You can call this operation to query a list of files in a personal drive on which a user is granted permissions.
        
        @param request: ListReceivedFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReceivedFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListReceivedFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_received_file',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListReceivedFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_received_file(
        self,
        request: pds_20220301_models.ListReceivedFileRequest,
    ) -> pds_20220301_models.ListReceivedFileResponse:
        """
        @summary Queries a list of files that are shared with a user. You can call this operation to query a list of files in a personal drive on which a user is granted permissions.
        
        @param request: ListReceivedFileRequest
        @return: ListReceivedFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_received_file_with_options(request, headers, runtime)

    async def list_received_file_async(
        self,
        request: pds_20220301_models.ListReceivedFileRequest,
    ) -> pds_20220301_models.ListReceivedFileResponse:
        """
        @summary Queries a list of files that are shared with a user. You can call this operation to query a list of files in a personal drive on which a user is granted permissions.
        
        @param request: ListReceivedFileRequest
        @return: ListReceivedFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_received_file_with_options_async(request, headers, runtime)

    def list_recyclebin_with_options(
        self,
        request: pds_20220301_models.ListRecyclebinRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListRecyclebinResponse:
        """
        @summary Queries the information about files and folders in the recycle bin.
        
        @param request: ListRecyclebinRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecyclebinResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRecyclebinResponse(),
            self.execute(params, req, runtime)
        )

    async def list_recyclebin_with_options_async(
        self,
        request: pds_20220301_models.ListRecyclebinRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListRecyclebinResponse:
        """
        @summary Queries the information about files and folders in the recycle bin.
        
        @param request: ListRecyclebinRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecyclebinResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRecyclebin',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRecyclebinResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_recyclebin(
        self,
        request: pds_20220301_models.ListRecyclebinRequest,
    ) -> pds_20220301_models.ListRecyclebinResponse:
        """
        @summary Queries the information about files and folders in the recycle bin.
        
        @param request: ListRecyclebinRequest
        @return: ListRecyclebinResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_recyclebin_with_options(request, headers, runtime)

    async def list_recyclebin_async(
        self,
        request: pds_20220301_models.ListRecyclebinRequest,
    ) -> pds_20220301_models.ListRecyclebinResponse:
        """
        @summary Queries the information about files and folders in the recycle bin.
        
        @param request: ListRecyclebinRequest
        @return: ListRecyclebinResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_recyclebin_with_options_async(request, headers, runtime)

    def list_revision_with_options(
        self,
        request: pds_20220301_models.ListRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListRevisionResponse:
        """
        @summary Queries the versions of a file.
        
        @param request: ListRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def list_revision_with_options_async(
        self,
        request: pds_20220301_models.ListRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListRevisionResponse:
        """
        @summary Queries the versions of a file.
        
        @param request: ListRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_revision(
        self,
        request: pds_20220301_models.ListRevisionRequest,
    ) -> pds_20220301_models.ListRevisionResponse:
        """
        @summary Queries the versions of a file.
        
        @param request: ListRevisionRequest
        @return: ListRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_revision_with_options(request, headers, runtime)

    async def list_revision_async(
        self,
        request: pds_20220301_models.ListRevisionRequest,
    ) -> pds_20220301_models.ListRevisionResponse:
        """
        @summary Queries the versions of a file.
        
        @param request: ListRevisionRequest
        @return: ListRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_revision_with_options_async(request, headers, runtime)

    def list_share_link_with_options(
        self,
        request: pds_20220301_models.ListShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListShareLinkResponse:
        """
        @summary Queries shares.
        
        @description This operation is discontinued. To query shares, you can call the SearchShareLink operation.
        
        @param request: ListShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['creator'] = request.creator
        if not UtilClient.is_unset(request.include_cancelled):
            body['include_cancelled'] = request.include_cancelled
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def list_share_link_with_options_async(
        self,
        request: pds_20220301_models.ListShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListShareLinkResponse:
        """
        @summary Queries shares.
        
        @description This operation is discontinued. To query shares, you can call the SearchShareLink operation.
        
        @param request: ListShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creator):
            body['creator'] = request.creator
        if not UtilClient.is_unset(request.include_cancelled):
            body['include_cancelled'] = request.include_cancelled
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_share_link(
        self,
        request: pds_20220301_models.ListShareLinkRequest,
    ) -> pds_20220301_models.ListShareLinkResponse:
        """
        @summary Queries shares.
        
        @description This operation is discontinued. To query shares, you can call the SearchShareLink operation.
        
        @param request: ListShareLinkRequest
        @return: ListShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_share_link_with_options(request, headers, runtime)

    async def list_share_link_async(
        self,
        request: pds_20220301_models.ListShareLinkRequest,
    ) -> pds_20220301_models.ListShareLinkResponse:
        """
        @summary Queries shares.
        
        @description This operation is discontinued. To query shares, you can call the SearchShareLink operation.
        
        @param request: ListShareLinkRequest
        @return: ListShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_share_link_with_options_async(request, headers, runtime)

    def list_tags_with_options(
        self,
        request: pds_20220301_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListTagsResponse:
        """
        @summary Queries tags.
        
        @description You can call this operation to query the tags within the specified drive at a time. The top 2,000 tags of the images are returned.
        
        @param request: ListTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: pds_20220301_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListTagsResponse:
        """
        @summary Queries tags.
        
        @description You can call this operation to query the tags within the specified drive at a time. The top 2,000 tags of the images are returned.
        
        @param request: ListTagsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/list_tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: pds_20220301_models.ListTagsRequest,
    ) -> pds_20220301_models.ListTagsResponse:
        """
        @summary Queries tags.
        
        @description You can call this operation to query the tags within the specified drive at a time. The top 2,000 tags of the images are returned.
        
        @param request: ListTagsRequest
        @return: ListTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    async def list_tags_async(
        self,
        request: pds_20220301_models.ListTagsRequest,
    ) -> pds_20220301_models.ListTagsResponse:
        """
        @summary Queries tags.
        
        @description You can call this operation to query the tags within the specified drive at a time. The top 2,000 tags of the images are returned.
        
        @param request: ListTagsRequest
        @return: ListTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tags_with_options_async(request, headers, runtime)

    def list_uploaded_parts_with_options(
        self,
        request: pds_20220301_models.ListUploadedPartsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListUploadedPartsResponse:
        """
        @summary Queries the file parts that are uploaded.
        
        @param request: ListUploadedPartsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUploadedPartsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.part_number_marker):
            body['part_number_marker'] = request.part_number_marker
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUploadedParts',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_uploaded_parts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUploadedPartsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_uploaded_parts_with_options_async(
        self,
        request: pds_20220301_models.ListUploadedPartsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListUploadedPartsResponse:
        """
        @summary Queries the file parts that are uploaded.
        
        @param request: ListUploadedPartsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUploadedPartsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.part_number_marker):
            body['part_number_marker'] = request.part_number_marker
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUploadedParts',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/list_uploaded_parts',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUploadedPartsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_uploaded_parts(
        self,
        request: pds_20220301_models.ListUploadedPartsRequest,
    ) -> pds_20220301_models.ListUploadedPartsResponse:
        """
        @summary Queries the file parts that are uploaded.
        
        @param request: ListUploadedPartsRequest
        @return: ListUploadedPartsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_uploaded_parts_with_options(request, headers, runtime)

    async def list_uploaded_parts_async(
        self,
        request: pds_20220301_models.ListUploadedPartsRequest,
    ) -> pds_20220301_models.ListUploadedPartsResponse:
        """
        @summary Queries the file parts that are uploaded.
        
        @param request: ListUploadedPartsRequest
        @return: ListUploadedPartsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_uploaded_parts_with_options_async(request, headers, runtime)

    def list_user_with_options(
        self,
        request: pds_20220301_models.ListUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListUserResponse:
        """
        @summary Queries users.
        
        @param request: ListUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUserResponse(),
            self.execute(params, req, runtime)
        )

    async def list_user_with_options_async(
        self,
        request: pds_20220301_models.ListUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ListUserResponse:
        """
        @summary Queries users.
        
        @param request: ListUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ListUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_user(
        self,
        request: pds_20220301_models.ListUserRequest,
    ) -> pds_20220301_models.ListUserResponse:
        """
        @summary Queries users.
        
        @param request: ListUserRequest
        @return: ListUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_with_options(request, headers, runtime)

    async def list_user_async(
        self,
        request: pds_20220301_models.ListUserRequest,
    ) -> pds_20220301_models.ListUserResponse:
        """
        @summary Queries users.
        
        @param request: ListUserRequest
        @return: ListUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_with_options_async(request, headers, runtime)

    def move_file_with_options(
        self,
        request: pds_20220301_models.MoveFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.MoveFileResponse:
        """
        @summary Moves files or folders.
        
        @param request: MoveFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/move',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.MoveFileResponse(),
            self.execute(params, req, runtime)
        )

    async def move_file_with_options_async(
        self,
        request: pds_20220301_models.MoveFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.MoveFileResponse:
        """
        @summary Moves files or folders.
        
        @param request: MoveFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/move',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.MoveFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def move_file(
        self,
        request: pds_20220301_models.MoveFileRequest,
    ) -> pds_20220301_models.MoveFileResponse:
        """
        @summary Moves files or folders.
        
        @param request: MoveFileRequest
        @return: MoveFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.move_file_with_options(request, headers, runtime)

    async def move_file_async(
        self,
        request: pds_20220301_models.MoveFileRequest,
    ) -> pds_20220301_models.MoveFileResponse:
        """
        @summary Moves files or folders.
        
        @param request: MoveFileRequest
        @return: MoveFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.move_file_with_options_async(request, headers, runtime)

    def query_order_price_with_options(
        self,
        request: pds_20220301_models.QueryOrderPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.QueryOrderPriceResponse:
        """
        @summary 查询凌霄订单价格
        
        @param request: QueryOrderPriceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrderPriceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.instance_id):
            body['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            body['order_type'] = request.order_type
        if not UtilClient.is_unset(request.package):
            body['package'] = request.package
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['period_unit'] = request.period_unit
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        if not UtilClient.is_unset(request.user_count):
            body['user_count'] = request.user_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderPrice',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/query_order_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.QueryOrderPriceResponse(),
            self.execute(params, req, runtime)
        )

    async def query_order_price_with_options_async(
        self,
        request: pds_20220301_models.QueryOrderPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.QueryOrderPriceResponse:
        """
        @summary 查询凌霄订单价格
        
        @param request: QueryOrderPriceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrderPriceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.instance_id):
            body['instance_id'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            body['order_type'] = request.order_type
        if not UtilClient.is_unset(request.package):
            body['package'] = request.package
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['period_unit'] = request.period_unit
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        if not UtilClient.is_unset(request.user_count):
            body['user_count'] = request.user_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderPrice',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/query_order_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.QueryOrderPriceResponse(),
            await self.execute_async(params, req, runtime)
        )

    def query_order_price(
        self,
        request: pds_20220301_models.QueryOrderPriceRequest,
    ) -> pds_20220301_models.QueryOrderPriceResponse:
        """
        @summary 查询凌霄订单价格
        
        @param request: QueryOrderPriceRequest
        @return: QueryOrderPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_order_price_with_options(request, headers, runtime)

    async def query_order_price_async(
        self,
        request: pds_20220301_models.QueryOrderPriceRequest,
    ) -> pds_20220301_models.QueryOrderPriceResponse:
        """
        @summary 查询凌霄订单价格
        
        @param request: QueryOrderPriceRequest
        @return: QueryOrderPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_order_price_with_options_async(request, headers, runtime)

    def remove_face_group_file_with_options(
        self,
        request: pds_20220301_models.RemoveFaceGroupFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RemoveFaceGroupFileResponse:
        """
        @summary 从人脸分组中的移除指定的文件
        
        @param request: RemoveFaceGroupFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveFaceGroupFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.face_group_id):
            body['face_group_id'] = request.face_group_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveFaceGroupFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/albums/unassign_facegroup_item',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RemoveFaceGroupFileResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_face_group_file_with_options_async(
        self,
        request: pds_20220301_models.RemoveFaceGroupFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RemoveFaceGroupFileResponse:
        """
        @summary 从人脸分组中的移除指定的文件
        
        @param request: RemoveFaceGroupFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveFaceGroupFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.face_group_id):
            body['face_group_id'] = request.face_group_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveFaceGroupFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/albums/unassign_facegroup_item',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RemoveFaceGroupFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_face_group_file(
        self,
        request: pds_20220301_models.RemoveFaceGroupFileRequest,
    ) -> pds_20220301_models.RemoveFaceGroupFileResponse:
        """
        @summary 从人脸分组中的移除指定的文件
        
        @param request: RemoveFaceGroupFileRequest
        @return: RemoveFaceGroupFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_face_group_file_with_options(request, headers, runtime)

    async def remove_face_group_file_async(
        self,
        request: pds_20220301_models.RemoveFaceGroupFileRequest,
    ) -> pds_20220301_models.RemoveFaceGroupFileResponse:
        """
        @summary 从人脸分组中的移除指定的文件
        
        @param request: RemoveFaceGroupFileRequest
        @return: RemoveFaceGroupFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_face_group_file_with_options_async(request, headers, runtime)

    def remove_group_member_with_options(
        self,
        request: pds_20220301_models.RemoveGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RemoveGroupMemberResponse:
        """
        @summary Removes a member from a group.
        
        @param request: RemoveGroupMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveGroupMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.member_id):
            body['member_id'] = request.member_id
        if not UtilClient.is_unset(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupMember',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/remove_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RemoveGroupMemberResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_group_member_with_options_async(
        self,
        request: pds_20220301_models.RemoveGroupMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RemoveGroupMemberResponse:
        """
        @summary Removes a member from a group.
        
        @param request: RemoveGroupMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveGroupMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.member_id):
            body['member_id'] = request.member_id
        if not UtilClient.is_unset(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveGroupMember',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/remove_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RemoveGroupMemberResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_group_member(
        self,
        request: pds_20220301_models.RemoveGroupMemberRequest,
    ) -> pds_20220301_models.RemoveGroupMemberResponse:
        """
        @summary Removes a member from a group.
        
        @param request: RemoveGroupMemberRequest
        @return: RemoveGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_group_member_with_options(request, headers, runtime)

    async def remove_group_member_async(
        self,
        request: pds_20220301_models.RemoveGroupMemberRequest,
    ) -> pds_20220301_models.RemoveGroupMemberResponse:
        """
        @summary Removes a member from a group.
        
        @param request: RemoveGroupMemberRequest
        @return: RemoveGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_group_member_with_options_async(request, headers, runtime)

    def remove_story_files_with_options(
        self,
        request: pds_20220301_models.RemoveStoryFilesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RemoveStoryFilesResponse:
        """
        @summary 故事移除文件
        
        @param request: RemoveStoryFilesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveStoryFilesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveStoryFiles',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/remove_story_files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RemoveStoryFilesResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_story_files_with_options_async(
        self,
        request: pds_20220301_models.RemoveStoryFilesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RemoveStoryFilesResponse:
        """
        @summary 故事移除文件
        
        @param request: RemoveStoryFilesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveStoryFilesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveStoryFiles',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/remove_story_files',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RemoveStoryFilesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_story_files(
        self,
        request: pds_20220301_models.RemoveStoryFilesRequest,
    ) -> pds_20220301_models.RemoveStoryFilesResponse:
        """
        @summary 故事移除文件
        
        @param request: RemoveStoryFilesRequest
        @return: RemoveStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_story_files_with_options(request, headers, runtime)

    async def remove_story_files_async(
        self,
        request: pds_20220301_models.RemoveStoryFilesRequest,
    ) -> pds_20220301_models.RemoveStoryFilesResponse:
        """
        @summary 故事移除文件
        
        @param request: RemoveStoryFilesRequest
        @return: RemoveStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_story_files_with_options_async(request, headers, runtime)

    def restore_file_with_options(
        self,
        request: pds_20220301_models.RestoreFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RestoreFileResponse:
        """
        @summary Restores a file or folder from the recycle bin.
        
        @param request: RestoreFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreFileResponse(),
            self.execute(params, req, runtime)
        )

    async def restore_file_with_options_async(
        self,
        request: pds_20220301_models.RestoreFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RestoreFileResponse:
        """
        @summary Restores a file or folder from the recycle bin.
        
        @param request: RestoreFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def restore_file(
        self,
        request: pds_20220301_models.RestoreFileRequest,
    ) -> pds_20220301_models.RestoreFileResponse:
        """
        @summary Restores a file or folder from the recycle bin.
        
        @param request: RestoreFileRequest
        @return: RestoreFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_file_with_options(request, headers, runtime)

    async def restore_file_async(
        self,
        request: pds_20220301_models.RestoreFileRequest,
    ) -> pds_20220301_models.RestoreFileResponse:
        """
        @summary Restores a file or folder from the recycle bin.
        
        @param request: RestoreFileRequest
        @return: RestoreFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restore_file_with_options_async(request, headers, runtime)

    def restore_revision_with_options(
        self,
        request: pds_20220301_models.RestoreRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RestoreRevisionResponse:
        """
        @summary Restores a historical version of a file. You cannot restore the latest version of a file.
        
        @param request: RestoreRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def restore_revision_with_options_async(
        self,
        request: pds_20220301_models.RestoreRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.RestoreRevisionResponse:
        """
        @summary Restores a historical version of a file. You cannot restore the latest version of a file.
        
        @param request: RestoreRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestoreRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/restore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.RestoreRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def restore_revision(
        self,
        request: pds_20220301_models.RestoreRevisionRequest,
    ) -> pds_20220301_models.RestoreRevisionResponse:
        """
        @summary Restores a historical version of a file. You cannot restore the latest version of a file.
        
        @param request: RestoreRevisionRequest
        @return: RestoreRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_revision_with_options(request, headers, runtime)

    async def restore_revision_async(
        self,
        request: pds_20220301_models.RestoreRevisionRequest,
    ) -> pds_20220301_models.RestoreRevisionResponse:
        """
        @summary Restores a historical version of a file. You cannot restore the latest version of a file.
        
        @param request: RestoreRevisionRequest
        @return: RestoreRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restore_revision_with_options_async(request, headers, runtime)

    def scan_file_with_options(
        self,
        request: pds_20220301_models.ScanFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ScanFileResponse:
        """
        @summary Scans files.
        
        @param request: ScanFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ScanFileResponse(),
            self.execute(params, req, runtime)
        )

    async def scan_file_with_options_async(
        self,
        request: pds_20220301_models.ScanFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.ScanFileResponse:
        """
        @summary Scans files.
        
        @param request: ScanFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScanFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.ScanFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def scan_file(
        self,
        request: pds_20220301_models.ScanFileRequest,
    ) -> pds_20220301_models.ScanFileResponse:
        """
        @summary Scans files.
        
        @param request: ScanFileRequest
        @return: ScanFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scan_file_with_options(request, headers, runtime)

    async def scan_file_async(
        self,
        request: pds_20220301_models.ScanFileRequest,
    ) -> pds_20220301_models.ScanFileResponse:
        """
        @summary Scans files.
        
        @param request: ScanFileRequest
        @return: ScanFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scan_file_with_options_async(request, headers, runtime)

    def search_address_groups_with_options(
        self,
        request: pds_20220301_models.SearchAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchAddressGroupsResponse:
        """
        @summary Queries location-based groups based on specific locations.
        
        @param request: SearchAddressGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAddressGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_level):
            body['address_level'] = request.address_level
        if not UtilClient.is_unset(request.address_names):
            body['address_names'] = request.address_names
        if not UtilClient.is_unset(request.br_geo_point):
            body['br_geo_point'] = request.br_geo_point
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.tl_geo_point):
            body['tl_geo_point'] = request.tl_geo_point
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/search_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchAddressGroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def search_address_groups_with_options_async(
        self,
        request: pds_20220301_models.SearchAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchAddressGroupsResponse:
        """
        @summary Queries location-based groups based on specific locations.
        
        @param request: SearchAddressGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAddressGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address_level):
            body['address_level'] = request.address_level
        if not UtilClient.is_unset(request.address_names):
            body['address_names'] = request.address_names
        if not UtilClient.is_unset(request.br_geo_point):
            body['br_geo_point'] = request.br_geo_point
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.tl_geo_point):
            body['tl_geo_point'] = request.tl_geo_point
        if not UtilClient.is_unset(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchAddressGroups',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/search_address_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchAddressGroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_address_groups(
        self,
        request: pds_20220301_models.SearchAddressGroupsRequest,
    ) -> pds_20220301_models.SearchAddressGroupsResponse:
        """
        @summary Queries location-based groups based on specific locations.
        
        @param request: SearchAddressGroupsRequest
        @return: SearchAddressGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_address_groups_with_options(request, headers, runtime)

    async def search_address_groups_async(
        self,
        request: pds_20220301_models.SearchAddressGroupsRequest,
    ) -> pds_20220301_models.SearchAddressGroupsResponse:
        """
        @summary Queries location-based groups based on specific locations.
        
        @param request: SearchAddressGroupsRequest
        @return: SearchAddressGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_address_groups_with_options_async(request, headers, runtime)

    def search_domains_with_options(
        self,
        request: pds_20220301_models.SearchDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchDomainsResponse:
        """
        @summary Search domain with specified attributes
        
        @param request: SearchDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchDomains',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchDomainsResponse(),
            self.execute(params, req, runtime)
        )

    async def search_domains_with_options_async(
        self,
        request: pds_20220301_models.SearchDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchDomainsResponse:
        """
        @summary Search domain with specified attributes
        
        @param request: SearchDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchDomains',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchDomainsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_domains(
        self,
        request: pds_20220301_models.SearchDomainsRequest,
    ) -> pds_20220301_models.SearchDomainsResponse:
        """
        @summary Search domain with specified attributes
        
        @param request: SearchDomainsRequest
        @return: SearchDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_domains_with_options(request, headers, runtime)

    async def search_domains_async(
        self,
        request: pds_20220301_models.SearchDomainsRequest,
    ) -> pds_20220301_models.SearchDomainsResponse:
        """
        @summary Search domain with specified attributes
        
        @param request: SearchDomainsRequest
        @return: SearchDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_domains_with_options_async(request, headers, runtime)

    def search_drive_with_options(
        self,
        request: pds_20220301_models.SearchDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchDriveResponse:
        """
        @summary Queries drives.
        
        @param request: SearchDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def search_drive_with_options_async(
        self,
        request: pds_20220301_models.SearchDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchDriveResponse:
        """
        @summary Queries drives.
        
        @param request: SearchDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_drive(
        self,
        request: pds_20220301_models.SearchDriveRequest,
    ) -> pds_20220301_models.SearchDriveResponse:
        """
        @summary Queries drives.
        
        @param request: SearchDriveRequest
        @return: SearchDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_drive_with_options(request, headers, runtime)

    async def search_drive_async(
        self,
        request: pds_20220301_models.SearchDriveRequest,
    ) -> pds_20220301_models.SearchDriveResponse:
        """
        @summary Queries drives.
        
        @param request: SearchDriveRequest
        @return: SearchDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_drive_with_options_async(request, headers, runtime)

    def search_file_with_options(
        self,
        request: pds_20220301_models.SearchFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchFileResponse:
        """
        @summary Queries files. For more information about best practices, visit https://help.aliyun.com/document_detail/175890.html.
        
        @param request: SearchFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.recursive):
            body['recursive'] = request.recursive
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchFileResponse(),
            self.execute(params, req, runtime)
        )

    async def search_file_with_options_async(
        self,
        request: pds_20220301_models.SearchFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchFileResponse:
        """
        @summary Queries files. For more information about best practices, visit https://help.aliyun.com/document_detail/175890.html.
        
        @param request: SearchFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.recursive):
            body['recursive'] = request.recursive
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_file(
        self,
        request: pds_20220301_models.SearchFileRequest,
    ) -> pds_20220301_models.SearchFileResponse:
        """
        @summary Queries files. For more information about best practices, visit https://help.aliyun.com/document_detail/175890.html.
        
        @param request: SearchFileRequest
        @return: SearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_file_with_options(request, headers, runtime)

    async def search_file_async(
        self,
        request: pds_20220301_models.SearchFileRequest,
    ) -> pds_20220301_models.SearchFileResponse:
        """
        @summary Queries files. For more information about best practices, visit https://help.aliyun.com/document_detail/175890.html.
        
        @param request: SearchFileRequest
        @return: SearchFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_file_with_options_async(request, headers, runtime)

    def search_share_link_with_options(
        self,
        request: pds_20220301_models.SearchShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchShareLinkResponse:
        """
        @summary Queries share URLs.
        
        @param request: SearchShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creators):
            body['creators'] = request.creators
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def search_share_link_with_options_async(
        self,
        request: pds_20220301_models.SearchShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchShareLinkResponse:
        """
        @summary Queries share URLs.
        
        @param request: SearchShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creators):
            body['creators'] = request.creators
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.order_direction):
            body['order_direction'] = request.order_direction
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_share_link(
        self,
        request: pds_20220301_models.SearchShareLinkRequest,
    ) -> pds_20220301_models.SearchShareLinkResponse:
        """
        @summary Queries share URLs.
        
        @param request: SearchShareLinkRequest
        @return: SearchShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_share_link_with_options(request, headers, runtime)

    async def search_share_link_async(
        self,
        request: pds_20220301_models.SearchShareLinkRequest,
    ) -> pds_20220301_models.SearchShareLinkResponse:
        """
        @summary Queries share URLs.
        
        @param request: SearchShareLinkRequest
        @return: SearchShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_share_link_with_options_async(request, headers, runtime)

    def search_similar_image_clusters_with_options(
        self,
        request: pds_20220301_models.SearchSimilarImageClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchSimilarImageClustersResponse:
        """
        @summary 获取相似图片聚类结果
        
        @param request: SearchSimilarImageClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchSimilarImageClustersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchSimilarImageClusters',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/query_similar_image_clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchSimilarImageClustersResponse(),
            self.execute(params, req, runtime)
        )

    async def search_similar_image_clusters_with_options_async(
        self,
        request: pds_20220301_models.SearchSimilarImageClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchSimilarImageClustersResponse:
        """
        @summary 获取相似图片聚类结果
        
        @param request: SearchSimilarImageClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchSimilarImageClustersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchSimilarImageClusters',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/query_similar_image_clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchSimilarImageClustersResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_similar_image_clusters(
        self,
        request: pds_20220301_models.SearchSimilarImageClustersRequest,
    ) -> pds_20220301_models.SearchSimilarImageClustersResponse:
        """
        @summary 获取相似图片聚类结果
        
        @param request: SearchSimilarImageClustersRequest
        @return: SearchSimilarImageClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_similar_image_clusters_with_options(request, headers, runtime)

    async def search_similar_image_clusters_async(
        self,
        request: pds_20220301_models.SearchSimilarImageClustersRequest,
    ) -> pds_20220301_models.SearchSimilarImageClustersResponse:
        """
        @summary 获取相似图片聚类结果
        
        @param request: SearchSimilarImageClustersRequest
        @return: SearchSimilarImageClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_similar_image_clusters_with_options_async(request, headers, runtime)

    def search_stories_with_options(
        self,
        request: pds_20220301_models.SearchStoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchStoriesResponse:
        """
        @summary 查询故事列表
        
        @param request: SearchStoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchStoriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cover_image_thumbnail_process):
            body['cover_image_thumbnail_process'] = request.cover_image_thumbnail_process
        if not UtilClient.is_unset(request.cover_video_thumbnail_process):
            body['cover_video_thumbnail_process'] = request.cover_video_thumbnail_process
        if not UtilClient.is_unset(request.create_time_range):
            body['create_time_range'] = request.create_time_range
        if not UtilClient.is_unset(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.face_group_ids):
            body['face_group_ids'] = request.face_group_ids
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        if not UtilClient.is_unset(request.story_end_time_range):
            body['story_end_time_range'] = request.story_end_time_range
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        if not UtilClient.is_unset(request.story_name):
            body['story_name'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time_range):
            body['story_start_time_range'] = request.story_start_time_range
        if not UtilClient.is_unset(request.story_type):
            body['story_type'] = request.story_type
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        if not UtilClient.is_unset(request.with_empty_stories):
            body['with_empty_stories'] = request.with_empty_stories
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchStories',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/find_stories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchStoriesResponse(),
            self.execute(params, req, runtime)
        )

    async def search_stories_with_options_async(
        self,
        request: pds_20220301_models.SearchStoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchStoriesResponse:
        """
        @summary 查询故事列表
        
        @param request: SearchStoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchStoriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cover_image_thumbnail_process):
            body['cover_image_thumbnail_process'] = request.cover_image_thumbnail_process
        if not UtilClient.is_unset(request.cover_video_thumbnail_process):
            body['cover_video_thumbnail_process'] = request.cover_video_thumbnail_process
        if not UtilClient.is_unset(request.create_time_range):
            body['create_time_range'] = request.create_time_range
        if not UtilClient.is_unset(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.face_group_ids):
            body['face_group_ids'] = request.face_group_ids
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.sort):
            body['sort'] = request.sort
        if not UtilClient.is_unset(request.story_end_time_range):
            body['story_end_time_range'] = request.story_end_time_range
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        if not UtilClient.is_unset(request.story_name):
            body['story_name'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time_range):
            body['story_start_time_range'] = request.story_start_time_range
        if not UtilClient.is_unset(request.story_type):
            body['story_type'] = request.story_type
        if not UtilClient.is_unset(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        if not UtilClient.is_unset(request.with_empty_stories):
            body['with_empty_stories'] = request.with_empty_stories
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchStories',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/find_stories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchStoriesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_stories(
        self,
        request: pds_20220301_models.SearchStoriesRequest,
    ) -> pds_20220301_models.SearchStoriesResponse:
        """
        @summary 查询故事列表
        
        @param request: SearchStoriesRequest
        @return: SearchStoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_stories_with_options(request, headers, runtime)

    async def search_stories_async(
        self,
        request: pds_20220301_models.SearchStoriesRequest,
    ) -> pds_20220301_models.SearchStoriesResponse:
        """
        @summary 查询故事列表
        
        @param request: SearchStoriesRequest
        @return: SearchStoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_stories_with_options_async(request, headers, runtime)

    def search_user_with_options(
        self,
        request: pds_20220301_models.SearchUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchUserResponse:
        """
        @summary Searches for users.
        
        @param request: SearchUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.nick_name_for_fuzzy):
            body['nick_name_for_fuzzy'] = request.nick_name_for_fuzzy
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchUserResponse(),
            self.execute(params, req, runtime)
        )

    async def search_user_with_options_async(
        self,
        request: pds_20220301_models.SearchUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.SearchUserResponse:
        """
        @summary Searches for users.
        
        @param request: SearchUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            body['marker'] = request.marker
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.nick_name_for_fuzzy):
            body['nick_name_for_fuzzy'] = request.nick_name_for_fuzzy
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/search',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.SearchUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_user(
        self,
        request: pds_20220301_models.SearchUserRequest,
    ) -> pds_20220301_models.SearchUserResponse:
        """
        @summary Searches for users.
        
        @param request: SearchUserRequest
        @return: SearchUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_user_with_options(request, headers, runtime)

    async def search_user_async(
        self,
        request: pds_20220301_models.SearchUserRequest,
    ) -> pds_20220301_models.SearchUserResponse:
        """
        @summary Searches for users.
        
        @param request: SearchUserRequest
        @return: SearchUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_user_with_options_async(request, headers, runtime)

    def token_with_options(
        self,
        request: pds_20220301_models.TokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.TokenResponse:
        """
        @summary Generates an access token based on Open Authorization (OAuth) 2.0.
        
        @description For more information about how to access Drive and Photo Service from a web server application by using OAuth 2.0, visit [OAuth 2.0 For Web Server Applications](https://www.alibabacloud.com/help/zh/pds/drive-and-photo-service-dev/user-guide/oauth-2-0-access-process-for-web-server-applications).
        For more information about how to access Drive and Photo Service by using a JSON Web Token (JWT) application, visit [Access process for JWT applications](https://www.alibabacloud.com/help/zh/pds/drive-and-photo-service-dev/user-guide/access-process-for-jwt-applications).
        
        @param request: TokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assertion):
            body['assertion'] = request.assertion
        if not UtilClient.is_unset(request.client_id):
            body['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grant_type'] = request.grant_type
        if not UtilClient.is_unset(request.redirect_uri):
            body['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            body['refresh_token'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Token',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/oauth/token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TokenResponse(),
            self.execute(params, req, runtime)
        )

    async def token_with_options_async(
        self,
        request: pds_20220301_models.TokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.TokenResponse:
        """
        @summary Generates an access token based on Open Authorization (OAuth) 2.0.
        
        @description For more information about how to access Drive and Photo Service from a web server application by using OAuth 2.0, visit [OAuth 2.0 For Web Server Applications](https://www.alibabacloud.com/help/zh/pds/drive-and-photo-service-dev/user-guide/oauth-2-0-access-process-for-web-server-applications).
        For more information about how to access Drive and Photo Service by using a JSON Web Token (JWT) application, visit [Access process for JWT applications](https://www.alibabacloud.com/help/zh/pds/drive-and-photo-service-dev/user-guide/access-process-for-jwt-applications).
        
        @param request: TokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assertion):
            body['assertion'] = request.assertion
        if not UtilClient.is_unset(request.client_id):
            body['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            body['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.grant_type):
            body['grant_type'] = request.grant_type
        if not UtilClient.is_unset(request.redirect_uri):
            body['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            body['refresh_token'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Token',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/oauth/token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TokenResponse(),
            await self.execute_async(params, req, runtime)
        )

    def token(
        self,
        request: pds_20220301_models.TokenRequest,
    ) -> pds_20220301_models.TokenResponse:
        """
        @summary Generates an access token based on Open Authorization (OAuth) 2.0.
        
        @description For more information about how to access Drive and Photo Service from a web server application by using OAuth 2.0, visit [OAuth 2.0 For Web Server Applications](https://www.alibabacloud.com/help/zh/pds/drive-and-photo-service-dev/user-guide/oauth-2-0-access-process-for-web-server-applications).
        For more information about how to access Drive and Photo Service by using a JSON Web Token (JWT) application, visit [Access process for JWT applications](https://www.alibabacloud.com/help/zh/pds/drive-and-photo-service-dev/user-guide/access-process-for-jwt-applications).
        
        @param request: TokenRequest
        @return: TokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.token_with_options(request, headers, runtime)

    async def token_async(
        self,
        request: pds_20220301_models.TokenRequest,
    ) -> pds_20220301_models.TokenResponse:
        """
        @summary Generates an access token based on Open Authorization (OAuth) 2.0.
        
        @description For more information about how to access Drive and Photo Service from a web server application by using OAuth 2.0, visit [OAuth 2.0 For Web Server Applications](https://www.alibabacloud.com/help/zh/pds/drive-and-photo-service-dev/user-guide/oauth-2-0-access-process-for-web-server-applications).
        For more information about how to access Drive and Photo Service by using a JSON Web Token (JWT) application, visit [Access process for JWT applications](https://www.alibabacloud.com/help/zh/pds/drive-and-photo-service-dev/user-guide/access-process-for-jwt-applications).
        
        @param request: TokenRequest
        @return: TokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.token_with_options_async(request, headers, runtime)

    def trash_file_with_options(
        self,
        request: pds_20220301_models.TrashFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.TrashFileResponse:
        """
        @summary Moves a file or folder to the recycle bin.
        
        @param request: TrashFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TrashFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TrashFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/trash',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TrashFileResponse(),
            self.execute(params, req, runtime)
        )

    async def trash_file_with_options_async(
        self,
        request: pds_20220301_models.TrashFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.TrashFileResponse:
        """
        @summary Moves a file or folder to the recycle bin.
        
        @param request: TrashFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TrashFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TrashFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/recyclebin/trash',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.TrashFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def trash_file(
        self,
        request: pds_20220301_models.TrashFileRequest,
    ) -> pds_20220301_models.TrashFileResponse:
        """
        @summary Moves a file or folder to the recycle bin.
        
        @param request: TrashFileRequest
        @return: TrashFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trash_file_with_options(request, headers, runtime)

    async def trash_file_async(
        self,
        request: pds_20220301_models.TrashFileRequest,
    ) -> pds_20220301_models.TrashFileResponse:
        """
        @summary Moves a file or folder to the recycle bin.
        
        @param request: TrashFileRequest
        @return: TrashFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.trash_file_with_options_async(request, headers, runtime)

    def un_link_account_with_options(
        self,
        request: pds_20220301_models.UnLinkAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UnLinkAccountResponse:
        """
        @summary Unlink Account Binding
        
        @param request: UnLinkAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnLinkAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnLinkAccount',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/unlink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UnLinkAccountResponse(),
            self.execute(params, req, runtime)
        )

    async def un_link_account_with_options_async(
        self,
        request: pds_20220301_models.UnLinkAccountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UnLinkAccountResponse:
        """
        @summary Unlink Account Binding
        
        @param request: UnLinkAccountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnLinkAccountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra):
            body['extra'] = request.extra
        if not UtilClient.is_unset(request.identity):
            body['identity'] = request.identity
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnLinkAccount',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/account/unlink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UnLinkAccountResponse(),
            await self.execute_async(params, req, runtime)
        )

    def un_link_account(
        self,
        request: pds_20220301_models.UnLinkAccountRequest,
    ) -> pds_20220301_models.UnLinkAccountResponse:
        """
        @summary Unlink Account Binding
        
        @param request: UnLinkAccountRequest
        @return: UnLinkAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_link_account_with_options(request, headers, runtime)

    async def un_link_account_async(
        self,
        request: pds_20220301_models.UnLinkAccountRequest,
    ) -> pds_20220301_models.UnLinkAccountResponse:
        """
        @summary Unlink Account Binding
        
        @param request: UnLinkAccountRequest
        @return: UnLinkAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_link_account_with_options_async(request, headers, runtime)

    def update_domain_with_options(
        self,
        request: pds_20220301_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateDomainResponse:
        """
        @summary Update domain information.
        
        @param request: UpdateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_id):
            body['domain_id'] = request.domain_id
        if not UtilClient.is_unset(request.domain_name):
            body['domain_name'] = request.domain_name
        if not UtilClient.is_unset(request.init_drive_enable):
            body['init_drive_enable'] = request.init_drive_enable
        if not UtilClient.is_unset(request.init_drive_size):
            body['init_drive_size'] = request.init_drive_size
        if not UtilClient.is_unset(request.published_app_access_strategy):
            body['published_app_access_strategy'] = request.published_app_access_strategy
        if not UtilClient.is_unset(request.size_quota):
            body['size_quota'] = request.size_quota
        if not UtilClient.is_unset(request.user_count_quota):
            body['user_count_quota'] = request.user_count_quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomain',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def update_domain_with_options_async(
        self,
        request: pds_20220301_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateDomainResponse:
        """
        @summary Update domain information.
        
        @param request: UpdateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain_id):
            body['domain_id'] = request.domain_id
        if not UtilClient.is_unset(request.domain_name):
            body['domain_name'] = request.domain_name
        if not UtilClient.is_unset(request.init_drive_enable):
            body['init_drive_enable'] = request.init_drive_enable
        if not UtilClient.is_unset(request.init_drive_size):
            body['init_drive_size'] = request.init_drive_size
        if not UtilClient.is_unset(request.published_app_access_strategy):
            body['published_app_access_strategy'] = request.published_app_access_strategy
        if not UtilClient.is_unset(request.size_quota):
            body['size_quota'] = request.size_quota
        if not UtilClient.is_unset(request.user_count_quota):
            body['user_count_quota'] = request.user_count_quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDomain',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/domain/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_domain(
        self,
        request: pds_20220301_models.UpdateDomainRequest,
    ) -> pds_20220301_models.UpdateDomainResponse:
        """
        @summary Update domain information.
        
        @param request: UpdateDomainRequest
        @return: UpdateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_domain_with_options(request, headers, runtime)

    async def update_domain_async(
        self,
        request: pds_20220301_models.UpdateDomainRequest,
    ) -> pds_20220301_models.UpdateDomainResponse:
        """
        @summary Update domain information.
        
        @param request: UpdateDomainRequest
        @return: UpdateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_domain_with_options_async(request, headers, runtime)

    def update_drive_with_options(
        self,
        request: pds_20220301_models.UpdateDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateDriveResponse:
        """
        @summary Modifies a drive.
        
        @param request: UpdateDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def update_drive_with_options_async(
        self,
        request: pds_20220301_models.UpdateDriveRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateDriveResponse:
        """
        @summary Modifies a drive.
        
        @param request: UpdateDriveRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDriveResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.drive_name):
            body['drive_name'] = request.drive_name
        if not UtilClient.is_unset(request.owner):
            body['owner'] = request.owner
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDrive',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/drive/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_drive(
        self,
        request: pds_20220301_models.UpdateDriveRequest,
    ) -> pds_20220301_models.UpdateDriveResponse:
        """
        @summary Modifies a drive.
        
        @param request: UpdateDriveRequest
        @return: UpdateDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_drive_with_options(request, headers, runtime)

    async def update_drive_async(
        self,
        request: pds_20220301_models.UpdateDriveRequest,
    ) -> pds_20220301_models.UpdateDriveResponse:
        """
        @summary Modifies a drive.
        
        @param request: UpdateDriveRequest
        @return: UpdateDriveResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_drive_with_options_async(request, headers, runtime)

    def update_facegroup_with_options(
        self,
        request: pds_20220301_models.UpdateFacegroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateFacegroupResponse:
        """
        @summary Updates a face-based group.
        
        @param request: UpdateFacegroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFacegroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.group_cover_face_id):
            body['group_cover_face_id'] = request.group_cover_face_id
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFacegroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/update_facegroup_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFacegroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_facegroup_with_options_async(
        self,
        request: pds_20220301_models.UpdateFacegroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateFacegroupResponse:
        """
        @summary Updates a face-based group.
        
        @param request: UpdateFacegroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFacegroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.group_cover_face_id):
            body['group_cover_face_id'] = request.group_cover_face_id
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        if not UtilClient.is_unset(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFacegroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/update_facegroup_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFacegroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_facegroup(
        self,
        request: pds_20220301_models.UpdateFacegroupRequest,
    ) -> pds_20220301_models.UpdateFacegroupResponse:
        """
        @summary Updates a face-based group.
        
        @param request: UpdateFacegroupRequest
        @return: UpdateFacegroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_facegroup_with_options(request, headers, runtime)

    async def update_facegroup_async(
        self,
        request: pds_20220301_models.UpdateFacegroupRequest,
    ) -> pds_20220301_models.UpdateFacegroupResponse:
        """
        @summary Updates a face-based group.
        
        @param request: UpdateFacegroupRequest
        @return: UpdateFacegroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_facegroup_with_options_async(request, headers, runtime)

    def update_file_with_options(
        self,
        request: pds_20220301_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateFileResponse:
        """
        @summary Modifies the information about a file instead of the file data.
        
        @param request: UpdateFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.starred):
            body['starred'] = request.starred
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFileResponse(),
            self.execute(params, req, runtime)
        )

    async def update_file_with_options_async(
        self,
        request: pds_20220301_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateFileResponse:
        """
        @summary Modifies the information about a file instead of the file data.
        
        @param request: UpdateFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.hidden):
            body['hidden'] = request.hidden
        if not UtilClient.is_unset(request.labels):
            body['labels'] = request.labels
        if not UtilClient.is_unset(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.starred):
            body['starred'] = request.starred
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFile',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_file(
        self,
        request: pds_20220301_models.UpdateFileRequest,
    ) -> pds_20220301_models.UpdateFileResponse:
        """
        @summary Modifies the information about a file instead of the file data.
        
        @param request: UpdateFileRequest
        @return: UpdateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_file_with_options(request, headers, runtime)

    async def update_file_async(
        self,
        request: pds_20220301_models.UpdateFileRequest,
    ) -> pds_20220301_models.UpdateFileResponse:
        """
        @summary Modifies the information about a file instead of the file data.
        
        @param request: UpdateFileRequest
        @return: UpdateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_file_with_options_async(request, headers, runtime)

    def update_group_with_options(
        self,
        request: pds_20220301_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateGroupResponse:
        """
        @summary Modifies the information about a group.
        
        @param request: UpdateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: pds_20220301_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateGroupResponse:
        """
        @summary Modifies the information about a group.
        
        @param request: UpdateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['group_id'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            body['group_name'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/group/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_group(
        self,
        request: pds_20220301_models.UpdateGroupRequest,
    ) -> pds_20220301_models.UpdateGroupResponse:
        """
        @summary Modifies the information about a group.
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_with_options(request, headers, runtime)

    async def update_group_async(
        self,
        request: pds_20220301_models.UpdateGroupRequest,
    ) -> pds_20220301_models.UpdateGroupResponse:
        """
        @summary Modifies the information about a group.
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_group_with_options_async(request, headers, runtime)

    def update_identity_to_benefit_pkg_mapping_with_options(
        self,
        request: pds_20220301_models.UpdateIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateIdentityToBenefitPkgMappingResponse:
        """
        @summary Updates the mapping between an entity and a benefit package. You can call this operation to associate a benefit package with a user.
        
        @param request: UpdateIdentityToBenefitPkgMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIdentityToBenefitPkgMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['amount'] = request.amount
        if not UtilClient.is_unset(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not UtilClient.is_unset(request.expire_time):
            body['expire_time'] = request.expire_time
        if not UtilClient.is_unset(request.identity_id):
            body['identity_id'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIdentityToBenefitPkgMapping',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/benefit/identity_to_benefit_pkg_mapping/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateIdentityToBenefitPkgMappingResponse(),
            self.execute(params, req, runtime)
        )

    async def update_identity_to_benefit_pkg_mapping_with_options_async(
        self,
        request: pds_20220301_models.UpdateIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateIdentityToBenefitPkgMappingResponse:
        """
        @summary Updates the mapping between an entity and a benefit package. You can call this operation to associate a benefit package with a user.
        
        @param request: UpdateIdentityToBenefitPkgMappingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIdentityToBenefitPkgMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['amount'] = request.amount
        if not UtilClient.is_unset(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not UtilClient.is_unset(request.expire_time):
            body['expire_time'] = request.expire_time
        if not UtilClient.is_unset(request.identity_id):
            body['identity_id'] = request.identity_id
        if not UtilClient.is_unset(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIdentityToBenefitPkgMapping',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/benefit/identity_to_benefit_pkg_mapping/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateIdentityToBenefitPkgMappingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_identity_to_benefit_pkg_mapping(
        self,
        request: pds_20220301_models.UpdateIdentityToBenefitPkgMappingRequest,
    ) -> pds_20220301_models.UpdateIdentityToBenefitPkgMappingResponse:
        """
        @summary Updates the mapping between an entity and a benefit package. You can call this operation to associate a benefit package with a user.
        
        @param request: UpdateIdentityToBenefitPkgMappingRequest
        @return: UpdateIdentityToBenefitPkgMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_identity_to_benefit_pkg_mapping_with_options(request, headers, runtime)

    async def update_identity_to_benefit_pkg_mapping_async(
        self,
        request: pds_20220301_models.UpdateIdentityToBenefitPkgMappingRequest,
    ) -> pds_20220301_models.UpdateIdentityToBenefitPkgMappingResponse:
        """
        @summary Updates the mapping between an entity and a benefit package. You can call this operation to associate a benefit package with a user.
        
        @param request: UpdateIdentityToBenefitPkgMappingRequest
        @return: UpdateIdentityToBenefitPkgMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_identity_to_benefit_pkg_mapping_with_options_async(request, headers, runtime)

    def update_revision_with_options(
        self,
        request: pds_20220301_models.UpdateRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateRevisionResponse:
        """
        @summary Updates the version information. You can call this operation to permanently retain a version or modify the description of a version. You can permanently retain up to 50 versions of a file.
        
        @param request: UpdateRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.keep_forever):
            body['keep_forever'] = request.keep_forever
        if not UtilClient.is_unset(request.revision_description):
            body['revision_description'] = request.revision_description
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def update_revision_with_options_async(
        self,
        request: pds_20220301_models.UpdateRevisionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateRevisionResponse:
        """
        @summary Updates the version information. You can call this operation to permanently retain a version or modify the description of a version. You can permanently retain up to 50 versions of a file.
        
        @param request: UpdateRevisionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRevisionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.file_id):
            body['file_id'] = request.file_id
        if not UtilClient.is_unset(request.keep_forever):
            body['keep_forever'] = request.keep_forever
        if not UtilClient.is_unset(request.revision_description):
            body['revision_description'] = request.revision_description
        if not UtilClient.is_unset(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRevision',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/file/revision/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_revision(
        self,
        request: pds_20220301_models.UpdateRevisionRequest,
    ) -> pds_20220301_models.UpdateRevisionResponse:
        """
        @summary Updates the version information. You can call this operation to permanently retain a version or modify the description of a version. You can permanently retain up to 50 versions of a file.
        
        @param request: UpdateRevisionRequest
        @return: UpdateRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_revision_with_options(request, headers, runtime)

    async def update_revision_async(
        self,
        request: pds_20220301_models.UpdateRevisionRequest,
    ) -> pds_20220301_models.UpdateRevisionResponse:
        """
        @summary Updates the version information. You can call this operation to permanently retain a version or modify the description of a version. You can permanently retain up to 50 versions of a file.
        
        @param request: UpdateRevisionRequest
        @return: UpdateRevisionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_revision_with_options_async(request, headers, runtime)

    def update_share_link_with_options(
        self,
        request: pds_20220301_models.UpdateShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateShareLinkResponse:
        """
        @summary Modifies a share link.
        
        @param request: UpdateShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_count):
            body['download_count'] = request.download_count
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.office_editable):
            body['office_editable'] = request.office_editable
        if not UtilClient.is_unset(request.preview_count):
            body['preview_count'] = request.preview_count
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.report_count):
            body['report_count'] = request.report_count
        if not UtilClient.is_unset(request.save_count):
            body['save_count'] = request.save_count
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.video_preview_count):
            body['video_preview_count'] = request.video_preview_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def update_share_link_with_options_async(
        self,
        request: pds_20220301_models.UpdateShareLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateShareLinkResponse:
        """
        @summary Modifies a share link.
        
        @param request: UpdateShareLinkRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateShareLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.disable_download):
            body['disable_download'] = request.disable_download
        if not UtilClient.is_unset(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not UtilClient.is_unset(request.disable_save):
            body['disable_save'] = request.disable_save
        if not UtilClient.is_unset(request.download_count):
            body['download_count'] = request.download_count
        if not UtilClient.is_unset(request.download_limit):
            body['download_limit'] = request.download_limit
        if not UtilClient.is_unset(request.expiration):
            body['expiration'] = request.expiration
        if not UtilClient.is_unset(request.office_editable):
            body['office_editable'] = request.office_editable
        if not UtilClient.is_unset(request.preview_count):
            body['preview_count'] = request.preview_count
        if not UtilClient.is_unset(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not UtilClient.is_unset(request.report_count):
            body['report_count'] = request.report_count
        if not UtilClient.is_unset(request.save_count):
            body['save_count'] = request.save_count
        if not UtilClient.is_unset(request.save_limit):
            body['save_limit'] = request.save_limit
        if not UtilClient.is_unset(request.share_id):
            body['share_id'] = request.share_id
        if not UtilClient.is_unset(request.share_name):
            body['share_name'] = request.share_name
        if not UtilClient.is_unset(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.video_preview_count):
            body['video_preview_count'] = request.video_preview_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShareLink',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/share_link/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_share_link(
        self,
        request: pds_20220301_models.UpdateShareLinkRequest,
    ) -> pds_20220301_models.UpdateShareLinkResponse:
        """
        @summary Modifies a share link.
        
        @param request: UpdateShareLinkRequest
        @return: UpdateShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_share_link_with_options(request, headers, runtime)

    async def update_share_link_async(
        self,
        request: pds_20220301_models.UpdateShareLinkRequest,
    ) -> pds_20220301_models.UpdateShareLinkResponse:
        """
        @summary Modifies a share link.
        
        @param request: UpdateShareLinkRequest
        @return: UpdateShareLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_share_link_with_options_async(request, headers, runtime)

    def update_story_with_options(
        self,
        request: pds_20220301_models.UpdateStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateStoryResponse:
        """
        @summary 更新故事
        
        @param request: UpdateStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cover):
            body['cover'] = request.cover
        if not UtilClient.is_unset(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        if not UtilClient.is_unset(request.story_name):
            body['story_name'] = request.story_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/update_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def update_story_with_options_async(
        self,
        request: pds_20220301_models.UpdateStoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateStoryResponse:
        """
        @summary 更新故事
        
        @param request: UpdateStoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStoryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cover):
            body['cover'] = request.cover
        if not UtilClient.is_unset(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not UtilClient.is_unset(request.drive_id):
            body['drive_id'] = request.drive_id
        if not UtilClient.is_unset(request.story_id):
            body['story_id'] = request.story_id
        if not UtilClient.is_unset(request.story_name):
            body['story_name'] = request.story_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStory',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/image/update_story',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_story(
        self,
        request: pds_20220301_models.UpdateStoryRequest,
    ) -> pds_20220301_models.UpdateStoryResponse:
        """
        @summary 更新故事
        
        @param request: UpdateStoryRequest
        @return: UpdateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_story_with_options(request, headers, runtime)

    async def update_story_async(
        self,
        request: pds_20220301_models.UpdateStoryRequest,
    ) -> pds_20220301_models.UpdateStoryResponse:
        """
        @summary 更新故事
        
        @param request: UpdateStoryRequest
        @return: UpdateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_story_with_options_async(request, headers, runtime)

    def update_user_with_options(
        self,
        request: pds_20220301_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateUserResponse:
        """
        @summary Modifies the information about a user.
        
        @param request: UpdateUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateUserResponse(),
            self.execute(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: pds_20220301_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pds_20220301_models.UpdateUserResponse:
        """
        @summary Modifies the information about a user.
        
        @param request: UpdateUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.avatar):
            body['avatar'] = request.avatar
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not UtilClient.is_unset(request.nick_name):
            body['nick_name'] = request.nick_name
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.role):
            body['role'] = request.role
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/v2/user/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pds_20220301_models.UpdateUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_user(
        self,
        request: pds_20220301_models.UpdateUserRequest,
    ) -> pds_20220301_models.UpdateUserResponse:
        """
        @summary Modifies the information about a user.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_with_options(request, headers, runtime)

    async def update_user_async(
        self,
        request: pds_20220301_models.UpdateUserRequest,
    ) -> pds_20220301_models.UpdateUserResponse:
        """
        @summary Modifies the information about a user.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_user_with_options_async(request, headers, runtime)
